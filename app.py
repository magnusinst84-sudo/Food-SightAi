"""
FoodSight AI - Flask Backend Server (Deployment Build)
=======================================================

This is the deployment-optimised backend for the FoodSight AI web application.
It uses TensorFlow Lite (tflite-runtime) instead of full TensorFlow to
stay within the memory limits of free-tier hosting services like Render.

Author: FoodSight AI Team
Date: February 2026
"""

from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
# Use LiteRT (successor to tflite-runtime) for low-memory deployment
try:
    from ai_edge_litert.interpreter import Interpreter as TFLiteInterpreter
except ImportError:
    try:
        from tflite_runtime.interpreter import Interpreter as TFLiteInterpreter
    except ImportError:
        import tensorflow as tf
        TFLiteInterpreter = tf.lite.Interpreter
import numpy as np
import os
import logging
import threading
import time
from datetime import datetime
import shutil
from dotenv import load_dotenv
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import uuid

# Load environment variables
load_dotenv()

from nutrition_data import NUTRITION_DATABASE, get_nutrition_info, get_all_dishes
from dataset_config import EXPANDED_CLASS_NAMES, DATASET_STATS, CATEGORY_MAPPING, REGION_MAPPING

# New imports for Auth and DB
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['MAX_CONTENT_LENGTH'] = int(os.getenv('MAX_CONTENT_LENGTH', 5 * 1024 * 1024))
app.config['UPLOAD_FOLDER'] = os.path.join(basedir, 'uploads')
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'webp'}
# Use absolute path for SQLite
default_db = 'sqlite:///' + os.path.join(basedir, 'instance', 'users.db')
db_url = os.getenv('DATABASE_URL', default_db)

# Ensure the database URL is absolute for SQLite
if db_url.startswith('sqlite:///'):
    db_path = db_url.replace('sqlite:///', '')
    if not os.path.isabs(db_path):
        db_url = 'sqlite:///' + os.path.abspath(os.path.join(basedir, db_path))

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', os.urandom(24))
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

# Initialize Extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Rate Limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

# User Model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    # Profile fields
    height = db.Column(db.Float, nullable=True)
    weight = db.Column(db.Float, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    activity_level = db.Column(db.String(20), nullable=True)
    daily_cal_target = db.Column(db.Integer, nullable=True)
    daily_protein_target = db.Column(db.Integer, nullable=True)
    allergies = db.Column(db.String(200), nullable=True)
    # Relationship to history
    history = db.relationship('ScanHistory', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

# Scan History Model
class ScanHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    dish_name = db.Column(db.String(100), nullable=False)
    calories = db.Column(db.Integer)
    image_url = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'dish_name': self.dish_name,
            'calories': self.calories,
            'image_url': self.image_url,
            'timestamp': self.timestamp.isoformat()
        }

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Food class names
# Try to load dynamically from training results first
CLASS_NAMES = []

def load_class_names():
    """Load class names from the trained model's artifact file."""
    global CLASS_NAMES
    
    # Paths to check
    paths_to_check = [
        os.path.join('..', '02_Results_And_Evaluation', 'class_names.txt'),
        os.path.join('02_Results_And_Evaluation', 'class_names.txt'),
        'class_names.txt',
        os.path.join('scripts', 'class_names.txt')
    ]
    
    for path in paths_to_check:
        if os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    CLASS_NAMES = [line.strip() for line in f.readlines() if line.strip()]
                logger.info(f"[OK] Loaded {len(CLASS_NAMES)} classes from {path}")
                return
            except Exception as e:
                logger.error(f"Failed to load class names from {path}: {e}")

    # Fallback to dataset directory scanning
    dataset_path = os.path.join('dataset', 'train')
    if not CLASS_NAMES and os.path.exists(dataset_path):
        try:
            CLASS_NAMES = sorted([d for d in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, d))])
            logger.info(f"[OK] Loaded {len(CLASS_NAMES)} classes from dataset directory")
            return
        except Exception as e:
            logger.error(f"Failed to scan dataset directory: {e}")

    # Final fallback to config file
    if not CLASS_NAMES:
        logger.warning("[WARNING] Could not load dynamic classes. Falling back to dataset_config.py")
        CLASS_NAMES = EXPANDED_CLASS_NAMES

# Load classes on module import
load_class_names()

# Flag for compatibility
USE_EXPANDED_DATASET = True

# --- TFLITE MODEL LOADING ---
interpreter = None          # TFLite Interpreter instance
_input_details = None       # Cached input tensor details
_output_details = None      # Cached output tensor details
model = None                # Kept for API compatibility (health check etc.)
_model_load_lock = threading.Lock()

def create_directories():
    """Create necessary directories if they don't exist"""
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(os.path.join(basedir, 'instance'), exist_ok=True)
    os.makedirs('static/samples', exist_ok=True)
    logger.info("[OK] Directories created/verified")

def _load_model_sync():
    """Load the TFLite model. Called lazily on first predict or via /api/warmup."""
    global interpreter, _input_details, _output_details, model
    model_paths = [
        os.path.join(basedir, 'foodsight_v6.tflite'),
    ]
    for p in model_paths:
        if os.path.exists(p):
            try:
                logger.info(f"Loading TFLite model: {p}")
                interpreter = TFLiteInterpreter(model_path=p)
                interpreter.allocate_tensors()
                _input_details = interpreter.get_input_details()
                _output_details = interpreter.get_output_details()
                model = interpreter  # So health-check sees model != None
                logger.info(f"TFLite model loaded successfully  "
                            f"(input shape: {_input_details[0]['shape']}, "
                            f"dtype: {_input_details[0]['dtype']})")
                return True
            except Exception as e:
                logger.error(f"Failed to load {p}: {e}")
    logger.warning("No model could be loaded")
    return False

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def preprocess_image(img_path):
    """
    Preprocess image for model inference.
    Returns: np.float32 array of shape (1, 224, 224, 3) with values in [0, 1].
    Uses PIL + numpy only.
    """
    try:
        from PIL import Image as PILImage
        img = PILImage.open(img_path).convert('RGB').resize((224, 224))
        # NO normalisation — model was trained on raw [0, 255] pixel values
        # (image_dataset_from_directory has no rescaling by default)
        img_array = np.array(img, dtype=np.float32)            # shape: (224, 224, 3), range [0, 255]
        img_array = np.expand_dims(img_array, axis=0)          # shape: (1, 224, 224, 3)
        return img_array

    except Exception as e:
        logger.error(f"Error preprocessing image: {str(e)}")
        raise

# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({
        'error': 'Too Many Requests',
        'message': 'Slow down! You are making too many requests. Please try again later.'
    }), 429

@app.errorhandler(413)
def request_entity_too_large(e):
    return jsonify({
        'error': 'File Too Large',
        'message': f'The file exceeds the maximum allowed size of {app.config["MAX_CONTENT_LENGTH"] // (1024*1024)}MB.'
    }), 413

# ============================================================================
# API ENDPOINTS
# ============================================================================

@app.route('/')
def index():
    """Serve the main application page"""
    return render_template('index.html')

@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to verify server and model status.
    """
    return jsonify({
        'status': 'healthy',
        'model_loaded': interpreter is not None,
        'backend': 'tflite_runtime',
        'timestamp': datetime.now().isoformat(),
        'version': '4.0.0 (TFLite Deploy)'
    })

@app.route('/api/warmup')
def warmup():
    """Pre-load the model so the first prediction is fast."""
    if interpreter is not None:
        return jsonify({'model_loaded': True, 'message': 'Model already loaded'})
    with _model_load_lock:
        if interpreter is not None:
            return jsonify({'model_loaded': True, 'message': 'Model already loaded'})
        ok = _load_model_sync()
    return jsonify({'model_loaded': ok, 'message': 'Model loaded' if ok else 'Model failed to load'}), 200 if ok else 503

@app.route('/api/predict', methods=['POST'])
@limiter.limit("5 per minute")
def predict():
    """
    Main prediction endpoint for food classification.
    """
    start_time = time.time()
    try:
        # Lazy-load model on first request
        if interpreter is None:
            with _model_load_lock:
                if interpreter is None:
                    logger.info("Model not loaded; loading now...")
                    ok = _load_model_sync()
                    if not ok:
                        return jsonify({
                            'error': 'Model not loaded',
                            'message': 'The AI model could not be loaded. Please try again.'
                        }), 503
            if interpreter is None:
                return jsonify({'error': 'Model not loaded', 'message': 'AI model unavailable.'}), 503
        
        # Check if file is in request
        if 'file' not in request.files:
            return jsonify({
                'error': 'No file provided',
                'message': 'Please upload an image file.'
            }), 400
        
        file = request.files['file']
        
        # Check if file is selected
        if file.filename == '':
            return jsonify({'error': 'No file selected', 'message': 'Please select an image file to upload.'}), 400
        
        # Secure File Validation
        # 1. MIME check via Magic Bytes
        # Note: 'magic' library needs to be imported (e.g., `import magic`)
        # For this example, assuming `magic` is available or this is a placeholder.
        # If `magic` is not available, this part will cause an error.
        try:
            import magic
            header = file.read(1024)
            file.seek(0)
            mime = magic.from_buffer(header, mime=True)
            if mime not in ['image/jpeg', 'image/png', 'image/webp']:
                return jsonify({'error': f'Invalid file type: {mime}. Only JPG, PNG, WEBP allowed.'}), 400
        except ImportError:
            logger.warning("Python 'magic' library not found. Skipping MIME type validation.")
        except Exception as e:
            logger.error(f"Error during MIME type validation: {e}")
            return jsonify({'error': 'File validation failed', 'message': 'Could not validate file type.'}), 500

        if file and allowed_file(file.filename):
            # 2. Filename Sanitization with UUID
            # Note: 'uuid' library needs to be imported (e.g., `import uuid`)
            # For this example, assuming `uuid` is available.
            import uuid
            ext = file.filename.rsplit('.', 1)[1].lower()
            filename = f"{uuid.uuid4().hex}.{ext}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            # Ensure upload folder exists
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            
            file.save(filepath)
            
            logger.info(f"Processing image: {filename}")

            try:
                # 1. Preprocess
                input_data = preprocess_image(filepath)

                # 2. TFLite Inference
                # Cast input to the dtype expected by the model
                expected_dtype = _input_details[0]['dtype']
                if input_data.dtype != expected_dtype:
                    input_data = input_data.astype(expected_dtype)
                interpreter.set_tensor(_input_details[0]['index'], input_data)
                interpreter.invoke()
                probabilities = interpreter.get_tensor(_output_details[0]['index'])[0]

                # 3. Post-process
                top_idx = int(np.argmax(probabilities))
                predicted_class = CLASS_NAMES[top_idx]
                confidence = float(probabilities[top_idx] * 100)

                # Top 3
                top3_indices = probabilities.argsort()[-3:][::-1]
                top_3 = [
                    {'class': CLASS_NAMES[int(idx)], 'confidence': float(probabilities[idx] * 100)}
                    for idx in top3_indices
                ]

                logger.info(f"Prediction: {predicted_class} ({confidence:.2f}%) [{round((time.time()-start_time)*1000)}ms]")

                # 4. Cleanup
                try:
                    os.remove(filepath)
                except Exception:
                    pass

                # 5. Nutrition lookup
                portion = request.form.get('portion', 'medium')
                nutrition_info = get_nutrition_info(predicted_class, portion)

                response_data = {
                    'success': True,
                    'predicted_class': predicted_class,
                    'confidence': round(confidence, 2),
                    'top_3': top_3,
                    'timestamp': datetime.now().isoformat(),
                    'inference_ms': round((time.time() - start_time) * 1000, 2)
                }

                if nutrition_info:
                    from nutrition_data import get_health_indicators, calculate_health_score, get_dietary_suitability
                    response_data['nutrition'] = nutrition_info
                    response_data['health_indicators'] = get_health_indicators(nutrition_info)
                    response_data['health_score'] = calculate_health_score(nutrition_info)
                    response_data['suitability'] = get_dietary_suitability(nutrition_info)

                    # Dietary warnings based on user profile
                    warnings = []
                    if current_user.is_authenticated and current_user.allergies:
                        user_allergies = [a.strip().lower() for a in current_user.allergies.split(",")]
                        dish_allergens = [a.lower() for a in nutrition_info.get("allergens", [])]
                        for allergy in user_allergies:
                            if allergy in dish_allergens:
                                warnings.append(allergy.title())
                    if warnings:
                        response_data['warnings'] = f"Warning: This dish contains {', '.join(warnings)}."

                return jsonify(response_data)

            except Exception as e:
                try:
                    os.remove(filepath)
                except Exception:
                    pass
                logger.error(f"Inference error: {str(e)}", exc_info=True)
                return jsonify({
                    'error': 'Analysis failed',
                    'message': 'An error occurred while processing your image. Please try again.'
                }), 500
        else:
            return jsonify({
                'error': 'Invalid file type',
                'message': f'Allowed file types: {", ".join(app.config["ALLOWED_EXTENSIONS"])}'
            }), 400

    except Exception as e:
        logger.error(f"Prediction error: {str(e)}", exc_info=True)
        return jsonify({
            'error': 'Prediction failed',
            'message': 'An error occurred while processing your image. Please try again.'
        }), 500

@app.route('/api/classes', methods=['GET'])
def get_classes():
    """
    Get list of all food classes the model can recognize.
    """
    return jsonify({
        'classes': CLASS_NAMES,
        'count': len(CLASS_NAMES)
    })

@app.route('/static/samples/<path:filename>')
def serve_sample(filename):
    """Serve sample images"""
    return send_from_directory('static/samples', filename)

@app.route('/api/nutrition/<dish_name>', methods=['GET'])
def get_nutrition(dish_name):
    """
    Get nutrition information for a specific dish.
    """
    # Decode and normalize dish name
    from urllib.parse import unquote
    dish_name = unquote(dish_name)
    
    # Get portion size from query params
    portion = request.args.get('portion', 'medium')
    quantity = request.args.get('q')
    unit = request.args.get('u')
    
    nutrition_info = get_nutrition_info(dish_name, quantity=quantity, unit=unit, portion=portion)
    
    if nutrition_info:
        from nutrition_data import get_health_indicators, calculate_health_score, get_dietary_suitability
        return jsonify({
            'success': True,
            'dish_name': dish_name,
            'nutrition': nutrition_info,
            'health_indicators': get_health_indicators(nutrition_info),
            'health_score': calculate_health_score(nutrition_info),
            'suitability': get_dietary_suitability(nutrition_info)
        })
    else:
        return jsonify({
            'error': 'Dish not found',
            'message': f'No nutrition information available for "{dish_name}"'
        }), 404

@app.route('/api/nutrition/all', methods=['GET'])
def get_all_nutrition():
    """
    Get nutrition information for all dishes.
    """
    return jsonify({
        'success': True,
        'total_dishes': len(NUTRITION_DATABASE),
        'dishes': NUTRITION_DATABASE
    })

@app.route('/api/dataset/info', methods=['GET'])
def get_dataset_info():
    """
    Get information about the expanded dataset.
    """
    return jsonify({
        'success': True,
        'current_model': {
            'classes': CLASS_NAMES,
            'total_classes': len(CLASS_NAMES),
            'status': 'active'
        },
        'expanded_dataset': {
            'classes': EXPANDED_CLASS_NAMES,
            'total_classes': len(EXPANDED_CLASS_NAMES),
            'status': 'ready_for_training',
            'statistics': DATASET_STATS
        },
        'categories': list(CATEGORY_MAPPING.keys()),
        'regions': list(REGION_MAPPING.keys())
    })

@app.route('/api/dishes/category/<category>', methods=['GET'])
def get_dishes_by_category(category):
    """
    Get all dishes in a specific category.
    """
    from urllib.parse import unquote
    category = unquote(category)
    
    dishes = CATEGORY_MAPPING.get(category, [])
    
    if dishes:
        return jsonify({
            'success': True,
            'category': category,
            'dishes': dishes,
            'count': len(dishes)
        })
    else:
        return jsonify({
            'error': 'Category not found',
            'message': f'No dishes found for category "{category}"',
            'available_categories': list(CATEGORY_MAPPING.keys())
        }), 404

@app.route('/api/dishes/region/<region>', methods=['GET'])
def get_dishes_by_region(region):
    """
    Get all dishes from a specific region.
    """
    from urllib.parse import unquote
    region = unquote(region)
    
    dishes = REGION_MAPPING.get(region, [])
    
    if dishes:
        return jsonify({
            'success': True,
            'region': region,
            'dishes': dishes,
            'count': len(dishes)
        })
    else:
        return jsonify({
            'error': 'Region not found',
            'message': f'No dishes found for region "{region}"',
            'available_regions': list(REGION_MAPPING.keys())
        }), 404

# ============================================================================
# SEARCH ENDPOINT
# ============================================================================

@app.route('/api/search', methods=['GET'])
@limiter.limit("10 per minute")
def search_food():
    """
    Search for a food item in the nutrition database.
    """
    query = request.args.get('q', '').strip()
    if not query:
        return jsonify({'error': 'No query provided'}), 400

    # Search in NUTRITION_DATABASE
    results = []
    query_lower = query.lower()
    
    # Exact match first
    if query in NUTRITION_DATABASE:
        results.append(query)
    else:
        # Partial match
        for dish in NUTRITION_DATABASE.keys():
            if query_lower in dish.lower():
                results.append(dish)

    if not results:
        return jsonify({
            'success': False,
            'message': 'This food item is not in our database yet. Please wait for future updates!',
            'query': query
        })

    # For now, return the best match if multiple found, or just the first one
    best_match = results[0]
    portion = request.args.get('portion', 'medium')
    nutrition_info = get_nutrition_info(best_match, portion)

    if nutrition_info:
        from nutrition_data import get_health_indicators, calculate_health_score, get_dietary_suitability
        return jsonify({
            'success': True,
            'predicted_class': best_match,
            'confidence': 100.0, # Search match is 100% "confident" that it's that dish
            'nutrition': nutrition_info,
            'health_indicators': get_health_indicators(nutrition_info),
            'health_score': calculate_health_score(nutrition_info),
            'suitability': get_dietary_suitability(nutrition_info),
            'top_3': [{'class': best_match, 'confidence': 100.0}],
            'is_search': True
        })
    
    return jsonify({
        'success': False,
        'message': 'Failed to retrieve nutrition info for match.',
        'query': query
    })

# ============================================================================
# AUTH ENDPOINTS
# ============================================================================

@app.route('/api/auth/status', methods=['GET'])
def auth_status():
    if current_user.is_authenticated:
        return jsonify({
            'authenticated': True,
            'username': current_user.username,
            'has_allergies': bool(current_user.allergies)
        })
    return jsonify({'authenticated': False})

@app.route('/api/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'GET':
        return jsonify({
            'success': True,
            'profile': {
                'username': current_user.username,
                'height': current_user.height,
                'weight': current_user.weight,
                'age': current_user.age,
                'activity_level': current_user.activity_level,
                'daily_cal_target': current_user.daily_cal_target,
                'daily_protein_target': current_user.daily_protein_target,
                'allergies': current_user.allergies
            }
        })
    elif request.method == 'POST':
        data = request.json
        current_user.height = data.get('height', current_user.height)
        current_user.weight = data.get('weight', current_user.weight)
        current_user.age = data.get('age', current_user.age)
        current_user.activity_level = data.get('activity_level', current_user.activity_level)
        current_user.daily_cal_target = data.get('daily_cal_target', current_user.daily_cal_target)
        current_user.daily_protein_target = data.get('daily_protein_target', current_user.daily_protein_target)
        current_user.allergies = data.get('allergies', current_user.allergies)
        
        db.session.commit()
        return jsonify({'success': True, 'message': 'Profile updated successfully'})

@app.route('/profile')
@login_required
def profile_page():
    return render_template('profile.html')

@app.route('/api/auth/signup', methods=['POST'])
@limiter.limit("5 per minute")
def signup():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Missing fields'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'User already exists'}), 400

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'success': True, 'message': 'User created successfully'})

@app.route('/api/auth/login', methods=['POST'])
@limiter.limit("5 per minute")
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        login_user(user)
        return jsonify({'success': True, 'username': user.username})
    
    return jsonify({'error': 'Invalid username or password'}), 401

@app.route('/api/auth/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({'success': True, 'message': 'Logged out successfully'})

# History Endpoints
@app.route('/api/history/save', methods=['POST'])
@login_required
def save_history():
    data = request.json
    dish_name = data.get('dish_name')
    calories = data.get('calories')
    # image_url removed for privacy as requested

    if not dish_name:
        return jsonify({'error': 'Missing dish name'}), 400

    new_entry = ScanHistory(
        user_id=current_user.id,
        dish_name=dish_name,
        calories=calories
        # image_url=None
    )
    db.session.add(new_entry)
    db.session.commit()

    return jsonify({'success': True, 'message': 'History saved'})

@app.route('/api/history', methods=['DELETE'])
@login_required
def clear_history():
    """Clear all scan history for the current user"""
    ScanHistory.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()
    return jsonify({'success': True, 'message': 'History cleared successfully'})

@app.route('/api/history', methods=['GET'])
@login_required
def get_history():
    history = ScanHistory.query.filter_by(user_id=current_user.id).order_by(ScanHistory.timestamp.desc()).all()
    return jsonify({
        'success': True,
        'history': [entry.to_dict() for entry in history]
    })

# ============================================================================
# APPLICATION STARTUP
# ============================================================================

def initialize_app():
    """Initialize the application on startup"""
    logger.info("=" * 60)
    logger.info("FoodSight AI - Starting Application")
    logger.info("=" * 60)
    
    # Create necessary directories
    create_directories()

    # Initialize Database
    with app.app_context():
        db.create_all()
        logger.info("[OK] Database initialized")
    
    # Model loads lazily on first /api/predict or /api/warmup call
    logger.info("[OK] Model will load on first prediction request (lazy load)")
    
    logger.info("=" * 60)
    logger.info("✓ Application ready!")
    logger.info("=" * 60)

# Initialize on import
initialize_app()

if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("FoodSight AI - Web Application")
    print("=" * 60)
    print("\nServer starting at: http://localhost:5001")
    print("API Health Check: http://localhost:5001/api/health")
    print("\nPress Ctrl+C to stop the server\n")
    print("=" * 60 + "\n")
    
    # Run Flask server (debug off for production-like local testing)
    port = int(os.getenv('PORT', 5001))
    app.run(
        host='0.0.0.0',
        port=port,
        debug=os.getenv('DEBUG', 'False').lower() == 'true',
        use_reloader=False
    )
