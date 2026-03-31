"""
FoodSight AI - Dataset Configuration
=====================================

Configuration for expanded Indian food dataset with 25 classes.
This file defines the complete dataset structure for model training.

Author: FoodSight AI Team
Date: February 2026
"""

# Complete list of food classes (100 dishes)
EXPANDED_CLASS_NAMES = [
    'Aloo Gobi', 'Aloo Mutter', 'Aloo Paratha', 'Amritsari Kulcha', 'Appam', 
    'Aviyal', 'Balushahi', 'Bhindi Masala', 'Biryani', 'Bisi Bele Bath', 
    'Burger', 'Butter Naan', 'Chaas', 'Chai', 'Chana Masala', 
    'Chapati', 'Chicken 65', 'Chicken Chettinad', 'Chicken Wings', 'Chilli Chicken', 
    'Chivda', 'Chole Bhature', 'Curd Rice', 'Dabeli', 'Dal Khichdi', 
    'Dal Makhani', 'Dhokla', 'Egg Curry', 'Falooda', 'Fish Curry', 
    'Fish Fry', 'Fried Rice', 'Gajar Ka Halwa', 'Garlic Bread', 'Garlic Naan', 
    'Ghevar', 'Grilled Sandwich', 'Gujhia', 'Gulab Jamun', 'Hara Bhara Kebab', 
    'Idiyappam', 'Idli', 'Jalebi', 'Kaathi Rolls', 'Kadai Paneer', 
    'Kaju Katli', 'Karimeen Pollichathu', 'Kerala Fish Curry', 'Kheer', 'Kothu Parotta', 
    'Kulfi', 'Laddu', 'Lemon Rice', 'Litti Chokha', 'Macher Jhol', 
    'Manchurian', 'Masala Dosa', 'Masala Papad', 'Medu Vada', 'Methi Thepla', 
    'Misal Pav', 'Modak', 'Momos', 'Moong Dal Halwa', 'Mysore Pak', 
    'Navratan Korma', 'Paani Puri', 'Pakora', 'Palak Paneer', 'Paneer Masala', 
    'Paniyaram', 'Papdi Chaat', 'Pav Bhaji', 'Payasam', 'Phirni', 
    'Pizza', 'Poha', 'Pongal', 'Puran Poli', 'Puri Bhaji', 
    'Puttu', 'Rajma Chawal', 'Rasam', 'Rasgulla', 'Rava Dosa', 
    'Sabudana Khichdi', 'Sabudana Vada', 'Sambar Rice', 'Samosa', 'Sandesh', 
    'Seekh Kebab', 'Set Dosa', 'Sev Puri', 'Tamarind Rice', 'Thali', 
    'Thukpa', 'Unni Appam', 'Upma', 'Uttapam', 'Vada Pav'
]

# Category mappings
CATEGORY_MAPPING = {
    "Main Course": [
        'Aloo Gobi', 'Aloo Mutter', 'Aloo Paratha', 'Amritsari Kulcha', 'Aviyal', 
        'Bhindi Masala', 'Biryani', 'Bisi Bele Bath', 'Butter Naan', 'Chana Masala', 
        'Chapati', 'Chicken Chettinad', 'Chilli Chicken', 'Chole Bhature', 'Curd Rice', 
        'Dal Khichdi', 'Dal Makhani', 'Egg Curry', 'Fish Curry', 'Fish Fry', 
        'Fried Rice', 'Garlic Naan', 'Grilled Sandwich', 'Hara Bhara Kebab', 
        'Kadai Paneer', 'Karimeen Pollichathu', 'Kerala Fish Curry', 'Kothu Parotta', 'Lemon Rice', 
        'Litti Chokha', 'Macher Jhol', 'Manchurian', 'Masala Dosa', 'Misal Pav', 
        'Navratan Korma', 'Palak Paneer', 'Paneer Masala', 'Puri Bhaji', 
        'Rajma Chawal', 'Rava Dosa', 'Sambar Rice', 'Kaathi Rolls', 
        'Seekh Kebab', 'Set Dosa', 'Tamarind Rice', 'Thali', 'Thukpa', 
        'Upma', 'Uttapam'
    ],
    "Breakfast": [
        'Aloo Paratha', 'Amritsari Kulcha', 'Appam', 'Dhokla', 'Idiyappam', 
        'Idli', 'Masala Dosa', 'Medu Vada', 'Methi Thepla', 'Misal Pav', 
        'Paniyaram', 'Poha', 'Pongal', 'Puri Bhaji', 'Puttu', 
        'Rava Dosa', 'Sabudana Khichdi', 'Set Dosa', 'Upma', 'Uttapam', 
        'Vada Pav', 'Chapati'
    ],
    "Street Food": [
        'Burger', 'Chicken 65', 'Chivda', 'Chole Bhature', 'Dabeli', 
        'Kaathi Rolls', 'Kothu Parotta', 'Masala Papad', 'Misal Pav', 'Momos', 
        'Paani Puri', 'Pakora', 'Papdi Chaat', 'Pav Bhaji', 'Samosa', 
        'Sev Puri', 'Vada Pav'
    ],
    "Dessert": [
        'Balushahi', 'Falooda', 'Gajar Ka Halwa', 'Ghevar', 'Gujhia', 
        'Gulab Jamun', 'Jalebi', 'Kaju Katli', 'Kheer', 'Kulfi', 
        'Laddu', 'Modak', 'Moong Dal Halwa', 'Mysore Pak', 'Payasam', 
        'Phirni', 'Puran Poli', 'Rasgulla', 'Sandesh', 'Unni Appam'
    ],
    "Beverage": [
        'Chaas', 'Chai', 'Falooda', 'Rasam'
    ],
    "Appetizer/Snack": [
        'Chicken 65', 'Chicken Wings', 'Chivda', 'Fish Fry', 'Garlic Bread', 
        'Masala Papad', 'Pakora', 'Sabudana Vada', 'Samosa', 'Unni Appam'
    ]
}

# Regional mappings
REGION_MAPPING = {
    "North India": [
        'Aloo Gobi', 'Aloo Mutter', 'Aloo Paratha', 'Amritsari Kulcha', 'Balushahi', 
        'Bhindi Masala', 'Butter Naan', 'Chai', 'Chana Masala', 'Chapati', 
        'Chole Bhature', 'Dal Khichdi', 'Dal Makhani', 'Egg Curry', 'Gajar Ka Halwa', 
        'Garlic Naan', 'Gujhia', 'Gulab Jamun', 'Hara Bhara Kebab', 'Jalebi', 
        'Kadai Paneer', 'Kaju Katli', 'Kheer', 'Kulfi', 'Moong Dal Halwa', 
        'Navratan Korma', 'Paani Puri', 'Pakora', 'Palak Paneer', 'Paneer Masala', 
        'Phirni', 'Puri Bhaji', 'Rajma Chawal', 'Samosa', 'Seekh Kebab'
    ],
    "South India": [
        'Appam', 'Aviyal', 'Biryani', 'Bisi Bele Bath', 'Chicken 65', 
        'Chicken Chettinad', 'Curd Rice', 'Fish Fry', 'Idiyappam', 'Idli', 
        'Karimeen Pollichathu', 'Kerala Fish Curry', 'Kothu Parotta', 'Lemon Rice', 'Masala Dosa', 
        'Medu Vada', 'Mysore Pak', 'Paniyaram', 'Payasam', 'Pongal', 
        'Puttu', 'Rasam', 'Rava Dosa', 'Sambar Rice', 'Set Dosa', 
        'Tamarind Rice', 'Unni Appam', 'Upma', 'Uttapam'
    ],
    "West India": [
        'Chaas', 'Chivda', 'Dabeli', 'Dhokla', 'Ghevar', 'Methi Thepla', 
        'Misal Pav', 'Modak', 'Pav Bhaji', 'Poha', 'Puran Poli', 
        'Sabudana Khichdi', 'Sabudana Vada', 'Sev Puri', 'Thali', 'Vada Pav'
    ],
    "East India": [
        'Fish Curry', 'Litti Chokha', 'Macher Jhol', 'Momos', 'Rasgulla', 
        'Sandesh', 'Kaathi Rolls', 'Thukpa'
    ],
    "International/Fusion": [
        'Burger', 'Chicken Wings', 'Chilli Chicken', 'Fried Rice', 
        'Garlic Bread', 'Grilled Sandwich', 'Manchurian', 'Pizza'
    ]
}

# Dietary classifications
VEGETARIAN_DISHES = [
    'Aloo Gobi', 'Aloo Mutter', 'Aloo Paratha', 'Amritsari Kulcha', 'Appam', 
    'Aviyal', 'Balushahi', 'Bhindi Masala', 'Bisi Bele Bath', 'Burger', 
    'Butter Naan', 'Chaas', 'Chai', 'Chana Masala', 'Chapati', 
    'Chivda', 'Chole Bhature', 'Curd Rice', 'Dabeli', 'Dal Khichdi', 
    'Dal Makhani', 'Dhokla', 'Falooda', 'Fried Rice', 'Gajar Ka Halwa', 
    'Garlic Bread', 'Garlic Naan', 'Ghevar', 'Grilled Sandwich', 'Gujhia', 
    'Gulab Jamun', 'Hara Bhara Kebab', 'Idiyappam', 'Idli', 'Jalebi', 
    'Kadai Paneer', 'Kaju Katli', 'Kheer', 'Kulfi', 'Laddu', 
    'Lemon Rice', 'Litti Chokha', 'Manchurian', 'Masala Dosa', 'Masala Papad', 
    'Medu Vada', 'Methi Thepla', 'Misal Pav', 'Modak', 'Momos', 
    'Moong Dal Halwa', 'Mysore Pak', 'Navratan Korma', 'Paani Puri', 'Pakora', 
    'Palak Paneer', 'Paneer Masala', 'Paniyaram', 'Papdi Chaat', 'Pav Bhaji', 
    'Payasam', 'Phirni', 'Pizza', 'Poha', 'Pongal', 
    'Puran Poli', 'Puri Bhaji', 'Puttu', 'Rajma Chawal', 'Rasam', 
    'Rasgulla', 'Rava Dosa', 'Sabudana Khichdi', 'Sabudana Vada', 'Sambar Rice', 
    'Samosa', 'Sandesh', 'Set Dosa', 'Sev Puri', 'Tamarind Rice', 
    'Thali', 'Unni Appam', 'Upma', 'Uttapam', 'Vada Pav'
]

VEGAN_DISHES = [
    'Aloo Gobi', 'Aloo Mutter', 'Appam', 'Bhindi Masala', 'Chaas', 
    'Chai', 'Chapati', 'Chivda', 'Chana Masala', 'Dal Khichdi', 
    'Dhokla', 'Idiyappam', 'Idli', 'Lemon Rice', 'Masala Dosa', 
    'Medu Vada', 'Misal Pav', 'Momos', 'Paani Puri', 'Poha', 
    'Pongal', 'Puttu', 'Rajma Chawal', 'Rasam', 'Rava Dosa', 
    'Sabudana Khichdi', 'Sambar Rice', 'Set Dosa', 'Tamarind Rice', 'Upma', 
    'Uttapam'
]

NON_VEGETARIAN_DISHES = [
    'Biryani', 'Chicken 65', 'Chicken Chettinad', 'Chicken Wings', 'Chilli Chicken', 
    'Egg Curry', 'Fish Curry', 'Fish Fry', 'Kaathi Rolls', 'Karimeen Pollichathu', 
    'Kerala Fish Curry', 'Macher Jhol', 'Seekh Kebab', 'Thukpa'
]


# Dataset structure for training
DATASET_CONFIG = {
    "total_classes": len(EXPANDED_CLASS_NAMES),
    "image_size": (224, 224),
    "color_mode": "rgb",
    "batch_size": 32,
    "validation_split": 0.2,
    "test_split": 0.1,
    "min_images_per_class": 80,
    "recommended_images_per_class": 100,
    "augmentation": {
        "rotation_range": 20,
        "width_shift_range": 0.2,
        "height_shift_range": 0.2,
        "shear_range": 0.2,
        "zoom_range": 0.2,
        "horizontal_flip": True,
        "fill_mode": "nearest"
    }
}

# Data sources and collection guidelines
DATA_COLLECTION_SOURCES = {
    "kaggle_datasets": [
        "Indian Food Classification Dataset",
        "Food-101 Dataset (filtered for Indian dishes)",
        "Indian Food Images Dataset"
    ],
    "web_scraping": [
        "Google Images (with proper filtering)",
        "Food blogs and recipe websites",
        "Restaurant menus and food delivery apps"
    ],
    "manual_collection": [
        "Personal photography",
        "Team member contributions",
        "Local restaurant collaborations"
    ]
}

# Expected dataset structure
DATASET_STRUCTURE = """
dataset/
├── train/
│   ├── Chole Bhature/ (~420 images)
│   ├── Dal Makhani/ (~420 images)
│   ├── Idli/ (~420 images)
│   ├── ... (all 100 classes)
│   └── Rasgulla/ (~420 images)
├── validation/
│   ├── Chole Bhature/ (~120 images)
│   ├── Dal Makhani/ (~120 images)
│   └── ... (all 100 classes)
└── test/
    ├── Chole Bhature/ (~60 images)
    ├── Dal Makhani/ (~60 images)
    └── ... (all 100 classes)

Total images: ~60,000 (600 per class × 100 classes)
"""

# Model architecture recommendations
MODEL_RECOMMENDATIONS = {
    "base_model": "MobileNetV3Large",
    "alternatives": ["EfficientNetB1", "ResNet50", "InceptionV3"],
    "input_shape": (224, 224, 3),
    "output_classes": 100,
    "transfer_learning": True,
    "fine_tuning": True,
    "fine_tune_from_layer": 100,
    "optimizer": "adam",
    "learning_rate": 0.0001,
    "epochs": 40,
    "early_stopping_patience": 5,
    "target_accuracy": 0.85
}


def get_class_index(class_name):
    """Get the index of a class name."""
    try:
        return EXPANDED_CLASS_NAMES.index(class_name)
    except ValueError:
        return -1


def get_class_name(index):
    """Get the class name from an index."""
    if 0 <= index < len(EXPANDED_CLASS_NAMES):
        return EXPANDED_CLASS_NAMES[index]
    return None


def get_category(dish_name):
    """Get the category of a dish."""
    for category, dishes in CATEGORY_MAPPING.items():
        if dish_name in dishes:
            return category
    return "Unknown"


def get_region(dish_name):
    """Get the region of a dish."""
    for region, dishes in REGION_MAPPING.items():
        if dish_name in dishes:
            return region
    return "Unknown"


def is_vegetarian(dish_name):
    """Check if a dish is vegetarian."""
    return dish_name in VEGETARIAN_DISHES


def is_vegan(dish_name):
    """Check if a dish is vegan."""
    return dish_name in VEGAN_DISHES


def is_non_vegetarian(dish_name):
    """Check if a dish is non-vegetarian."""
    return dish_name in NON_VEGETARIAN_DISHES


# Statistics
DATASET_STATS = {
    "total_dishes": len(EXPANDED_CLASS_NAMES),
    "vegetarian_count": len(VEGETARIAN_DISHES),
    "vegan_count": len(VEGAN_DISHES),
    "non_vegetarian_count": len(NON_VEGETARIAN_DISHES),
    "categories": len(CATEGORY_MAPPING),
    "regions": len(REGION_MAPPING),
    "north_indian_count": len(REGION_MAPPING["North India"]),
    "south_indian_count": len(REGION_MAPPING["South India"]),
    "west_indian_count": len(REGION_MAPPING["West India"]),
    "east_indian_count": len(REGION_MAPPING["East India"])
}
