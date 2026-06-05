"""
Ingredient-builder configuration for build-your-own style chains.
Item names must exactly match what is stored in the DB for that chain.
"""

BUILDER_CONFIGS: dict[str, dict] = {

    # ── CHIPOTLE ──────────────────────────────────────────────────────────────
    "chipotle": {
        "meal_types": [
            {"id": "bowl",       "name": "Bowl",         "icon": "🥣", "description": "All your favourites in a bowl",             "base_items": []},
            {"id": "burrito",    "name": "Burrito",       "icon": "🌯", "description": "Wrapped in a warm flour tortilla",           "base_items": ["Flour Tortilla"]},
            {"id": "taco-crispy","name": "Crispy Tacos",  "icon": "🌮", "description": "Three crispy corn shells",                   "base_items": ["Crispy Corn Taco Shells (3)"]},
            {"id": "taco-soft",  "name": "Soft Tacos",    "icon": "🫔", "description": "Three soft flour tortillas",                 "base_items": ["Soft Flour Taco Shells (3)"]},
            {"id": "salad",      "name": "Salad",          "icon": "🥗", "description": "Fresh romaine base",                         "base_items": ["Romaine Lettuce"]},
            {"id": "quesadilla", "name": "Quesadilla",    "icon": "🧀", "description": "Flour tortilla + cheese + your protein",     "base_items": ["Flour Tortilla", "Cheese"]},
        ],
        "ingredient_groups": [
            {"id": "protein",  "name": "Protein",  "required": True,  "max_selections": 1,  "none_label": None,       "items": ["Chicken", "Steak", "Barbacoa", "Carnitas", "Sofritas", "Fajita Veggies"]},
            {"id": "rice",     "name": "Rice",     "required": False, "max_selections": 1,  "none_label": "No Rice",  "items": ["White Rice", "Brown Rice"]},
            {"id": "beans",    "name": "Beans",    "required": False, "max_selections": 1,  "none_label": "No Beans", "items": ["Black Beans", "Pinto Beans"]},
            {"id": "salsa",    "name": "Salsa",    "required": False, "max_selections": 3,  "none_label": None,       "items": ["Mild Salsa", "Corn Salsa", "Tomatillo Green-Chili Salsa", "Tomatillo Red-Chili Salsa"]},
            {"id": "toppings", "name": "Extras",   "required": False, "max_selections": 10, "none_label": None,       "items": ["Cheese", "Sour Cream", "Queso Blanco", "Guacamole", "Romaine Lettuce", "Fajita Veggies"]},
        ],
    },

    # ── QDOBA ─────────────────────────────────────────────────────────────────
    "qdoba": {
        "meal_types": [
            {"id": "bowl",       "name": "Bowl",       "icon": "🥣", "description": "Loaded bowl, no tortilla",           "base_items": []},
            {"id": "burrito",    "name": "Burrito",     "icon": "🌯", "description": "Wrapped in a flour tortilla",         "base_items": ["Flour Tortilla"]},
            {"id": "taco",       "name": "Tacos",       "icon": "🌮", "description": "Three tacos with your choice of shell","base_items": []},
            {"id": "salad",      "name": "Salad",        "icon": "🥗", "description": "Crispy tortilla base + greens",       "base_items": []},
            {"id": "quesadilla", "name": "Quesadilla",  "icon": "🧀", "description": "Flour tortilla + cheese + protein",   "base_items": ["Flour Tortilla", "Shredded Cheese"]},
        ],
        "ingredient_groups": [
            {"id": "protein",  "name": "Protein",  "required": True,  "max_selections": 1,  "none_label": None,       "items": ["Grilled Chicken", "Grilled Steak", "Ground Beef", "Pulled Pork", "Impossible Protein"]},
            {"id": "rice",     "name": "Rice",     "required": False, "max_selections": 1,  "none_label": "No Rice",  "items": ["Cilantro Lime Rice", "Brown Rice"]},
            {"id": "beans",    "name": "Beans",    "required": False, "max_selections": 1,  "none_label": "No Beans", "items": ["Black Beans", "Pinto Beans"]},
            {"id": "salsa",    "name": "Salsa",    "required": False, "max_selections": 2,  "none_label": None,       "items": ["Pico de Gallo", "Roasted Tomato Salsa", "Salsa Verde", "Mango Salsa", "Corn Salsa"]},
            {"id": "toppings", "name": "Toppings", "required": False, "max_selections": 10, "none_label": None,       "items": ["Shredded Cheese", "Sour Cream", "Guacamole", "Shredded Lettuce", "Queso Diablo", "Fajita Veggies"]},
        ],
    },

    # ── SUBWAY ────────────────────────────────────────────────────────────────
    "subway": {
        "meal_types": [
            {"id": "six",      "name": "6-inch Sub",  "icon": "🥖", "description": "Personal size sandwich",   "base_items": ["Italian White (6\")"]},
            {"id": "footlong", "name": "Footlong",    "icon": "🥖", "description": "Full size sandwich",       "base_items": ["Italian White (12\")"]},
            {"id": "wrap",     "name": "Wrap",         "icon": "🌯", "description": "Flatbread wrap",           "base_items": ["Flatbread Wrap"]},
            {"id": "salad",    "name": "Salad",         "icon": "🥗", "description": "No bread, all fillings",  "base_items": []},
        ],
        "ingredient_groups": [
            {"id": "bread6",   "name": "Bread (6\")",   "required": False, "max_selections": 1,  "none_label": None,          "items": ["Italian White (6\")", "9-Grain Wheat (6\")", "Honey Oat (6\")", "Rosemary Parmesan (6\")"]},
            {"id": "bread12",  "name": "Bread (12\")",  "required": False, "max_selections": 1,  "none_label": None,          "items": ["Italian White (12\")", "9-Grain Wheat (12\")"]},
            {"id": "protein",  "name": "Protein",        "required": True,  "max_selections": 1,  "none_label": None,          "items": ["Sliced Turkey", "Sliced Ham", "Tuna", "Roast Beef", "Rotisserie Chicken", "Steak Strips", "Spicy Italian Meats", "BLT Bacon"]},
            {"id": "cheese",   "name": "Cheese",          "required": False, "max_selections": 1,  "none_label": "No Cheese",   "items": ["American", "Swiss", "Provolone", "Pepper Jack"]},
            {"id": "veggies",  "name": "Vegetables",      "required": False, "max_selections": 12, "none_label": None,          "items": ["Lettuce", "Tomatoes", "Onions", "Bell Peppers", "Cucumbers", "Black Olives", "Pickles", "Spinach", "Banana Peppers", "Jalapeños", "Avocado"]},
            {"id": "sauce",    "name": "Sauce",            "required": False, "max_selections": 2,  "none_label": None,          "items": ["Mayonnaise", "Yellow Mustard", "Ranch Dressing", "Honey Mustard", "Sweet Onion Sauce", "Chipotle Southwest", "Oil & Vinegar"]},
        ],
    },

    # ── JIMMY JOHN'S ──────────────────────────────────────────────────────────
    "jimmy-johns": {
        "meal_types": [
            {"id": "sub",    "name": "8\" Sub",   "icon": "🥖", "description": "Classic French bread sub",      "base_items": ["French Bread (8\")"]},
            {"id": "slim",   "name": "Slim",       "icon": "🥖", "description": "Lighter bread, same fillings",  "base_items": ["Slim (8\")"]},
            {"id": "unwich", "name": "Unwich",     "icon": "🥗", "description": "Lettuce wrap — no bread",       "base_items": ["Unwich Lettuce Wrap"]},
        ],
        "ingredient_groups": [
            {"id": "bread",   "name": "Change Bread", "required": False, "max_selections": 1,  "none_label": None,         "items": ["French Bread (8\")", "Wheat Bread (8\")"]},
            {"id": "protein", "name": "Protein",       "required": True,  "max_selections": 2,  "none_label": None,         "items": ["Sliced Turkey", "Sliced Ham", "Tuna Salad", "Roast Beef", "Capicola", "Salami", "Provolone Cheese"]},
            {"id": "veggies", "name": "Vegetables",    "required": False, "max_selections": 10, "none_label": None,         "items": ["Lettuce", "Tomato", "Onion", "Cucumber", "Avocado Spread"]},
            {"id": "sauce",   "name": "Sauce",         "required": False, "max_selections": 2,  "none_label": None,         "items": ["Mayonnaise", "Mustard", "JJ Dressing (Oil & Vinegar)"]},
        ],
    },

    # ── JERSEY MIKE'S ─────────────────────────────────────────────────────────
    "jersey-mikes": {
        "meal_types": [
            {"id": "regular", "name": "Regular Sub", "icon": "🥖", "description": "7–8 inch sub",        "base_items": ["White Bread (Regular)"]},
            {"id": "large",   "name": "Giant Sub",   "icon": "🥖", "description": "14–15 inch sub",       "base_items": ["White Bread (Large)"]},
            {"id": "wrap",    "name": "Lettuce Wrap","icon": "🥗", "description": "No bread option",      "base_items": ["Lettuce Wrap"]},
        ],
        "ingredient_groups": [
            {"id": "bread",   "name": "Change Bread", "required": False, "max_selections": 1,  "none_label": None,         "items": ["White Bread (Regular)", "Wheat Bread (Regular)", "Rosemary Parmesan (Regular)"]},
            {"id": "protein", "name": "Protein",       "required": True,  "max_selections": 3,  "none_label": None,         "items": ["Turkey Breast", "Roast Beef", "Ham", "Tuna", "Capicola", "Prosciuttini", "Genoa Salami", "Pepperoni", "Chicken"]},
            {"id": "cheese",  "name": "Cheese",         "required": False, "max_selections": 1,  "none_label": "No Cheese", "items": ["Provolone", "Swiss", "American", "Pepper Jack"]},
            {"id": "veggies", "name": "Vegetables",     "required": False, "max_selections": 10, "none_label": None,        "items": ["Lettuce", "Tomato", "Onion", "Peppers", "Vinegar Peppers"]},
            {"id": "sauce",   "name": "Condiments",     "required": False, "max_selections": 3,  "none_label": None,        "items": ["Olive Oil Blend", "Red Wine Vinegar", "Mayonnaise", "Mustard"]},
        ],
    },

    # ── FIREHOUSE SUBS ────────────────────────────────────────────────────────
    "firehouse-subs": {
        "meal_types": [
            {"id": "medium", "name": "Medium Sub",  "icon": "🥖", "description": "Classic medium Firehouse sub",  "base_items": ["White Roll (Medium)"]},
            {"id": "large",  "name": "Large Sub",   "icon": "🥖", "description": "Full size large sub",            "base_items": ["White Roll (Large)"]},
        ],
        "ingredient_groups": [
            {"id": "bread",   "name": "Change Bread", "required": False, "max_selections": 1,  "none_label": None,        "items": ["White Roll (Medium)", "Wheat Roll (Medium)", "Gluten Free Roll"]},
            {"id": "protein", "name": "Protein",       "required": True,  "max_selections": 2,  "none_label": None,        "items": ["Turkey Breast", "Smoked Turkey", "Ham", "Roast Beef", "Salami", "Pepperoni", "Chicken", "Meatballs", "Pastrami"]},
            {"id": "cheese",  "name": "Cheese",         "required": False, "max_selections": 1,  "none_label": "No Cheese","items": ["Provolone", "Swiss", "American", "Cheddar", "Pepper Jack"]},
            {"id": "veggies", "name": "Vegetables",     "required": False, "max_selections": 10, "none_label": None,       "items": ["Lettuce", "Tomato", "Onion", "Banana Peppers", "Jalapeños", "Pickles"]},
            {"id": "sauce",   "name": "Sauce",          "required": False, "max_selections": 2,  "none_label": None,       "items": ["Mayonnaise", "Mustard", "Ranch", "Firehouse Signature Mustard"]},
        ],
    },
}
