/**
 * FoodSight AI - Frontend JavaScript
 * ===================================
 * Handles image upload, API communication, and results display
 */

// API Configuration
const API_BASE_URL = '/api';

// DOM Elements
let uploadZone, fileInput, previewSection, previewImage, loadingSection, resultsSection;
let foodSearchInput, searchBtn, authContainer, authModal, loginBtn;
let historyBtn, profileLinkBtn, profileModal, persistentHistoryList, clearHistoryBtn;

/**
 * Initialize the application when DOM is loaded
 */
document.addEventListener('DOMContentLoaded', function () {
    console.log('🍛 FoodSight AI - Initializing...');

    // Get DOM elements
    uploadZone = document.getElementById('uploadZone');
    fileInput = document.getElementById('fileInput');
    previewSection = document.getElementById('previewSection');
    previewImage = document.getElementById('previewImage');
    loadingSection = document.getElementById('loadingSection');
    resultsSection = document.getElementById('resultsSection');

    // Auth & Search Elements
    foodSearchInput = document.getElementById('foodSearchInput');
    searchBtn = document.getElementById('searchBtn');
    authContainer = document.getElementById('authContainer');
    authModal = document.getElementById('authModal');
    loginBtn = document.getElementById('loginBtn');

    // Profile Elements
    historyBtn = document.getElementById('historyBtn');
    profileLinkBtn = document.getElementById('profileLinkBtn');
    profileModal = document.getElementById('profileModal');
    persistentHistoryList = document.getElementById('persistentHistoryList');
    clearHistoryBtn = document.getElementById('clearHistoryBtn');

    // Setup event listeners
    setupEventListeners();

    if (clearHistoryBtn) {
        clearHistoryBtn.addEventListener('click', clearPersistentHistory);
    }
    // Check API health
    checkAPIHealth();

    // Check Auth Status
    checkAuthStatus();

    // Init full-page auth flow + calorie tracker
    if (typeof initAuthAndTracker === 'function') initAuthAndTracker();

    console.log('✓ Application initialized');
});

/**
 * Setup all event listeners for the application
 */
function setupEventListeners() {
    // Upload zone click
    uploadZone.addEventListener('click', () => {
        fileInput.click();
    });

    // File input change
    fileInput.addEventListener('change', handleFileSelect);

    // Drag and drop events
    uploadZone.addEventListener('dragover', handleDragOver);
    uploadZone.addEventListener('dragleave', handleDragLeave);
    uploadZone.addEventListener('drop', handleDrop);

    // Predict button
    const predictBtn = document.getElementById('predictBtn');
    if (predictBtn) {
        predictBtn.addEventListener('click', handlePredict);
    }

    // Remove image button
    const removeBtn = document.getElementById('removeBtn');
    if (removeBtn) {
        removeBtn.addEventListener('click', handleRemoveImage);
    }

    // Portion selector (New flexible input)
    const recalculateBtn = document.getElementById('recalculateBtn');
    if (recalculateBtn) {
        recalculateBtn.addEventListener('click', handlePortionChange);
    }

    // Also trigger on unit change for better UX
    const portionUnitSelect = document.getElementById('portionUnit');
    if (portionUnitSelect) {
        portionUnitSelect.addEventListener('change', handlePortionChange);
    }

    // Search listeners
    if (searchBtn) searchBtn.addEventListener('click', handleSearch);
    if (foodSearchInput) {
        foodSearchInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') handleSearch();
        });
    }

    // Auth listeners
    if (loginBtn) loginBtn.addEventListener('click', () => {
        if (window.currentUser) {
            handleLogout();
        } else {
            showAuthModal('login');
        }
    });

    const closeAuthModal = document.getElementById('closeAuthModal');
    if (closeAuthModal) closeAuthModal.addEventListener('click', () => authModal.style.display = 'none');

    const toggleSignup = document.getElementById('toggleSignup');
    if (toggleSignup) toggleSignup.addEventListener('click', (e) => {
        e.preventDefault();
        showAuthModal('signup');
    });

    const toggleLogin = document.getElementById('toggleLogin');
    if (toggleLogin) toggleLogin.addEventListener('click', (e) => {
        e.preventDefault();
        showAuthModal('login');
    });

    const loginForm = document.getElementById('loginForm');
    if (loginForm) loginForm.addEventListener('submit', handleLogin);

    const signupForm = document.getElementById('signupForm');
    if (signupForm) signupForm.addEventListener('submit', handleSignup);

    // Profile listeners
    if (historyBtn) historyBtn.addEventListener('click', () => {
        profileModal.style.display = 'flex';
        fetchPersistentHistory();
    });

    const closeProfileModal = document.getElementById('closeProfileModal');
    if (closeProfileModal) closeProfileModal.addEventListener('click', () => profileModal.style.display = 'none');

    console.log('✓ Event listeners setup complete');
}

/**
 * Check if the backend API is healthy
 */
async function checkAPIHealth() {
    try {
        const response = await fetch(`${API_BASE_URL}/health`);
        const data = await response.json();

        if (data.status === 'healthy' && data.model_loaded) {
            console.log('✓ API is healthy and model is loaded');
        } else {
            console.warn('⚠ API is running but model may not be loaded');
        }
    } catch (error) {
        console.error('❌ Could not connect to API:', error);
        showError('Could not connect to the server. Please make sure the backend is running.');
    }
}

/**
 * Handle food search
 */
async function handleSearch() {
    const query = foodSearchInput.value.trim();
    if (!query) return;

    console.log('🔍 Searching for:', query);

    // Show loading state
    loadingSection.classList.add('active');
    resultsSection.classList.remove('active');

    // Clear and hide preview for searches (Privacy)
    if (previewImage) previewImage.src = '';
    if (previewSection) previewSection.classList.remove('active');
    window.selectedFile = null;
    if (fileInput) fileInput.value = '';

    try {
        const response = await fetch(`${API_BASE_URL}/search?q=${encodeURIComponent(query)}`);
        const data = await response.json();

        loadingSection.classList.remove('active');

        if (data.success) {
            console.log('✓ Search successful:', data.predicted_class);
            // Hide preview if searching
            previewSection.classList.remove('active');
            displayResults(data);
        } else {
            // "Wait for future updates" prompt logic
            showError(data.message || 'Item not found');
        }
    } catch (error) {
        console.error('❌ Search error:', error);
        loadingSection.classList.remove('active');
        showError('Search failed. Please try again.');
    }
}

/**
 * Auth Functions
 */

async function checkAuthStatus() {
    try {
        const response = await fetch(`${API_BASE_URL}/auth/status`);
        const data = await response.json();
        if (data.authenticated) {
            window.currentUser = data.username;
            updateAuthUI(true);
        }
    } catch (error) {
        console.error('Error checking auth status:', error);
    }
}

function showAuthModal(mode) {
    authModal.style.display = 'flex';
    const loginForm = document.getElementById('loginForm');
    const signupForm = document.getElementById('signupForm');
    const title = document.getElementById('authModalTitle');

    if (mode === 'login') {
        loginForm.style.display = 'block';
        signupForm.style.display = 'none';
        title.textContent = 'Login';
    } else {
        loginForm.style.display = 'none';
        signupForm.style.display = 'block';
        title.textContent = 'Sign Up';
    }
}

async function handleLogin(e) {
    e.preventDefault();
    const username = document.getElementById('loginUsername').value;
    const password = document.getElementById('loginPassword').value;

    try {
        const response = await fetch(`${API_BASE_URL}/auth/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();
        if (response.ok) {
            window.currentUser = data.username;
            updateAuthUI(true);
            authModal.style.display = 'none';
            // Show success toast
            showSuccessToast(`Welcome back, ${data.username}!`);
        } else {
            showError(data.error || 'Login failed');
        }
    } catch (error) {
        showError('Login failed. Please try again.');
    }
}

async function handleSignup(e) {
    e.preventDefault();
    const username = document.getElementById('signupUsername').value;
    const password = document.getElementById('signupPassword').value;

    try {
        const response = await fetch(`${API_BASE_URL}/auth/signup`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();
        if (response.ok) {
            // Show success, maybe switch to login or auto-login
            showSuccessToast('Account created! Please login.');
            showAuthModal('login');
        } else {
            showError(data.error || 'Signup failed');
        }
    } catch (error) {
        showError('Signup failed. Please try again.');
    }
}

async function handleLogout() {
    try {
        await fetch(`${API_BASE_URL}/auth/logout`);
        window.currentUser = null;
        updateAuthUI(false);
        showSuccessToast('Logged out successfully');
    } catch (error) {
        console.error('Logout failed');
    }
}

function updateAuthUI(isAuthenticated) {
    const loginBtn = document.getElementById('loginBtn');
    const historyBtn = document.getElementById('historyBtn');
    const profileLinkBtn = document.getElementById('profileLinkBtn');
    if (isAuthenticated) {
        loginBtn.innerHTML = `<i class="fas fa-sign-out-alt"></i> Logout (${window.currentUser})`;
        loginBtn.classList.remove('btn-secondary');
        loginBtn.classList.add('btn-primary');
        if (historyBtn) historyBtn.style.display = 'block';
        if (profileLinkBtn) profileLinkBtn.style.display = 'block';
    } else {
        loginBtn.innerHTML = `<i class="fas fa-sign-in-alt"></i> Login`;
        loginBtn.classList.remove('btn-primary');
        loginBtn.classList.add('btn-secondary');
        if (historyBtn) historyBtn.style.display = 'none';
        if (profileLinkBtn) profileLinkBtn.style.display = 'none';
    }
}

/**
 * Persistent History Functions
 */

async function saveToPersistentHistory(data) {
    if (!window.currentUser) return;

    try {
        await fetch(`${API_BASE_URL}/history/save`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                dish_name: data.predicted_class,
                calories: data.nutrition ? data.nutrition.nutrition.calories : 0,
                image_url: '' // Future: support image uploads
            })
        });
        console.log('✓ Scan saved to persistent history');
    } catch (error) {
        console.error('Error saving history:', error);
    }
}

async function fetchPersistentHistory() {
    try {
        const response = await fetch(`${API_BASE_URL}/history`);
        const data = await response.json();
        if (data.success) {
            displayPersistentHistory(data.history);
        }
    } catch (error) {
        console.error('Error fetching history:', error);
        persistentHistoryList.innerHTML = '<p class="text-center" style="color: #ff6b6b;">Error loading history</p>';
    }
}

function displayPersistentHistory(history) {
    if (!history || history.length === 0) {
        persistentHistoryList.innerHTML = '<p class="text-center" style="color: var(--text-muted);">No history found. Start scanning!</p>';
        return;
    }

    persistentHistoryList.innerHTML = history.map(item => {
        const date = new Date(item.timestamp).toLocaleDateString();
        const time = new Date(item.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        return `
            <div class="history-item" style="display: flex; justify-content: space-between; align-items: center; padding: 1rem; margin-bottom: 0.5rem; background: rgba(255,255,255,0.03); border-radius: 8px; border-left: 4px solid var(--accent-color);">
                <div>
                    <strong style="display: block; color: var(--text-primary);">${item.dish_name}</strong>
                    <span style="font-size: 0.8rem; color: var(--text-muted);">${date} at ${time}</span>
                </div>
                <div style="text-align: right;">
                    <div style="font-weight: bold; color: var(--accent-color);">${item.calories} kcal</div>
                </div>
            </div>
        `;
    }).join('');
}

function showSuccessToast(message) {
    const toast = document.createElement('div');
    toast.className = 'glass-card animate-slide-in-right';
    toast.style.cssText = `
        position: fixed; top: 20px; right: 20px; z-index: 1000;
        background: rgba(46, 204, 113, 0.2); border: 1px solid rgba(46, 204, 113, 0.5);
        padding: 1rem 1.5rem; border-radius: 12px; color: white;
    `;
    toast.innerHTML = `<i class="fas fa-check-circle"></i> ${message}`;
    document.body.appendChild(toast);
    setTimeout(() => {
        toast.style.opacity = '0';
        setTimeout(() => toast.remove(), 500);
    }, 3000);
}

/**
 * Handle drag over event
 */
function handleDragOver(e) {
    e.preventDefault();
    e.stopPropagation();
    uploadZone.classList.add('dragover');
}

/**
 * Handle drag leave event
 */
function handleDragLeave(e) {
    e.preventDefault();
    e.stopPropagation();
    uploadZone.classList.remove('dragover');
}

/**
 * Handle drop event
 */
function handleDrop(e) {
    e.preventDefault();
    e.stopPropagation();
    uploadZone.classList.remove('dragover');

    const files = e.dataTransfer.files;
    if (files.length > 0) {
        handleFile(files[0]);
    }
}

/**
 * Handle file selection from input
 */
function handleFileSelect(e) {
    const files = e.target.files;
    if (files.length > 0) {
        handleFile(files[0]);
    }
}

/**
 * Process the selected file
 */
function handleFile(file) {
    // Validate file type
    // Validate file type
    const validTypes = ['image/jpeg', 'image/jpg', 'image/png', 'image/gif', 'image/bmp', 'image/webp'];
    if (!validTypes.includes(file.type)) {
        showError('Please select a valid image file (JPG, PNG, GIF, BMP, WEBP)');
        return;
    }

    // Validate file size (16MB max)
    const maxSize = 16 * 1024 * 1024; // 16MB
    if (file.size > maxSize) {
        showError('File size must be less than 16MB');
        return;
    }

    console.log('✓ File selected:', file.name);

    // Read and display the image
    const reader = new FileReader();
    reader.onload = function (e) {
        previewImage.src = e.target.result;
        previewSection.classList.add('active');
        resultsSection.classList.remove('active');
    };
    reader.readAsDataURL(file);

    // Store the file for later upload
    window.selectedFile = file;
}

/**
 * Handle image removal
 */
function handleRemoveImage() {
    previewSection.classList.remove('active');
    resultsSection.classList.remove('active');
    fileInput.value = '';
    window.selectedFile = null;
    console.log('✓ Image removed');
}

/**
 * Handle prediction request
 */
async function handlePredict() {
    if (!window.selectedFile) {
        showError('Please select an image first');
        return;
    }

    console.log('🔮 Starting prediction...');

    // Show loading state
    loadingSection.classList.add('active');
    resultsSection.classList.remove('active');

    // Create form data
    const formData = new FormData();
    formData.append('file', window.selectedFile);

    try {
        // Send prediction request
        const response = await fetch(`${API_BASE_URL}/predict`, {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        // Hide loading
        loadingSection.classList.remove('active');

        if (response.ok && data.success) {
            console.log('✓ Prediction successful:', data.predicted_class);
            displayResults(data);
        } else {
            throw new Error(data.message || 'Prediction failed');
        }

    } catch (error) {
        console.error('❌ Prediction error:', error);
        loadingSection.classList.remove('active');
        showError(error.message || 'An error occurred during prediction. Please try again.');
    }
}

/**
 * Display prediction results
 */
function displayResults(data) {
    // Update predicted dish
    document.getElementById('predictedDish').textContent = data.predicted_class;

    // Update confidence score
    document.getElementById('confidenceScore').textContent = `${data.confidence}%`;

    // Update top 3 predictions
    const top3Container = document.getElementById('top3Predictions');
    top3Container.innerHTML = '';

    if (data.top_3 && Array.isArray(data.top_3)) {
        data.top_3.forEach((prediction, index) => {
            const item = createPredictionItem(prediction, index + 1);
            if (item) top3Container.appendChild(item);
        });
    } else {
        // Just show the primary match if top_3 missing (fallback)
        const item = createPredictionItem({ class: data.predicted_class, confidence: data.confidence }, 1);
        if (item) top3Container.appendChild(item);
    }

    // Results Display with Staggered Animation
    if (data.nutrition) {
        const warningContainer = document.getElementById('allergyWarningContainer');
        if (warningContainer) {
            if (data.warnings) {
                warningContainer.style.display = 'block';
                warningContainer.innerHTML = `<i class="fas fa-exclamation-triangle" style="color: #ffccd5; font-size: 1.5rem; margin-right: 0.5rem; vertical-align: middle;"></i> <strong style="vertical-align: middle;">${data.warnings}</strong>`;
            } else {
                warningContainer.style.display = 'none';
                warningContainer.innerHTML = '';
            }
        }

        // Add slight delay for nutrition info to let the main card expand first
        setTimeout(() => {
            displayNutritionInfo(data.nutrition, data.predicted_class, data.health_indicators);
            renderHealthScoreMeter(data.health_score);
            renderDietarySuitability(data.suitability);
            updateDailySummary(data);
            // Log to calorie tracker + meal log
            if (typeof logScanToTracker === 'function') logScanToTracker(data);
        }, 300);
    }

    // Show success animation
    showSuccessAnimation();

    // Save to local history - REDUNDANT (now handled inside updateDailySummary)
    // saveToHistory(data);

    // Save to persistent backend history if logged in
    saveToPersistentHistory(data);

    // Show results section with animation
    setTimeout(() => {
        resultsSection.classList.add('active');
        resultsSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

        // Show portion selector
        const portionSelector = document.getElementById('portionSelector');
        if (portionSelector) {
            portionSelector.style.display = 'block';
            // Reset to medium
            const mediumBtn = document.querySelector('input[name="portion"][value="medium"]');
            if (mediumBtn) mediumBtn.checked = true;
        }
    }, 100);

    console.log('✓ Results displayed');
}

/**
 * Create a prediction item element
 */
function createPredictionItem(prediction, rank) {
    const item = document.createElement('div');
    item.className = 'prediction-item';

    const header = document.createElement('div');
    header.className = 'prediction-header';

    const dishName = document.createElement('span');
    dishName.className = 'dish-name';
    const className = prediction.class || prediction.predicted_class || 'Unknown';
    dishName.textContent = `${rank}. ${className}`;

    const confidenceValue = document.createElement('span');
    confidenceValue.className = 'confidence-value';
    const confidence = typeof prediction.confidence === 'number' ? prediction.confidence : 0;
    confidenceValue.textContent = `${confidence.toFixed(2)}%`;

    header.appendChild(dishName);
    header.appendChild(confidenceValue);

    const bar = document.createElement('div');
    bar.className = 'confidence-bar';

    const fill = document.createElement('div');
    fill.className = 'confidence-fill';
    fill.style.width = '0%';

    // Animate the bar
    setTimeout(() => {
        fill.style.width = `${prediction.confidence}%`;
    }, 100 * rank);

    bar.appendChild(fill);
    item.appendChild(header);
    item.appendChild(bar);

    return item;
}

/**
 * Show error message
 */
function showError(message) {
    // Create error notification
    const errorDiv = document.createElement('div');
    errorDiv.className = 'glass-card';
    errorDiv.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        max-width: 400px;
        background: rgba(245, 87, 108, 0.2);
        border: 1px solid rgba(245, 87, 108, 0.5);
        padding: 1rem 1.5rem;
        border-radius: 12px;
        z-index: 1000;
        animation: slideInRight 0.3s ease;
    `;

    errorDiv.innerHTML = `
        <div style="display: flex; align-items: center; gap: 1rem;">
            <span style="font-size: 1.5rem;">⚠️</span>
            <div>
                <strong style="color: #fff;">Error</strong>
                <p style="margin: 0; color: #ffccd5;">${message}</p>
            </div>
        </div>
    `;

    document.body.appendChild(errorDiv);

    // Remove after 5 seconds
    setTimeout(() => {
        errorDiv.style.animation = 'slideOutRight 0.3s ease';
        setTimeout(() => errorDiv.remove(), 300);
    }, 5000);

    console.error('❌ Error:', message);
}

/**
 * Handle sample image click
 */
function handleSampleClick(imagePath, dishName) {
    console.log('📸 Sample image clicked:', dishName);

    // Load the sample image
    fetch(imagePath)
        .then(response => response.blob())
        .then(blob => {
            const file = new File([blob], `${dishName}.jpg`, { type: 'image/jpeg' });
            handleFile(file);
        })
        .catch(error => {
            console.error('Error loading sample image:', error);
            showError('Could not load sample image');
        });
}

/**
 * Display nutrition information
 */
function displayNutritionInfo(nutrition, dishName, healthIndicators) {
    const nutritionSection = document.getElementById('nutritionSection');
    if (!nutritionSection) {
        console.warn('Nutrition section not found in HTML');
        return;
    }

    // Clear previous content
    nutritionSection.innerHTML = '';

    // Create nutrition card
    const nutritionCard = document.createElement('div');
    nutritionCard.className = 'glass-card nutrition-card';
    nutritionCard.style.cssText = 'margin-top: 1.5rem; animation: fadeIn 0.5s ease;';

    // Build nutrition HTML
    nutritionCard.innerHTML = `
        <h3 style="margin-bottom: 1rem; color: var(--primary-color); display: flex; align-items: center; gap: 0.5rem;">
            <span>🥗</span>
            <span>Nutrition Information</span>
        </h3>

        ${createHealthBadges(healthIndicators)}
        ${createDietaryBadges(nutrition.dietary_info)}
        ${createNutritionFacts(nutrition.nutrition, nutrition.serving_size)}
        ${createMacroVisualization(nutrition.nutrition)}
        ${createAdditionalInfo(nutrition)}
    `;

    nutritionSection.appendChild(nutritionCard);
    console.log('✓ Nutrition information displayed');
}

/**
 * Create health indicator badges
 */
function createHealthBadges(healthIndicators) {
    if (!healthIndicators || healthIndicators.length === 0) {
        return '';
    }

    const badges = healthIndicators.map(indicator => `
        <span class="health-badge" style="
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: linear-gradient(135deg, rgba(78, 205, 196, 0.2), rgba(68, 163, 160, 0.1));
            border: 1px solid rgba(78, 205, 196, 0.4);
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.875rem;
            color: #4ecdc4;
            font-weight: 500;
        " title="${indicator.description}">
            <span style="font-size: 1.2rem;">${indicator.icon}</span>
            <span>${indicator.badge}</span>
        </span>
    `).join('');

    return `
        <div class="health-badges" style="display: flex; flex-wrap: wrap; gap: 0.75rem; margin-bottom: 1.5rem; padding-bottom: 1rem; border-bottom: 1px solid rgba(255,255,255,0.1);">
            ${badges}
        </div>
    `;
}

/**
 * Create dietary badges
 */
function createDietaryBadges(dietaryInfo) {
    const badges = [];

    if (dietaryInfo.vegetarian) {
        badges.push('<span class="dietary-badge veg">🌱 Vegetarian</span>');
    }
    if (dietaryInfo.vegan) {
        badges.push('<span class="dietary-badge vegan">🌿 Vegan</span>');
    }
    if (dietaryInfo.gluten_free) {
        badges.push('<span class="dietary-badge gf">🌾 Gluten-Free</span>');
    }
    if (dietaryInfo.dairy_free) {
        badges.push('<span class="dietary-badge df">🥛 Dairy-Free</span>');
    }
    if (dietaryInfo.spicy) {
        badges.push('<span class="dietary-badge spicy">🌶️ Spicy</span>');
    }

    if (badges.length === 0) return '';

    return `
        <div class="dietary-badges" style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 1.5rem;">
            ${badges.join('')}
        </div>
    `;
}

/**
 * Create nutrition facts table
 */
function createNutritionFacts(nutrition, servingSize) {
    return `
        <div class="nutrition-facts">
            <div style="background: rgba(255,255,255,0.05); padding: 0.75rem; border-radius: 8px; margin-bottom: 1rem;">
                <strong>Serving Size:</strong> ${servingSize}
            </div>
            
            <table class="nutrition-table" style="width: 100%; border-collapse: collapse;">
                <tr style="border-bottom: 2px solid rgba(255,255,255,0.1);">
                    <th style="text-align: left; padding: 0.75rem 0; color: var(--primary-color);">Nutrient</th>
                    <th style="text-align: right; padding: 0.75rem 0; color: var(--primary-color);">Amount</th>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                    <td style="padding: 0.75rem 0;"><strong>Calories</strong></td>
                    <td style="text-align: right; padding: 0.75rem 0;"><strong>${nutrition.calories} kcal</strong></td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                    <td style="padding: 0.75rem 0;">Protein</td>
                    <td style="text-align: right; padding: 0.75rem 0;">${nutrition.protein_g}g</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                    <td style="padding: 0.75rem 0;">Carbohydrates</td>
                    <td style="text-align: right; padding: 0.75rem 0;">${nutrition.carbs_g}g</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                    <td style="padding: 0.75rem 0;">Fats</td>
                    <td style="text-align: right; padding: 0.75rem 0;">${nutrition.fats_g}g</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                    <td style="padding: 0.75rem 0;">Fiber</td>
                    <td style="text-align: right; padding: 0.75rem 0;">${nutrition.fiber_g}g</td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.05);">
                    <td style="padding: 0.75rem 0;">Sugar</td>
                    <td style="text-align: right; padding: 0.75rem 0;">${nutrition.sugar_g}g</td>
                </tr>
                <tr>
                    <td style="padding: 0.75rem 0;">Sodium</td>
                    <td style="text-align: right; padding: 0.75rem 0;">${nutrition.sodium_mg}mg</td>
                </tr>
            </table>
        </div>
    `;
}

/**
 * Create macro visualization bars
 */
function createMacroVisualization(nutrition) {
    const total = nutrition.protein_g + nutrition.carbs_g + nutrition.fats_g;
    const proteinPercent = (nutrition.protein_g / total * 100).toFixed(1);
    const carbsPercent = (nutrition.carbs_g / total * 100).toFixed(1);
    const fatsPercent = (nutrition.fats_g / total * 100).toFixed(1);

    return `
        <div class="macro-visualization" style="margin-top: 1.5rem;">
            <h4 style="margin-bottom: 1.5rem; color: var(--text-color); text-align: center;">Macronutrient Distribution</h4>
            
            <div class="circular-charts">
                ${createCircularChart('Protein', nutrition.protein_g, proteinPercent, 'protein', '#ff6b6b', '#ff8787')}
                ${createCircularChart('Carbs', nutrition.carbs_g, carbsPercent, 'carbs', '#4ecdc4', '#44a3a0')}
                ${createCircularChart('Fats', nutrition.fats_g, fatsPercent, 'fats', '#f7b731', '#f39c12')}
            </div>
        </div>
    `;
}

/**
 * Create circular SVG chart
 */
function createCircularChart(name, value, percentage, type, color1, color2) {
    const radius = 50;
    const circumference = 2 * Math.PI * radius;
    const offset = circumference - (percentage / 100) * circumference;

    return `
        <div class="circular-chart animate-fade-in delay-${type === 'protein' ? '1' : type === 'carbs' ? '2' : '3'}">
            <svg class="circular-chart-svg" viewBox="0 0 120 120">
                <defs>
                    <linearGradient id="${type}Gradient" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" stop-color="${color1}" />
                        <stop offset="100%" stop-color="${color2}" />
                    </linearGradient>
                </defs>
                <circle class="circular-bg" cx="60" cy="60" r="${radius}" />
                <circle 
                    class="circular-progress ${type}" 
                    cx="60" 
                    cy="60" 
                    r="${radius}"
                    stroke-dasharray="${circumference}"
                    stroke-dashoffset="${offset}"
                />
                <text x="60" y="65" text-anchor="middle" fill="white" font-size="20" font-weight="bold" transform="rotate(90 60 60)">
                    ${percentage}%
                </text>
            </svg>
            <div class="circular-label">
                <span class="circular-value">${value}g</span>
                <div class="circular-name">${name}</div>
            </div>
        </div>
    `;
}

/**
 * Show success animation after prediction
 */
function showSuccessAnimation() {
    // Create success toast
    const toast = document.createElement('div');
    toast.className = 'success-toast';
    toast.innerHTML = `
        <span style="font-size: 1.5rem;">✓</span>
        <span>Classification Complete!</span>
    `;
    document.body.appendChild(toast);

    // Remove toast after animation
    setTimeout(() => {
        toast.remove();
    }, 2500);

    // Create ripple ring effect
    const ripple = document.createElement('div');
    ripple.className = 'ripple-ring';
    document.body.appendChild(ripple);

    setTimeout(() => {
        ripple.remove();
    }, 1000);

    // Add pulse to results section
    setTimeout(() => {
        const resultsSection = document.getElementById('resultsSection');
        if (resultsSection) {
            resultsSection.classList.add('pulse-success');
            setTimeout(() => {
                resultsSection.classList.remove('pulse-success');
            }, 800);
        }
    }, 100);
}

/**
 * Create additional nutrition info
 */
function createAdditionalInfo(nutrition) {
    let allergenText = 'None';
    if (nutrition.allergens && nutrition.allergens.length > 0) {
        allergenText = nutrition.allergens.map(a => a.charAt(0).toUpperCase() + a.slice(1)).join(', ');
    }

    return `
        <div class="additional-info" style="margin-top: 1.5rem; padding-top: 1.5rem; border-top: 1px solid rgba(255,255,255,0.1);">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
                <div>
                    <div style="color: var(--text-secondary); font-size: 0.875rem; margin-bottom: 0.25rem;">Region</div>
                    <div style="color: var(--text-color); font-weight: 500;">${nutrition.region}</div>
                </div>
                <div>
                    <div style="color: var(--text-secondary); font-size: 0.875rem; margin-bottom: 0.25rem;">Category</div>
                    <div style="color: var(--text-color); font-weight: 500;">${nutrition.category}</div>
                </div>
                <div>
                    <div style="color: var(--text-secondary); font-size: 0.875rem; margin-bottom: 0.25rem;">Allergens</div>
                    <div style="color: ${nutrition.allergens && nutrition.allergens.length > 0 ? '#ff6b6b' : '#4ecdc4'}; font-weight: 500;">${allergenText}</div>
                </div>
            </div>
            <div style="margin-top: 1rem; padding: 1rem; background: rgba(255,255,255,0.05); border-radius: 8px; font-size: 0.875rem; line-height: 1.6;">
                ${nutrition.description}
            </div>
        </div>
    `;
}

// Add CSS for animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOutRight {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

/**
 * Handle portion size change (Legacy radio buttons or new input)
 */
async function handlePortionChange() {
    const qtyInput = document.getElementById('portionQuantity');
    const unitSelect = document.getElementById('portionUnit');
    const currentDish = document.getElementById('predictedDish').textContent;

    if (!qtyInput || !unitSelect) return;

    const qty = qtyInput.value;
    const unit = unitSelect.value;

    console.log(`⚖️ Portion updated: ${qty} ${unit} for ${currentDish}`);

    try {
        const response = await fetch(`${API_BASE_URL}/nutrition/${encodeURIComponent(currentDish)}?q=${qty}&u=${unit}`);
        const data = await response.json();

        if (data.success && data.nutrition) {
            displayNutritionInfo(data.nutrition, currentDish, data.health_indicators);
            if (data.health_score) renderHealthScoreMeter(data.health_score);
            if (data.suitability) renderDietarySuitability(data.suitability);

            // Note: We don't automatically update daily summary/history on portion change 
            // to avoid cluttering history with every small adjustment. 
            // The user would need to "save" or it's saved on initial prediction.
        }
    } catch (error) {
        console.error('Error updating portion:', error);
        showError('Could not update nutrition info');
    }
}

/* ============================================================================
   HISTORY SIDEBAR FUNCTIONALITY
   ============================================================================ */

/**
 * Save prediction to history
 */

function saveToHistory(data, session) {
    try {
        // --- DE-DUPLICATION CHECK ---
        const lastSaveTime = window._lastSaveTime || 0;
        const now = Date.now();
        const lastDish = window._lastSaveDish || "";

        // If saved in the last 2 seconds and same dish, skip
        if (now - lastSaveTime < 2000 && lastDish === data.predicted_class) {
            console.log('🛡️ Duplicate history save prevented');
            return;
        }

        window._lastSaveTime = now;
        window._lastSaveDish = data.predicted_class;
        // -----------------------------

        // Get existing history
        let history = JSON.parse(localStorage.getItem('foodsight_history') || '[]');

        // Create history entry
        const entry = {
            id: now, // Use precise timestamp
            timestamp: new Date().toISOString(),
            date: new Date().toLocaleDateString(),
            time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
            dish: data.predicted_class,
            calories: Math.round(data.nutrition.calories || (data.nutrition.nutrition ? data.nutrition.nutrition.calories : 0)),
            session: session || getCurrentSession(),
            confidence: data.confidence,
            nutrition: data.nutrition,
            health_indicators: data.health_indicators
        };

        // Add to beginning and limit to 50 items
        history.unshift(entry);
        history = history.slice(0, 50);

        // Save back to localStorage
        localStorage.setItem('foodsight_history', JSON.stringify(history));

        // Update history UI if sidebar is open
        renderHistorySidebar();

        // Also update Streak
        calculateStreak();

    } catch (error) {
        console.error('Error saving to history:', error);
    }
}

/**
 * Load and render history sidebar
 */
function renderHistorySidebar() {
    const historyList = document.getElementById('historyList');
    if (!historyList) return;

    try {
        const history = JSON.parse(localStorage.getItem('foodsight_history') || '[]');

        if (history.length === 0) {
            historyList.innerHTML = `
                <div class="history-empty">
                    <p>No recent scans yet.</p>
                    <p style="font-size: 0.9rem; margin-top: 0.5rem;">Your predictions will appear here!</p>
                </div>
            `;
            return;
        }

        historyList.innerHTML = history
            .filter(entry => entry.dish && entry.dish !== 'undefined') // Filter invalid entries
            .map((entry, index) => {
                const timeAgo = getTimeAgo(new Date(entry.timestamp));
                return `
                <div class="history-item animate-fade-in delay-${Math.min(index + 1, 5)}" data-index="${index}">
                    <div class="history-details-compact">
                        <div class="history-dish-name">${entry.dish}</div>
                        <div class="history-meta">
                            <span class="history-confidence">${entry.confidence.toFixed(1)}%</span> • 
                            <span class="history-time">${timeAgo}</span>
                        </div>
                    </div>
                </div>
            `;
            }).join('');

        // Add click handlers
        document.querySelectorAll('.history-item').forEach(item => {
            item.addEventListener('click', () => {
                const index = parseInt(item.dataset.index);
                loadHistoryItem(index);
            });
        });

    } catch (error) {
        console.error('Error rendering history:', error);
    }
}

/**
 * Load a history item and display it
 */
function loadHistoryItem(index) {
    try {
        const history = JSON.parse(localStorage.getItem('foodsight_history') || '[]');
        const entry = history[index];

        if (!entry) return;

        // Reconstruct data format
        const data = {
            predicted_class: entry.dish,
            confidence: entry.confidence,
            nutrition: entry.nutrition,
            health_indicators: entry.health_indicators || [],
            top_3: [] // Not saved in history
        };

        // Set preview image removed for privacy in history loading
        // previewImage.src = entry.thumbnail;
        // previewSection.classList.add('active');

        // Display results
        document.getElementById('predictedDish').textContent = data.predicted_class;
        document.getElementById('confidenceScore').textContent = `${data.confidence}%`;

        if (data.nutrition) {
            displayNutritionInfo(data.nutrition, data.predicted_class, data.health_indicators);
        }

        resultsSection.classList.add('active');
        resultsSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

        // Close sidebar
        toggleHistorySidebar();

        console.log('✓ Loaded history item:', entry.dish);

    } catch (error) {
        console.error('Error loading history item:', error);
    }
}

/**
 * Toggle history sidebar
 */
function toggleHistorySidebar() {
    const sidebar = document.getElementById('historySidebar');
    if (sidebar) {
        sidebar.classList.toggle('active');
        if (sidebar.classList.contains('active')) {
            renderHistorySidebar();
        }
    }
}

/**
 * Get relative time string
 */
function getTimeAgo(date) {
    const seconds = Math.floor((new Date() - date) / 1000);

    if (seconds < 60) return 'Just now';
    if (seconds < 3600) return `${Math.floor(seconds / 60)}m ago`;
    if (seconds < 86400) return `${Math.floor(seconds / 3600)}h ago`;
    return `${Math.floor(seconds / 86400)}d ago`;
}

/**
 * Initialize history sidebar on page load
 */
function initHistorySidebar() {
    // Add history button if it doesn't exist
    if (!document.getElementById('historyToggle')) {
        const toggleBtn = document.createElement('button');
        toggleBtn.id = 'historyToggle';
        toggleBtn.className = 'history-toggle';
        toggleBtn.innerHTML = '📜 History';
        toggleBtn.addEventListener('click', toggleHistorySidebar);
        document.body.appendChild(toggleBtn);
    }

    // Add sidebar if it doesn't exist
    if (!document.getElementById('historySidebar')) {
        const sidebar = document.createElement('div');
        sidebar.id = 'historySidebar';
        sidebar.className = 'history-sidebar';
        sidebar.innerHTML = `
            <div class="history-header">
                <h3>Recent Scans</h3>
                <button class="history-close" onclick="toggleHistorySidebar()">×</button>
            </div>
            <div id="historyList" class="history-list"></div>
        `;
        document.body.appendChild(sidebar);
    }
}


/* ============================================================================
   ABOUT MODAL FUNCTIONALITY
   ============================================================================ */

function initAboutModal() {
    const modal = document.getElementById('aboutModal');
    const btn = document.getElementById('aboutLink');
    const closeBtn = document.getElementById('closeModal');

    if (!modal || !btn || !closeBtn) return;

    // Open modal
    btn.onclick = function (e) {
        e.preventDefault();
        modal.style.display = "block";
    }

    // Close modal
    closeBtn.onclick = function () {
        modal.style.display = "none";
    }

    // Close on outside click
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    // Close on Escape key
    document.addEventListener('keydown', function (event) {
        if (event.key === "Escape" && modal.style.display === "block") {
            modal.style.display = "none";
        }
    });
}

/* ============================================================================
   INITIALIZATION
   ============================================================================ */

/* ============================================================================
   ADVANCED NUTRITION & HEALTH LOGIC
   ============================================================================ */

/**
 * Render Health Score Meter (Semi-circular gauge)
 */
function renderHealthScoreMeter(score) {
    const container = document.getElementById('healthScoreMeter');
    if (!container) return;

    const percentage = score || 0;
    const radius = 60;
    const circumference = 2 * Math.PI * radius;
    const offset = circumference - (percentage / 100) * circumference;

    // Determine color based on score
    let color = '#f5576c'; // Red (Bad)
    if (percentage > 40) color = '#f7b731'; // Orange (Average)
    if (percentage > 70) color = '#2ecc71'; // Green (Good)

    container.innerHTML = `
        <svg class="health-meter-svg" viewBox="0 0 140 140">
            <circle class="health-meter-bg" cx="70" cy="70" r="${radius}" />
            <circle class="health-meter-progress" 
                cx="70" cy="70" r="${radius}"
                stroke="${color}"
                stroke-dasharray="${circumference}"
                stroke-dashoffset="${circumference}"
            />
        </svg>
        <div class="health-score-text">
            <span class="score-value" style="color: ${color}">${percentage}</span>
            <span class="score-label">Health Score</span>
        </div>
    `;

    // Animate the meter
    setTimeout(() => {
        const progressCircle = container.querySelector('.health-meter-progress');
        if (progressCircle) {
            progressCircle.style.strokeDashoffset = offset;
        }
    }, 100);
}

/**
 * Render Dietary Suitability Recommendations
 */
function renderDietarySuitability(suitability) {
    const container = document.getElementById('suitabilitySection');
    if (!container || !suitability) return;

    const { recommended_for, avoid_for } = suitability;

    container.innerHTML = `
        <h3 style="margin-bottom: 1rem; color: var(--primary-color);">👨‍⚕️ Dietary Suitability</h3>
        <div class="suitability-grid">
            <div class="suitability-column">
                <h4>✅ Recommended For</h4>
                <div class="suitability-list">
                    ${recommended_for.length > 0
            ? recommended_for.map(item => `
                            <div class="suitability-item can">
                                <strong>${item.target}</strong>
                                <span>${item.reason}</span>
                            </div>
                        `).join('')
            : '<div class="suitability-item"><span>Generally safe for most adults</span></div>'}
                </div>
            </div>
            <div class="suitability-column">
                <h4 style="color: #ff4d4d;">🚫 Health Precautions</h4>
                <div class="suitability-list">
                    ${avoid_for.length > 0
            ? avoid_for.map(item => `
                            <div class="suitability-item cannot">
                                <strong>${item.target}</strong>
                                <span>${item.reason}</span>
                            </div>
                        `).join('')
            : '<div class="suitability-item"><span>No specific dietary warnings</span></div>'}
                </div>
            </div>
        </div>
    `;
}

/**
 * Get current session based on time of day
 */
function getCurrentSession() {
    const hour = new Date().getHours();
    if (hour >= 5 && hour < 11) return 'Breakfast';
    if (hour >= 11 && hour < 16) return 'Lunch';
    if (hour >= 16 && hour < 19) return 'Snack';
    return 'Dinner';
}

/**
 * Update and Persist Session-Wise Nutrition Summary
 */
function updateDailySummary(data) {
    try {
        if (!data.nutrition) return;

        const today = new Date().toLocaleDateString();
        let summary = JSON.parse(localStorage.getItem('foodsight_daily_summary') || 'null');

        // Reset if it's a new day or old format
        if (!summary || summary.date !== today || !summary.sessions) {
            summary = {
                date: today,
                sessions: {
                    'Breakfast': { calories: 0, protein: 0, carbs: 0, fats: 0, count: 0 },
                    'Lunch': { calories: 0, protein: 0, carbs: 0, fats: 0, count: 0 },
                    'Snack': { calories: 0, protein: 0, carbs: 0, fats: 0, count: 0 },
                    'Dinner': { calories: 0, protein: 0, carbs: 0, fats: 0, count: 0 }
                },
                total: { calories: 0, protein: 0, carbs: 0, fats: 0, count: 0 }
            };
        }

        const rootNutrition = data.nutrition;
        if (!rootNutrition || !rootNutrition.nutrition) return;
        const nutrition = rootNutrition.nutrition;

        // Get selected session from UI or auto-detect
        const sessionSelect = document.getElementById('sessionSelect');
        const session = sessionSelect ? sessionSelect.value : getCurrentSession();

        // Update Session
        const s = summary.sessions[session];
        s.calories = (s.calories || 0) + Math.round(nutrition.calories || 0);
        s.protein = (s.protein || 0) + Math.round(nutrition.protein_g || 0);
        s.carbs = (s.carbs || 0) + Math.round(nutrition.carbs_g || 0);
        s.fats = (s.fats || 0) + Math.round(nutrition.fats_g || 0);
        s.count = (s.count || 0) + 1;

        // Update Total
        const t = summary.total;
        t.calories = (t.calories || 0) + Math.round(nutrition.calories || 0);
        t.protein = (t.protein || 0) + Math.round(nutrition.protein_g || 0);
        t.carbs = (t.carbs || 0) + Math.round(nutrition.carbs_g || 0);
        t.fats = (t.fats || 0) + Math.round(nutrition.fats_g || 0);
        t.count = (t.count || 0) + 1;

        localStorage.setItem('foodsight_daily_summary', JSON.stringify(summary));

        // Pass full data and session to saveToHistory
        saveToHistory(data, session);

        renderDailySummary();
        renderHistory(); // Refresh history UI if open


    } catch (error) {
        console.error('Error updating daily summary:', error);
    }
}

/**
 * Update History Log
 */


/**
 * Calculate and Render Streak
 */
function calculateStreak() {
    try {
        let history = JSON.parse(localStorage.getItem('foodsight_history') || '[]');
        if (history.length === 0) return;

        const uniqueDates = [...new Set(history.map(item => item.date))].sort((a, b) => new Date(b) - new Date(a));
        let streak = 0;
        let today = new Date().toLocaleDateString();

        // If logged today, streak starts at 1
        if (uniqueDates.includes(today)) {
            streak = 1;
            let checks = 1;
            // Check previous days
            while (true) {
                let prevDate = new Date();
                prevDate.setDate(prevDate.getDate() - checks);
                if (uniqueDates.includes(prevDate.toLocaleDateString())) {
                    streak++;
                    checks++;
                } else {
                    break;
                }
            }
        }

        document.getElementById('streakCount').innerText = streak;
    } catch (e) {
        console.error("Error calculating streak", e);
    }
}

/**
 * Render History Modal List
 */
function renderHistory() {
    const list = document.getElementById('historyList');
    if (!list) return;

    const history = JSON.parse(localStorage.getItem('foodsight_history') || '[]');
    if (history.length === 0) {
        list.innerHTML = '<p style="text-align: center; color: var(--text-muted); padding: 1rem;">No meals logged yet. Start scanning!</p>';
        return;
    }

    list.innerHTML = history
        .filter(item => item.dish && item.dish !== 'undefined') // Filter invalid entries
        .map(item => `
        <div class="history-item">
            <div class="history-details">
                <h4>${item.dish}</h4>
                <p>${item.session || 'Snack'} • ${item.date} ${item.time || item.timestamp}</p>
            </div>
            <div style="font-weight: bold; color: var(--success-color);">
                ${item.calories} kcal
            </div>
        </div>
    `).join('');
}

/* ============================================================================
   CAMERA FUNCTIONALITY
   ============================================================================ */

let cameraStream = null;
let useFrontCamera = false;

function initCameraFeatures() {
    const cameraBtn = document.getElementById('cameraBtn');
    const closeBtn = document.getElementById('closeCameraModal');
    const captureBtn = document.getElementById('captureBtn');
    const switchBtn = document.getElementById('switchCameraBtn');
    const modal = document.getElementById('cameraModal');

    if (cameraBtn) {
        cameraBtn.addEventListener('click', () => {
            modal.style.display = 'block';
            startCamera();
        });
    }

    if (closeBtn) {
        closeBtn.addEventListener('click', () => {
            closeCamera();
        });
    }

    if (captureBtn) {
        captureBtn.addEventListener('click', captureImage);
    }

    if (switchBtn) {
        switchBtn.addEventListener('click', () => {
            useFrontCamera = !useFrontCamera;
            startCamera();
        });
    }

    // Close on outside click
    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeCamera();
        }
    });
}

async function startCamera() {
    const video = document.getElementById('cameraVideo');
    stopCamera(); // Stop existing stream if any

    const constraints = {
        video: {
            facingMode: useFrontCamera ? 'user' : 'environment',
            width: { ideal: 1280 },
            height: { ideal: 720 }
        }
    };

    try {
        cameraStream = await navigator.mediaDevices.getUserMedia(constraints);
        video.srcObject = cameraStream;
    } catch (err) {
        console.error("Error accessing camera:", err);
        showError("Could not access camera. Please allow permissions.");
    }
}

function stopCamera() {
    if (cameraStream) {
        cameraStream.getTracks().forEach(track => track.stop());
        cameraStream = null;
    }
}

function closeCamera() {
    document.getElementById('cameraModal').style.display = 'none';
    stopCamera();
}

function captureImage() {
    const video = document.getElementById('cameraVideo');
    const canvas = document.getElementById('cameraCanvas');

    if (!video.videoWidth) return;

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    const ctx = canvas.getContext('2d');
    if (useFrontCamera) {
        ctx.scale(-1, 1); // Mirror if front camera
        ctx.drawImage(video, -canvas.width, 0, canvas.width, canvas.height);
    } else {
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    }

    canvas.toBlob((blob) => {
        const file = new File([blob], `capture_${Date.now()}.jpg`, { type: 'image/jpeg' });
        handleFile(file);
        closeCamera();
    }, 'image/jpeg', 0.9);
}

/* ============================================================================
   SHARE CARD FUNCTIONALITY
   ============================================================================ */

function initShareFeature() {
    const shareBtn = document.getElementById('shareBtn');
    if (shareBtn) {
        shareBtn.addEventListener('click', generateShareCard);
    }
}

function generateShareCard() {
    // 1. Populate the hidden card
    const dishName = document.getElementById('predictedDish').innerText;
    const calories = document.querySelector('.circular-value') ? document.querySelector('.circular-value').innerText : '0g'; // Fallback
    // Note: The structure might vary, let's grab from data if possible, or DOM

    // Better way: grab from last prediction data if stored, or DOM text
    const summary = JSON.parse(localStorage.getItem('foodsight_daily_summary') || 'null');

    document.getElementById('shareCardDish').innerText = dishName;
    document.getElementById('shareCardImage').src = previewImage.src;

    // We need to grab specifically the values for THIS dish. 
    // Since we don't have a global 'currentPrediction' var easily accessible without refactor,
    // let's scrape the DOM for the Circular Charts.

    // Attempt to find circular values
    const circularValues = document.querySelectorAll('.circular-value');
    if (circularValues.length >= 3) {
        // Assuming order Protein, Carbs, Fats based on app.js createMacroVisualization
        document.getElementById('shareCardProt').innerText = circularValues[0].innerText;
    }

    // Calories specific to the dish is inside .nutrition-table or we can find it
    // Actually, let's just use the History log's latest entry if available or scrape DOM
    // Scrape DOM:
    const nutritionTable = document.querySelector('.nutrition-table');
    if (nutritionTable) {
        const calRow = nutritionTable.rows[1]; // 2nd row is Calories
        if (calRow) {
            const calText = calRow.cells[1].innerText;
            document.getElementById('shareCardCal').innerText = calText.replace(' kcal', '');
        }
    }

    const container = document.getElementById('shareCardContainer');

    // 2. Generate Image
    html2canvas(container.firstElementChild, {
        backgroundColor: null,
        scale: 2 // High res
    }).then(canvas => {
        // 3. Download
        const link = document.createElement('a');
        link.download = `FoodSight_${dishName.replace(/\s+/g, '_')}.png`;
        link.href = canvas.toDataURL('image/png');
        link.click();

        // Success Toast
        showError("Card downloaded! 📸"); // Reusing showError with success message/color... wait, showError is red.
        // Let's create a temporary Quick Toast
        const toast = document.createElement('div');
        toast.className = 'success-toast';
        toast.innerHTML = '<span>📥 Image saved!</span>';
        document.body.appendChild(toast);
        setTimeout(() => toast.remove(), 2000);
    });
}

/* ============================================================================
   INITIALIZATION
   ============================================================================ */
// Call on load
document.addEventListener('DOMContentLoaded', () => {
    initHistorySidebar();
    initAboutModal();
    initCameraFeatures();
    initShareFeature();
    // ... other inits exist below? No, this block replaces previous init
    calculateStreak();

    // Render daily summary
    renderDailySummary();
});

/**
 * Render Daily Nutrition Summary Card
 */
function renderDailySummary() {
    const container = document.getElementById('dailySummaryContainer');
    if (!container) return;

    try {
        const today = new Date().toLocaleDateString();
        const summary = JSON.parse(localStorage.getItem('foodsight_daily_summary') || 'null');
        const currentSession = getCurrentSession();

        // Initial State or New Day
        if (!summary || summary.date !== today || !summary.sessions) {
            container.innerHTML = `
                <div class="daily-summary-card glass-card" style="padding: 1rem; border-radius: var(--radius-md);">
                     <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                        <span style="color: var(--text-secondary); font-size: 0.9rem;">Today's Nutrition</span>
                        <span class="session-badge">${currentSession}</span>
                    </div>
                    <p style="margin: 0; color: var(--text-muted); font-size: 0.9rem;">Start scanning specific meals to see your breakdown!</p>
                </div>
            `;
            return;
        }

        const total = summary.total;

        // Try to get profile goals if user is logged in
        let profileHtml = '';
        if (window.currentUser) {
            // We'll need an async fetch to get the profile, or store it in localStorage on load.
            // For now, let's try to get it synchronously if available, otherwise just use a default or fetch it asynchronously.
            // To keep it simple, we'll fetch and re-render.
            if (!container.dataset.profileFetched) {
                container.dataset.profileFetched = 'true';
                fetchUserProfileAndRenderSummary(container, summary, currentSession, total);
                return; // Let the async function handle rendering
            }
        } else {
            // Not logged in, render basic summary
            renderBasicSummary(container, summary, currentSession, total);
        }

    } catch (error) {
        console.error('Error rendering daily summary:', error);
    }
}

async function fetchUserProfileAndRenderSummary(container, summary, currentSession, total) {
    try {
        const res = await fetch('/api/profile');
        if (res.ok) {
            const data = await res.json();
            if (data.success && data.profile) {
                renderAdvancedSummary(container, summary, currentSession, total, data.profile);
                return;
            }
        }
    } catch (err) {
        console.error('Error fetching profile for summary:', err);
    }
    // Fallback to basic
    renderBasicSummary(container, summary, currentSession, total);
}

function renderBasicSummary(container, summary, currentSession, total) {
    container.innerHTML = `
        <div class="daily-summary-card glass-card" style="padding: 1.2rem; border-radius: var(--radius-md);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">
                <h4 style="margin: 0; font-size: 1rem; color: var(--text-primary);">Today's Overview</h4>
                 <button onclick="localStorage.removeItem('foodsight_daily_summary'); renderDailySummary();" style="background: none; border: none; color: var(--text-muted); cursor: pointer; font-size: 0.8rem;">Reset</button>
            </div>

            <div class="session-grid" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.5rem; margin-bottom: 1rem;">
                ${Object.entries(summary.sessions).map(([name, data]) => `
                    <div class="session-item ${data.count > 0 ? 'active' : ''}" style="text-align: center; padding: 0.5rem; background: rgba(255,255,255,0.03); border-radius: 8px;">
                        <div style="font-size: 0.75rem; color: var(--text-muted); margin-bottom: 0.2rem;">${name}</div>
                        <div style="font-weight: 700; color: ${data.count > 0 ? 'var(--primary-color)' : 'var(--text-secondary)'};">${data.calories || 0}</div>
                    </div>
                `).join('')}
                <div class="summary-stat">
                    <span class="summary-value" style="font-size: 1.5rem; display: block; font-weight: 700; color: var(--text-primary);">${total.calories || 0}</span>
                    <span class="summary-label" style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px;">Calories</span>
                </div>
                <div class="summary-stat">
                    <span class="summary-value" style="font-size: 1.2rem; display: block; font-weight: 700; color: var(--text-primary);">${total.protein || 0}g</span>
                    <span class="summary-label" style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px;">Protein</span>
                </div>
                <div class="summary-stat">
                    <span class="summary-value" style="font-size: 1.2rem; display: block; font-weight: 700; color: var(--text-primary);">${total.carbs || 0}g</span>
                    <span class="summary-label" style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px;">Carbs</span>
                </div>
                <div class="summary-stat">
                    <span class="summary-value" style="font-size: 1.2rem; display: block; font-weight: 700; color: var(--text-primary);">${total.fats || 0}g</span>
                    <span class="summary-label" style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px;">Fats</span>
                </div>
            </div>
        </div>
    `;
    container.dataset.profileFetched = ''; // Reset flag
}

function renderAdvancedSummary(container, summary, currentSession, total, profile) {
    const calTarget = profile.daily_cal_target || 2000;
    const proteinTarget = profile.daily_protein_target || 50;

    // Calculate percentages
    const calPct = Math.min(100, Math.round((total.calories / calTarget) * 100));
    const proteinPct = Math.min(100, Math.round((total.protein / proteinTarget) * 100));

    container.innerHTML = `
        <div class="daily-summary-card glass-card" style="padding: 1.2rem; border-radius: var(--radius-md);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">
                <h4 style="margin: 0; font-size: 1rem; color: var(--text-primary);">Today's Overview</h4>
                 <div>
                    <a href="/profile" style="color: var(--primary-color); font-size: 0.8rem; text-decoration: none; margin-right: 1rem;"><i class="fas fa-edit"></i> Edit Goals</a>
                    <button onclick="localStorage.removeItem('foodsight_daily_summary'); renderDailySummary();" style="background: none; border: none; color: var(--text-muted); cursor: pointer; font-size: 0.8rem;">Reset</button>
                 </div>
            </div>

            <div class="session-grid" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.5rem; margin-bottom: 1rem;">
                ${Object.entries(summary.sessions).map(([name, data]) => `
                    <div class="session-item ${data.count > 0 ? 'active' : ''}" style="text-align: center; padding: 0.5rem; background: rgba(255,255,255,0.03); border-radius: 8px;">
                        <div style="font-size: 0.75rem; color: var(--text-muted); margin-bottom: 0.2rem;">${name}</div>
                        <div style="font-weight: 700; color: ${data.count > 0 ? 'var(--primary-color)' : 'var(--text-secondary)'};">${data.calories || 0}</div>
                    </div>
                `).join('')}
            </div>

            <div style="margin-bottom: 0.5rem; display: flex; justify-content: space-between;">
                <span style="font-size: 0.85rem; color: var(--text-secondary);">Calories</span>
                <span style="font-size: 0.85rem; font-weight: bold; color: ${total.calories > calTarget ? '#ff6b6b' : 'var(--primary-color)'};">${total.calories || 0} / ${calTarget} kcal</span>
            </div>
            <div style="width: 100%; height: 8px; background: rgba(255,255,255,0.1); border-radius: 4px; overflow: hidden; margin-bottom: 1rem;">
                <div style="height: 100%; width: ${calPct}%; background: ${total.calories > calTarget ? '#ff6b6b' : 'var(--primary-color)'}; border-radius: 4px; transition: width 0.5s ease;"></div>
            </div>

            <div style="margin-bottom: 0.5rem; display: flex; justify-content: space-between;">
                <span style="font-size: 0.85rem; color: var(--text-secondary);">Protein</span>
                <span style="font-size: 0.85rem; font-weight: bold; color: var(--accent-color);">${total.protein || 0}g / ${proteinTarget}g</span>
            </div>
            <div style="width: 100%; height: 8px; background: rgba(255,255,255,0.1); border-radius: 4px; overflow: hidden; margin-bottom: 1rem;">
                <div style="height: 100%; width: ${proteinPct}%; background: var(--accent-color); border-radius: 4px; transition: width 0.5s ease;"></div>
            </div>

            <div style="display: flex; justify-content: space-between; gap: 1rem;">
                <div class="summary-stat">
                    <span class="summary-value" style="font-size: 1.1rem; display: block; font-weight: 700; color: var(--text-primary);">${total.carbs || 0}g</span>
                    <span class="summary-label" style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px;">Carbs</span>
                </div>
                <div class="summary-stat">
                    <span class="summary-value" style="font-size: 1.1rem; display: block; font-weight: 700; color: var(--text-primary);">${total.fats || 0}g</span>
                    <span class="summary-label" style="font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px;">Fats</span>
                </div>
            </div>
        </div>
    `;
    container.dataset.profileFetched = ''; // Reset flag
}


function initApp() {
    initHistorySidebar();
    initAboutModal();
    renderDailySummary(); // Load summary on start
}

/**
 * Clear all persistent history from backend
 */
async function clearPersistentHistory() {
    if (!confirm('Are you sure you want to clear your entire scan history? This will remove all records from the server.')) {
        return;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/history`, {
            method: 'DELETE'
        });
        const data = await response.json();

        if (data.success) {
            showSuccessToast('History cleared successfully!');

            // Clear local storage history too
            localStorage.removeItem('foodsight_history');
            localStorage.removeItem('foodsight_daily_summary');

            // Refresh UI
            if (typeof renderHistorySidebar === 'function') renderHistorySidebar();
            if (typeof renderDailySummary === 'function') renderDailySummary();

            // Close modal if open
            const profileModal = document.getElementById('profileModal');
            if (profileModal) profileModal.style.display = 'none';
        } else {
            showError(data.error || 'Failed to clear history');
        }
    } catch (error) {
        console.error('❌ Clear history error:', error);
        showError('Request failed. Please try again.');
    }
}

/**
 * Show success toast (reused or new)
 */
function showSuccessToast(message) {
    const toast = document.createElement('div');
    toast.className = 'success-toast';
    toast.style.cssText = `
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        background: var(--success-color, #2ecc71);
        color: white;
        padding: 1rem 2rem;
        border-radius: 50px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2);
        z-index: 10000;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        animation: slideInUp 0.3s ease-out;
    `;
    toast.innerHTML = `<i class="fas fa-check-circle"></i> ${message}`;
    document.body.appendChild(toast);
    setTimeout(() => {
        toast.style.animation = 'fadeOut 0.3s ease-in forwards';
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

// Initialize when DOM is loaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initApp);
} else {
    initApp();
}

console.log('✓ FoodSight AI JavaScript loaded');
