"""
Seed data with published nutrition facts for all 50 chains.
Values sourced from official restaurant nutrition pages.
Run:  python main.py --seed
      python main.py --seed --chains mcdonalds chipotle
"""
from base_scraper import MenuItemData

# ─────────────────────────────────────────────────────────────────────────────
# Each entry: (name, category, serving_size, cal, fat, sat, trans, chol, sod,
#              carb, fiber, sugar, protein)
# ─────────────────────────────────────────────────────────────────────────────

def _item(name, cat, sz, cal, fat, sat, trans, chol, sod, carb, fiber, sug, prot):
    return MenuItemData(
        name=name, category=cat, serving_size=sz,
        calories=cal, total_fat_g=fat, saturated_fat_g=sat, trans_fat_g=trans,
        cholesterol_mg=chol, sodium_mg=sod, total_carbs_g=carb,
        dietary_fiber_g=fiber, total_sugars_g=sug, protein_g=prot,
    )


SEED: dict[str, dict] = {

    # ──────────────────────────── McDONALD'S ─────────────────────────────────
    "mcdonalds": {
        "chain": dict(name="McDonald's", slug="mcdonalds",
                      website="https://www.mcdonalds.com", cuisine_type="Fast Food"),
        "items": [
            _item("Big Mac",                  "Burgers",   "7.6 oz",  550, 30, 10, 1.0,  80, 1010, 45, 3,  9, 25),
            _item("McDouble",                 "Burgers",   "5.4 oz",  400, 20,  8, 1.0,  65,  920, 35, 2,  7, 22),
            _item("Quarter Pounder w/Cheese", "Burgers",   "7.3 oz",  520, 26, 13, 1.5,  95, 1090, 43, 2, 10, 30),
            _item("McChicken",                "Chicken",   "5.2 oz",  400, 17,  3, 0.0,  40,  660, 42, 2,  5, 15),
            _item("Crispy Chicken Sandwich",  "Chicken",   "7.4 oz",  470, 20,  3, 0.0,  60,  870, 46, 3,  5, 26),
            _item("10 pc Chicken McNuggets",  "Chicken",   "6.2 oz",  420, 25,  4, 0.0,  75,  890, 26, 1,  0, 22),
            _item("Filet-O-Fish",             "Fish",      "5.0 oz",  380, 18,  3, 0.0,  40,  580, 38, 1,  5, 15),
            _item("Medium French Fries",      "Sides",     "3.6 oz",  320, 15,  2, 0.0,   0,  400, 44, 4,  0,  4),
            _item("Small French Fries",       "Sides",     "2.5 oz",  230, 11,  1, 0.0,   0,  290, 31, 3,  0,  3),
            _item("Side Salad",               "Salads",    "3.1 oz",   15,  0,  0, 0.0,   0,   10,  3, 1,  1,  1),
            _item("Egg McMuffin",             "Breakfast", "4.8 oz",  310, 13,  5, 0.0, 255,  760, 30, 2,  3, 17),
            _item("Sausage McMuffin w/Egg",   "Breakfast", "6.2 oz",  480, 28, 10, 0.0, 285,  960, 31, 2,  3, 21),
            _item("Hotcakes",                 "Breakfast", "5.8 oz",  600, 17, 11, 0.0,  60,  670,102, 2, 45, 10),
            _item("Hash Browns",              "Breakfast", "2.0 oz",  150,  9,  1, 0.0,   0,  290, 17, 2,  0,  1),
            _item("McFlurry with Oreo",       "Desserts",  "12 fl oz",510, 13,  8, 0.0,  50,  280, 82, 0, 65, 12),
            _item("Vanilla Soft Serve Cone",  "Desserts",  "3.3 oz",  200,  5,  3, 0.0,  20,   90, 32, 0, 25,  5),
            # Drinks
            _item("Medium Soft Drink",        "Drinks",    "22 fl oz",210,  0,  0, 0.0,   0,   35, 58, 0, 58,  0),
            _item("Large Soft Drink",         "Drinks",    "30 fl oz",290,  0,  0, 0.0,   0,   50, 79, 0, 79,  0),
            _item("Large Dr Pepper",          "Drinks",    "30 fl oz",310,  0,  0, 0.0,   0,   75, 86, 0, 86,  0),
            _item("Medium Diet Coke",         "Drinks",    "22 fl oz",  0,  0,  0, 0.0,   0,   55,  0, 0,  0,  0),
            _item("Medium Orange Juice",      "Drinks",    "12 fl oz",150,  0,  0, 0.0,   0,    5, 36, 0, 34,  2),
            _item("Medium McCafé Coffee",     "Drinks",    "16 fl oz",  0,  0,  0, 0.0,   0,    5,  1, 0,  0,  0),
            _item("Large Sweet Tea",          "Drinks",    "30 fl oz",160,  0,  0, 0.0,   0,   15, 43, 0, 43,  0),
        ],
    },

    # ──────────────────────────── CHIPOTLE ───────────────────────────────────
    "chipotle": {
        "chain": dict(name="Chipotle", slug="chipotle",
                      website="https://www.chipotle.com", cuisine_type="Mexican"),
        "items": [
            _item("Chicken Burrito Bowl",     "Bowls",     "~15 oz",  665, 24,  7, 0.0,  90, 1500, 70, 11, 4, 53),
            _item("Steak Burrito Bowl",       "Bowls",     "~15 oz",  645, 24,  8, 0.5,  80, 1510, 68, 11, 4, 46),
            _item("Sofritas Burrito Bowl",    "Bowls",     "~15 oz",  580, 21,  5, 0.0,   0, 1340, 71, 12, 4, 22),
            _item("Chicken Burrito",          "Burritos",  "~16 oz",  960, 34,  9, 0.5, 125, 2150,106, 13, 5, 56),
            _item("Chicken Tacos (3)",        "Tacos",     "~12 oz",  455, 17,  5, 0.5,  90, 1085, 42,  7, 3, 35),
            _item("Chicken Salad",            "Salads",    "~14 oz",  445, 23,  6, 0.0,  90, 1015, 28,  9, 4, 38),
            _item("White Rice",               "Ingredients","~4 oz",  210,  3,  1, 0.0,   0,  350, 40,  1, 0,  4),
            _item("Brown Rice",               "Ingredients","~4 oz",  210,  4,  1, 0.0,   0,  210, 41,  2, 0,  5),
            _item("Black Beans",              "Ingredients","~4 oz",  130,  1,  0, 0.0,   0,  250, 22,  8, 0,  8),
            _item("Pinto Beans",              "Ingredients","~4 oz",  120,  1,  0, 0.0,   0,  310, 22,  8, 0,  7),
            _item("Cheese",                   "Ingredients","~1 oz",  110,  9,  5, 0.0,  30,  180,  0,  0, 0,  6),
            _item("Sour Cream",               "Ingredients","~2 oz",  120, 10,  7, 0.0,  30,   30,  2,  0, 1,  2),
            _item("Guacamole",                "Ingredients","~4 oz",  230, 22,  3, 0.0,   0,  375,  8,  6, 0,  2),
            _item("Mild Salsa",               "Ingredients","~3.5 oz", 25,  0,  0, 0.0,   0,  490,  5,  1, 3,  1),
            _item("Chips",                    "Sides",     "~4 oz",   540, 24,  4, 0.0,   0,  490, 73,  5, 1,  8),
        ],
    },

    # ──────────────────────────── STARBUCKS ──────────────────────────────────
    "starbucks": {
        "chain": dict(name="Starbucks", slug="starbucks",
                      website="https://www.starbucks.com", cuisine_type="Coffee / Café"),
        "items": [
            _item("Caffe Latte (Grande)",         "Hot Coffees",   "16 fl oz", 190,  7,  4, 0.0, 25, 170, 19, 0, 18, 13),
            _item("Caffe Americano (Grande)",     "Hot Coffees",   "16 fl oz",  15,  0,  0, 0.0,  0,  15,  3, 0,  0,  1),
            _item("Cappuccino (Grande)",           "Hot Coffees",   "16 fl oz", 120,  4,  3, 0.0, 15, 115, 12, 0, 11,  8),
            _item("Pumpkin Spice Latte (Grande)", "Hot Coffees",   "16 fl oz", 380, 13,  8, 0.0, 50, 240, 52, 0, 50, 14),
            _item("Mocha Frappuccino (Grande)",   "Frappuccinos",  "16 fl oz", 370,  9,  6, 0.0, 35, 240, 62, 1, 57,  5),
            _item("Caramel Frappuccino (Grande)", "Frappuccinos",  "16 fl oz", 380,  5,  4, 0.0, 20, 280, 76, 0, 65,  5),
            _item("Vanilla Latte (Grande)",       "Hot Coffees",   "16 fl oz", 250,  6,  4, 0.0, 25, 170, 37, 0, 35, 13),
            _item("Cold Brew Coffee (Venti)",     "Cold Coffees",  "24 fl oz",  20,  0,  0, 0.0,  0,  25,  5, 0,  5,  1),
            _item("Iced Caffe Latte (Grande)",    "Cold Coffees",  "16 fl oz", 130,  5,  3, 0.0, 20, 115, 13, 0, 11,  8),
            _item("Chocolate Croissant",           "Bakery",        "3.3 oz",  340, 18,  9, 0.0, 35, 330, 37, 2, 12,  7),
            _item("Blueberry Muffin",             "Bakery",        "4.2 oz",  380, 13,  2, 0.0, 55, 360, 61, 2, 37,  6),
            _item("Cheese & Fruit Protein Box",   "Snacks & Sandwiches","~6 oz",480, 25, 10, 0.0, 60, 630, 45, 5, 23, 25),
            _item("Chicken & Bacon Sandwich",     "Snacks & Sandwiches","~7 oz",440, 16,  5, 0.0, 70, 850, 46, 2,  5, 29),
            _item("Turkey Pesto Sandwich",        "Snacks & Sandwiches","~6 oz",400, 14,  3, 0.0, 50, 850, 44, 4,  5, 24),
            _item("Impossible Breakfast Sandwich","Snacks & Sandwiches","~7 oz",430, 18,  6, 0.0,  0, 780, 47, 3,  4, 24),
        ],
    },

    # ──────────────────────────── SUBWAY ─────────────────────────────────────
    "subway": {
        "chain": dict(name="Subway", slug="subway",
                      website="https://www.subway.com", cuisine_type="Sandwiches"),
        "items": [
            _item("Italian BMT (6\")",        "Footlongs & Subs", "~7 oz",  410, 18,  6, 0.0, 55, 1310, 40, 3,  6, 22),
            _item("Tuna (6\")",               "Footlongs & Subs", "~7 oz",  480, 28,  5, 0.0, 45,  660, 39, 3,  5, 19),
            _item("Turkey Breast (6\")",      "Footlongs & Subs", "~7 oz",  280,  4,  1, 0.0, 25,  760, 40, 3,  6, 20),
            _item("Steak & Cheese (6\")",     "Footlongs & Subs", "~8 oz",  380, 11,  5, 0.0, 60,  910, 40, 3,  6, 28),
            _item("Veggie Delite (6\")",      "Footlongs & Subs", "~5 oz",  200,  2,  0, 0.0,  0,  280, 38, 3,  5,  9),
            _item("Spicy Italian (6\")",      "Footlongs & Subs", "~7 oz",  480, 24,  9, 0.0, 65, 1600, 40, 3,  6, 22),
            _item("Meatball Marinara (6\")",  "Footlongs & Subs", "~9 oz",  480, 18,  6, 0.5, 40, 1210, 57, 4, 10, 22),
            _item("Oven Roasted Chicken (6\")","Footlongs & Subs","~8 oz",  320,  5,  1, 0.0, 45,  610, 40, 3,  6, 24),
            _item("Chicken Caesar (6\")",     "Footlongs & Subs", "~8 oz",  430, 18,  4, 0.0, 65, 1080, 40, 3,  6, 25),
            _item("Chips",                    "Sides",            "1 oz",   140,  7,  1, 0.0,  0,  120, 18, 1,  1,  2),
            _item("Cookie",                   "Desserts",         "1.5 oz", 210, 10,  5, 0.0, 15,  130, 29, 1, 16,  2),
        ],
    },

    # ──────────────────────────── TACO BELL ──────────────────────────────────
    "taco-bell": {
        "chain": dict(name="Taco Bell", slug="taco-bell",
                      website="https://www.tacobell.com", cuisine_type="Mexican"),
        "items": [
            _item("Crunchy Taco",             "Tacos",     "2.8 oz",  170,  9,  3, 0.0, 25,  300, 13, 3,  1,  8),
            _item("Soft Taco",                "Tacos",     "3.5 oz",  180,  7,  3, 0.0, 25,  450, 18, 2,  2,  9),
            _item("Doritos Locos Taco",        "Tacos",     "2.9 oz",  170,  9,  3, 0.0, 25,  370, 14, 2,  1,  8),
            _item("Chalupa Supreme",           "Chalupas",  "5.3 oz",  350, 17,  5, 0.0, 40,  650, 33, 3,  3, 16),
            _item("Crunchwrap Supreme",        "Crunchwraps","~7 oz",  530, 21,  7, 0.0, 55, 1280, 65, 5,  6, 20),
            _item("Bean Burrito",              "Burritos",  "7.2 oz",  380,  9,  3, 0.0, 10, 1140, 58,  9,  3, 14),
            _item("Chicken Quesadilla",        "Quesadillas","5.7 oz", 470, 24,  9, 0.0, 80, 1050, 38, 3,  3, 26),
            _item("Nacho Cheese Doritos Fries","Sides",     "~5 oz",   400, 22,  3, 0.0,  0,  680, 46, 4,  0,  5),
            _item("Cinnabon Delights (4pk)",   "Desserts",  "2.9 oz",  310, 17,  8, 4.0, 10,  170, 35, 0, 16,  3),
            _item("Mountain Dew Baja Blast (20oz)","Drinks","20 fl oz",250,  0,  0, 0.0,  0,  100, 68, 0, 68,  0),
        ],
    },

    # ──────────────────────────── BURGER KING ────────────────────────────────
    "burger-king": {
        "chain": dict(name="Burger King", slug="burger-king",
                      website="https://www.bk.com", cuisine_type="Fast Food"),
        "items": [
            _item("Whopper",                  "Burgers",   "9.9 oz",  660, 40, 12, 1.0,  95, 980,  49, 2, 11, 28),
            _item("Whopper Jr",               "Burgers",   "5.7 oz",  340, 18,  6, 0.5,  55, 590,  28, 1,  6, 16),
            _item("Double Whopper",           "Burgers",   "13.2 oz", 900, 57, 20, 1.5, 160,1050,  49, 2, 11, 48),
            _item("Cheeseburger",             "Burgers",   "4.3 oz",  300, 14,  6, 0.5,  50, 710,  27, 1,  6, 16),
            _item("Original Chicken Sandwich","Chicken",   "8.1 oz",  660, 39,  9, 0.0,  75,1020,  49, 3,  5, 28),
            _item("Chicken Fries (9pc)",      "Chicken",   "3.8 oz",  290, 18,  4, 0.0,  25, 840,  19, 1,  0, 14),
            _item("Medium Onion Rings",       "Sides",     "3.5 oz",  410, 22,  5, 4.5,   0, 680,  49, 2,  7,  5),
            _item("Medium French Fries",      "Sides",     "3.8 oz",  380, 19,  5, 0.0,   0, 480,  49, 3,  0,  4),
            _item("Croissan'wich w/Egg & Cheese","Breakfast","4.7 oz",360, 22, 10, 0.0, 160, 730,  26, 1,  5, 14),
            _item("Hershey's Sundae Pie",     "Desserts",  "3.0 oz",  310, 19, 13, 0.0,   5, 170,  32, 1, 21,  4),
            _item("Medium Soft Drink",        "Drinks",    "22 fl oz",210,  0,  0, 0.0,   0,   35, 58, 0, 58,  0),
            _item("Large Soft Drink",         "Drinks",    "30 fl oz",290,  0,  0, 0.0,   0,   50, 79, 0, 79,  0),
            _item("Large Dr Pepper",          "Drinks",    "30 fl oz",310,  0,  0, 0.0,   0,   75, 86, 0, 86,  0),
            _item("Medium Diet Coke",         "Drinks",    "22 fl oz",  0,  0,  0, 0.0,   0,   55,  0, 0,  0,  0),
        ],
    },

    # ──────────────────────────── WENDY'S ────────────────────────────────────
    "wendys": {
        "chain": dict(name="Wendy's", slug="wendys",
                      website="https://www.wendys.com", cuisine_type="Fast Food"),
        "items": [
            _item("Dave's Single",            "Burgers",   "7.7 oz",  590, 34, 13, 1.5, 110,1010,  37, 2,  9, 30),
            _item("Dave's Double",            "Burgers",   "10.8 oz", 890, 56, 24, 2.5, 195,1270,  38, 2,  9, 50),
            _item("Baconator",                "Burgers",   "10.1 oz", 940, 61, 27, 2.0, 215,1720,  36, 1,  8, 57),
            _item("Jr. Cheeseburger",         "Burgers",   "4.5 oz",  290, 13,  5, 0.5,  50, 630,  26, 1,  6, 17),
            _item("Spicy Chicken Sandwich",   "Chicken",   "7.7 oz",  530, 25,  5, 0.0,  75,1210,  47, 2,  6, 28),
            _item("Grilled Chicken Sandwich", "Chicken",   "7.6 oz",  370, 10,  2, 0.0,  90, 990,  36, 2,  5, 34),
            _item("Medium Frosty (Chocolate)","Frosty",    "16 fl oz",460, 12,  8, 0.0,  50, 200,  78, 0, 57, 10),
            _item("Medium French Fries",      "Sides",     "4.4 oz",  410, 20,  4, 0.0,   0, 530,  55, 4,  0,  5),
            _item("Apple Pecan Chicken Salad","Salads",    "~13 oz",  340, 13,  6, 0.0,  80, 910,  30, 4, 22, 30),
            _item("Chili (Small)",            "Sides",     "8 oz",    170,  5,  2, 0.0,  40, 800,  17, 4,  5, 15),
            _item("Baked Potato (Plain)",     "Sides",     "10 oz",   270,  0,  0, 0.0,   0,  20,  61, 7,  3,  7),
            _item("Medium Soft Drink",        "Drinks",    "22 fl oz",210,  0,  0, 0.0,   0,   35, 58, 0, 58,  0),
            _item("Large Soft Drink",         "Drinks",    "30 fl oz",290,  0,  0, 0.0,   0,   50, 79, 0, 79,  0),
            _item("Large Dr Pepper",          "Drinks",    "30 fl oz",310,  0,  0, 0.0,   0,   75, 86, 0, 86,  0),
            _item("Large Frosty (Chocolate)", "Frosty",    "20 fl oz",580, 15, 10, 0.0,  60, 250,  96, 0, 70, 12),
        ],
    },

    # ──────────────────────────── CHICK-FIL-A ────────────────────────────────
    "chick-fil-a": {
        "chain": dict(name="Chick-fil-A", slug="chick-fil-a",
                      website="https://www.chick-fil-a.com", cuisine_type="Fast Food"),
        "items": [
            _item("Chicken Sandwich",         "Sandwiches","6.0 oz",  440, 19,  4, 0.0,  80,1350,  40, 1,  5, 28),
            _item("Spicy Chicken Sandwich",   "Sandwiches","6.0 oz",  450, 19,  4, 0.0,  80,1460,  41, 1,  6, 28),
            _item("Deluxe Chicken Sandwich",  "Sandwiches","8.1 oz",  520, 24,  6, 0.0, 100,1450,  43, 2,  7, 32),
            _item("Grilled Chicken Sandwich", "Sandwiches","7.1 oz",  380, 11,  3, 0.0, 100,1120,  40, 2,  7, 30),
            _item("8 pc Chicken Nuggets",     "Nuggets",   "3.9 oz",  250, 11,  2, 0.0,  80, 770,  11, 0,  1, 27),
            _item("12 pc Chicken Nuggets",    "Nuggets",   "5.9 oz",  380, 17,  3, 0.0, 120,1160,  17, 0,  2, 40),
            _item("Grilled Nuggets (8pc)",    "Nuggets",   "3.5 oz",  140,  3,  1, 0.0,  85, 530,   3, 0,  1, 25),
            _item("Waffle Potato Fries (Medium)","Sides",  "3.8 oz",  420, 23,  4, 0.0,   0, 290,  47, 4,  0,  5),
            _item("Mac & Cheese (Medium)",    "Sides",     "4.8 oz",  440, 26, 12, 0.0,  60, 900,  37, 1,  4, 16),
            _item("Fruit Cup (Medium)",       "Sides",     "6.0 oz",   70,  0,  0, 0.0,   0,   0,  16, 1, 13,  1),
            _item("Kale Crunch Side",         "Sides",     "2.6 oz",  120,  8,  1, 0.0,   0, 170,   9, 2,  4,  3),
            _item("Peach Milkshake (Small)",  "Desserts",  "14 fl oz",490, 13,  8, 0.0,  50, 210,  81, 0, 75, 10),
            _item("Chocolate Chunk Cookie",   "Desserts",  "2.9 oz",  360, 18,  9, 0.0,  40, 200,  46, 2, 29,  4),
            _item("Medium Lemonade",          "Drinks",    "16 fl oz",170,  0,  0, 0.0,   0,   15, 46, 0, 44,  0),
            _item("Large Lemonade",           "Drinks",    "32 fl oz",340,  0,  0, 0.0,   0,   30, 92, 0, 88,  0),
            _item("Medium Sweet Tea",         "Drinks",    "16 fl oz",120,  0,  0, 0.0,   0,   15, 32, 0, 32,  0),
            _item("Medium Soft Drink",        "Drinks",    "22 fl oz",210,  0,  0, 0.0,   0,   35, 58, 0, 58,  0),
            _item("Large Soft Drink",         "Drinks",    "32 fl oz",310,  0,  0, 0.0,   0,   50, 86, 0, 86,  0),
            _item("Large Dr Pepper",          "Drinks",    "32 fl oz",310,  0,  0, 0.0,   0,   75, 86, 0, 86,  0),
        ],
    },

    # ──────────────────────────── KFC ────────────────────────────────────────
    "kfc": {
        "chain": dict(name="KFC", slug="kfc",
                      website="https://www.kfc.com", cuisine_type="Fast Food"),
        "items": [
            _item("Original Recipe Breast",   "Chicken",   "~5.5 oz", 390, 21,  5, 0.0, 145,1010,  11, 0,  0, 39),
            _item("Extra Crispy Breast",      "Chicken",   "~5.7 oz", 490, 29,  7, 0.0, 115, 860,  20, 0,  0, 36),
            _item("Original Recipe Thigh",    "Chicken",   "~3.9 oz", 280, 18,  4, 0.0,  95, 710,   8, 0,  0, 22),
            _item("Chicken Sandwich",         "Sandwiches","~7.5 oz", 650, 38, 10, 0.0, 100,1090,  46, 2,  8, 28),
            _item("Spicy Chicken Sandwich",   "Sandwiches","~7.5 oz", 630, 36, 10, 0.0, 100,1370,  46, 2,  7, 28),
            _item("Famous Bowl",              "Bowls",     "~13 oz",  710, 34,  8, 0.0, 100,2200,  80, 5,  4, 26),
            _item("Mashed Potatoes w/Gravy",  "Sides",     "~4.8 oz", 160,  5,  1, 0.0,   0, 540,  25, 2,  1,  3),
            _item("Coleslaw",                 "Sides",     "~4 oz",   170,  9,  1, 0.0,  10, 210,  22, 2, 10,  1),
            _item("Biscuit",                  "Sides",     "~2 oz",   180,  8,  4, 0.0,   0, 530,  24, 1,  2,  3),
            _item("Mac & Cheese",             "Sides",     "~4.8 oz", 140,  6,  3, 0.0,  15, 690,  17, 0,  3,  5),
            _item("Medium Soft Drink",        "Drinks",    "22 fl oz",210,  0,  0, 0.0,   0,   35, 58, 0, 58,  0),
            _item("Large Soft Drink",         "Drinks",    "32 fl oz",310,  0,  0, 0.0,   0,   50, 86, 0, 86,  0),
            _item("Large Dr Pepper",          "Drinks",    "32 fl oz",310,  0,  0, 0.0,   0,   75, 86, 0, 86,  0),
        ],
    },

    # ──────────────────────────── POPEYES ────────────────────────────────────
    "popeyes": {
        "chain": dict(name="Popeyes", slug="popeyes",
                      website="https://www.popeyes.com", cuisine_type="Fast Food"),
        "items": [
            _item("Classic Chicken Sandwich", "Sandwiches","~7 oz",   700, 42, 14, 0.0,  70,1443,  50, 2,  7, 28),
            _item("Spicy Chicken Sandwich",   "Sandwiches","~7 oz",   700, 42, 14, 0.0,  70,1441,  50, 2,  7, 28),
            _item("Breast (Mild/Spicy)",      "Chicken",   "~5.8 oz", 440, 27,  9, 0.0, 115,1330,  15, 0,  0, 37),
            _item("Thigh (Mild/Spicy)",       "Chicken",   "~3.3 oz", 300, 21,  8, 0.0,  85, 860,  10, 0,  0, 18),
            _item("Tenders (3pc Mild)",       "Tenders",   "~4.5 oz", 340, 17,  5, 0.0,  95, 870,  18, 0,  0, 31),
            _item("Red Beans & Rice",         "Sides",     "~5.1 oz", 230,  6,  2, 0.0,  10, 730,  35, 4,  1,  8),
            _item("Cajun Fries (Regular)",    "Sides",     "~3 oz",   260, 12,  3, 0.0,   0, 770,  35, 3,  0,  4),
            _item("Coleslaw",                 "Sides",     "~4 oz",   270, 17,  3, 0.0,  20, 210,  26, 2, 11,  2),
            _item("Biscuit",                  "Sides",     "~2.5 oz", 260, 13,  5, 0.0,   0, 520,  32, 1,  4,  4),
            _item("Mashed Potatoes w/Gravy",  "Sides",     "~5 oz",   110,  3,  1, 0.0,   5, 530,  17, 1,  1,  3),
            _item("Medium Soft Drink",        "Drinks",    "22 fl oz",210,  0,  0, 0.0,   0,   35, 58, 0, 58,  0),
            _item("Large Soft Drink",         "Drinks",    "32 fl oz",310,  0,  0, 0.0,   0,   50, 86, 0, 86,  0),
            _item("Large Dr Pepper",          "Drinks",    "32 fl oz",310,  0,  0, 0.0,   0,   75, 86, 0, 86,  0),
        ],
    },

    # ──────────────────────────── PANERA BREAD ───────────────────────────────
    "panera": {
        "chain": dict(name="Panera Bread", slug="panera",
                      website="https://www.panerabread.com", cuisine_type="Bakery / Café"),
        "items": [
            _item("Broccoli Cheddar Soup (Bowl)","Soups", "~12 oz",  360, 22, 13, 0.0,  65,1340,  27, 3,  6, 16),
            _item("Mac & Cheese (Bowl)",         "Mac",   "~12 oz",  990, 58, 32, 0.0, 165,1570, 100, 4, 13, 34),
            _item("Fuji Apple Chicken Salad",    "Salads","~12 oz",  570, 27,  5, 0.0, 120, 740,  53, 5, 41, 30),
            _item("Caesar Salad",                "Salads","~11 oz",  480, 33,  6, 0.0,  50, 980,  27, 4,  4, 22),
            _item("Chicken Noodle Soup (Bowl)",  "Soups", "~12 oz",  190,  4,  1, 0.0,  60,1630,  26, 2,  3, 13),
            _item("Bacon Turkey Bravo Sandwich", "Sandwiches","~12 oz",700, 28,  8, 0.0, 100,2230, 66, 3,  9, 44),
            _item("Frontega Chicken Panini",     "Sandwiches","~11 oz",830, 37, 11, 0.0, 155,1660, 80, 4,  9, 43),
            _item("Strawberry Banana Smoothie",  "Drinks","16 fl oz", 280,  2,  0, 0.0,   5, 110,  59, 4, 48,  7),
            _item("Cinnamon Crunch Bagel",       "Bakery","~4.5 oz", 440,  6,  3, 0.0,   0, 310,  88, 3, 18,  9),
            _item("Blueberry Muffin",            "Bakery","~5.8 oz", 460, 15,  3, 0.0,  60, 450,  73, 2, 40,  7),
            _item("Chocolate Chip Cookie",       "Bakery","~2.8 oz", 440, 24, 13, 0.0,  50, 310,  55, 2, 32,  5),
        ],
    },

    # ──────────────────────────── SONIC ──────────────────────────────────────
    "sonic": {
        "chain": dict(name="Sonic Drive-In", slug="sonic",
                      website="https://www.sonicdrivein.com", cuisine_type="Fast Food"),
        "items": [
            _item("Classic Cheeseburger",     "Burgers",   "~6 oz",   610, 37, 13, 1.5, 100, 920,  45, 2,  9, 27),
            _item("Jr. Deluxe Cheeseburger",  "Burgers",   "~4.5 oz", 420, 25,  9, 0.5,  60, 620,  31, 2,  7, 18),
            _item("Crispy Chicken Sandwich",  "Chicken",   "~7 oz",   590, 29,  6, 0.0,  60,1130,  57, 3,  8, 25),
            _item("Corn Dog",                 "Corn Dogs", "~2.7 oz", 220, 11,  3, 1.0,  35, 510,  25, 1,  7,  7),
            _item("Medium Tater Tots",        "Sides",     "~3.5 oz", 290, 16,  3, 0.0,   0, 540,  34, 3,  0,  4),
            _item("Medium Onion Rings",       "Sides",     "~3.3 oz", 340, 18,  3, 3.5,   0, 390,  40, 2,  3,  4),
            _item("Medium Vanilla Shake",     "Shakes",    "16 fl oz",600, 25, 17, 0.5,  90, 300,  85, 0, 65, 10),
            _item("Medium Cherry Limeade",    "Drinks",    "20 fl oz",250,  0,  0, 0.0,   0,  25,  65, 0, 63,  0),
            _item("Small Soft Serve Cone",    "Desserts",  "~3 oz",   180,  5,  3, 0.0,  20,  95,  29, 0, 22,  4),
        ],
    },

    # ──────────────────────────── PANDA EXPRESS ──────────────────────────────
    "panda-express": {
        "chain": dict(name="Panda Express", slug="panda-express",
                      website="https://www.pandaexpress.com", cuisine_type="Asian"),
        "items": [
            _item("Orange Chicken",           "Entrees",   "5.7 oz",  490, 23,  5, 0.0,  95, 820,  51, 1, 19, 25),
            _item("Beijing Beef",             "Entrees",   "5.6 oz",  480, 24,  5, 0.0,  60, 910,  55, 1, 24, 14),
            _item("Broccoli Beef",            "Entrees",   "5.3 oz",  150,  7,  1, 0.0,  15, 520,  13, 1,  4, 10),
            _item("Kung Pao Chicken",         "Entrees",   "5.7 oz",  290, 16,  3, 0.0,  95, 930,  22, 2,  7, 23),
            _item("Honey Walnut Shrimp",      "Entrees",   "3.9 oz",  430, 23,  4, 0.0, 115, 400,  40, 1, 17, 16),
            _item("Chow Mein",                "Sides",     "9.3 oz",  510, 22,  4, 0.0,   0, 980,  70, 8,  6, 13),
            _item("Fried Rice",               "Sides",     "9.2 oz",  620, 26,  5, 0.0, 160,1070,  85, 3,  3, 15),
            _item("White Steamed Rice",       "Sides",     "8.1 oz",  380,  0,  0, 0.0,   0,   0,  86, 0,  0,  7),
            _item("Super Greens",             "Sides",     "7.2 oz",   90,  3,  0, 0.0,   0, 380,  13, 5,  5,  6),
            _item("Egg Roll (1 pc)",          "Appetizers","3.1 oz",  200,  9,  2, 0.0,  10, 390,  25, 2,  1,  5),
            _item("Cream Cheese Rangoon",     "Appetizers","2.4 oz",  190, 10,  4, 0.0,  25, 190,  20, 1,  3,  4),
        ],
    },

    # ──────────────────────────── FIVE GUYS ──────────────────────────────────
    "five-guys": {
        "chain": dict(name="Five Guys", slug="five-guys",
                      website="https://www.fiveguys.com", cuisine_type="Fast Food"),
        "items": [
            _item("Hamburger",                "Burgers",   "~9 oz",   700, 43, 20, 2.5, 125, 430,  39, 2,  9, 40),
            _item("Little Hamburger",         "Burgers",   "~5.5 oz", 480, 26, 12, 1.5,  75, 380,  39, 2,  9, 22),
            _item("Cheeseburger",             "Burgers",   "~10 oz",  840, 56, 28, 2.5, 175, 900,  40, 2,  9, 51),
            _item("Bacon Burger",             "Burgers",   "~10.5 oz",840, 55, 23, 2.5, 155, 730,  40, 2,  9, 48),
            _item("Hot Dog",                  "Hot Dogs",  "~5.5 oz", 580, 36, 15, 0.5, 100,1170,  46, 2,  9, 22),
            _item("BLT",                      "Sandwiches","~5 oz",   580, 38, 19, 0.5, 100, 760,  41, 2,  9, 17),
            _item("Regular Fries",            "Fries",     "~17 oz",  953, 41,  9, 0.0,   0, 962, 131, 9,  0, 13),
            _item("Little Fries",             "Fries",     "~8.5 oz", 476, 21,  4, 0.0,   0, 481,  65, 4,  0,  7),
            _item("Regular Cajun Fries",      "Fries",     "~17 oz",  953, 41,  9, 0.0,   0,1422, 131, 9,  0, 13),
            _item("Vanilla Milkshake",        "Milkshakes","24 fl oz",790, 20, 12, 0.0,  80, 510, 135, 0,120, 17),
            _item("Medium Soft Drink",        "Drinks",    "22 fl oz",210,  0,  0, 0.0,   0,   35, 58, 0, 58,  0),
            _item("Large Soft Drink",         "Drinks",    "32 fl oz",310,  0,  0, 0.0,   0,   50, 86, 0, 86,  0),
            _item("Large Dr Pepper",          "Drinks",    "32 fl oz",310,  0,  0, 0.0,   0,   75, 86, 0, 86,  0),
        ],
    },

    # ──────────────────────────── ARBY'S ─────────────────────────────────────
    "arbys": {
        "chain": dict(name="Arby's", slug="arbys",
                      website="https://arbys.com", cuisine_type="Fast Food"),
        "items": [
            _item("Classic Roast Beef",       "Sandwiches","~5.4 oz", 360, 14,  5, 0.5,  65, 970,  37, 2,  6, 23),
            _item("French Dip & Swiss",       "Sandwiches","~8.7 oz", 510, 20,  8, 0.0, 110,1680,  42, 2,  6, 37),
            _item("Beef 'n Cheddar Classic",  "Sandwiches","~6.5 oz", 450, 20,  7, 0.5,  75,1310,  45, 2,  9, 22),
            _item("Half Pound Beef 'n Cheddar","Sandwiches","~9.5 oz",690, 33, 12, 0.5, 130,1970,  58, 3, 12, 38),
            _item("Chicken Tenders (3pc)",    "Chicken",   "~4.2 oz", 360, 16,  3, 0.0,  45,1130,  35, 2,  0, 21),
            _item("Curly Fries (Medium)",     "Sides",     "~4 oz",   430, 22,  5, 0.0,   0,1150,  54, 4,  0,  5),
            _item("Steakhouse Onion Rings",   "Sides",     "~4.2 oz", 430, 20,  4, 4.0,   0, 490,  57, 3, 10,  5),
            _item("Jamocha Shake (Small)",    "Desserts",  "12 fl oz",490, 12,  8, 0.0,  45, 380,  81, 0, 64, 11),
            _item("Medium Soft Drink",        "Drinks",    "22 fl oz",210,  0,  0, 0.0,   0,   35, 58, 0, 58,  0),
            _item("Large Soft Drink",         "Drinks",    "32 fl oz",310,  0,  0, 0.0,   0,   50, 86, 0, 86,  0),
            _item("Large Dr Pepper",          "Drinks",    "32 fl oz",310,  0,  0, 0.0,   0,   75, 86, 0, 86,  0),
        ],
    },

    # ──────────────────────────── DAIRY QUEEN ────────────────────────────────
    "dairy-queen": {
        "chain": dict(name="Dairy Queen", slug="dairy-queen",
                      website="https://www.dairyqueen.com", cuisine_type="Fast Food"),
        "items": [
            _item("Blizzard Oreo (Medium)",   "Blizzards", "15 fl oz",730, 26, 14, 0.5,  75, 440, 114, 0, 88, 14),
            _item("Blizzard Reese's (Medium)","Blizzards", "15 fl oz",790, 30, 17, 0.5,  65, 480, 117, 2, 95, 17),
            _item("Blizzard M&M's (Medium)",  "Blizzards", "15 fl oz",770, 28, 18, 0.5,  75, 340, 119, 1,103, 13),
            _item("DQ Cheeseburger",          "Burgers",   "~5 oz",   400, 21,  9, 0.5,  60, 870,  33, 2,  8, 20),
            _item("1/4 lb GrillBurger",       "Burgers",   "~7 oz",   530, 29, 12, 1.0, 100,1030,  38, 2,  8, 29),
            _item("Chicken Strip Basket (4pc)","Chicken",  "~9.5 oz", 1010,51, 11, 0.0,  80,2110,  102,5, 10, 38),
            _item("Medium Soft Serve Cone",   "Ice Cream", "~5.1 oz", 330, 10,  6, 0.0,  30, 190,  52, 0, 39,  8),
            _item("Dipped Cone (Medium)",      "Ice Cream", "~5.8 oz", 470, 22, 14, 0.0,  30, 200,  63, 1, 48,  8),
            _item("Medium French Fries",       "Sides",     "~3.8 oz", 330, 14,  3, 0.0,   0, 730,  46, 3,  0,  4),
            _item("Pecan Mudslide",            "Desserts",  "~7 oz",   720, 31, 13, 0.0,  40, 420, 103, 2, 75, 11),
            _item("Medium Soft Drink",        "Drinks",    "22 fl oz",210,  0,  0, 0.0,   0,   35, 58, 0, 58,  0),
            _item("Large Soft Drink",         "Drinks",    "32 fl oz",310,  0,  0, 0.0,   0,   50, 86, 0, 86,  0),
            _item("Large Dr Pepper",          "Drinks",    "32 fl oz",310,  0,  0, 0.0,   0,   75, 86, 0, 86,  0),
        ],
    },

    # ──────────────────────────── CULVER'S ───────────────────────────────────
    "culvers": {
        "chain": dict(name="Culver's", slug="culvers",
                      website="https://www.culvers.com", cuisine_type="Fast Food"),
        "items": [
            _item("ButterBurger The Original","Burgers",   "~5.4 oz", 390, 17,  7, 0.5,  65, 500,  36, 1,  6, 22),
            _item("Double ButterBurger w/Cheese","Burgers","~8.5 oz", 670, 40, 18, 1.0, 140, 900,  36, 1,  6, 40),
            _item("Chicken Filet Sandwich",   "Chicken",   "~7 oz",   500, 22,  4, 0.0,  75, 760,  46, 2,  5, 28),
            _item("Walleye Sandwich",         "Seafood",   "~6.5 oz", 550, 26,  5, 0.0,  90, 640,  49, 2,  4, 28),
            _item("Fresh Cheese Curds",       "Sides",     "~5.5 oz", 650, 42, 20, 0.0, 110, 680,  43, 0,  4, 26),
            _item("Crinkle Cut Fries (Reg)",  "Sides",     "~4 oz",   370, 17,  3, 0.0,   0, 490,  50, 4,  0,  5),
            _item("Concrete Mixer (Small)",   "Frozen Custard","12 oz",565, 30, 16, 0.0, 120, 230,  68, 0, 53, 10),
            _item("Vanilla Dish",             "Frozen Custard","~3 oz",310, 18, 10, 0.0,  95, 100,  31, 0, 27,  6),
            _item("Pot Roast Sandwich",       "Sandwiches","~8 oz",   510, 21, 10, 0.0,  95,1420,  47, 1,  6, 32),
        ],
    },

    # ──────────────────────────── JIMMY JOHN'S ───────────────────────────────
    "jimmy-johns": {
        "chain": dict(name="Jimmy John's", slug="jimmy-johns",
                      website="https://www.jimmyjohns.com", cuisine_type="Sandwiches"),
        "items": [
            _item("The J.J. Gargantuan (8\")",  "Subs",     "~15 oz",  820, 44, 15, 0.5, 150,2780, 52, 3,  5, 52),
            _item("Italian Night Club (8\")",   "Subs",     "~12 oz",  680, 37, 12, 0.5, 105,2420, 50, 2,  5, 33),
            _item("Slim Turkey Tom (8\")",      "Slim Subs","~7 oz",   490, 20,  5, 0.0,  55,1400, 50, 2,  4, 31),
            _item("Turkey Tom (8\")",           "Subs",     "~9 oz",   560, 26,  7, 0.0,  65,1400, 50, 2,  4, 28),
            _item("Vito (8\")",                 "Subs",     "~9 oz",   580, 33, 11, 0.5,  85,2020, 46, 2,  4, 26),
            _item("Beach Club (8\")",           "Subs",     "~10 oz",  620, 32,  8, 0.0,  75,1710, 47, 2,  5, 30),
            _item("Tuna Fish (8\")",            "Subs",     "~10 oz",  700, 44,  8, 0.0,  50,1450, 47, 2,  4, 26),
            _item("Side of Chips",              "Sides",    "1 oz",    140,  8,  1, 0.0,   0, 125, 16, 1,  1,  2),
            _item("Cookie",                     "Desserts", "~2.5 oz", 420, 19, 10, 0.0,  45, 270, 59, 1, 34,  5),
        ],
    },

    # ──────────────────────────── WINGSTOP ───────────────────────────────────
    "wingstop": {
        "chain": dict(name="Wingstop", slug="wingstop",
                      website="https://www.wingstop.com", cuisine_type="Wings"),
        "items": [
            _item("Classic Wings (6pc)",          "Wings",  "~6 oz",   420, 28,  8, 0.0, 120, 450,  2, 0, 0, 37),
            _item("Boneless Wings (6pc)",         "Wings",  "~5 oz",   360, 19,  4, 0.0,  60,1040, 26, 1, 1, 21),
            _item("Classic Wings Lemon Pepper",   "Wings",  "~6 oz",   430, 29,  8, 0.0, 120, 860,  4, 0, 0, 37),
            _item("Chicken Tenders (5pc)",        "Tenders","~5.5 oz", 460, 22,  4, 0.0,  75,1240, 32, 1, 1, 32),
            _item("Large Seasoned Fries",         "Sides",  "~7 oz",   590, 30,  6, 0.0,   0,2040, 75, 6, 0,  9),
            _item("Ranch Dip",                    "Sauces", "1.5 oz",  200, 22,  4, 0.0,  10, 260,  1, 0, 1,  1),
            _item("Louisiana Rub Wings (6pc)",    "Wings",  "~6 oz",   420, 28,  8, 0.0, 120, 660,  3, 0, 0, 37),
        ],
    },

    # ──────────────────────────── RAISING CANE'S ─────────────────────────────
    "raising-canes": {
        "chain": dict(name="Raising Cane's", slug="raising-canes",
                      website="https://www.raisingcanes.com", cuisine_type="Fast Food"),
        "items": [
            _item("Chicken Finger (1pc)",     "Chicken",   "1.5 oz",  130,  7,  1, 0.0,  30, 290,  7, 0, 0, 10),
            _item("The Box Combo (4pc)",       "Combos",   "~14 oz",  830, 42,  8, 0.0, 130,1640, 74, 3, 7, 37),
            _item("The Caniac (6pc)",          "Combos",   "~19 oz", 1070, 55, 10, 0.0, 195,2080, 93, 4, 9, 52),
            _item("Crinkle Cut Fries",         "Sides",    "~4 oz",   320, 14,  3, 0.0,   0, 430, 45, 3, 0,  5),
            _item("Coleslaw",                  "Sides",    "~4 oz",   132,  9,  1, 0.0,  10, 251, 12, 1, 7,  1),
            _item("Texas Toast (1 slice)",     "Sides",    "~2 oz",   146,  5,  1, 0.0,   0, 310, 22, 1, 2,  4),
            _item("Cane's Sauce",              "Sauces",   "1.5 oz",  190, 20,  3, 0.0,  15, 450,  3, 0, 2,  0),
            _item("Lemonade",                  "Drinks",   "22 fl oz",220,  0,  0, 0.0,   0,  60, 55, 0,54,  0),
        ],
    },

    # ──────────────────────────── BUFFALO WILD WINGS ─────────────────────────
    "buffalo-wild-wings": {
        "chain": dict(name="Buffalo Wild Wings", slug="buffalo-wild-wings",
                      website="https://www.buffalowildwings.com", cuisine_type="Wings"),
        "items": [
            _item("Traditional Wings (6pc)",  "Wings",     "~7 oz",   430, 27,  9, 0.0, 145, 490,  0, 0, 0, 41),
            _item("Boneless Wings (6pc)",     "Wings",     "~6 oz",   380, 22,  5, 0.0,  55,1100, 20, 1, 1, 23),
            _item("Buffalo Sauce Wings",      "Wings",     "~7 oz",   430, 27,  9, 0.0, 145,1110,  2, 0, 1, 41),
            _item("Chicken Sandwich",         "Sandwiches","~8 oz",   660, 33,  6, 0.0,  75,1410, 58, 3, 7, 33),
            _item("Cheeseburger",             "Burgers",   "~9 oz",   790, 46, 17, 1.0, 135,1170, 47, 2,10, 46),
            _item("Cheese Curds",             "Appetizers","~5 oz",   650, 42, 20, 0.0, 110, 680, 43, 0, 4, 26),
            _item("Loaded Totchos",           "Appetizers","~12 oz",  930, 56, 22, 0.0, 120,2160, 78, 6, 6, 34),
            _item("House Salad",              "Salads",    "~7 oz",   300, 22,  8, 0.0,  30, 560, 16, 3, 6, 13),
            _item("Street Tacos (3pc Chicken)","Tacos",    "~10 oz",  640, 28,  8, 0.0, 115,1500, 60, 3, 7, 38),
        ],
    },

    # ──────────────────────────── APPLEBEE'S ─────────────────────────────────
    "applebees": {
        "chain": dict(name="Applebee's", slug="applebees",
                      website="https://www.applebees.com", cuisine_type="Casual Dining"),
        "items": [
            _item("Classic Bacon Cheeseburger","Burgers",  "~11 oz", 1050, 68, 26, 2.0, 175,1700, 50, 2, 12, 60),
            _item("Fiesta Lime Chicken",       "Chicken",  "~14 oz",  1270,66, 20, 1.0, 245,3540, 104,5, 19, 70),
            _item("Grilled Chicken Sandwich",  "Sandwiches","~9 oz",  570, 22,  6, 0.0, 115,1420, 43, 2,  7, 48),
            _item("Riblet Basket",             "Ribs",     "~11 oz",  1570,96, 29, 1.5, 240,2580, 101,4, 35, 67),
            _item("Double Crunch Shrimp",      "Seafood",  "~8 oz",   770, 41,  6, 0.0, 240,1920, 70, 3,  4, 32),
            _item("Oriental Chicken Salad",    "Salads",   "~14 oz",  1380,91, 14, 0.0, 220,1230, 95, 6, 47, 46),
            _item("Loaded Mashed Potatoes",    "Sides",    "~8 oz",   600, 35, 17, 0.0,  65,1440, 57, 5,  5, 20),
            _item("Boneless Wings (8pc)",      "Appetizers","~7 oz",  750, 44,  9, 0.0, 110,2520, 50, 3,  5, 38),
            _item("Triple Chocolate Meltdown", "Desserts", "~5 oz",   970, 46, 22, 0.0, 115, 660, 130,3, 85, 13),
        ],
    },

    # ──────────────────────────── CHILI'S ────────────────────────────────────
    "chilis": {
        "chain": dict(name="Chili's", slug="chilis",
                      website="https://www.chilis.com", cuisine_type="Casual Dining"),
        "items": [
            _item("Original Cheeseburger",    "Burgers",   "~12 oz",  1170,79, 29, 3.0, 195,1930, 56, 3, 12, 63),
            _item("Crispy Chicken Sandwich",  "Sandwiches","~10 oz",  810, 42, 10, 0.0, 130,1770, 62, 3,  8, 42),
            _item("Classic Nachos",           "Appetizers","~17 oz", 1580,98, 35, 1.0, 170,2940,107, 11,14, 58),
            _item("Fajitas Chicken (for one)","Fajitas",   "~13 oz", 1490,73, 14, 0.0, 195,4420, 123,11,19,103),
            _item("Cajun Chicken Pasta",      "Pasta",     "~16 oz", 1080,51, 20, 0.0, 195,3200, 94, 5, 11, 60),
            _item("Loaded Mashed Potatoes",   "Sides",     "~8 oz",   440, 26,  8, 0.0,  30, 720, 45, 4,  4, 10),
            _item("House Salad",              "Salads",    "~7 oz",   250, 17,  4, 0.0,  15, 500, 16, 3,  7,  9),
            _item("Molten Chocolate Cake",    "Desserts",  "~5 oz",   1060,50, 28, 0.0, 135, 640,148, 4,103, 14),
        ],
    },

    # ──────────────────────────── OLIVE GARDEN ───────────────────────────────
    "olive-garden": {
        "chain": dict(name="Olive Garden", slug="olive-garden",
                      website="https://www.olivegarden.com", cuisine_type="Italian"),
        "items": [
            _item("Fettuccine Alfredo",        "Pasta",    "~23 oz", 1200,63, 38, 0.0, 175,1350, 122,6, 12, 44),
            _item("Spaghetti & Meatballs",     "Pasta",    "~23 oz",  890, 28, 11, 0.5, 100,2190, 117,9, 18, 47),
            _item("Chicken Parmigiana",        "Chicken",  "~17 oz", 1060,45, 14, 0.0, 245,2870,  74,5, 12, 91),
            _item("Chicken Alfredo",           "Pasta",    "~23 oz", 1270,68, 42, 0.0, 235,1730, 107,5, 10, 65),
            _item("Lasagna Classico",          "Pasta",    "~15 oz",  870, 43, 22, 0.0, 165,2480,  68,7, 15, 58),
            _item("Tour of Italy",             "Combination","~21 oz",1570,77, 32, 0.0, 285,3650, 130,8, 21,100),
            _item("House Salad (no dressing)", "Salads",   "~9 oz",   100,  5,  2, 0.0,  15, 580,  10,3,  5,  4),
            _item("Breadstick (no dipping)",   "Breadsticks","~2 oz", 140,  3,  0, 0.0,   0, 460,  26,1,  1,  5),
            _item("Tiramisu",                  "Desserts", "~8 oz",   470, 28, 15, 0.0, 165, 150,  46,1, 30, 10),
        ],
    },

    # ──────────────────────────── TEXAS ROADHOUSE ────────────────────────────
    "texas-roadhouse": {
        "chain": dict(name="Texas Roadhouse", slug="texas-roadhouse",
                      website="https://www.texasroadhouse.com", cuisine_type="Casual Dining"),
        "items": [
            _item("6 oz Sirloin",             "Steaks",    "~7 oz",   250, 10,  4, 0.0, 105, 650,   0,0,  0, 38),
            _item("12 oz Ribeye",             "Steaks",    "~13 oz",  760, 51, 21, 0.0, 215,1260,   0,0,  0, 72),
            _item("Country Fried Chicken",    "Chicken",   "~11 oz",  750, 37, 10, 0.0, 140,2110,  60,2,  5, 50),
            _item("Grilled Chicken",          "Chicken",   "~7 oz",   250,  5,  1, 0.0, 125, 630,   1,0,  0, 49),
            _item("Herb Crusted Chicken",     "Chicken",   "~9 oz",   510, 21, 11, 0.0, 175,1260,  22,1,  2, 59),
            _item("Mashed Potatoes",          "Sides",     "~6 oz",   200,  9,  5, 0.0,  25, 490,  24,2,  2,  5),
            _item("Seasoned Rice",            "Sides",     "~6 oz",   230,  4,  1, 0.0,   0, 500,  41,1,  1,  6),
            _item("Baked Potato",             "Sides",     "~10 oz",  270,  0,  0, 0.0,   0,  25,  61,7,  2,  7),
            _item("Fresh-Baked Bread (1 loaf)","Bread",    "~2 oz",   150,  2,  1, 0.0,   0, 240,  27,1,  3,  4),
            _item("Rolls (2pc)",              "Bread",     "~4 oz",   300,  4,  2, 0.0,   0, 480,  54,2,  6,  8),
        ],
    },

    # ──────────────────────────── SHAKE SHACK ────────────────────────────────
    "shake-shack": {
        "chain": dict(name="Shake Shack", slug="shake-shack",
                      website="https://www.shakeshack.com", cuisine_type="Fast Food"),
        "items": [
            _item("ShackBurger",              "Burgers",   "~6 oz",   500, 29, 13, 1.5,  90, 830,  32,1,  8, 27),
            _item("SmokeShack",               "Burgers",   "~7 oz",   630, 38, 16, 2.0, 120,1110,  33,1,  9, 36),
            _item("Veggie Shack",             "Burgers",   "~8 oz",   630, 34, 12, 0.5,  75, 970,  54,6,  9, 21),
            _item("ShackMeister Burger",      "Burgers",   "~7.5 oz", 680, 43, 18, 2.0, 120,1230,  34,1, 10, 37),
            _item("Chick'n Shack",            "Chicken",   "~7 oz",   670, 41,  8, 0.0,  95,1180,  42,2,  5, 32),
            _item("Crinkle Cut Fries",        "Fries",     "~4 oz",   330, 18,  3, 0.0,   0, 360,  40,3,  0,  4),
            _item("Cheese Fries",             "Fries",     "~5 oz",   500, 30,  9, 0.0,  20, 720,  47,3,  2,  9),
            _item("Vanilla Shake",            "Shakes",    "16 fl oz",660, 34, 22, 0.0, 140, 310,  79,0, 71, 14),
            _item("Hot Fudge Sundae",         "Desserts",  "~6 oz",   420, 17, 11, 0.0,  65, 130,  63,0, 53,  7),
        ],
    },

    # ──────────────────────────── JERSEY MIKE'S ──────────────────────────────
    "jersey-mikes": {
        "chain": dict(name="Jersey Mike's", slug="jersey-mikes",
                      website="https://www.jerseymikes.com", cuisine_type="Sandwiches"),
        "items": [
            _item("The Original Italian (Regular)","Subs","~10 oz",  700, 38, 14, 0.5, 100,2340, 55,3,  5, 34),
            _item("Club Supreme (Regular)",    "Subs",     "~10 oz",  510, 21,  8, 0.0,  90,1750, 52,3,  7, 33),
            _item("Turkey & Provolone (Regular)","Subs",  "~9 oz",   460, 18,  6, 0.0,  75,1650, 52,3,  7, 27),
            _item("Chipotle Chicken Cheese Steak","Subs", "~10 oz",  720, 38, 11, 0.5, 120,1800, 57,3,  7, 39),
            _item("BLT (Regular)",             "Subs",     "~8 oz",   630, 37, 13, 0.5,  80,1790, 53,3,  7, 23),
            _item("Veggie (Regular)",          "Subs",     "~9 oz",   420, 14,  6, 0.0,  25,1180, 55,4,  9, 19),
            _item("Chips",                     "Sides",    "1 oz",    140,  7,  1, 0.0,   0, 160, 18,1,  0,  2),
            _item("Brownie",                   "Desserts", "~3 oz",   390, 17,  4, 0.0,  15, 130, 56,2, 39,  4),
        ],
    },

    # ──────────────────────────── FIREHOUSE SUBS ─────────────────────────────
    "firehouse-subs": {
        "chain": dict(name="Firehouse Subs", slug="firehouse-subs",
                      website="https://www.firehousesubs.com", cuisine_type="Sandwiches"),
        "items": [
            _item("Hook & Ladder (Medium)",   "Subs",     "~10 oz",  580, 22,  8, 0.0, 105,1710, 58,3,  8, 37),
            _item("Turkey Breast (Medium)",   "Subs",     "~9 oz",   480, 13,  5, 0.0,  95,1830, 57,3,  8, 32),
            _item("Firehouse Meatball (Med)", "Subs",     "~13 oz",  920, 48, 20, 1.0, 175,2920, 80,5, 14, 52),
            _item("Chicken Bacon Ranch (Med)","Subs",     "~10 oz",  620, 25,  7, 0.0, 120,1840, 57,3,  7, 43),
            _item("HERO (Medium)",            "Subs",     "~10 oz",  660, 32, 11, 0.5, 120,2290, 57,3,  8, 41),
            _item("Club on a Sub (Medium)",   "Subs",     "~10 oz",  590, 21,  7, 0.0, 105,2100, 62,3,  9, 37),
            _item("Chips",                    "Sides",    "1 oz",    150,  8,  1, 0.0,   0, 105, 18,1,  0,  2),
        ],
    },

    # ──────────────────────────── NOODLES & COMPANY ──────────────────────────
    "noodles-and-company": {
        "chain": dict(name="Noodles & Company", slug="noodles-and-company",
                      website="https://www.noodles.com", cuisine_type="Asian"),
        "items": [
            _item("Mac & Cheese (Regular)",   "American",  "~10 oz",  500, 20,  9, 0.0,  55,1000, 62,3, 11, 18),
            _item("Spaghetti & Meatballs",    "American",  "~14 oz",  780, 27, 11, 0.5, 100,1620,  90,7, 11, 42),
            _item("Pad Thai Chicken",         "Asian",     "~13 oz",  770, 24,  5, 0.0, 175,1790,  92,5, 22, 41),
            _item("Japanese Pan Noodles",     "Asian",     "~13 oz",  580, 15,  2, 0.0,   0,1490,  92,7, 24, 18),
            _item("Wisconsin Mac & Cheese",   "American",  "~10 oz",  740, 38, 21, 0.0,  95,1360,  68,3, 13, 26),
            _item("Thai Green Curry Soup",    "Soups",     "~12 oz",  290, 11,  8, 0.0,  50, 850,  37,3, 10, 14),
            _item("Zoodles (Zucchini) Plain", "American",  "~7 oz",    60,  3,  1, 0.0,   5, 100,   7,2,  5,  4),
            _item("French Baguette",          "Sides",     "~2 oz",   150,  1,  0, 0.0,   0, 280,  29,1,  2,  5),
        ],
    },

    # ──────────────────────────── QDOBA ──────────────────────────────────────
    "qdoba": {
        "chain": dict(name="Qdoba", slug="qdoba",
                      website="https://www.qdoba.com", cuisine_type="Mexican"),
        "items": [
            _item("Grilled Chicken Burrito",  "Burritos",  "~15 oz",  900, 39, 12, 0.5, 115,2270,  89,9, 10, 47),
            _item("3-Cheese Nachos (Chicken)","Nachos",    "~17 oz",  860, 41, 16, 0.5, 130,2380,  84,9,  5, 43),
            _item("Chicken Taco (per taco)",  "Tacos",     "~4 oz",   225,  9,  3, 0.0,  35, 530,  22,2,  2, 14),
            _item("Chicken Bowl",             "Bowls",     "~14 oz",  600, 23,  6, 0.0,  95,1880,  57,7,  6, 37),
            _item("Impossible Fajita Bowl",   "Bowls",     "~14 oz",  570, 21,  6, 0.0,   0,1680,  64,9,  6, 24),
            _item("Queso w/Chips",            "Sides",     "~7 oz",   510, 26,  9, 0.0,  30,1290,  55,5,  3, 17),
            _item("Guacamole (2oz)",          "Sides",     "2 oz",    100, 10,  1, 0.0,   0, 170,   4,3,  1,  1),
        ],
    },

    # ──────────────────────────── JACK IN THE BOX ────────────────────────────
    "jack-in-the-box": {
        "chain": dict(name="Jack in the Box", slug="jack-in-the-box",
                      website="https://www.jackinthebox.com", cuisine_type="Fast Food"),
        "items": [
            _item("Jumbo Jack",               "Burgers",   "~9 oz",   600, 34, 13, 1.0,  80, 730,  45,2,  9, 26),
            _item("Ultimate Cheeseburger",    "Burgers",   "~10 oz",  780, 53, 21, 2.5, 145,1220,  41,2,  9, 42),
            _item("Spicy Chicken Sandwich",   "Chicken",   "~8 oz",   530, 26,  5, 0.0,  55,1070,  49,2,  7, 22),
            _item("Sourdough Jack",           "Burgers",   "~9 oz",   700, 46, 18, 1.0, 100,1200,  34,1,  7, 34),
            _item("Tacos (2pc)",              "Tacos",     "~4 oz",   360, 18,  8, 1.0,  35, 620,  36,4,  2, 12),
            _item("Medium Curly Fries",       "Sides",     "~3.5 oz", 400, 20,  5, 0.0,   0,1120,  51,4,  0,  5),
            _item("Mini Churros (5pc)",       "Desserts",  "~2 oz",   210,  8,  4, 1.5,   0, 190,  30,1, 12,  3),
            _item("Strawberry Shake (Med)",   "Shakes",    "16 fl oz",680, 26, 17, 0.0,  95, 330, 101,0, 82, 11),
        ],
    },

    # ──────────────────────────── WHATABURGER ────────────────────────────────
    "whataburger": {
        "chain": dict(name="Whataburger", slug="whataburger",
                      website="https://whataburger.com", cuisine_type="Fast Food"),
        "items": [
            _item("Whataburger",              "Burgers",   "~9.4 oz", 590, 26, 10, 1.0,  80,1100,  58,2,  9, 30),
            _item("Double Whataburger",       "Burgers",   "~11 oz",  860, 48, 18, 1.5, 155,1310,  59,2, 10, 50),
            _item("Patty Melt",               "Burgers",   "~8.5 oz", 620, 33, 13, 1.0, 100,1130,  50,2,  9, 34),
            _item("Spicy Chicken Sandwich",   "Chicken",   "~7 oz",   510, 22,  5, 0.0,  65,1190,  47,2,  6, 28),
            _item("Taquito w/Cheese (Bkfast)","Breakfast", "~5 oz",   340, 19,  7, 0.0, 225, 770,  26,1,  2, 17),
            _item("Honey Butter Chicken Biscuit","Breakfast","~6 oz", 470, 23,  9, 0.0,  45, 950,  50,1, 10, 17),
            _item("Medium French Fries",      "Sides",     "~3.5 oz", 360, 17,  4, 0.0,   0, 410,  47,3,  0,  5),
            _item("Chocolate Shake (Medium)", "Shakes",    "16 fl oz",750, 17, 11, 0.0,  70, 430, 137,0,110, 14),
            _item("Medium Soft Drink",        "Drinks",    "22 fl oz",210,  0,  0, 0.0,   0,   35, 58, 0, 58,  0),
            _item("Large Soft Drink",         "Drinks",    "32 fl oz",310,  0,  0, 0.0,   0,   50, 86, 0, 86,  0),
            _item("Large Dr Pepper",          "Drinks",    "32 fl oz",310,  0,  0, 0.0,   0,   75, 86, 0, 86,  0),
        ],
    },

    # ──────────────────────────── RED ROBIN ──────────────────────────────────
    "red-robin": {
        "chain": dict(name="Red Robin", slug="red-robin",
                      website="https://www.redrobin.com", cuisine_type="Casual Dining"),
        "items": [
            _item("Gourmet Cheeseburger",     "Burgers",   "~11 oz",  769, 44, 18, 1.5, 165,1095,  40,2, 11, 45),
            _item("Royal Red Robin Burger",   "Burgers",   "~13 oz",  897, 57, 22, 2.0, 425,1153,  41,2, 11, 53),
            _item("Burnin' Love Burger",      "Burgers",   "~11 oz",  873, 56, 21, 2.0, 165,1340,  43,3, 11, 49),
            _item("Clucks & Fries Chicken",   "Chicken",   "~9 oz",   756, 45,  8, 0.0, 125,1565,  46,3,  5, 40),
            _item("California Chicken Wrap",  "Sandwiches","~12 oz",  731, 41,  8, 0.0, 120,1300,  51,5,  7, 40),
            _item("Bottomless Steak Fries",   "Sides",     "~5 oz",   408, 19,  4, 0.0,   0, 566,  55,5,  0,  6),
            _item("Towering Onion Rings",     "Appetizers","~9 oz",   947, 47,  7, 5.0,   0,1291, 120,5, 20,  8),
            _item("Freckled Lemonade",        "Drinks",    "16 fl oz",260,  0,  0, 0.0,   0,  30,  65,1, 63,  0),
            _item("Monster Brownie Sundae",   "Desserts",  "~10 oz", 1410,55, 33, 0.0, 130, 390, 220,5,167, 18),
        ],
    },

    # ──────────────────────────── IHOP ───────────────────────────────────────
    "ihop": {
        "chain": dict(name="IHOP", slug="ihop",
                      website="https://www.ihop.com", cuisine_type="Breakfast"),
        "items": [
            _item("Original Buttermilk Pancakes (3pc)","Pancakes","~7 oz",510, 9, 3, 0.0,  15,1580,  95,2, 14, 11),
            _item("Belgian Waffle",           "Waffles",   "~5 oz",   620, 30, 12, 0.5, 165,1170,  72,2, 12, 16),
            _item("Two x Two x Two",          "Combos",    "~11 oz", 1030, 58, 22, 0.5, 630,2460,  83,3, 15, 47),
            _item("Chicken & Waffles",        "Combos",    "~14 oz", 1170, 59, 17, 0.5, 140,2600, 108,4,  9, 55),
            _item("Country Fried Steak",      "Entrees",   "~14 oz", 1040, 60, 20, 1.5, 115,2940,  87,5, 11, 36),
            _item("Avocado Toast",            "Breakfast", "~9 oz",   550, 25,  7, 0.0,  55,1040,  66,9, 11, 20),
            _item("Big Steak Omelette",       "Omelettes", "~14 oz",  820, 50, 19, 0.5, 885,2310,  35,2,  6, 59),
            _item("Simple & Fit Veggie Omelette","Omelettes","~12 oz",330, 14,  5, 0.0, 545,1060,  23,4,  9, 30),
            _item("Hash Browns",              "Sides",     "~4 oz",   200, 11,  2, 0.0,   0, 540,  22,2,  0,  3),
        ],
    },

    # ──────────────────────────── DENNY'S ────────────────────────────────────
    "dennys": {
        "chain": dict(name="Denny's", slug="dennys",
                      website="https://www.dennys.com", cuisine_type="Breakfast"),
        "items": [
            _item("Grand Slam",               "Slams",     "~12 oz",  710, 35, 12, 0.5, 545,1690,  73,5, 14, 33),
            _item("Original Grand Slam",      "Slams",     "~12 oz",  680, 36, 12, 0.5, 420,1750,  68,4, 12, 29),
            _item("Buttermilk Pancakes (3pc)","Pancakes",  "~6 oz",   420,  6,  2, 0.0,   0,1200,  79,3, 11,  9),
            _item("Moons Over My Hammy",      "Slams",     "~12 oz",  810, 49, 21, 0.5, 585,1960,  53,3,  5, 44),
            _item("Lumberjack Slam",          "Slams",     "~15 oz", 1050, 65, 22, 0.5, 620,2530,  79,5, 13, 47),
            _item("Classic Cheeseburger",     "Burgers",   "~9 oz",   750, 44, 18, 1.0, 120,1520,  45,2,  9, 38),
            _item("Fit Fare Veggie Skillet",  "Skillets",  "~12 oz",  410, 20,  7, 0.0, 410,1230,  36,4,  5, 27),
            _item("Hash Browns",              "Sides",     "~4 oz",   220, 13,  2, 0.0,   0, 500,  23,2,  0,  3),
            _item("French Toast (2 slices)",  "French Toast","~5 oz", 440, 14,  6, 0.0, 110,1020,  66,3, 13, 13),
        ],
    },

    # ──────────────────────────── DUNKIN' ────────────────────────────────────
    "dunkin": {
        "chain": dict(name="Dunkin'", slug="dunkin",
                      website="https://www.dunkindonuts.com", cuisine_type="Coffee / Café"),
        "items": [
            _item("Caramel Macchiato (Med)",  "Hot Drinks","16 fl oz",360, 10,  6, 0.0,  40, 160,  57,0, 53, 12),
            _item("Iced Coffee (Med)",        "Iced Drinks","24 fl oz",310,  9,  5, 0.0,  30, 220,  51,0, 48,  8),
            _item("Cold Brew (Med)",          "Cold Brew","24 fl oz",   30,  0,  0, 0.0,   0,  25,   4,0,  4,  1),
            _item("Glazed Donut",             "Donuts",    "~2 oz",   260, 12,  5, 0.0,   0, 240,  35,1, 15,  3),
            _item("Boston Kreme Donut",       "Donuts",    "~3 oz",   300, 13,  5, 0.0,   0, 300,  40,1, 19,  4),
            _item("Bacon Egg & Cheese Croissant","Sandwiches","~5 oz",500, 29, 14, 0.0, 175,1180,  43,2,  5, 18),
            _item("Bagel w/Cream Cheese",     "Bakery",    "~5 oz",   440, 11,  6, 0.0,  30, 710,  74,3, 11, 14),
            _item("Munchkins Glazed (5pc)",   "Donuts",    "~2 oz",   260, 12,  5, 0.0,   0, 250,  36,1, 17,  3),
            _item("Multigrain Bagel",         "Bakery",    "~4.5 oz", 390,  5,  1, 0.0,   0, 610,  75,5, 10, 14),
        ],
    },

    # ──────────────────────────── CRACKER BARREL ─────────────────────────────
    "cracker-barrel": {
        "chain": dict(name="Cracker Barrel", slug="cracker-barrel",
                      website="https://www.crackerbarrel.com", cuisine_type="Casual Dining"),
        "items": [
            _item("Chicken n' Dumplins",      "Chicken",   "~14 oz",  520, 23,  8, 0.0, 100,1890,  50,3,  7, 31),
            _item("Country Fried Steak",      "Beef",      "~12 oz",  760, 38, 13, 2.0,  95,2620,  74,3,  9, 29),
            _item("Old Timer's Breakfast",    "Breakfast", "~14 oz",  770, 44, 17, 0.5, 615,2340,  61,4, 10, 36),
            _item("Sunrise Sampler",          "Breakfast", "~17 oz",  960, 56, 21, 1.0, 655,2830,  73,4, 14, 46),
            _item("Pancake Breakfast (4pc)",  "Breakfast", "~10 oz",  760, 24,  9, 0.5, 325,1790, 110,4, 23, 24),
            _item("Grilled Chicken",          "Chicken",   "~7 oz",   290,  6,  2, 0.0, 145, 650,   6,0,  2, 52),
            _item("Hashbrown Casserole",      "Sides",     "~8 oz",   350, 19, 10, 0.0,  45, 870,  36,2,  5,  9),
            _item("Turnip Greens",            "Sides",     "~6 oz",    25,  0,  0, 0.0,   0, 260,   3,2,  0,  2),
            _item("Apple Pie",                "Desserts",  "~6 oz",   530, 22,  9, 0.0,  35, 530,  78,2, 43,  5),
        ],
    },

    # ──────────────────────────── OUTBACK STEAKHOUSE ─────────────────────────
    "outback": {
        "chain": dict(name="Outback Steakhouse", slug="outback",
                      website="https://www.outback.com", cuisine_type="Casual Dining"),
        "items": [
            _item("Bloomin' Onion",           "Appetizers","~16 oz", 1950,122, 48, 4.0, 165,3840, 163,12, 22, 22),
            _item("Outback Special (9oz)",    "Steaks",    "~9 oz",   490, 27, 12, 1.5, 155, 620,   1,0,  0, 60),
            _item("Grilled Salmon",           "Seafood",   "~8 oz",   460, 26,  6, 0.0, 120, 660,  10,1,  3, 49),
            _item("Victoria's Filet (6oz)",   "Steaks",    "~6 oz",   260, 11,  5, 0.5, 100, 390,   0,0,  0, 39),
            _item("Chicken on the Barbie",    "Chicken",   "~8 oz",   360, 18,  5, 0.0, 115,1130,  10,1,  2, 42),
            _item("Alice Springs Chicken",    "Chicken",   "~14 oz",  790, 42, 18, 0.0, 195,2020,  30,2,  6, 74),
            _item("Baked Potato",             "Sides",     "~10 oz",  360,  3,  1, 0.0,   5, 225,  77,7,  5,  8),
            _item("Steamed Broccoli",         "Sides",     "~5 oz",    70,  3,  2, 0.0,   5, 270,   7,3,  2,  5),
            _item("Chocolate Thunder Down Under","Desserts","~12 oz",1550,76, 28, 0.0, 115, 800, 206,7,137, 19),
        ],
    },

    # ──────────────────────────── RED LOBSTER ────────────────────────────────
    "red-lobster": {
        "chain": dict(name="Red Lobster", slug="red-lobster",
                      website="https://www.redlobster.com", cuisine_type="Seafood"),
        "items": [
            _item("Cheddar Bay Biscuit",      "Bread",     "~2 oz",   160,  9,  3, 0.0,  20, 380,  16,0,  1,  3),
            _item("Grilled Salmon",           "Seafood",   "~9 oz",   490, 27,  6, 0.0, 160, 570,  10,1,  3, 55),
            _item("Shrimp Linguine Alfredo",  "Pasta",     "~18 oz", 1230,66, 40, 0.0, 325,2270, 100,5, 13, 54),
            _item("Walt's Favorite Shrimp",   "Seafood",   "~9 oz",   490, 25,  5, 0.0, 200, 980,  37,2,  3, 30),
            _item("Lobster & Langostino Pizza","Pizza",    "~12 oz",  630, 28,  8, 0.0, 100,1350,  61,3,  7, 32),
            _item("Wood-Grilled Chicken",     "Chicken",   "~8 oz",   270, 11,  3, 0.0, 150,1040,   2,0,  1, 41),
            _item("New England Clam Chowder (Cup)","Soups","~6 oz",  290, 17,  8, 0.0,  55, 950,  23,1,  4,  9),
            _item("Garlic Shrimp Scampi",     "Seafood",   "~6 oz",   450, 33, 10, 0.0, 245,1510,  12,1,  1, 27),
        ],
    },

    # ──────────────────────────── TGI FRIDAYS ────────────────────────────────
    "tgi-fridays": {
        "chain": dict(name="TGI Fridays", slug="tgi-fridays",
                      website="https://www.tgifridays.com", cuisine_type="Casual Dining"),
        "items": [
            _item("Jack Daniel's Burger",     "Burgers",   "~13 oz",  990, 56, 23, 2.0, 160,1700,  63,3, 26, 54),
            _item("Whiskey-Glazed Chicken",   "Chicken",   "~12 oz",  760, 30, 10, 0.0, 205,2080,  66,2, 38, 54),
            _item("Loaded Potato Skins",      "Appetizers","~9 oz",   750, 43, 20, 0.5, 105,1300,  60,5,  5, 26),
            _item("Mozzarella Sticks",        "Appetizers","~8 oz",   720, 38, 18, 0.5,  85,1890,  61,2,  6, 30),
            _item("Sizzling Chicken & Shrimp","Entrees",   "~16 oz",  870, 46, 17, 0.5, 290,2700,  55,4,  9, 67),
            _item("Strawberry Fields Salad",  "Salads",    "~13 oz",  580, 34, 11, 0.0,  80, 780,  39,5, 25, 29),
            _item("Brownie Obsession",        "Desserts",  "~7 oz",   1110,54, 30, 0.0,  80, 600, 146,4,100, 14),
        ],
    },

    # ──────────────────────────── BOB EVANS ──────────────────────────────────
    "bob-evans": {
        "chain": dict(name="Bob Evans", slug="bob-evans",
                      website="https://www.bobevans.com", cuisine_type="Breakfast"),
        "items": [
            _item("Farmer's Choice Breakfast","Breakfast", "~14 oz",  840, 50, 18, 0.5, 620,2130,  63,4, 11, 40),
            _item("Buttermilk Hotcakes (3pc)","Hotcakes",  "~8 oz",   580, 13,  3, 0.0,  25,1290,  98,3, 25, 15),
            _item("Country Fried Chicken",    "Chicken",   "~12 oz",  710, 38, 10, 1.0, 130,1690,  60,3,  6, 34),
            _item("Pot Roast Dinner",         "Beef",      "~14 oz",  490, 18,  7, 0.0, 125,2060,  43,4,  8, 38),
            _item("Grilled Chicken Salad",    "Salads",    "~12 oz",  400, 19,  6, 0.0, 115,1280,  20,4,  8, 43),
            _item("Mashed Potatoes",          "Sides",     "~6 oz",   190,  9,  5, 0.0,  25, 580,  23,2,  2,  4),
            _item("Biscuits & Gravy",         "Breakfast", "~8 oz",   480, 24, 10, 0.5,  35,1650,  55,2,  4, 13),
        ],
    },

    # ──────────────────────────── HARDEE'S ───────────────────────────────────
    "hardees": {
        "chain": dict(name="Hardee's", slug="hardees",
                      website="https://www.hardees.com", cuisine_type="Fast Food"),
        "items": [
            _item("Monster Thickburger",      "Burgers",   "~10.7 oz",1320,95, 37, 3.0, 245,1880,  45,2,  9, 71),
            _item("Original Thickburger",     "Burgers",   "~8 oz",   710, 43, 16, 1.5, 115, 960,  45,2,  9, 35),
            _item("Big Chicken Fillet",       "Chicken",   "~7.5 oz", 670, 33,  7, 0.0,  75,1490,  61,3,  8, 33),
            _item("Made from Scratch Biscuit","Breakfast", "~3.7 oz", 370, 19,  8, 0.0,   0, 910,  43,1,  4,  6),
            _item("Bacon, Egg & Cheese Biscuit","Breakfast","~6.5 oz",560, 33, 15, 0.0, 250,1440,  43,1,  4, 21),
            _item("Medium Natural-Cut Fries", "Sides",     "~3.5 oz", 330, 14,  3, 0.0,   0, 390,  47,4,  0,  4),
            _item("Hand-Scooped Chocolate Shake (Med)","Shakes","16 fl oz",680, 29, 19, 0.0, 100, 530, 92,0, 81, 14),
        ],
    },

    # ──────────────────────────── DEL TACO ───────────────────────────────────
    "del-taco": {
        "chain": dict(name="Del Taco", slug="del-taco",
                      website="https://www.deltaco.com", cuisine_type="Mexican"),
        "items": [
            _item("Classic Chicken Burrito",  "Burritos",  "~8.5 oz", 530, 21,  6, 0.0,  75,1250,  56,5,  4, 29),
            _item("Carne Asada Burrito",      "Burritos",  "~10 oz",  580, 23,  8, 0.5, 100,1520,  58,4,  4, 38),
            _item("Crispy Chicken Taco",      "Tacos",     "~3.8 oz", 290, 15,  4, 0.0,  30, 570,  28,3,  2, 12),
            _item("Epic Shrimp Taco",         "Tacos",     "~4 oz",   200,  9,  2, 0.0,  45, 510,  22,2,  3, 10),
            _item("Bean & Cheese Burrito",    "Burritos",  "~6.5 oz", 430, 14,  6, 0.0,  25,1050,  58,8,  3, 15),
            _item("Crinkle Cut Fries (Reg)",  "Sides",     "~3 oz",   260, 11,  2, 0.0,   0, 440,  37,3,  0,  4),
            _item("Chocolate Shake (Small)",  "Shakes",    "12 fl oz",540, 19, 13, 0.0,  70, 370,  81,0, 74, 11),
        ],
    },

    # ──────────────────────────── EL POLLO LOCO ──────────────────────────────
    "el-pollo-loco": {
        "chain": dict(name="El Pollo Loco", slug="el-pollo-loco",
                      website="https://www.elpolloloco.com", cuisine_type="Mexican"),
        "items": [
            _item("Fire-Grilled Chicken Breast","Chicken", "~6 oz",   190,  7,  2, 0.0, 110, 640,   0,0,  0, 33),
            _item("Chicken Avocado Burrito",  "Burritos",  "~12 oz",  740, 33, 10, 0.0, 130,1560,  73,8,  5, 38),
            _item("Pollo Bowl",               "Bowls",     "~14 oz",  570, 17,  3, 0.0, 110,1450,  65,8,  4, 39),
            _item("Chicken Taco (per taco)",  "Tacos",     "~4 oz",   190,  7,  2, 0.0,  50, 460,  18,2,  1, 14),
            _item("Avocado Salad",            "Salads",    "~13 oz",  490, 31,  7, 0.0, 100,1350,  29,7,  5, 31),
            _item("Pinto Beans",              "Sides",     "~5 oz",   170,  2,  0, 0.0,   0, 710,  28,9,  1,  9),
            _item("Chips & Guacamole",        "Sides",     "~5 oz",   380, 22,  3, 0.0,   0, 530,  41,5,  1,  5),
        ],
    },

    # ──────────────────────────── LONGHORN STEAKHOUSE ────────────────────────
    "longhorn": {
        "chain": dict(name="LongHorn Steakhouse", slug="longhorn",
                      website="https://www.longhornsteakhouse.com", cuisine_type="Casual Dining"),
        "items": [
            _item("Flo's Filet (7oz)",        "Steaks",    "~7 oz",   290, 14,  6, 0.0, 115, 630,   2,0,  0, 40),
            _item("Outlaw Ribeye (18oz)",      "Steaks",    "~18 oz", 1110,69, 27, 2.0, 300,1510,   3,0,  0,116),
            _item("Cowboy Pork Chops",        "Pork",      "~12 oz",  670, 42, 15, 0.0, 195,1900,  16,0, 13, 55),
            _item("Grilled Chicken & Strawberry Salad","Salads","~14 oz",510, 26, 11, 0.0, 105, 830, 31,4, 22, 40),
            _item("Fire-Grilled Corn on the Cob","Sides",  "~5 oz",  160,  6,  1, 0.0,   5, 190,  24,3,  8,  4),
            _item("Seasoned Rice",            "Sides",     "~5 oz",   190,  3,  1, 0.0,   0, 530,  35,1,  0,  5),
            _item("LongHorn Salmon",          "Seafood",   "~8 oz",   580, 37,  7, 0.0, 140, 990,  18,2,  8, 50),
            _item("Chocolate Stampede",       "Desserts",  "~14 oz", 1790,87, 45, 0.5, 200,1020, 239,8,164, 25),
        ],
    },

    # ──────────────────────────── IN-N-OUT BURGER ────────────────────────────
    "in-n-out": {
        "chain": dict(name="In-N-Out Burger", slug="in-n-out",
                      website="https://www.in-n-out.com", cuisine_type="Fast Food"),
        "items": [
            _item("Hamburger",                "Burgers",   "~7.8 oz", 390, 19,  5, 0.0,  40, 650,  39,3,  5, 16),
            _item("Cheeseburger",             "Burgers",   "~8.6 oz", 480, 27,  9, 0.0,  60, 1000,  39,3,  5, 22),
            _item("Double-Double",            "Burgers",   "~10.8 oz",670, 41, 18, 0.0, 120,1440,  39,3,  5, 37),
            _item("Animal Style Burger",      "Burgers",   "~9.5 oz", 660, 43, 17, 0.0,  95,1050,  39,3, 10, 27),
            _item("French Fries",             "Fries",     "~5 oz",   395, 18,  5, 0.0,   0, 245,  54,2,  0,  7),
            _item("Animal Style Fries",       "Fries",     "~7 oz",   750, 46, 17, 0.0,  85, 510,  59,3,  7, 14),
            _item("Chocolate Shake",          "Shakes",    "15 fl oz",590, 29, 19, 0.0, 100, 360,  73,0, 68, 12),
            _item("Strawberry Shake",         "Shakes",    "15 fl oz",690, 27, 19, 0.0,  95, 290,  98,0, 92, 11),
            _item("Grilled Cheese",           "Burgers",   "~6 oz",   380, 22,  8, 0.0,  40, 670,  30,2,  6, 13),
            _item("Protein Style (no bun)",   "Burgers",   "~7 oz",   240, 17,  9, 0.0,  60, 370,   8,3,  5, 13),
        ],
    },

    # ──────────────────────────── PIZZA HUT ──────────────────────────────────
    "pizza-hut": {
        "chain": dict(name="Pizza Hut", slug="pizza-hut",
                      website="https://www.pizzahut.com", cuisine_type="Pizza"),
        "items": [
            _item("Pepperoni Pizza Hand Tossed (1 slice, Med)","Pizza","~3.8 oz",290,13, 6, 0.0, 35, 640, 31,2, 3, 14),
            _item("Cheese Pizza Hand Tossed (1 slice, Med)",  "Pizza","~3.6 oz",240, 9, 5, 0.0, 25, 500, 30,2, 3, 12),
            _item("Supreme Pizza Pan (1 slice, Med)",          "Pizza","~4.7 oz",360,18, 7, 0.0, 45, 760, 33,2, 4, 16),
            _item("BBQ Chicken Pizza (1 slice, Med)",          "Pizza","~4.3 oz",280, 9, 4, 0.0, 40, 580, 33,2, 7, 16),
            _item("Stuffed Crust Pepperoni (1 slice, Med)",    "Pizza","~4.9 oz",370,16, 8, 0.0, 40, 760, 37,2, 3, 18),
            _item("Breadstick (1pc)",          "Sides",     "~1.4 oz", 140,  5,  1, 0.0,  0, 220,  20,1, 1,  4),
            _item("WingStreet Bone-In (2pc)",  "Wings",     "~2.5 oz", 180, 12,  4, 0.0, 75, 360,   5,0, 1, 13),
            _item("Cinnabon Mini Rolls (2pc)", "Desserts",  "~2.3 oz", 170,  6,  2, 0.0,  5, 170,  26,0,12,  3),
        ],
    },

    # ──────────────────────────── DOMINO'S ───────────────────────────────────
    "dominos": {
        "chain": dict(name="Domino's", slug="dominos",
                      website="https://www.dominos.com", cuisine_type="Pizza"),
        "items": [
            _item("Pepperoni Pizza Hand Tossed (1 slice, Med)","Pizza","~2.7 oz",200, 8, 3, 0.0, 20, 430, 23,1, 2, 10),
            _item("Cheese Pizza Thin (1 slice, Med)",          "Pizza","~1.9 oz",150, 6, 3, 0.0, 15, 360, 16,1, 1,  7),
            _item("ExtravaganZZa (1 slice, Med)",              "Pizza","~3.8 oz",260,12, 5, 0.0, 35, 590, 26,1, 3, 13),
            _item("Pacific Veggie (1 slice, Med)",             "Pizza","~3.4 oz",220, 8, 4, 0.0, 20, 460, 27,1, 3, 10),
            _item("Parmesan Bread Bites (16pc)","Bread",       "~4 oz",  370, 14, 4, 0.0,  0, 700, 48,2, 4, 12),
            _item("Cheesy Bread (2 pc)",        "Bread",       "~2 oz",  170,  8, 3, 0.0, 10, 290, 18,1, 1,  7),
            _item("Chocolate Lava Crunch (1pc)","Desserts",    "~1.7 oz",340, 20,12, 0.0, 30, 240, 39,1,24,  4),
            _item("Boneless Chicken (8pc)",     "Chicken",     "~5 oz",  410, 18, 4, 0.0, 60,1020, 38,2, 4, 22),
        ],
    },

    # ──────────────────────────── LITTLE CAESARS ─────────────────────────────
    "little-caesars": {
        "chain": dict(name="Little Caesars", slug="little-caesars",
                      website="https://littlecaesars.com", cuisine_type="Pizza"),
        "items": [
            _item("Hot-N-Ready Pepperoni (1 slice)","Pizza","~2.8 oz",280,12, 5, 0.0, 25, 570, 29,1, 3, 13),
            _item("Hot-N-Ready Cheese (1 slice)",   "Pizza","~2.6 oz",250,10, 4, 0.0, 20, 480, 28,1, 3, 11),
            _item("Deep! Deep! Dish Pepperoni (1 slice)","Pizza","~3.9 oz",350,16,7, 0.0, 35, 760, 34,2, 3, 17),
            _item("ExtraMostBestest Pepperoni (1 slice)","Pizza","~3.4 oz",320,14,7, 0.0, 35, 720, 30,1, 3, 16),
            _item("Crazy Bread (1 pc)",         "Bread",       "~1.4 oz", 90,  3, 1, 0.0,  0, 160, 13,0, 0,  3),
            _item("Italian Cheese Bread (1 pc)","Bread",       "~2.0 oz",160,  8, 3, 0.0, 10, 330, 17,0, 1,  6),
            _item("Caesar Wings Buffalo (4pc)", "Wings",       "~3.8 oz",280, 18, 5, 0.0, 85, 920, 12,0, 1, 19),
            _item("Stuffed Crazy Bread (1 pc)", "Bread",       "~2.5 oz",170,  7, 3, 0.0,  5, 340, 21,1, 1,  7),
        ],
    },

    # ──────────────────────────── PAPA JOHN'S ────────────────────────────────
    "papa-johns": {
        "chain": dict(name="Papa John's", slug="papa-johns",
                      website="https://www.papajohns.com", cuisine_type="Pizza"),
        "items": [
            _item("Pepperoni Original (1 slice, Med)","Pizza","~2.8 oz",300,14, 6, 0.0, 30, 680, 30,1, 3, 13),
            _item("Cheese Original (1 slice, Med)",   "Pizza","~2.7 oz",260,11, 5, 0.0, 25, 560, 30,1, 3, 11),
            _item("The Works (1 slice, Med)",          "Pizza","~3.9 oz",330,15, 6, 0.0, 35, 770, 32,2, 4, 14),
            _item("BBQ Chicken & Bacon (1 slice, Med)","Pizza","~3.7 oz",330,14, 5, 0.0, 45, 730, 33,1, 6, 16),
            _item("Garlic Parmesan Breadsticks","Sides","~3.8 oz",       290, 8, 2, 0.0,  0, 620, 42,2, 2,  9),
            _item("Buffalo Wings (5pc)",        "Wings",       "~5 oz",  380, 26, 8, 0.0,120,1360, 14,0, 2, 23),
            _item("Double Chocolate Chip Brownie","Desserts","~3 oz",    430, 20, 9, 0.5, 45, 300, 60,2,38,  5),
        ],
    },

    # ──────────────────────────── ZAXBY'S ────────────────────────────────────
    "zaxbys": {
        "chain": dict(name="Zaxby's", slug="zaxbys",
                      website="https://www.zaxbys.com", cuisine_type="Fast Food"),
        "items": [
            _item("Chicken Fingerz (5pc)",    "Fingerz",   "~5 oz",   430, 21,  4, 0.0,  95, 900,  25,1,  1, 37),
            _item("The Signature Sandwich",   "Sandwiches","~8 oz",   640, 37,  8, 0.0,  90,1700,  42,2,  7, 34),
            _item("Buffalo Blue Cheese Salad","Salads",    "~13 oz",  670, 41, 10, 0.0, 130,2440,  35,5,  7, 40),
            _item("Boneless Wings (6pc)",     "Wings",     "~6 oz",   410, 21,  4, 0.0,  80,1660,  27,1,  3, 27),
            _item("Crinkle Fries (Regular)",  "Sides",     "~4 oz",   320, 15,  3, 0.0,   0, 780,  42,4,  0,  5),
            _item("Tongue Torch Sauce",       "Sauces",    "1.5 oz",   25,  0,  0, 0.0,   0, 870,   6,0,  4,  0),
            _item("Chocolate Cake",           "Desserts",  "~4 oz",   600, 29, 14, 0.0,  80, 520,  83,2, 56,  7),
        ],
    },

    # ──────────────────────────── JERSEY MIKE'S (already above) ──────────────
    # ──────────────────────────── DOMINO'S (already above) ───────────────────

}  # end SEED dict
