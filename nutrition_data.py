"""
FoodSight AI - Nutrition Database
==================================

Comprehensive nutrition information for Indian food dishes.
All nutritional values are approximate and based on standard serving sizes.

Author: FoodSight AI Team
Date: January 2026
"""

# Comprehensive nutrition database for all 100 supported dishes
NUTRITION_DATABASE = {
    # 1. Aloo Gobi (New)
    "Aloo Gobi": {
        "nutrition": { "calories": 180, "protein_g": 4, "carbs_g": 25, "fats_g": 8, "fiber_g": 5, "sugar_g": 4, "sodium_mg": 450 },
        "vitamins_minerals": { "vitamin_c_mg": 45, "calcium_mg": 40, "iron_mg": 1.8, "potassium_mg": 520 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": [],
        "serving_size": "1 bowl (200g)",
        "region": "North India",
        "category": "Main Course",
        "description": "Dry curry made with potatoes and cauliflower"
    },
    # 2. Aloo Mutter (New)
    "Aloo Mutter": {
        "nutrition": { "calories": 210, "protein_g": 5, "carbs_g": 30, "fats_g": 9, "fiber_g": 6, "sugar_g": 5, "sodium_mg": 420 },
        "vitamins_minerals": { "vitamin_a_iu": 400, "calcium_mg": 35, "iron_mg": 2.2, "potassium_mg": 480 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": [],
        "serving_size": "1 bowl (200g)",
        "region": "North India",
        "category": "Main Course",
        "description": "Potatoes and green peas curry"
    },
    # 3. Aloo Paratha
    "Aloo Paratha": {
        "nutrition": { "calories": 320, "protein_g": 8, "carbs_g": 48, "fats_g": 11, "fiber_g": 4, "sugar_g": 2, "sodium_mg": 420 },
        "vitamins_minerals": { "vitamin_c_mg": 12, "calcium_mg": 68, "iron_mg": 2.4, "potassium_mg": 380 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": False, "dairy_free": False, "spicy": False },
        "allergens": ["gluten", "dairy"],
        "serving_size": "2 pieces (200g)",
        "region": "North India",
        "category": "Breakfast",
        "description": "Whole wheat flatbread stuffed with spiced potato filling"
    },
    # 2. Biryani
    "Biryani": {
        "nutrition": { "calories": 350, "protein_g": 12, "carbs_g": 45, "fats_g": 12, "fiber_g": 3, "sugar_g": 2, "sodium_mg": 600 },
        "vitamins_minerals": { "vitamin_a_iu": 300, "calcium_mg": 80, "iron_mg": 2.5, "potassium_mg": 300 },
        "dietary_info": { "vegetarian": False, "vegan": False, "gluten_free": True, "dairy_free": False, "spicy": True },
        "allergens": ["dairy"],
        "serving_size": "1 plate (300g)",
        "region": "South India/North India",
        "category": "Main Course",
        "description": "Aromatic rice dish cooked with spices and meat or vegetables"
    },
    # 3. Burger
    "Burger": {
        "nutrition": { "calories": 295, "protein_g": 17, "carbs_g": 30, "fats_g": 12, "fiber_g": 2, "sugar_g": 5, "sodium_mg": 650 },
        "vitamins_minerals": { "calcium_mg": 80, "iron_mg": 2.5, "potassium_mg": 250 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": False, "dairy_free": True, "spicy": False },
        "allergens": ["gluten", "dairy"],
        "serving_size": "1 burger (200g)",
        "region": "International/Fusion",
        "category": "Main Course",
        "description": "Vegetable patty in a bun with lettuce and sauces"
    },
    # 4. Butter Naan
    "Butter Naan": {
        "nutrition": { "calories": 260, "protein_g": 8, "carbs_g": 45, "fats_g": 5, "fiber_g": 2, "sugar_g": 2, "sodium_mg": 320 },
        "vitamins_minerals": { "calcium_mg": 35, "iron_mg": 1.5, "potassium_mg": 110 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": False, "dairy_free": False, "spicy": False },
        "allergens": ["gluten", "dairy"],
        "serving_size": "1 piece (90g)",
        "region": "North India",
        "category": "Main Course",
        "description": "Leavened flatbread baked in tandoor with butter"
    },
    # 5. Chai
    "Chai": {
        "nutrition": { "calories": 120, "protein_g": 3, "carbs_g": 18, "fats_g": 4, "fiber_g": 0, "sugar_g": 12, "sodium_mg": 25 },
        "vitamins_minerals": { "calcium_mg": 90, "iron_mg": 0.2, "potassium_mg": 140 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": True, "dairy_free": False, "spicy": False },
        "allergens": ["dairy"],
        "serving_size": "1 cup (150ml)",
        "region": "North India",
        "category": "Beverage",
        "description": "Spiced tea made with milk and sugar"
    },
    # 6. Chapati
    "Chapati": {
        "nutrition": { "calories": 104, "protein_g": 3, "carbs_g": 20, "fats_g": 1, "fiber_g": 3, "sugar_g": 0, "sodium_mg": 120 },
        "vitamins_minerals": { "vitamin_b1_mg": 0.2, "calcium_mg": 20, "iron_mg": 1.0, "potassium_mg": 100 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": False, "dairy_free": True, "spicy": False },
        "allergens": ["gluten"],
        "serving_size": "1 piece (40g)",
        "region": "North India",
        "category": "Main Course",
        "description": "Unleavened flatbread made from whole wheat flour"
    },
    # 7. Chilli Chicken
    "Chilli Chicken": {
        "nutrition": { "calories": 380, "protein_g": 28, "carbs_g": 18, "fats_g": 22, "fiber_g": 2, "sugar_g": 6, "sodium_mg": 850 },
        "vitamins_minerals": { "vitamin_c_mg": 25, "calcium_mg": 40, "iron_mg": 1.8, "potassium_mg": 420 },
        "dietary_info": { "vegetarian": False, "vegan": False, "gluten_free": False, "dairy_free": True, "spicy": True },
        "allergens": ["soy", "gluten"],
        "serving_size": "1 bowl (250g)",
        "region": "International/Fusion",
        "category": "Main Course",
        "description": "Indo-Chinese spicy chicken dish with bell peppers"
    },
    # 8. Chole Bhature
    "Chole Bhature": {
        "nutrition": { "calories": 500, "protein_g": 14, "carbs_g": 60, "fats_g": 22, "fiber_g": 8, "sugar_g": 4, "sodium_mg": 680 },
        "vitamins_minerals": { "vitamin_c_mg": 12, "calcium_mg": 85, "iron_mg": 3.2, "potassium_mg": 420 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": False, "dairy_free": False, "spicy": True },
        "allergens": ["gluten", "dairy"],
        "serving_size": "2 bhature with chole (300g)",
        "region": "North India",
        "category": "Main Course",
        "description": "Deep-fried bread served with spicy chickpea curry"
    },
    # 9. Dal Khichdi
    "Dal Khichdi": {
        "nutrition": { "calories": 320, "protein_g": 10, "carbs_g": 55, "fats_g": 6, "fiber_g": 4, "sugar_g": 1, "sodium_mg": 420 },
        "vitamins_minerals": { "vitamin_c_mg": 8, "calcium_mg": 45, "iron_mg": 2.5, "potassium_mg": 350 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": False, "spicy": False },
        "allergens": ["dairy"], # Often has ghee
        "serving_size": "1 bowl (300g)",
        "region": "North India",
        "category": "Main Course",
        "description": "Comfort food made of rice and lentils cooked together"
    },
    # 10. Dal Makhani
    "Dal Makhani": {
        "nutrition": { "calories": 320, "protein_g": 14, "carbs_g": 35, "fats_g": 12, "fiber_g": 10, "sugar_g": 3, "sodium_mg": 520 },
        "vitamins_minerals": { "vitamin_a_iu": 450, "calcium_mg": 120, "iron_mg": 4.5, "potassium_mg": 580 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": True, "dairy_free": False, "spicy": False },
        "allergens": ["dairy"],
        "serving_size": "1 bowl (250g)",
        "region": "North India",
        "category": "Main Course",
        "description": "Creamy black lentil curry cooked with butter and cream"
    },
    # 11. Dhokla
    "Dhokla": {
        "nutrition": { "calories": 150, "protein_g": 6, "carbs_g": 25, "fats_g": 4, "fiber_g": 2, "sugar_g": 4, "sodium_mg": 480 },
        "vitamins_minerals": { "vitamin_c_mg": 5, "calcium_mg": 40, "iron_mg": 1.2, "potassium_mg": 150 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": False },
        "allergens": [],
        "serving_size": "2 pieces (100g)",
        "region": "West India",
        "category": "Breakfast",
        "description": "Steamed savory cake made from fermented gram flour batter"
    },
    # 12. Egg Curry (New)
    "Egg Curry": {
        "nutrition": { "calories": 250, "protein_g": 14, "carbs_g": 12, "fats_g": 18, "fiber_g": 2, "sugar_g": 3, "sodium_mg": 520 },
        "vitamins_minerals": { "vitamin_a_iu": 600, "calcium_mg": 60, "iron_mg": 2.2, "potassium_mg": 320 },
        "dietary_info": { "vegetarian": False, "vegan": False, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": ["egg"],
        "serving_size": "1 bowl (250g)",
        "region": "North India",
        "category": "Main Course",
        "description": "Boiled eggs simmered in a spicy tomato-onion gravy"
    },
    # 13. Fish Curry (New)
    "Fish Curry": {
        "nutrition": { "calories": 300, "protein_g": 25, "carbs_g": 8, "fats_g": 20, "fiber_g": 2, "sugar_g": 2, "sodium_mg": 580 },
        "vitamins_minerals": { "vitamin_a_iu": 400, "calcium_mg": 50, "iron_mg": 1.5, "potassium_mg": 450 },
        "dietary_info": { "vegetarian": False, "vegan": False, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": ["fish"],
        "serving_size": "1 bowl (250g)",
        "region": "East India/South India",
        "category": "Main Course",
        "description": "Fish fillets simmered in a tangy spiced gravy"
    },
    # 14. Fried Rice
    "Fried Rice": {
        "nutrition": { "calories": 350, "protein_g": 8, "carbs_g": 55, "fats_g": 10, "fiber_g": 3, "sugar_g": 2, "sodium_mg": 600 },
        "vitamins_minerals": { "vitamin_a_iu": 350, "calcium_mg": 30, "iron_mg": 1.8, "potassium_mg": 220 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": False },
        "allergens": ["soy"],
        "serving_size": "1 bowl (250g)",
        "region": "International/Fusion",
        "category": "Main Course",
        "description": "Stir-fried rice with vegetables (and optional egg/chicken)"
    },
    # 15. Gajar Ka Halwa (Added Back)
    "Gajar Ka Halwa": {
        "nutrition": { "calories": 300, "protein_g": 4, "carbs_g": 45, "fats_g": 12, "fiber_g": 2, "sugar_g": 35, "sodium_mg": 60 },
        "vitamins_minerals": { "vitamin_a_iu": 3000, "calcium_mg": 100, "iron_mg": 1.0, "potassium_mg": 300 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": True, "dairy_free": False, "spicy": False },
        "allergens": ["dairy", "nuts"],
        "serving_size": "1 bowl (150g)",
        "region": "North India",
        "category": "Dessert",
        "description": "Sweet carrot pudding made with milk, sugar, and ghee"
    },
    # 16. Garlic Naan
    "Garlic Naan": {
        "nutrition": { "calories": 290, "protein_g": 8, "carbs_g": 46, "fats_g": 7, "fiber_g": 2, "sugar_g": 2, "sodium_mg": 400 },
        "vitamins_minerals": { "calcium_mg": 45, "iron_mg": 1.8, "potassium_mg": 125 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": False, "dairy_free": True, "spicy": False },
        "allergens": ["gluten", "dairy"],
        "serving_size": "1 piece (110g)",
        "region": "North India",
        "category": "Main Course",
        "description": "Leavened flatbread topped with minced garlic and butter"
    },
    # 17. Grilled Sandwich
    "Grilled Sandwich": {
        "nutrition": { "calories": 350, "protein_g": 10, "carbs_g": 45, "fats_g": 16, "fiber_g": 4, "sugar_g": 4, "sodium_mg": 580 },
        "vitamins_minerals": { "calcium_mg": 120, "iron_mg": 2.5, "potassium_mg": 280 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": False, "dairy_free": False, "spicy": False },
        "allergens": ["gluten", "dairy"],
        "serving_size": "1 sandwich (200g)",
        "region": "International/Fusion",
        "category": "Main Course",
        "description": "Toasted bread sandwich with vegetable and cheese filling"
    },
    # 18. Gulab Jamun
    "Gulab Jamun": {
        "nutrition": { "calories": 180, "protein_g": 2, "carbs_g": 30, "fats_g": 8, "fiber_g": 0, "sugar_g": 25, "sodium_mg": 40 },
        "vitamins_minerals": { "calcium_mg": 60, "iron_mg": 0.5, "potassium_mg": 80 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": False, "dairy_free": False, "spicy": False },
        "allergens": ["gluten", "dairy"],
        "serving_size": "2 pieces (80g)",
        "region": "North India",
        "category": "Dessert",
        "description": "Deep-fried milk solids soaked in sugar syrup"
    },
    # 19. Hara Bhara Kebab
    "Hara Bhara Kebab": {
        "nutrition": { "calories": 220, "protein_g": 8, "carbs_g": 24, "fats_g": 12, "fiber_g": 4, "sugar_g": 2, "sodium_mg": 380 },
        "vitamins_minerals": { "vitamin_a_iu": 2500, "calcium_mg": 85, "iron_mg": 3.4, "potassium_mg": 360 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": [],
        "serving_size": "3 pieces (120g)",
        "region": "North India",
        "category": "Main Course",
        "description": "Spinach and green pea patties"
    },
    # 20. Idli
    "Idli": {
        "nutrition": { "calories": 60, "protein_g": 2, "carbs_g": 12, "fats_g": 0, "fiber_g": 1, "sugar_g": 0, "sodium_mg": 50 },
        "vitamins_minerals": { "vitamin_b1_mg": 0.1, "calcium_mg": 15, "iron_mg": 0.5, "potassium_mg": 40 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": False },
        "allergens": [],
        "serving_size": "1 piece (50g)",
        "region": "South India",
        "category": "Breakfast",
        "description": "Steamed rice and lentil cakes"
    },
    # 21. Jalebi
    "Jalebi": {
        "nutrition": { "calories": 250, "protein_g": 2, "carbs_g": 45, "fats_g": 10, "fiber_g": 0, "sugar_g": 30, "sodium_mg": 20 },
        "vitamins_minerals": { "calcium_mg": 10, "iron_mg": 0.5, "potassium_mg": 30 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": False, "dairy_free": True, "spicy": False },
        "allergens": ["gluten"],
        "serving_size": "3 pieces (80g)",
        "region": "North India",
        "category": "Dessert",
        "description": "Crispy fried batter soaked in syrup"
    },
    # 22. Kaathi Rolls
    "Kaathi Rolls": {
        "nutrition": { "calories": 420, "protein_g": 14, "carbs_g": 48, "fats_g": 18, "fiber_g": 4, "sugar_g": 5, "sodium_mg": 650 },
        "vitamins_minerals": { "calcium_mg": 70, "iron_mg": 2.8, "potassium_mg": 350 },
        "dietary_info": { "vegetarian": False, "vegan": False, "gluten_free": False, "dairy_free": True, "spicy": True },
        "allergens": ["gluten"],
        "serving_size": "1 roll (200g)",
        "region": "East India",
        "category": "Street Food",
        "description": "Skewered roasted meat wrapped in paratha bread"
    },
    # 23. Kadai Paneer
    "Kadai Paneer": {
        "nutrition": { "calories": 380, "protein_g": 16, "carbs_g": 18, "fats_g": 28, "fiber_g": 4, "sugar_g": 6, "sodium_mg": 620 },
        "vitamins_minerals": { "vitamin_a_iu": 520, "calcium_mg": 280, "iron_mg": 2.4, "potassium_mg": 340 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": True, "dairy_free": False, "spicy": True },
        "allergens": ["dairy"],
        "serving_size": "1 bowl (200g)",
        "region": "North India",
        "category": "Main Course",
        "description": "Cottage cheese cooked with bell peppers in spicy tomato gravy"
    },
    # 24. Kaju Katli (New)
    "Kaju Katli": {
        "nutrition": { "calories": 150, "protein_g": 3, "carbs_g": 20, "fats_g": 8, "fiber_g": 1, "sugar_g": 15, "sodium_mg": 10 },
        "vitamins_minerals": { "calcium_mg": 15, "iron_mg": 0.8, "potassium_mg": 120 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": False },
        "allergens": ["nuts"],
        "serving_size": "2 pieces (50g)",
        "region": "North India",
        "category": "Dessert",
        "description": "Diamond-shaped sweet made from cashew nuts, sugar, and ghee"
    },
    # 25. Kheer
    "Kheer": {
        "nutrition": { "calories": 220, "protein_g": 6, "carbs_g": 38, "fats_g": 5, "fiber_g": 0, "sugar_g": 28, "sodium_mg": 65 },
        "vitamins_minerals": { "calcium_mg": 145, "iron_mg": 0.6, "potassium_mg": 185 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": True, "dairy_free": False, "spicy": False },
        "allergens": ["dairy", "nuts"],
        "serving_size": "1 bowl (150g)",
        "region": "North India",
        "category": "Dessert",
        "description": "Creamy rice pudding flavored with cardamom and nuts"
    },
    # 26. Kulfi
    "Kulfi": {
        "nutrition": { "calories": 280, "protein_g": 8, "carbs_g": 32, "fats_g": 14, "fiber_g": 0, "sugar_g": 26, "sodium_mg": 50 },
        "vitamins_minerals": { "calcium_mg": 160, "iron_mg": 0.4, "potassium_mg": 210 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": True, "dairy_free": False, "spicy": False },
        "allergens": ["dairy", "nuts"],
        "serving_size": "1 stick (90g)",
        "region": "North India",
        "category": "Dessert",
        "description": "Traditional Indian ice cream made with reduced milk"
    },
    # 27. Masala Dosa
    "Masala Dosa": {
        "nutrition": { "calories": 350, "protein_g": 8, "carbs_g": 55, "fats_g": 10, "fiber_g": 4, "sugar_g": 3, "sodium_mg": 480 },
        "vitamins_minerals": { "vitamin_c_mg": 15, "calcium_mg": 60, "iron_mg": 2.5, "potassium_mg": 400 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": [],
        "serving_size": "1 piece (250g)",
        "region": "South India",
        "category": "Main Course",
        "description": "Fermented crepe made from rice batter and black lentils"
    },
    # 28. Medu Vada (New)
    "Medu Vada": {
        "nutrition": { "calories": 235, "protein_g": 9, "carbs_g": 26, "fats_g": 10, "fiber_g": 6, "sugar_g": 1, "sodium_mg": 340 },
        "vitamins_minerals": { "vitamin_c_mg": 5, "calcium_mg": 58, "iron_mg": 3.2, "potassium_mg": 320 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": [],
        "serving_size": "2 pieces (120g)",
        "region": "South India",
        "category": "Breakfast",
        "description": "Deep-fried savory lentil donut"
    },
    # 29. Misal Pav (New)
    "Misal Pav": {
        "nutrition": { "calories": 420, "protein_g": 12, "carbs_g": 55, "fats_g": 18, "fiber_g": 8, "sugar_g": 5, "sodium_mg": 650 },
        "vitamins_minerals": { "vitamin_c_mg": 15, "calcium_mg": 85, "iron_mg": 4.0, "potassium_mg": 480 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": False, "dairy_free": True, "spicy": True },
        "allergens": ["gluten"],
        "serving_size": "1 plate (300g)",
        "region": "West India",
        "category": "Street Food",
        "description": "Spicy sprouted moth bean curry served with bread bun"
    },
    # 30. Modak (New)
    "Modak": {
        "nutrition": { "calories": 200, "protein_g": 3, "carbs_g": 35, "fats_g": 5, "fiber_g": 1, "sugar_g": 20, "sodium_mg": 20 },
        "vitamins_minerals": { "calcium_mg": 20, "iron_mg": 0.5, "potassium_mg": 80 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": True, "dairy_free": False, "spicy": False },
        "allergens": ["dairy", "coconut"],
        "serving_size": "2 pieces (80g)",
        "region": "West India",
        "category": "Dessert",
        "description": "Sweet rice flour dumpling filled with coconut and jaggery"
    },
    # 31. Momos
    "Momos": {
        "nutrition": { "calories": 220, "protein_g": 8, "carbs_g": 30, "fats_g": 6, "fiber_g": 2, "sugar_g": 2, "sodium_mg": 450 },
        "vitamins_minerals": { "vitamin_c_mg": 5, "calcium_mg": 30, "iron_mg": 1.5, "potassium_mg": 150 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": False, "dairy_free": True, "spicy": True },
        "allergens": ["gluten"],
        "serving_size": "6 pieces (150g)",
        "region": "East India",
        "category": "Street Food",
        "description": "Steamed dumplings with vegetable or meat filling"
    },
    # 32. Moong Dal Halwa (New)
    "Moong Dal Halwa": {
        "nutrition": { "calories": 350, "protein_g": 8, "carbs_g": 40, "fats_g": 18, "fiber_g": 2, "sugar_g": 30, "sodium_mg": 40 },
        "vitamins_minerals": { "calcium_mg": 45, "iron_mg": 1.2, "potassium_mg": 250 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": True, "dairy_free": False, "spicy": False },
        "allergens": ["dairy", "nuts"],
        "serving_size": "1 bowl (150g)",
        "region": "North India",
        "category": "Dessert",
        "description": "Rich sweet made with yellow lentils, ghee, and sugar"
    },
    # 33. Paani Puri
    "Paani Puri": {
        "nutrition": { "calories": 180, "protein_g": 4, "carbs_g": 32, "fats_g": 4, "fiber_g": 3, "sugar_g": 8, "sodium_mg": 420 },
        "vitamins_minerals": { "vitamin_c_mg": 25, "calcium_mg": 35, "iron_mg": 1.5, "potassium_mg": 280 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": False, "dairy_free": True, "spicy": True },
        "allergens": ["gluten"],
        "serving_size": "6 pieces (120g)",
        "region": "North India",
        "category": "Street Food",
        "description": "Crispy hollow puris filled with tangy tamarind water"
    },
    # 34. Pakora
    "Pakora": {
        "nutrition": { "calories": 300, "protein_g": 6, "carbs_g": 25, "fats_g": 20, "fiber_g": 3, "sugar_g": 2, "sodium_mg": 400 },
        "vitamins_minerals": { "vitamin_c_mg": 12, "calcium_mg": 40, "iron_mg": 2.0, "potassium_mg": 250 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": [],
        "serving_size": "1 plate (150g)",
        "region": "North India",
        "category": "Street Food",
        "description": "Vegetable fritters dipped in gram flour batter and fried"
    },
    # 35. Palak Paneer
    "Palak Paneer": {
        "nutrition": { "calories": 320, "protein_g": 16, "carbs_g": 12, "fats_g": 22, "fiber_g": 4, "sugar_g": 3, "sodium_mg": 480 },
        "vitamins_minerals": { "vitamin_a_iu": 9500, "calcium_mg": 350, "iron_mg": 4.8, "potassium_mg": 620 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": True, "dairy_free": False, "spicy": False },
        "allergens": ["dairy"],
        "serving_size": "1 bowl (250g)",
        "region": "North India",
        "category": "Main Course",
        "description": "Paneer cubes in creamy spinach gravy"
    },
    # 36. Paneer Masala
    "Paneer Masala": {
        "nutrition": { "calories": 380, "protein_g": 16, "carbs_g": 15, "fats_g": 28, "fiber_g": 2, "sugar_g": 5, "sodium_mg": 620 },
        "vitamins_minerals": { "vitamin_a_iu": 550, "calcium_mg": 280, "iron_mg": 2.0, "potassium_mg": 320 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": True, "dairy_free": False, "spicy": True },
        "allergens": ["dairy"],
        "serving_size": "1 bowl (220g)",
        "region": "North India",
        "category": "Main Course",
        "description": "Paneer cubes in a rich and spicy tomato gravy"
    },
    # 37. Pav Bhaji
    "Pav Bhaji": {
        "nutrition": { "calories": 450, "protein_g": 10, "carbs_g": 65, "fats_g": 18, "fiber_g": 6, "sugar_g": 8, "sodium_mg": 700 },
        "vitamins_minerals": { "vitamin_c_mg": 25, "calcium_mg": 80, "iron_mg": 3.0, "potassium_mg": 450 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": False, "dairy_free": False, "spicy": True },
        "allergens": ["gluten", "dairy"],
        "serving_size": "2 pavs with bhaji (300g)",
        "region": "West India",
        "category": "Street Food",
        "description": "Spicy mixed vegetable mash served with buttered bread roll"
    },
    # 38. Pizza
    "Pizza": {
        "nutrition": { "calories": 285, "protein_g": 12, "carbs_g": 36, "fats_g": 10, "fiber_g": 2, "sugar_g": 3, "sodium_mg": 580 },
        "vitamins_minerals": { "calcium_mg": 150, "iron_mg": 2.0, "potassium_mg": 200 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": False, "dairy_free": False, "spicy": False },
        "allergens": ["gluten", "dairy"],
        "serving_size": "2 slices (200g)",
        "region": "International/Fusion",
        "category": "Main Course",
        "description": "Standard vegetable pizza"
    },
    # 39. Poha
    "Poha": {
        "nutrition": { "calories": 180, "protein_g": 3, "carbs_g": 32, "fats_g": 6, "fiber_g": 2, "sugar_g": 1, "sodium_mg": 320 },
        "vitamins_minerals": { "vitamin_c_mg": 8, "calcium_mg": 20, "iron_mg": 4.5, "potassium_mg": 180 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": ["nuts"],
        "serving_size": "1 bowl (150g)",
        "region": "West India",
        "category": "Breakfast",
        "description": "Flattened rice sautéed with onions, spices and peanuts"
    },
    # 40. Puri Bhaji (Updated)
    "Puri Bhaji": {
        "nutrition": { "calories": 350, "protein_g": 6, "carbs_g": 45, "fats_g": 18, "fiber_g": 4, "sugar_g": 2, "sodium_mg": 550 },
        "vitamins_minerals": { "calcium_mg": 35, "iron_mg": 2.4, "potassium_mg": 380 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": False, "dairy_free": False, "spicy": True },
        "allergens": ["gluten", "dairy"],
        "serving_size": "3 puris with bhaji (250g)",
        "region": "North India",
        "category": "Breakfast/Main Course",
        "description": "Deep-fried whole wheat bread served with spiced potato curry"
    },
    # 41. Rajma Chawal
    "Rajma Chawal": {
        "nutrition": { "calories": 380, "protein_g": 15, "carbs_g": 62, "fats_g": 8, "fiber_g": 12, "sugar_g": 4, "sodium_mg": 540 },
        "vitamins_minerals": { "vitamin_c_mg": 10, "calcium_mg": 95, "iron_mg": 5.2, "potassium_mg": 680 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": [],
        "serving_size": "1 plate (300g)",
        "region": "North India",
        "category": "Main Course",
        "description": "Red kidney beans curry served with steamed rice"
    },
    # 42. Rasgulla (Added Back)
    "Rasgulla": {
        "nutrition": { "calories": 140, "protein_g": 4, "carbs_g": 30, "fats_g": 1, "fiber_g": 0, "sugar_g": 25, "sodium_mg": 30 },
        "vitamins_minerals": { "calcium_mg": 120, "iron_mg": 0.2, "potassium_mg": 50 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": True, "dairy_free": False, "spicy": False },
        "allergens": ["dairy"],
        "serving_size": "2 pieces (100g)",
        "region": "East India",
        "category": "Dessert",
        "description": "Syrupy dessert popular in the Indian subcontinent"
    },
    # 43. Rava Dosa
    "Rava Dosa": {
        "nutrition": { "calories": 320, "protein_g": 6, "carbs_g": 48, "fats_g": 10, "fiber_g": 2, "sugar_g": 1, "sodium_mg": 420 },
        "vitamins_minerals": { "calcium_mg": 40, "iron_mg": 1.8, "potassium_mg": 280 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": False, "dairy_free": True, "spicy": True },
        "allergens": ["gluten"], # Rava is semolina (wheat)
        "serving_size": "1 large dosa (200g)",
        "region": "South India",
        "category": "Breakfast",
        "description": "Thin, crispy crepe made from semolina batter"
    },
    # 44. Samosa
    "Samosa": {
        "nutrition": { "calories": 260, "protein_g": 4, "carbs_g": 32, "fats_g": 14, "fiber_g": 3, "sugar_g": 2, "sodium_mg": 380 },
        "vitamins_minerals": { "vitamin_c_mg": 6, "calcium_mg": 25, "iron_mg": 2.2, "potassium_mg": 220 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": False, "dairy_free": True, "spicy": True },
        "allergens": ["gluten"],
        "serving_size": "2 pieces (100g)",
        "region": "North India",
        "category": "Street Food",
        "description": "Fried pastry with a savory potato filling"
    },
    # 45. Seekh Kebab (New)
    "Seekh Kebab": {
        "nutrition": { "calories": 280, "protein_g": 22, "carbs_g": 8, "fats_g": 18, "fiber_g": 1, "sugar_g": 2, "sodium_mg": 600 },
        "vitamins_minerals": { "calcium_mg": 40, "iron_mg": 3.0, "potassium_mg": 350 },
        "dietary_info": { "vegetarian": False, "vegan": False, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": [],
        "serving_size": "2 pieces (150g)",
        "region": "North India",
        "category": "Main Course",
        "description": "Spiced minced meat grilled on skewers"
    },
    # 46. Uttapam (New)
    "Uttapam": {
        "nutrition": { "calories": 280, "protein_g": 9, "carbs_g": 42, "fats_g": 8, "fiber_g": 4, "sugar_g": 3, "sodium_mg": 380 },
        "vitamins_minerals": { "vitamin_c_mg": 15, "calcium_mg": 68, "iron_mg": 2.2, "potassium_mg": 320 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": False },
        "allergens": [],
        "serving_size": "1 large piece (200g)",
        "region": "South India",
        "category": "Breakfast",
        "description": "Thick pancake made from rice batter topped with vegetables"
    },
    # 47. Vada Pav
    "Vada Pav": {
        "nutrition": { "calories": 300, "protein_g": 6, "carbs_g": 45, "fats_g": 12, "fiber_g": 3, "sugar_g": 3, "sodium_mg": 580 },
        "vitamins_minerals": { "vitamin_c_mg": 12, "calcium_mg": 40, "iron_mg": 2.5, "potassium_mg": 300 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": False, "dairy_free": True, "spicy": True },
        "allergens": ["gluten"],
        "serving_size": "1 piece (150g)",
        "region": "West India",
        "category": "Street Food",
        "description": "Deep fried potato dumpling placed inside a bread bun"
    },
    # 48. Amritsari Kulcha (New)
    "Amritsari Kulcha": {
        "nutrition": { "calories": 310, "protein_g": 8, "carbs_g": 45, "fats_g": 12, "fiber_g": 3, "sugar_g": 2, "sodium_mg": 480 },
        "vitamins_minerals": { "calcium_mg": 60, "iron_mg": 2.0, "potassium_mg": 220 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": False, "dairy_free": False, "spicy": False },
        "allergens": ["gluten", "dairy"],
        "serving_size": "1 kulcha (120g)",
        "region": "North India",
        "category": "Main Course",
        "description": "Crispy leavened flatbread stuffed with potatoes and spices"
    },
    # 49. Balushahi (New)
    "Balushahi": {
        "nutrition": { "calories": 250, "protein_g": 3, "carbs_g": 35, "fats_g": 12, "fiber_g": 1, "sugar_g": 25, "sodium_mg": 40 },
        "vitamins_minerals": { "calcium_mg": 20, "iron_mg": 0.8, "potassium_mg": 60 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": False, "dairy_free": False, "spicy": False },
        "allergens": ["gluten", "dairy"],
        "serving_size": "2 pieces (80g)",
        "region": "North India",
        "category": "Dessert",
        "description": "Deep-fried dough sweet glazed with sugar syrup"
    },
    # 50. Bhindi Masala (New)
    "Bhindi Masala": {
        "nutrition": { "calories": 160, "protein_g": 3, "carbs_g": 18, "fats_g": 10, "fiber_g": 6, "sugar_g": 4, "sodium_mg": 380 },
        "vitamins_minerals": { "vitamin_c_mg": 25, "calcium_mg": 85, "iron_mg": 1.5, "potassium_mg": 420 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": [],
        "serving_size": "1 bowl (200g)",
        "region": "North India",
        "category": "Main Course",
        "description": "Okra sautéed with onions and spices"
    },
    # 51. Chaas (New)
    "Chaas": {
        "nutrition": { "calories": 60, "protein_g": 3, "carbs_g": 8, "fats_g": 2, "fiber_g": 0, "sugar_g": 6, "sodium_mg": 250 },
        "vitamins_minerals": { "calcium_mg": 120, "iron_mg": 0.1, "potassium_mg": 180 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": True, "dairy_free": False, "spicy": False },
        "allergens": ["dairy"],
        "serving_size": "1 glass (200ml)",
        "region": "West India",
        "category": "Beverage",
        "description": "Spiced buttermilk drink"
    },
    # 52. Chana Masala (New)
    "Chana Masala": {
        "nutrition": { "calories": 280, "protein_g": 12, "carbs_g": 40, "fats_g": 8, "fiber_g": 10, "sugar_g": 4, "sodium_mg": 520 },
        "vitamins_minerals": { "vitamin_c_mg": 8, "calcium_mg": 80, "iron_mg": 3.8, "potassium_mg": 450 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": [],
        "serving_size": "1 bowl (250g)",
        "region": "North India",
        "category": "Main Course",
        "description": "Spicy chickpea curry"
    },
    # 53. Chicken Wings (New)
    "Chicken Wings": {
        "nutrition": { "calories": 450, "protein_g": 25, "carbs_g": 10, "fats_g": 35, "fiber_g": 0, "sugar_g": 5, "sodium_mg": 950 },
        "vitamins_minerals": { "calcium_mg": 20, "iron_mg": 1.2, "potassium_mg": 220 },
        "dietary_info": { "vegetarian": False, "vegan": False, "gluten_free": False, "dairy_free": True, "spicy": True },
        "allergens": ["gluten", "soy"],
        "serving_size": "4 wings (200g)",
        "region": "International/Fusion",
        "category": "Appetizer/Snack",
        "description": "Fried chicken wings tossed in spicy sauces"
    },
    # 54. Chivda (New)
    "Chivda": {
        "nutrition": { "calories": 180, "protein_g": 4, "carbs_g": 25, "fats_g": 8, "fiber_g": 2, "sugar_g": 2, "sodium_mg": 320 },
        "vitamins_minerals": { "calcium_mg": 25, "iron_mg": 4.0, "potassium_mg": 150 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": ["nuts"],
        "serving_size": "1 bowl (40g)",
        "region": "West India",
        "category": "Street Food",
        "description": "Crispy savory snack made with flattened rice and nuts"
    },
    # 55. Dabeli (New)
    "Dabeli": {
        "nutrition": { "calories": 320, "protein_g": 8, "carbs_g": 48, "fats_g": 12, "fiber_g": 4, "sugar_g": 12, "sodium_mg": 580 },
        "vitamins_minerals": { "vitamin_c_mg": 10, "calcium_mg": 60, "iron_mg": 2.2, "potassium_mg": 300 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": False, "dairy_free": False, "spicy": True },
        "allergens": ["gluten", "dairy", "nuts"],
        "serving_size": "1 piece (150g)",
        "region": "West India",
        "category": "Street Food",
        "description": "Spicy potato burger from Gujarat"
    },
    # 56. Falooda (New)
    "Falooda": {
        "nutrition": { "calories": 380, "protein_g": 6, "carbs_g": 65, "fats_g": 10, "fiber_g": 2, "sugar_g": 45, "sodium_mg": 80 },
        "vitamins_minerals": { "calcium_mg": 220, "iron_mg": 0.5, "potassium_mg": 280 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": True, "dairy_free": False, "spicy": False },
        "allergens": ["dairy", "nuts"],
        "serving_size": "1 glass (300ml)",
        "region": "North India",
        "category": "Beverage",
        "description": "Chilled dessert drink with vermicelli and rose syrup"
    },
    # 57. Garlic Bread (New)
    "Garlic Bread": {
        "nutrition": { "calories": 250, "protein_g": 6, "carbs_g": 32, "fats_g": 10, "fiber_g": 2, "sugar_g": 2, "sodium_mg": 450 },
        "vitamins_minerals": { "calcium_mg": 80, "iron_mg": 1.5, "potassium_mg": 120 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": False, "dairy_free": False, "spicy": False },
        "allergens": ["gluten", "dairy"],
        "serving_size": "2 pieces (100g)",
        "region": "International/Fusion",
        "category": "Appetizer/Snack",
        "description": "Toasted bread with garlic and butter"
    },
    # 58. Ghevar (New)
    "Ghevar": {
        "nutrition": { "calories": 420, "protein_g": 4, "carbs_g": 55, "fats_g": 20, "fiber_g": 1, "sugar_g": 35, "sodium_mg": 60 },
        "vitamins_minerals": { "calcium_mg": 40, "iron_mg": 0.8, "potassium_mg": 110 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": False, "dairy_free": False, "spicy": False },
        "allergens": ["gluten", "dairy"],
        "serving_size": "1 piece (120g)",
        "region": "West India",
        "category": "Dessert",
        "description": "Honeycomb-shaped sweet crust from Rajasthan"
    },
    # 59. Gujhia (New)
    "Gujhia": {
        "nutrition": { "calories": 280, "protein_g": 5, "carbs_g": 38, "fats_g": 14, "fiber_g": 2, "sugar_g": 18, "sodium_mg": 40 },
        "vitamins_minerals": { "calcium_mg": 60, "iron_mg": 1.2, "potassium_mg": 140 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": False, "dairy_free": False, "spicy": False },
        "allergens": ["gluten", "dairy", "nuts"],
        "serving_size": "2 pieces (80g)",
        "region": "North India",
        "category": "Dessert",
        "description": "Deep-fried dumpling filled with khoya and nuts"
    },
    # 60. Idiyappam (New)
    "Idiyappam": {
        "nutrition": { "calories": 150, "protein_g": 3, "carbs_g": 32, "fats_g": 1, "fiber_g": 2, "sugar_g": 0, "sodium_mg": 40 },
        "vitamins_minerals": { "calcium_mg": 10, "iron_mg": 0.5, "potassium_mg": 80 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": False },
        "allergens": [],
        "serving_size": "3 pieces (120g)",
        "region": "South India",
        "category": "Breakfast",
        "description": "String hoppers made from rice flour"
    },
    # 61. Laddu (New)
    "Laddu": {
        "nutrition": { "calories": 185, "protein_g": 4, "carbs_g": 22, "fats_g": 10, "fiber_g": 2, "sugar_g": 12, "sodium_mg": 30 },
        "vitamins_minerals": { "calcium_mg": 40, "iron_mg": 1.5, "potassium_mg": 160 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": True, "dairy_free": False, "spicy": False },
        "allergens": ["dairy", "nuts"],
        "serving_size": "1 piece (50g)",
        "region": "North India",
        "category": "Dessert",
        "description": "Sweet balls made from gram flour, ghee, and sugar"
    },
    # 62. Masala Papad (New)
    "Masala Papad": {
        "nutrition": { "calories": 80, "protein_g": 4, "carbs_g": 10, "fats_g": 3, "fiber_g": 2, "sugar_g": 1, "sodium_mg": 450 },
        "vitamins_minerals": { "vitamin_c_mg": 8, "calcium_mg": 25, "iron_mg": 1.2, "potassium_mg": 180 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": [],
        "serving_size": "1 papad (40g)",
        "region": "North India",
        "category": "Appetizer/Snack",
        "description": "Roasted papad topped with spiced onions and tomatoes"
    },
    # 63. Mysore Pak (New)
    "Mysore Pak": {
        "nutrition": { "calories": 240, "protein_g": 2, "carbs_g": 28, "fats_g": 14, "fiber_g": 1, "sugar_g": 20, "sodium_mg": 20 },
        "vitamins_minerals": { "calcium_mg": 15, "iron_mg": 0.5, "potassium_mg": 80 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": True, "dairy_free": False, "spicy": False },
        "allergens": ["dairy"],
        "serving_size": "1 piece (50g)",
        "region": "South India",
        "category": "Dessert",
        "description": "Rich sweet made of gram flour, ghee, and sugar"
    },
    # 64. Navratan Korma (New)
    "Navratan Korma": {
        "nutrition": { "calories": 320, "protein_g": 8, "carbs_g": 25, "fats_g": 22, "fiber_g": 5, "sugar_g": 10, "sodium_mg": 550 },
        "vitamins_minerals": { "vitamin_a_iu": 800, "calcium_mg": 120, "iron_mg": 2.5, "potassium_mg": 480 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": True, "dairy_free": False, "spicy": False },
        "allergens": ["dairy", "nuts"],
        "serving_size": "1 bowl (250g)",
        "region": "North India",
        "category": "Main Course",
        "description": "Creamy vegetable curry with fruits and nuts"
    },
    # 65. Paniyaram (New)
    "Paniyaram": {
        "nutrition": { "calories": 180, "protein_g": 4, "carbs_g": 30, "fats_g": 5, "fiber_g": 3, "sugar_g": 2, "sodium_mg": 320 },
        "vitamins_minerals": { "calcium_mg": 40, "iron_mg": 1.2, "potassium_mg": 120 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": False },
        "allergens": [],
        "serving_size": "4 pieces (120g)",
        "region": "South India",
        "category": "Breakfast",
        "description": "Small steamed cakes made of fermented batter"
    },
    # 66. Papdi Chaat (New)
    "Papdi Chaat": {
        "nutrition": { "calories": 280, "protein_g": 6, "carbs_g": 42, "fats_g": 11, "fiber_g": 4, "sugar_g": 12, "sodium_mg": 680 },
        "vitamins_minerals": { "vitamin_c_mg": 15, "calcium_mg": 85, "iron_mg": 3.0, "potassium_mg": 350 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": False, "dairy_free": False, "spicy": True },
        "allergens": ["gluten", "dairy"],
        "serving_size": "1 plate (200g)",
        "region": "North India",
        "category": "Street Food",
        "description": "Wafers topped with potatoes, yogurt, and chutneys"
    },
    # 67. Phirni (New)
    "Phirni": {
        "nutrition": { "calories": 220, "protein_g": 5, "carbs_g": 35, "fats_g": 7, "fiber_g": 1, "sugar_g": 25, "sodium_mg": 60 },
        "vitamins_minerals": { "calcium_mg": 160, "iron_mg": 0.4, "potassium_mg": 220 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": True, "dairy_free": False, "spicy": False },
        "allergens": ["dairy", "nuts"],
        "serving_size": "1 bowl (150g)",
        "region": "North India",
        "category": "Dessert",
        "description": "Ground rice pudding served chilled"
    },
    # 68. Pongal (New)
    "Pongal": {
        "nutrition": { "calories": 320, "protein_g": 8, "carbs_g": 45, "fats_g": 14, "fiber_g": 4, "sugar_g": 1, "sodium_mg": 380 },
        "vitamins_minerals": { "calcium_mg": 45, "iron_mg": 3.5, "potassium_mg": 150 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": False, "spicy": False },
        "allergens": ["dairy"], # Uses ghee
        "serving_size": "1 bowl (250g)",
        "region": "South India",
        "category": "Breakfast",
        "description": "Savory rice and lentil porridge with black pepper"
    },
    # 69. Sabudana Khichdi (New)
    "Sabudana Khichdi": {
        "nutrition": { "calories": 350, "protein_g": 4, "carbs_g": 65, "fats_g": 8, "fiber_g": 2, "sugar_g": 2, "sodium_mg": 420 },
        "vitamins_minerals": { "vitamin_c_mg": 12, "calcium_mg": 30, "iron_mg": 2.5, "potassium_mg": 180 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": ["nuts"],
        "serving_size": "1 plate (200g)",
        "region": "West India",
        "category": "Breakfast",
        "description": "Sago pearls sautéed with potatoes and peanuts"
    },
    # 70. Sabudana Vada (New)
    "Sabudana Vada": {
        "nutrition": { "calories": 240, "protein_g": 3, "carbs_g": 35, "fats_g": 10, "fiber_g": 2, "sugar_g": 1, "sodium_mg": 350 },
        "vitamins_minerals": { "calcium_mg": 15, "iron_mg": 1.2, "potassium_mg": 140 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": ["nuts"],
        "serving_size": "2 pieces (120g)",
        "region": "West India",
        "category": "Appetizer/Snack",
        "description": "Deep-fried sago and potato fritters"
    },
    # 71. Set Dosa (New)
    "Set Dosa": {
        "nutrition": { "calories": 280, "protein_g": 6, "carbs_g": 45, "fats_g": 8, "fiber_g": 3, "sugar_g": 1, "sodium_mg": 380 },
        "vitamins_minerals": { "calcium_mg": 35, "iron_mg": 1.8, "potassium_mg": 220 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": False },
        "allergens": [],
        "serving_size": "3 small dosas (180g)",
        "region": "South India",
        "category": "Breakfast/Main Course",
        "description": "Soft and spongey dosas served in sets"
    },
    # 72. Sev Puri (New)
    "Sev Puri": {
        "nutrition": { "calories": 250, "protein_g": 5, "carbs_g": 35, "fats_g": 11, "fiber_g": 4, "sugar_g": 10, "sodium_mg": 620 },
        "vitamins_minerals": { "vitamin_c_mg": 12, "calcium_mg": 45, "iron_mg": 2.5, "potassium_mg": 280 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": False, "dairy_free": True, "spicy": True },
        "allergens": ["gluten"],
        "serving_size": "6 pieces (150g)",
        "region": "West India",
        "category": "Street Food",
        "description": "Crispy puris topped with potatoes, chutneys, and sev"
    },
    # 73. Thali (New)
    "Thali": {
        "nutrition": { "calories": 850, "protein_g": 28, "carbs_g": 110, "fats_g": 32, "fiber_g": 15, "sugar_g": 15, "sodium_mg": 1200 },
        "vitamins_minerals": { "vitamin_a_iu": 1500, "calcium_mg": 350, "iron_mg": 8.5, "potassium_mg": 950 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": False, "dairy_free": False, "spicy": True },
        "allergens": ["gluten", "dairy", "nuts"],
        "serving_size": "1 full thali (600g)",
        "region": "West India",
        "category": "Main Course",
        "description": "Complete Indian meal platter with various dishes"
    },
    # 74. Thukpa (New)
    "Thukpa": {
        "nutrition": { "calories": 380, "protein_g": 22, "carbs_g": 45, "fats_g": 12, "fiber_g": 6, "sugar_g": 4, "sodium_mg": 850 },
        "vitamins_minerals": { "vitamin_a_iu": 450, "calcium_mg": 60, "iron_mg": 3.2, "potassium_mg": 520 },
        "dietary_info": { "vegetarian": False, "vegan": False, "gluten_free": False, "dairy_free": True, "spicy": True },
        "allergens": ["gluten", "soy"],
        "serving_size": "1 bowl (400g)",
        "region": "East India",
        "category": "Main Course",
        "description": "Tibetan noodle soup with meat and vegetables"
    },
    # 75. Appam (New)
    "Appam": {
        "nutrition": { "calories": 120, "protein_g": 2, "carbs_g": 28, "fats_g": 1, "fiber_g": 1, "sugar_g": 2, "sodium_mg": 180 },
        "vitamins_minerals": { "calcium_mg": 15, "iron_mg": 0.5, "potassium_mg": 85 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": False },
        "allergens": [],
        "serving_size": "2 pieces (100g)",
        "region": "South India",
        "category": "Breakfast",
        "description": "Fermented rice and coconut milk pancakes"
    },
    # 76. Aviyal (New)
    "Aviyal": {
        "nutrition": { "calories": 240, "protein_g": 6, "carbs_g": 18, "fats_g": 18, "fiber_g": 8, "sugar_g": 4, "sodium_mg": 380 },
        "vitamins_minerals": { "vitamin_a_iu": 1200, "calcium_mg": 140, "iron_mg": 1.5, "potassium_mg": 550 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": True, "dairy_free": False, "spicy": False },
        "allergens": ["dairy"],
        "serving_size": "1 bowl (200g)",
        "region": "South India",
        "category": "Main Course",
        "description": "Mixed vegetable stew with coconut and yogurt"
    },
    # 77. Bisi Bele Bath (New)
    "Bisi Bele Bath": {
        "nutrition": { "calories": 320, "protein_g": 8, "carbs_g": 52, "fats_g": 10, "fiber_g": 6, "sugar_g": 3, "sodium_mg": 550 },
        "vitamins_minerals": { "vitamin_c_mg": 12, "calcium_mg": 45, "iron_mg": 2.2, "potassium_mg": 380 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": True, "dairy_free": False, "spicy": True },
        "allergens": ["dairy"],
        "serving_size": "1 bowl (250g)",
        "region": "South India",
        "category": "Main Course",
        "description": "Spicy rice and lentil mash with vegetables"
    },
    # 78. Chicken 65 (New)
    "Chicken 65": {
        "nutrition": { "calories": 350, "protein_g": 28, "carbs_g": 12, "fats_g": 22, "fiber_g": 1, "sugar_g": 1, "sodium_mg": 780 },
        "vitamins_minerals": { "calcium_mg": 25, "iron_mg": 1.2, "potassium_mg": 310 },
        "dietary_info": { "vegetarian": False, "vegan": False, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": [],
        "serving_size": "6 pieces (150g)",
        "region": "South India",
        "category": "Appetizer/Snack",
        "description": "Spicy, deep-fried chicken appetizer"
    },
    # 79. Chicken Chettinad (New)
    "Chicken Chettinad": {
        "nutrition": { "calories": 380, "protein_g": 32, "carbs_g": 10, "fats_g": 24, "fiber_g": 3, "sugar_g": 2, "sodium_mg": 680 },
        "vitamins_minerals": { "vitamin_a_iu": 400, "calcium_mg": 65, "iron_mg": 2.5, "potassium_mg": 520 },
        "dietary_info": { "vegetarian": False, "vegan": False, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": [],
        "serving_size": "1 bowl (250g)",
        "region": "South India",
        "category": "Main Course",
        "description": "Fiery Peppery Chicken Curry from Tamil Nadu"
    },
    # 80. Curd Rice (New)
    "Curd Rice": {
        "nutrition": { "calories": 280, "protein_g": 8, "carbs_g": 42, "fats_g": 9, "fiber_g": 1, "sugar_g": 4, "sodium_mg": 320 },
        "vitamins_minerals": { "calcium_mg": 220, "iron_mg": 0.5, "potassium_mg": 180 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": True, "dairy_free": False, "spicy": False },
        "allergens": ["dairy"],
        "serving_size": "1 bowl (250g)",
        "region": "South India",
        "category": "Main Course",
        "description": "Rice mixed with yogurt and tempered with spices"
    },
    # 81. Fish Fry (New)
    "Fish Fry": {
        "nutrition": { "calories": 310, "protein_g": 24, "carbs_g": 8, "fats_g": 20, "fiber_g": 1, "sugar_g": 0, "sodium_mg": 580 },
        "vitamins_minerals": { "calcium_mg": 45, "iron_mg": 1.5, "potassium_mg": 350 },
        "dietary_info": { "vegetarian": False, "vegan": False, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": [],
        "serving_size": "2 pieces (150g)",
        "region": "South India",
        "category": "Appetizer/Snack",
        "description": "Crispy pan-fried fish marinated in South Indian spices"
    },
    # 82. Karimeen Pollichathu (New)
    "Karimeen Pollichathu": {
        "nutrition": { "calories": 340, "protein_g": 26, "carbs_g": 12, "fats_g": 22, "fiber_g": 4, "sugar_g": 2, "sodium_mg": 620 },
        "vitamins_minerals": { "vitamin_a_iu": 600, "calcium_mg": 85, "iron_mg": 2.1, "potassium_mg": 480 },
        "dietary_info": { "vegetarian": False, "vegan": False, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": [],
        "serving_size": "1 whole fish (250g)",
        "region": "South India",
        "category": "Main Course",
        "description": "Pearl spot fish marinated and grilled in banana leaf"
    },
    # 83. Kerala Fish Curry (New)
    "Kerala Fish Curry": {
        "nutrition": { "calories": 280, "protein_g": 22, "carbs_g": 8, "fats_g": 18, "fiber_g": 2, "sugar_g": 2, "sodium_mg": 650 },
        "vitamins_minerals": { "vitamin_c_mg": 15, "calcium_mg": 40, "iron_mg": 1.8, "potassium_mg": 420 },
        "dietary_info": { "vegetarian": False, "vegan": False, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": [],
        "serving_size": "1 bowl (250g)",
        "region": "South India",
        "category": "Main Course",
        "description": "Spicy red fish curry with tamarind and coconut oil"
    },
    # 84. Kothu Parotta (New)
    "Kothu Parotta": {
        "nutrition": { "calories": 450, "protein_g": 18, "carbs_g": 55, "fats_g": 18, "fiber_g": 4, "sugar_g": 3, "sodium_mg": 880 },
        "vitamins_minerals": { "calcium_mg": 45, "iron_mg": 2.5, "potassium_mg": 320 },
        "dietary_info": { "vegetarian": False, "vegan": False, "gluten_free": False, "dairy_free": True, "spicy": True },
        "allergens": ["gluten"],
        "serving_size": "1 plate (300g)",
        "region": "South India",
        "category": "Street Food",
        "description": "Shredded parotta mixed with vegetables and meat"
    },
    # 85. Lemon Rice (New)
    "Lemon Rice": {
        "nutrition": { "calories": 310, "protein_g": 6, "carbs_g": 52, "fats_g": 10, "fiber_g": 2, "sugar_g": 2, "sodium_mg": 450 },
        "vitamins_minerals": { "vitamin_c_mg": 35, "calcium_mg": 25, "iron_mg": 1.5, "potassium_mg": 180 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": False },
        "allergens": ["nuts"],
        "serving_size": "1 bowl (250g)",
        "region": "South India",
        "category": "Main Course",
        "description": "Zesty rice flavored with lemon juice and tempering"
    },
    # 86. Litti Chokha (New)
    "Litti Chokha": {
        "nutrition": { "calories": 420, "protein_g": 12, "carbs_g": 65, "fats_g": 14, "fiber_g": 8, "sugar_g": 4, "sodium_mg": 1150 },
        "vitamins_minerals": { "calcium_mg": 85, "iron_mg": 4.5, "potassium_mg": 620 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": False, "dairy_free": False, "spicy": True },
        "allergens": ["gluten", "dairy"],
        "serving_size": "2 littis + chokha (250g)",
        "region": "East India",
        "category": "Main Course",
        "description": "Roasted wheat balls with sattu filling and mashed vegetables"
    },
    # 87. Macher Jhol (New)
    "Macher Jhol": {
        "nutrition": { "calories": 260, "protein_g": 20, "carbs_g": 10, "fats_g": 16, "fiber_g": 2, "sugar_g": 2, "sodium_mg": 580 },
        "vitamins_minerals": { "vitamin_a_iu": 400, "calcium_mg": 45, "iron_mg": 1.5, "potassium_mg": 380 },
        "dietary_info": { "vegetarian": False, "vegan": False, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": [],
        "serving_size": "1 bowl (250g)",
        "region": "East India",
        "category": "Main Course",
        "description": "Traditional Bengali fish stew with mustard oil"
    },
    # 88. Manchurian (New)
    "Manchurian": {
        "nutrition": { "calories": 320, "protein_g": 8, "carbs_g": 38, "fats_g": 16, "fiber_g": 4, "sugar_g": 10, "sodium_mg": 1200 },
        "vitamins_minerals": { "vitamin_c_mg": 15, "calcium_mg": 45, "iron_mg": 1.2, "potassium_mg": 280 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": False, "dairy_free": True, "spicy": True },
        "allergens": ["soy", "gluten"],
        "serving_size": "1 bowl (200g)",
        "region": "International/Fusion",
        "category": "Main Course",
        "description": "Veg dumplings in soy-based umami sauce"
    },
    # 89. Methi Thepla (New)
    "Methi Thepla": {
        "nutrition": { "calories": 140, "protein_g": 4, "carbs_g": 22, "fats_g": 5, "fiber_g": 3, "sugar_g": 1, "sodium_mg": 280 },
        "vitamins_minerals": { "calcium_mg": 120, "iron_mg": 2.2, "potassium_mg": 150 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": False, "dairy_free": False, "spicy": False },
        "allergens": ["gluten", "dairy"],
        "serving_size": "1 piece (50g)",
        "region": "West India",
        "category": "Breakfast",
        "description": "Gujarati flatbread made with fenugreek leaves"
    },
    # 90. Payasam (New)
    "Payasam": {
        "nutrition": { "calories": 280, "protein_g": 6, "carbs_g": 45, "fats_g": 10, "fiber_g": 1, "sugar_g": 35, "sodium_mg": 65 },
        "vitamins_minerals": { "calcium_mg": 180, "iron_mg": 0.5, "potassium_mg": 220 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": True, "dairy_free": False, "spicy": False },
        "allergens": ["dairy", "nuts"],
        "serving_size": "1 bowl (150ml)",
        "region": "South India",
        "category": "Dessert",
        "description": "Sweet milk pudding with vermicelli or rice"
    },
    # 91. Puran Poli (New)
    "Puran Poli": {
        "nutrition": { "calories": 320, "protein_g": 8, "carbs_g": 55, "fats_g": 8, "fiber_g": 4, "sugar_g": 25, "sodium_mg": 45 },
        "vitamins_minerals": { "calcium_mg": 35, "iron_mg": 2.8, "potassium_mg": 310 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": False, "dairy_free": False, "spicy": False },
        "allergens": ["gluten", "dairy"],
        "serving_size": "1 piece (100g)",
        "region": "West India",
        "category": "Dessert",
        "description": "Sweet lentil-stuffed flatbread"
    },
    # 92. Puttu (New)
    "Puttu": {
        "nutrition": { "calories": 240, "protein_g": 5, "carbs_g": 50, "fats_g": 3, "fiber_g": 3, "sugar_g": 1, "sodium_mg": 120 },
        "vitamins_minerals": { "calcium_mg": 15, "iron_mg": 0.8, "potassium_mg": 110 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": False },
        "allergens": [],
        "serving_size": "1 roll (150g)",
        "region": "South India",
        "category": "Breakfast",
        "description": "Steamed cylinders of ground rice and coconut"
    },
    # 93. Rasam (New)
    "Rasam": {
        "nutrition": { "calories": 60, "protein_g": 2, "carbs_g": 10, "fats_g": 2, "fiber_g": 2, "sugar_g": 2, "sodium_mg": 480 },
        "vitamins_minerals": { "vitamin_c_mg": 12, "calcium_mg": 35, "iron_mg": 1.2, "potassium_mg": 250 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": [],
        "serving_size": "1 bowl (200ml)",
        "region": "South India",
        "category": "Beverage",
        "description": "Spiced tamarind and tomato soup/drink"
    },
    # 94. Sambar Rice (New)
    "Sambar Rice": {
        "nutrition": { "calories": 340, "protein_g": 10, "carbs_g": 55, "fats_g": 10, "fiber_g": 8, "sugar_g": 4, "sodium_mg": 580 },
        "vitamins_minerals": { "vitamin_c_mg": 15, "calcium_mg": 65, "iron_mg": 2.8, "potassium_mg": 450 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": [],
        "serving_size": "1 bowl (300g)",
        "region": "South India",
        "category": "Main Course",
        "description": "Rice cooked with lentils and mixed vegetables"
    },
    # 95. Sandesh (New)
    "Sandesh": {
        "nutrition": { "calories": 150, "protein_g": 6, "carbs_g": 18, "fats_g": 6, "fiber_g": 0, "sugar_g": 16, "sodium_mg": 45 },
        "vitamins_minerals": { "calcium_mg": 140, "iron_mg": 0.2, "potassium_mg": 95 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": True, "dairy_free": False, "spicy": False },
        "allergens": ["dairy", "nuts"],
        "serving_size": "2 pieces (60g)",
        "region": "East India",
        "category": "Dessert",
        "description": "Soft Bengali sweet made from fresh paneer"
    },
    # 96. Tamarind Rice (New)
    "Tamarind Rice": {
        "nutrition": { "calories": 350, "protein_g": 6, "carbs_g": 58, "fats_g": 12, "fiber_g": 4, "sugar_g": 6, "sodium_mg": 520 },
        "vitamins_minerals": { "calcium_mg": 45, "iron_mg": 2.2, "potassium_mg": 210 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": True, "dairy_free": True, "spicy": True },
        "allergens": ["nuts"],
        "serving_size": "1 bowl (250g)",
        "region": "South India",
        "category": "Main Course",
        "description": "Tangy rice flavored with tamarind and spices"
    },
    # 97. Unni Appam (New)
    "Unni Appam": {
        "nutrition": { "calories": 180, "protein_g": 3, "carbs_g": 28, "fats_g": 7, "fiber_g": 1, "sugar_g": 15, "sodium_mg": 35 },
        "vitamins_minerals": { "calcium_mg": 25, "iron_mg": 0.8, "potassium_mg": 140 },
        "dietary_info": { "vegetarian": True, "vegan": False, "gluten_free": True, "dairy_free": True, "spicy": False },
        "allergens": [],
        "serving_size": "3 pieces (90g)",
        "region": "South India",
        "category": "Dessert/Snack",
        "description": "Sweet fried balls made with rice and banana"
    },
    # 98. Upma (New)
    "Upma": {
        "nutrition": { "calories": 210, "protein_g": 5, "carbs_g": 35, "fats_g": 6, "fiber_g": 3, "sugar_g": 2, "sodium_mg": 420 },
        "vitamins_minerals": { "vitamin_b1_mg": 0.15, "calcium_mg": 25, "iron_mg": 1.2, "potassium_mg": 160 },
        "dietary_info": { "vegetarian": True, "vegan": True, "gluten_free": False, "dairy_free": True, "spicy": False },
        "allergens": ["gluten"],
        "serving_size": "1 bowl (200g)",
        "region": "South India",
        "category": "Breakfast",
        "description": "Savory semolina porridge with vegetables"
    },
}

def get_nutrition_info(dish_name, quantity=None, unit=None, portion='medium'):
    """
    Retrieve nutrition information for a given dish.
    Supports fixed portions: 'small', 'medium', 'large', 'family'
    OR specific quantity and unit: quantity=150, unit='grams' or quantity=2, unit='pieces'
    """
    data = NUTRITION_DATABASE.get(dish_name, None)
    
    if not data:
        return None
        
    # Deep copy to avoid modifying original
    import copy
    import re
    result = copy.deepcopy(data)
    
    # Calculate multiplier
    mult = 1.0
    
    # 1. Check if specific quantity and unit provided
    if quantity is not None and unit:
        try:
            qty = float(quantity)
            serving_str = data.get('serving_size', '')
            
            # Parse base serving size (e.g., "1 piece (50g)" or "1 bowl (200g)")
            # Extract grams: "200g" or "200ml"
            gram_match = re.search(r'(\d+)\s*(g|ml)', serving_str)
            # Extract count: "1 piece" or "2 pieces" or "1 bowl"
            count_match = re.search(r'^(\d+)', serving_str)
            
            base_grams = float(gram_match.group(1)) if gram_match else 100.0
            base_count = float(count_match.group(1)) if count_match else 1.0
            
            if unit.lower() in ['g', 'grams', 'ml']:
                mult = qty / base_grams
            elif unit.lower() in ['pieces', 'piece', 'count', 'serving', 'servings', 'portion', 'portions', 'bowl', 'bowls']:
                mult = qty / base_count
            else:
                # Fallback to standard
                mult = 1.0
        except (ValueError, TypeError, ZeroDivisionError):
            mult = 1.0
    else:
        # 2. Use standard portion multipliers
        multipliers = {'small': 0.5, 'medium': 1.0, 'large': 1.5, 'extra_large': 1.5, 'family': 2.0}
        mult = multipliers.get(portion.lower(), 1.0)
    
    # Store the calculated multiplier and quantity for frontend reference
    result['portion_info'] = {
        'multiplier': mult,
        'applied_quantity': quantity,
        'applied_unit': unit,
        'applied_portion': portion if quantity is None else 'custom'
    }
    
    # Apply multiplier to nutrition values
    if mult != 1.0:
        for key, value in result['nutrition'].items():
            if isinstance(value, (int, float)):
                result['nutrition'][key] = round(value * mult, 1)
                
    return result

def get_all_dishes():
    """Retrieve list of all dishes in the database."""
    return list(NUTRITION_DATABASE.keys())

def get_health_indicators(nutrition_data):
    """
    Calculate health indicators based on nutritional values.
    Returns list of health indicator badges.
    
    Criteria:
    - High Fiber: >= 5g fiber per serving
    - Diabetic Friendly: Low sugar (< 10g) AND High fiber (>= 3g)
    - High Protein: >= 15g protein per serving
    - Heart Healthy: Low sodium (< 400mg) AND Low saturated fats
    - Low Calorie: < 200 calories per serving
    """
    indicators = []
    
    nutrition = nutrition_data['nutrition']
    fiber = nutrition.get('fiber_g', 0)
    protein = nutrition.get('protein_g', 0)
    sugar = nutrition.get('sugar_g', 0)
    sodium = nutrition.get('sodium_mg', 0)
    calories = nutrition.get('calories', 0)
    
    # High Fiber
    if fiber >= 5:
        indicators.append({
            "badge": "High Fiber",
            "icon": "🌾",
            "description": f"Excellent source of dietary fiber ({fiber}g)"
        })
    
    # Diabetic Friendly
    if sugar < 10 and fiber >= 3:
        indicators.append({
            "badge": "Diabetic Friendly",
            "icon": "💚",
            "description": "Low sugar with good fiber content"
        })
    
    # High Protein
    if protein >= 15:
        indicators.append({
            "badge": "High Protein",
            "icon": "💪",
            "description": f"Rich in protein ({protein}g)"
        })
    
    # Heart Healthy
    if sodium < 400:
        indicators.append({
            "badge": "Heart Healthy",
            "icon": "❤️",
            "description": f"Low sodium ({sodium}mg)"
        })
    
    # Low Calorie
    if calories < 200:
        indicators.append({
            "badge": "Low Calorie",
            "icon": "⚡",
            "description": f"Light option ({calories} kcal)"
        })
    
    return indicators

def calculate_health_score(nutrition_data):
    """
    Calculate a health score from 0-100 based on nutrient density.
    Parameters considered: Fiber, Protein (Positive) | Sugar, Sodium, Saturated Fats (Negative).
    """
    score = 50 # Base score
    
    nut = nutrition_data['nutrition']
    fiber = nut.get('fiber_g', 0)
    protein = nut.get('protein_g', 0)
    sugar = nut.get('sugar_g', 0)
    sodium = nut.get('sodium_mg', 0)
    calories = nut.get('calories', 0)
    
    # Positive points
    score += (fiber * 5)      # +5 for every gram of fiber
    score += (protein * 2)    # +2 for every gram of protein
    
    # Negative points
    score -= (sugar * 3)      # -3 for every gram of sugar
    score -= (sodium / 50)    # -1 for every 50mg of sodium
    
    # Calorie penalty for very high calorie items
    if calories > 600:
        score -= 10
    
    # Clamp score between 0 and 100
    return max(0, min(100, round(score)))

def get_dietary_suitability(nutrition_data):
    """
    Returns lists of who can and who should avoid this dish.
    """
    nut = nutrition_data['nutrition']
    diet = nutrition_data['dietary_info']
    
    can_eat = []
    cannot_eat = []
    
    # Recommendations (Who Can Eat)
    if nut.get('protein_g', 0) >= 15:
        can_eat.append({"target": "Athletes", "reason": "High protein content for muscle recovery"})
    if nut.get('fiber_g', 0) >= 5:
        can_eat.append({"target": "Weight Management", "reason": "High fiber helps in satiety"})
    if nut.get('sodium_mg', 0) < 400:
        can_eat.append({"target": "Heart Healthy", "reason": "Low sodium content"})
    if diet.get('vegetarian'):
        can_eat.append({"target": "Vegetarians", "reason": "Plant-based ingredients"})
    
    # Warnings (Who Should Avoid) - STRICTER THRESHOLDS & NEW ALERTS
    if nut.get('sugar_g', 0) > 10: # Lowered from 15g
        cannot_eat.append({"target": "Diabetics", "reason": "High sugar content (>10g) spike risk"})
    
    if nut.get('sodium_mg', 0) > 800: # Lowered from 1000mg
        cannot_eat.append({"target": "Hypertension", "reason": "Excessive sodium (>800mg)"})
        
    if nut.get('fats_g', 0) > 15: # New Warning
        cannot_eat.append({"target": "Heart Patients", "reason": "High fat content (>15g)"})
        
    if nut.get('carbs_g', 0) > 50: # New Warning
        cannot_eat.append({"target": "Keto/Low-Carb", "reason": "Very high carbs (>50g)"})
        
    if nut.get('calories', 0) > 500:
        cannot_eat.append({"target": "Calorie Watchers", "reason": "High calorie density (>500 kcal)"})
    
    # Allergens
    if nutrition_data.get('allergens'):
        for allergen in nutrition_data['allergens']:
            cannot_eat.append({"target": f"{allergen.capitalize()} Sensitive", "reason": f"Contains {allergen}"})

    return {
        "recommended_for": can_eat,
        "avoid_for": cannot_eat
    }
