"""
Ingredient-level seed data for build-your-own chains.
These items represent individual components (proteins, bread, toppings, etc.)
used by the ingredient builder UI.
Run:  python main.py --seed-builder
"""
from base_scraper import MenuItemData

def _i(name, cat, sz, cal, fat, sat, trans, chol, sod, carb, fiber, sug, prot):
    return MenuItemData(
        name=name, category=cat, serving_size=sz,
        calories=cal, total_fat_g=fat, saturated_fat_g=sat, trans_fat_g=trans,
        cholesterol_mg=chol, sodium_mg=sod, total_carbs_g=carb,
        dietary_fiber_g=fiber, total_sugars_g=sug, protein_g=prot,
    )

BUILDER_INGREDIENTS: dict[str, dict] = {

    # ── QDOBA ─────────────────────────────────────────────────────────────────
    "qdoba": {
        "chain": dict(name="Qdoba", slug="qdoba",
                      website="https://www.qdoba.com", cuisine_type="Mexican"),
        "items": [
            # Base
            _i("Flour Tortilla",         "Base",      "~4.5 oz",  320,  9, 3.5, 0.0,   0,  680, 50, 3,  2,  8),
            # Proteins
            _i("Grilled Chicken",        "Protein",   "~4 oz",    180,  7, 2.0, 0.0, 110,  400,  0, 0,  0, 32),
            _i("Grilled Steak",          "Protein",   "~4 oz",    150,  6, 2.0, 0.5,  65,  310,  1, 0,  0, 21),
            _i("Ground Beef",            "Protein",   "~4 oz",    200, 11, 4.0, 0.5,  60,  350,  3, 0,  0, 20),
            _i("Pulled Pork",            "Protein",   "~4 oz",    160,  7, 2.5, 0.0,  65,  430,  3, 0,  2, 19),
            _i("Impossible Protein",     "Protein",   "~4 oz",    150,  7, 2.0, 0.0,   0,  370,  8, 1,  1, 14),
            # Rice
            _i("Cilantro Lime Rice",     "Rice",      "~4 oz",    220,  3, 0.5, 0.0,   0,  480, 44, 2,  0,  5),
            _i("Brown Rice",             "Rice",      "~4 oz",    200,  4, 1.0, 0.0,   0,  220, 40, 3,  0,  5),
            # Beans
            _i("Black Beans",            "Beans",     "~4 oz",    130,  1, 0.0, 0.0,   0,  430, 22, 8,  1,  8),
            _i("Pinto Beans",            "Beans",     "~4 oz",    120,  1, 0.0, 0.0,   0,  380, 22, 8,  0,  7),
            # Salsa
            _i("Pico de Gallo",          "Salsa",     "~3 oz",     15,  0, 0.0, 0.0,   0,  200,  3, 1,  2,  1),
            _i("Roasted Tomato Salsa",   "Salsa",     "~3 oz",     25,  0, 0.0, 0.0,   0,  320,  5, 1,  3,  1),
            _i("Salsa Verde",            "Salsa",     "~3 oz",     25,  0, 0.0, 0.0,   0,  280,  4, 1,  2,  0),
            _i("Mango Salsa",            "Salsa",     "~3 oz",     45,  0, 0.0, 0.0,   0,  150, 10, 1,  8,  1),
            _i("Corn Salsa",             "Salsa",     "~3 oz",     70,  1, 0.0, 0.0,   0,  180, 14, 2,  3,  2),
            # Toppings
            _i("Shredded Cheese",        "Toppings",  "~1 oz",    110,  9, 5.0, 0.0,  30,  180,  0, 0,  0,  6),
            _i("Sour Cream",             "Toppings",  "~1.5 oz",   60,  5, 3.5, 0.0,  20,   15,  1, 0,  1,  1),
            _i("Guacamole",              "Toppings",  "~2 oz",    100,  9, 1.5, 0.0,   0,  200,  5, 3,  0,  1),
            _i("Shredded Lettuce",       "Toppings",  "~1 oz",      5,  0, 0.0, 0.0,   0,    5,  1, 0,  0,  0),
            _i("Queso Diablo",           "Toppings",  "~2 oz",     80,  5, 2.5, 0.0,  15,  470,  5, 0,  1,  3),
            _i("Fajita Veggies",         "Toppings",  "~2 oz",     20,  1, 0.0, 0.0,   0,  175,  4, 1,  2,  1),
        ],
    },

    # ── SUBWAY ────────────────────────────────────────────────────────────────
    "subway": {
        "chain": dict(name="Subway", slug="subway",
                      website="https://www.subway.com", cuisine_type="Sandwiches"),
        "items": [
            # Bread
            _i("Italian White (6\")",    "Bread",     "~2.5 oz",  180,  2, 0.5, 0.0,   0,  380, 35, 1,  4,  7),
            _i("9-Grain Wheat (6\")",    "Bread",     "~2.5 oz",  180,  2, 0.0, 0.0,   0,  370, 34, 3,  4,  7),
            _i("Honey Oat (6\")",        "Bread",     "~2.8 oz",  200,  3, 0.0, 0.0,   0,  390, 38, 3,  6,  7),
            _i("Rosemary Parmesan (6\")","Bread",     "~2.8 oz",  210,  4, 1.0, 0.0,   0,  430, 35, 2,  2,  8),
            _i("Italian White (12\")",   "Bread",     "~5 oz",    360,  4, 1.0, 0.0,   0,  760, 70, 2,  8, 14),
            _i("9-Grain Wheat (12\")",   "Bread",     "~5 oz",    360,  4, 0.0, 0.0,   0,  740, 68, 6,  8, 14),
            _i("Flatbread Wrap",         "Bread",     "~3 oz",    220,  5, 2.0, 0.0,   0,  360, 36, 2,  1,  8),
            # Proteins
            _i("Sliced Turkey",          "Protein",   "~2 oz",     60,  1, 0.5, 0.0,  25,  390,  1, 0,  0, 11),
            _i("Sliced Ham",             "Protein",   "~2 oz",     60,  2, 0.5, 0.0,  25,  430,  2, 0,  1,  9),
            _i("Tuna",                   "Protein",   "~4 scoops",190, 13, 2.5, 0.0,  30,  290,  3, 0,  1, 14),
            _i("Roast Beef",             "Protein",   "~2 oz",     80,  2, 1.0, 0.0,  30,  370,  1, 0,  0, 13),
            _i("Rotisserie Chicken",     "Protein",   "~2.5 oz",  100,  3, 1.0, 0.0,  55,  310,  0, 0,  0, 18),
            _i("Steak Strips",           "Protein",   "~2 oz",     80,  3, 1.5, 0.0,  30,  370,  2, 0,  1, 11),
            _i("Spicy Italian Meats",    "Protein",   "~2 oz",    160, 14, 5.0, 0.5,  50,  790,  0, 0,  0,  9),
            _i("BLT Bacon",              "Protein",   "~0.5 oz",   45,  4, 1.0, 0.0,  15,  190,  0, 0,  0,  4),
            # Cheese
            _i("American",               "Cheese",    "1 slice",   40,  4, 2.0, 0.0,  10,  200,  0, 0,  0,  2),
            _i("Swiss",                  "Cheese",    "1 slice",   50,  4, 2.5, 0.0,  15,   30,  0, 0,  0,  4),
            _i("Provolone",              "Cheese",    "1 slice",   50,  4, 2.0, 0.0,  10,  115,  0, 0,  0,  4),
            _i("Pepper Jack",            "Cheese",    "1 slice",   50,  5, 2.5, 0.0,  15,  110,  0, 0,  0,  3),
            # Veggies (per standard serving on 6")
            _i("Lettuce",                "Veggies",   "~0.5 oz",    5,  0, 0.0, 0.0,   0,    5,  1, 0,  0,  0),
            _i("Tomatoes",               "Veggies",   "~1 oz",      5,  0, 0.0, 0.0,   0,    0,  1, 0,  1,  0),
            _i("Onions",                 "Veggies",   "~0.5 oz",   10,  0, 0.0, 0.0,   0,    0,  2, 0,  1,  0),
            _i("Bell Peppers",           "Veggies",   "~0.5 oz",    5,  0, 0.0, 0.0,   0,    0,  1, 0,  1,  0),
            _i("Cucumbers",              "Veggies",   "~0.5 oz",    5,  0, 0.0, 0.0,   0,    0,  1, 0,  0,  0),
            _i("Black Olives",           "Veggies",   "~0.5 oz",   25,  2, 0.0, 0.0,   0,  125,  1, 0,  0,  0),
            _i("Pickles",                "Veggies",   "~0.5 oz",    5,  0, 0.0, 0.0,   0,  220,  1, 0,  0,  0),
            _i("Spinach",                "Veggies",   "~0.5 oz",    5,  0, 0.0, 0.0,   0,   15,  1, 0,  0,  0),
            _i("Banana Peppers",         "Veggies",   "~0.5 oz",    5,  0, 0.0, 0.0,   0,  130,  1, 0,  0,  0),
            _i("Jalapeños",              "Veggies",   "~0.5 oz",    5,  0, 0.0, 0.0,   0,  130,  1, 0,  0,  0),
            _i("Avocado",                "Veggies",   "~1 oz",     45,  4, 0.5, 0.0,   0,    0,  2, 1,  0,  1),
            # Sauces (per ~1.5 tbsp serving)
            _i("Mayonnaise",             "Sauce",     "1.5 tbsp", 110, 12, 2.0, 0.0,  10,   95,  0, 0,  0,  0),
            _i("Yellow Mustard",         "Sauce",     "1.5 tbsp",  10,  0, 0.0, 0.0,   0,  120,  1, 0,  0,  0),
            _i("Ranch Dressing",         "Sauce",     "1.5 tbsp", 110, 12, 2.0, 0.0,  10,  230,  1, 0,  1,  0),
            _i("Honey Mustard",          "Sauce",     "1.5 tbsp",  30,  0, 0.0, 0.0,   0,   75,  7, 0,  6,  0),
            _i("Sweet Onion Sauce",      "Sauce",     "1.5 tbsp",  40,  0, 0.0, 0.0,   0,   85,  9, 0,  8,  0),
            _i("Chipotle Southwest",     "Sauce",     "1.5 tbsp", 100, 10, 1.5, 0.0,  10,  220,  3, 0,  1,  0),
            _i("Oil & Vinegar",          "Sauce",     "1.5 tbsp",  35,  4, 0.5, 0.0,   0,    0,  0, 0,  0,  0),
        ],
    },

    # ── JIMMY JOHN'S ──────────────────────────────────────────────────────────
    "jimmy-johns": {
        "chain": dict(name="Jimmy John's", slug="jimmy-johns",
                      website="https://www.jimmyjohns.com", cuisine_type="Sandwiches"),
        "items": [
            # Bread
            _i("French Bread (8\")",     "Bread",     "~3.5 oz",  300,  2, 0.5, 0.0,   0,  590, 58, 2,  2, 11),
            _i("Slim (8\")",             "Bread",     "~2.8 oz",  240,  1, 0.5, 0.0,   0,  470, 46, 2,  2,  9),
            _i("Wheat Bread (8\")",      "Bread",     "~3.5 oz",  290,  3, 0.5, 0.0,   0,  580, 55, 4,  3, 12),
            _i("Unwich Lettuce Wrap",    "Bread",     "~2 oz",     10,  0, 0.0, 0.0,   0,   20,  2, 1,  1,  1),
            # Proteins
            _i("Sliced Turkey",          "Protein",   "~3 oz",     80,  1, 0.5, 0.0,  35,  570,  2, 0,  0, 15),
            _i("Sliced Ham",             "Protein",   "~3 oz",     75,  2, 0.5, 0.0,  35,  600,  2, 0,  1, 12),
            _i("Tuna Salad",             "Protein",   "~4 oz",    240, 18, 3.0, 0.0,  30,  340,  3, 0,  1, 18),
            _i("Roast Beef",             "Protein",   "~3 oz",    100,  3, 1.0, 0.0,  40,  490,  1, 0,  0, 18),
            _i("Capicola",               "Protein",   "~1.5 oz",   70,  4, 1.5, 0.0,  30,  580,  1, 0,  0,  7),
            _i("Salami",                 "Protein",   "~1.5 oz",  120, 10, 4.0, 0.0,  35,  530,  1, 0,  0,  6),
            _i("Provolone Cheese",       "Protein",   "~1 oz",     80,  6, 4.0, 0.0,  20,  195,  0, 0,  0,  6),
            # Veggies (included standard)
            _i("Lettuce",                "Veggies",   "~0.5 oz",    5,  0, 0.0, 0.0,   0,    5,  1, 0,  0,  0),
            _i("Tomato",                 "Veggies",   "~1 oz",      5,  0, 0.0, 0.0,   0,    0,  1, 0,  1,  0),
            _i("Onion",                  "Veggies",   "~0.5 oz",   10,  0, 0.0, 0.0,   0,    0,  2, 0,  1,  0),
            _i("Cucumber",               "Veggies",   "~0.5 oz",    5,  0, 0.0, 0.0,   0,    0,  1, 0,  0,  0),
            _i("Avocado Spread",         "Veggies",   "~1.5 oz",   60,  5, 1.0, 0.0,   0,   80,  3, 2,  0,  1),
            # Sauces
            _i("Mayonnaise",             "Sauce",     "1 tbsp",    90, 10, 1.5, 0.0,  10,   75,  0, 0,  0,  0),
            _i("Mustard",                "Sauce",     "1 tbsp",    10,  0, 0.0, 0.0,   0,  120,  1, 0,  0,  0),
            _i("JJ Dressing (Oil & Vinegar)","Sauce", "1.5 tbsp",  35,  4, 0.5, 0.0,   0,    0,  0, 0,  0,  0),
        ],
    },

    # ── JERSEY MIKE'S ─────────────────────────────────────────────────────────
    "jersey-mikes": {
        "chain": dict(name="Jersey Mike's", slug="jersey-mikes",
                      website="https://www.jerseymikes.com", cuisine_type="Sandwiches"),
        "items": [
            # Bread
            _i("White Bread (Regular)", "Bread",     "~4 oz",    320,  3, 0.5, 0.0,   0,  660, 61, 2,  5, 12),
            _i("Wheat Bread (Regular)", "Bread",     "~4 oz",    310,  3, 0.5, 0.0,   0,  650, 59, 4,  4, 13),
            _i("White Bread (Large)",   "Bread",     "~6 oz",    480,  5, 1.0, 0.0,   0,  990, 91, 3,  7, 18),
            _i("Rosemary Parmesan (Regular)","Bread","~4.5 oz",  350,  6, 2.0, 0.0,   5,  710, 60, 2,  4, 14),
            _i("Lettuce Wrap",          "Bread",     "~1 oz",     10,  0, 0.0, 0.0,   0,   15,  2, 1,  1,  1),
            # Proteins
            _i("Turkey Breast",         "Protein",   "~3 oz",     70,  1, 0.0, 0.0,  30,  540,  2, 0,  0, 14),
            _i("Roast Beef",            "Protein",   "~3 oz",    120,  5, 2.0, 0.0,  45,  540,  1, 0,  0, 18),
            _i("Ham",                   "Protein",   "~3 oz",     80,  2, 0.5, 0.0,  40,  760,  3, 0,  2, 12),
            _i("Tuna",                  "Protein",   "~4 oz",    230, 17, 2.5, 0.0,  30,  360,  3, 0,  1, 16),
            _i("Capicola",              "Protein",   "~2 oz",    100,  6, 2.0, 0.0,  40,  760,  1, 0,  0,  9),
            _i("Prosciuttini",          "Protein",   "~2 oz",    100,  6, 2.0, 0.0,  40,  760,  1, 0,  0,  9),
            _i("Genoa Salami",          "Protein",   "~2 oz",    150, 12, 4.5, 0.0,  40,  650,  1, 0,  0,  8),
            _i("Pepperoni",             "Protein",   "~2 oz",    140, 12, 4.0, 0.0,  45,  640,  1, 0,  0,  7),
            _i("Chicken",               "Protein",   "~3 oz",    110,  3, 1.0, 0.0,  60,  460,  1, 0,  0, 20),
            # Cheese
            _i("Provolone",             "Cheese",    "1 slice",   80,  6, 4.0, 0.0,  20,  195,  0, 0,  0,  6),
            _i("Swiss",                 "Cheese",    "1 slice",   60,  5, 3.0, 0.0,  15,   30,  0, 0,  0,  4),
            _i("American",              "Cheese",    "1 slice",   50,  4, 2.5, 0.0,  15,  250,  1, 0,  0,  3),
            _i("Pepper Jack",           "Cheese",    "1 slice",   60,  5, 3.0, 0.0,  15,  140,  0, 0,  0,  4),
            # Veggies
            _i("Lettuce",               "Veggies",   "~0.5 oz",    5,  0, 0.0, 0.0,   0,    5,  1, 0,  0,  0),
            _i("Tomato",                "Veggies",   "~1 oz",      5,  0, 0.0, 0.0,   0,    0,  1, 0,  1,  0),
            _i("Onion",                 "Veggies",   "~0.5 oz",   10,  0, 0.0, 0.0,   0,    0,  2, 0,  1,  0),
            _i("Peppers",               "Veggies",   "~0.5 oz",    5,  0, 0.0, 0.0,   0,    0,  1, 0,  1,  0),
            _i("Vinegar Peppers",       "Veggies",   "~0.5 oz",    5,  0, 0.0, 0.0,   0,  130,  1, 0,  0,  0),
            # Condiments
            _i("Olive Oil Blend",       "Sauce",     "1 tbsp",   120, 14, 2.0, 0.0,   0,    0,  0, 0,  0,  0),
            _i("Red Wine Vinegar",      "Sauce",     "1 tbsp",     0,  0, 0.0, 0.0,   0,    0,  0, 0,  0,  0),
            _i("Mayonnaise",            "Sauce",     "1 tbsp",    90, 10, 1.5, 0.0,  10,   75,  0, 0,  0,  0),
            _i("Mustard",               "Sauce",     "1 tbsp",    10,  0, 0.0, 0.0,   0,  120,  1, 0,  0,  0),
        ],
    },

    # ── FIREHOUSE SUBS ────────────────────────────────────────────────────────
    "firehouse-subs": {
        "chain": dict(name="Firehouse Subs", slug="firehouse-subs",
                      website="https://www.firehousesubs.com", cuisine_type="Sandwiches"),
        "items": [
            # Bread
            _i("White Roll (Medium)",   "Bread",     "~4 oz",    310,  2, 0.5, 0.0,   0,  640, 60, 2,  5, 12),
            _i("Wheat Roll (Medium)",   "Bread",     "~4 oz",    300,  3, 0.5, 0.0,   0,  630, 57, 4,  4, 13),
            _i("White Roll (Large)",    "Bread",     "~6 oz",    460,  3, 1.0, 0.0,   0,  960, 90, 3,  7, 18),
            _i("Gluten Free Roll",      "Bread",     "~3 oz",    220,  4, 0.5, 0.0,   0,  430, 41, 2,  3,  4),
            # Proteins
            _i("Turkey Breast",         "Protein",   "~3 oz",     70,  1, 0.0, 0.0,  30,  560,  2, 0,  0, 14),
            _i("Smoked Turkey",         "Protein",   "~3 oz",     80,  2, 0.5, 0.0,  35,  620,  2, 0,  1, 13),
            _i("Ham",                   "Protein",   "~3 oz",     80,  2, 0.5, 0.0,  40,  680,  3, 0,  2, 12),
            _i("Roast Beef",            "Protein",   "~3 oz",    120,  5, 2.0, 0.0,  45,  490,  1, 0,  0, 18),
            _i("Salami",                "Protein",   "~2 oz",    130, 11, 4.0, 0.0,  40,  570,  1, 0,  0,  6),
            _i("Pepperoni",             "Protein",   "~1.5 oz",  120, 10, 4.0, 0.0,  35,  520,  1, 0,  0,  6),
            _i("Chicken",               "Protein",   "~3 oz",    110,  3, 0.5, 0.0,  60,  480,  2, 0,  1, 19),
            _i("Meatballs",             "Protein",   "~4 oz",    250, 14, 6.0, 0.5,  75,  830, 15, 1,  5, 17),
            _i("Pastrami",              "Protein",   "~3 oz",    130,  6, 2.5, 0.0,  55,  780,  2, 0,  0, 16),
            # Cheese
            _i("Provolone",             "Cheese",    "1 slice",   80,  6, 4.0, 0.0,  20,  195,  0, 0,  0,  6),
            _i("Swiss",                 "Cheese",    "1 slice",   60,  5, 3.0, 0.0,  15,   30,  0, 0,  0,  4),
            _i("American",              "Cheese",    "1 slice",   50,  4, 2.5, 0.0,  15,  250,  1, 0,  0,  3),
            _i("Cheddar",               "Cheese",    "1 slice",   60,  5, 3.0, 0.0,  15,  100,  0, 0,  0,  4),
            _i("Pepper Jack",           "Cheese",    "1 slice",   60,  5, 3.0, 0.0,  15,  140,  0, 0,  0,  4),
            # Veggies
            _i("Lettuce",               "Veggies",   "~0.5 oz",    5,  0, 0.0, 0.0,   0,    5,  1, 0,  0,  0),
            _i("Tomato",                "Veggies",   "~1 oz",      5,  0, 0.0, 0.0,   0,    0,  1, 0,  1,  0),
            _i("Onion",                 "Veggies",   "~0.5 oz",   10,  0, 0.0, 0.0,   0,    0,  2, 0,  1,  0),
            _i("Banana Peppers",        "Veggies",   "~0.5 oz",    5,  0, 0.0, 0.0,   0,  130,  1, 0,  0,  0),
            _i("Jalapeños",             "Veggies",   "~0.5 oz",    5,  0, 0.0, 0.0,   0,  130,  1, 0,  0,  0),
            _i("Pickles",               "Veggies",   "~0.5 oz",    5,  0, 0.0, 0.0,   0,  220,  1, 0,  0,  0),
            # Sauces
            _i("Mayonnaise",            "Sauce",     "1 tbsp",    90, 10, 1.5, 0.0,  10,   75,  0, 0,  0,  0),
            _i("Mustard",               "Sauce",     "1 tbsp",    10,  0, 0.0, 0.0,   0,  120,  1, 0,  0,  0),
            _i("Ranch",                 "Sauce",     "1.5 tbsp", 110, 12, 2.0, 0.0,  10,  230,  1, 0,  1,  0),
            _i("Firehouse Signature Mustard","Sauce","1 tbsp",    25,  1, 0.0, 0.0,   0,  140,  3, 0,  2,  0),
        ],
    },
}
