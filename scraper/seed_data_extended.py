"""
Extended seed data — adds comprehensive menu items to existing chains.
Run:  python main.py --seed-extended
Items are upserted, so re-running is safe.
"""
from base_scraper import MenuItemData

def _item(name, cat, sz, cal, fat, sat, trans, chol, sod, carb, fiber, sug, prot):
    return MenuItemData(
        name=name, category=cat, serving_size=sz,
        calories=cal, total_fat_g=fat, saturated_fat_g=sat, trans_fat_g=trans,
        cholesterol_mg=chol, sodium_mg=sod, total_carbs_g=carb,
        dietary_fiber_g=fiber, total_sugars_g=sug, protein_g=prot,
    )

EXTENDED: dict[str, dict] = {

    # ── ARBY'S ───────────────────────────────────────────────────────────────
    "arbys": {
        "chain": dict(name="Arby's", slug="arbys",
                      website="https://arbys.com", cuisine_type="Fast Food"),
        "items": [
            _item("Junior Roast Beef",            "Sandwiches","2.9 oz",  210,  8,  2, 0.5,  40,  530, 24, 1,  4, 12),
            _item("Mid Roast Beef",               "Sandwiches","5.0 oz",  410, 17,  6, 0.5,  75, 1110, 40, 2,  7, 26),
            _item("Max Roast Beef",               "Sandwiches","7.7 oz",  490, 21,  8, 0.5,  90, 1340, 43, 2,  8, 32),
            _item("Double Beef 'n Cheddar",       "Sandwiches","7.0 oz",  560, 27, 10, 1.0, 115, 1760, 51, 2,  8, 33),
            _item("Beef 'n Cheddar Mid",          "Sandwiches","7.0 oz",  540, 25,  9, 0.5, 105, 1780, 49, 2, 11, 30),
            _item("Smokehouse Brisket",           "Sandwiches","~8 oz",   610, 32, 10, 1.0, 110, 1640, 49, 2, 11, 31),
            _item("Classic Greek Gyro",           "Gyros",     "~8 oz",   710, 41, 14, 1.0, 125, 1960, 52, 3,  5, 34),
            _item("Roast Turkey Gyro",            "Gyros",     "~8 oz",   470, 18,  6, 0.0, 100, 1590, 50, 3,  5, 32),
            _item("Reuben",                       "Sandwiches","~9 oz",   690, 38, 13, 0.0, 130, 2490, 44, 3,  5, 41),
            _item("Turkey Club",                  "Market Fresh","~11 oz",720, 37, 10, 0.0, 115, 2020, 60, 3,  8, 38),
            _item("Roast Turkey & Swiss",         "Market Fresh","~10 oz",470, 17,  6, 0.0,  95, 1390, 42, 3,  7, 37),
            _item("Pecan Chicken Salad Sandwich", "Market Fresh","~10 oz",800, 44, 10, 0.0,  95, 1010, 66, 4, 22, 33),
            _item("Crispy Chicken Sandwich",      "Chicken",   "~7 oz",   550, 24,  5, 0.0,  60, 1360, 52, 3,  6, 30),
            _item("Spicy Crispy Chicken",         "Chicken",   "~7 oz",   560, 24,  5, 0.0,  60, 1680, 53, 3,  6, 30),
            _item("Chicken Cordon Bleu",          "Chicken",   "~9 oz",   570, 25,  8, 0.0, 100, 1470, 49, 2,  8, 38),
            _item("Buttermilk Chicken Sandwich",  "Chicken",   "~8 oz",   620, 28,  7, 0.0,  90, 1560, 55, 3,  7, 37),
            _item("5pc Chicken Tenders",          "Chicken",   "~6 oz",   550, 25,  5, 0.0,  60, 1390, 43, 2,  0, 33),
            _item("Small Curly Fries",            "Sides",     "~2.7 oz", 290, 14,  3, 0.0,   0,  700, 40, 4,  0,  4),
            _item("Large Curly Fries",            "Sides",     "~7 oz",   640, 31,  6, 0.0,   0, 1900, 84, 7,  0,  8),
            _item("Small Crinkle Fries",          "Sides",     "~3 oz",   305, 13,  3, 0.0,   0,  660, 46, 4,  0,  4),
            _item("Mozzarella Sticks (4pc)",      "Sides",     "~4 oz",   430, 23, 10, 0.0,  30,  720, 38, 2,  4, 18),
            _item("Jalapeño Bites (5pc)",         "Sides",     "~3 oz",   340, 20,  9, 0.0,  30,  720, 29, 1,  4, 13),
            _item("Potato Cakes (2pc)",           "Sides",     "~2.6 oz", 230, 13,  2, 0.0,   0,  490, 27, 3,  0,  2),
            _item("Side Salad",                   "Sides",     "~3 oz",    70,  3,  1, 0.0,   5,  100,  8, 2,  4,  3),
            _item("Mac 'N Cheese",                "Sides",     "~4 oz",   390, 14,  8, 0.0,  40,  780, 53, 2,  7, 14),
            _item("Apple Turnover",               "Desserts",  "~3.4 oz", 380, 16,  8, 0.0,   0,  310, 55, 2, 27,  4),
            _item("Cherry Turnover",              "Desserts",  "~3.4 oz", 360, 16,  8, 0.0,   0,  310, 52, 2, 24,  4),
            _item("Vanilla Shake (Small)",        "Desserts",  "12 fl oz",475, 12,  8, 0.0,  45,  330, 70, 0, 58, 11),
            _item("Chocolate Shake (Small)",      "Desserts",  "12 fl oz",520, 12,  8, 0.0,  45,  340, 78, 1, 65, 11),
            _item("Strawberry Shake (Small)",     "Desserts",  "12 fl oz",495, 12,  8, 0.0,  45,  320, 74, 0, 62, 11),
        ],
    },

    # ── McDONALD'S ───────────────────────────────────────────────────────────
    "mcdonalds": {
        "chain": dict(name="McDonald's", slug="mcdonalds",
                      website="https://www.mcdonalds.com", cuisine_type="Fast Food"),
        "items": [
            _item("Double Quarter Pounder w/Cheese","Burgers","~9.8 oz", 740, 42, 19, 2.0, 175, 1360, 43, 2, 10, 48),
            _item("McDouble",                     "Burgers",   "~5.4 oz", 400, 20,  8, 1.0,  65,  920, 35, 2,  7, 22),
            _item("Double Cheeseburger",           "Burgers",   "~6.2 oz", 450, 24, 11, 1.0,  85, 1050, 35, 2,  7, 26),
            _item("Hamburger",                     "Burgers",   "~3.5 oz", 250, 9,   3, 0.5,  30,  510, 31, 1,  6, 12),
            _item("Cheeseburger",                  "Burgers",   "~4 oz",   300, 13,  6, 0.5,  45,  680, 32, 1,  7, 15),
            _item("McRib",                         "Burgers",   "~6.7 oz", 480, 22,  8, 0.0,  70, 1100, 45, 3, 11, 24),
            _item("Spicy McChicken",               "Chicken",   "~5.2 oz", 400, 17,  3, 0.0,  40,  750, 42, 2,  5, 15),
            _item("Buttermilk Crispy Chicken Tenders (4pc)","Chicken","~6 oz",490,23,4,0.0,  75,  970, 41, 2,  1, 27),
            _item("6pc Chicken McNuggets",         "Chicken",   "~3.6 oz", 250, 15,  2, 0.0,  45,  530, 16, 1,  0, 13),
            _item("20pc Chicken McNuggets",        "Chicken",   "~12 oz",  830, 49,  8, 0.0, 150, 1770, 52, 2,  0, 44),
            _item("Large French Fries",            "Sides",     "~5.4 oz", 490, 23,  3, 0.0,   0,  610, 66, 6,  0,  7),
            _item("Apple Slices",                  "Sides",     "~1.2 oz",  15,  0,  0, 0.0,   0,    0,  4, 0,  3,  0),
            _item("Southwest Grilled Chicken Salad","Salads",   "~12 oz",  350, 11,  4, 0.0,  80,  860, 27, 6,  7, 37),
            _item("Fruit & Maple Oatmeal",         "Breakfast", "~9.9 oz", 320,  4,  1, 0.0,   0,  150, 64, 4, 32,  5),
            _item("Bacon Egg & Cheese Biscuit",    "Breakfast", "~5.4 oz", 460, 26, 10, 0.0, 205, 1270, 36, 1,  3, 20),
            _item("Sausage Biscuit",               "Breakfast", "~3.8 oz", 430, 27,  9, 0.0,  35, 1010, 34, 1,  3, 11),
            _item("Sausage Burrito",               "Breakfast", "~3.9 oz", 300, 16,  6, 0.0, 185,  730, 26, 1,  2, 12),
            _item("Hotcakes & Sausage",            "Breakfast", "~8.4 oz", 780, 31, 12, 0.5, 100, 1100,104, 3, 46, 18),
            _item("Hot Caramel Sundae",            "Desserts",  "~6 oz",   340,  8,  5, 0.0,  30,  160, 61, 0, 43,  8),
            _item("Hot Fudge Sundae",              "Desserts",  "~6.1 oz", 330,  8,  5, 0.0,  30,  170, 56, 1, 40,  8),
            _item("Baked Apple Pie",               "Desserts",  "~2.7 oz", 240, 11,  5, 0.0,   0,  160, 34, 1, 13,  2),
        ],
    },

    # ── BURGER KING ──────────────────────────────────────────────────────────
    "burger-king": {
        "chain": dict(name="Burger King", slug="burger-king",
                      website="https://www.bk.com", cuisine_type="Fast Food"),
        "items": [
            _item("Triple Whopper",               "Burgers",   "~16.5 oz",1140,75, 27, 2.0, 225, 1110, 49, 2, 11, 67),
            _item("Bacon Whopper",                "Burgers",   "~11.3 oz", 790, 50, 15, 1.5, 120, 1170, 49, 2, 11, 35),
            _item("Impossible Whopper",           "Burgers",   "~9.9 oz",  630, 34, 11, 0.0,  10, 1080, 58, 4, 12, 25),
            _item("Big Fish Sandwich",            "Fish",      "~7.5 oz",  510, 27,  5, 0.0,  55, 1110, 47, 3,  7, 19),
            _item("Bacon Egg & Cheese Croissan'wich","Breakfast","~6.5 oz",490,31,13, 0.0, 200, 1080, 27, 1,  5, 20),
            _item("Sausage Egg & Cheese Croissan'wich","Breakfast","~7 oz",600,42,16, 0.0, 235, 1180, 27, 1,  5, 22),
            _item("French Toast Sticks (5pc)",    "Breakfast", "~3.2 oz",  310, 14,  3, 2.5,   0,  390, 41, 2, 14,  5),
            _item("Spicy Crispy Chicken Sandwich","Chicken",   "~8.1 oz",  700, 42, 10, 0.0,  75, 1430, 49, 3,  7, 29),
            _item("Tendercrisp Chicken Sandwich", "Chicken",   "~8.2 oz",  700, 38,  8, 0.0,  75, 1180, 57, 3,  7, 26),
            _item("8pc Chicken Nuggets",          "Chicken",   "~3.7 oz",  230, 14,  3, 0.0,  25,  610, 14, 1,  0, 11),
            _item("Large French Fries",           "Sides",     "~5.5 oz",  500, 25,  6, 0.0,   0,  630, 64, 4,  0,  6),
            _item("Small French Fries",           "Sides",     "~2.5 oz",  230, 11,  3, 0.0,   0,  290, 29, 2,  0,  3),
            _item("Large Onion Rings",            "Sides",     "~5.8 oz",  620, 33,  7, 7.0,   0, 1020, 73, 3, 10,  7),
            _item("Mozzarella Sticks (4pc)",      "Sides",     "~3.6 oz",  340, 19,  8, 0.0,  30,  640, 26, 1,  4, 16),
            _item("Chocolate Fudge Sundae",       "Desserts",  "~4.7 oz",  300,  7,  4, 0.0,  20,  135, 53, 1, 38,  6),
        ],
    },

    # ── WENDY'S ──────────────────────────────────────────────────────────────
    "wendys": {
        "chain": dict(name="Wendy's", slug="wendys",
                      website="https://www.wendys.com", cuisine_type="Fast Food"),
        "items": [
            _item("Son of Baconator",             "Burgers",   "~7.4 oz",  660, 39, 17, 1.5, 130, 1200, 36, 1,  8, 36),
            _item("Jr. Hamburger",                "Burgers",   "~4 oz",    250, 9,   3, 0.0,  40,  490, 26, 1,  5, 14),
            _item("Pretzel Bacon Pub Burger",     "Burgers",   "~10.8 oz", 920, 55, 22, 2.5, 155, 1520, 58, 2, 11, 48),
            _item("Grilled Chicken Wrap",         "Chicken",   "~7.5 oz",  290,  8,  2, 0.0,  65,  750, 26, 1,  3, 28),
            _item("Crispy Chicken Wrap",          "Chicken",   "~7.5 oz",  410, 19,  4, 0.0,  50,  870, 37, 1,  3, 20),
            _item("Spicy Chicken Sandwich",       "Chicken",   "~7.7 oz",  530, 25,  5, 0.0,  75, 1210, 47, 2,  6, 28),
            _item("Grilled Asiago Ranch Chicken", "Chicken",   "~8.2 oz",  570, 28,  8, 0.0, 125, 1420, 38, 2,  6, 40),
            _item("10pc Crispy Chicken Nuggets",  "Chicken",   "~5 oz",    450, 27,  5, 0.0,  55, 1060, 31, 1,  0, 18),
            _item("Small Frosty (Chocolate)",     "Frosty",    "12 fl oz", 340,  9,  6, 0.0,  40,  150, 57, 0, 42,  8),
            _item("Large Frosty (Chocolate)",     "Frosty",    "20 fl oz", 580, 14, 10, 0.0,  60,  250, 97, 0, 70, 12),
            _item("Large French Fries",           "Sides",     "~6 oz",    540, 26,  5, 0.0,   0,  700, 72, 5,  0,  7),
            _item("Small French Fries",           "Sides",     "~3 oz",    280, 13,  3, 0.0,   0,  370, 37, 3,  0,  4),
            _item("Taco Salad",                   "Salads",    "~15 oz",   680, 34, 14, 1.0, 100, 1480, 61, 8, 10, 34),
            _item("Parmesan Caesar Salad",        "Salads",    "~9 oz",    450, 28, 10, 0.0,  85, 1040, 20, 3,  5, 32),
            _item("Sour Cream & Chive Potato",    "Sides",     "~10 oz",   420, 13,  8, 0.0,  25,  440, 66, 7,  5, 10),
        ],
    },

    # ── CHICK-FIL-A ──────────────────────────────────────────────────────────
    "chick-fil-a": {
        "chain": dict(name="Chick-fil-A", slug="chick-fil-a",
                      website="https://www.chick-fil-a.com", cuisine_type="Fast Food"),
        "items": [
            _item("Spicy Deluxe Sandwich",        "Sandwiches","~8.4 oz",  550, 26,  7, 0.0, 100, 1650, 44, 2,  8, 33),
            _item("Grilled Nuggets (12pc)",        "Nuggets",   "~5.3 oz",  200,  4,  2, 0.0, 125,  790,  4, 0,  2, 37),
            _item("Chick-n-Strips (3pc)",          "Strips",    "~4.4 oz",  330, 15,  3, 0.0,  70,  890, 22, 1,  1, 30),
            _item("Chick-n-Strips (4pc)",          "Strips",    "~5.9 oz",  440, 20,  4, 0.0,  95, 1190, 30, 1,  1, 40),
            _item("Cool Wrap (Grilled)",           "Wraps",     "~11 oz",   350, 14,  5, 0.0, 110, 1040, 29, 3,  4, 34),
            _item("Cool Wrap (Crispy)",            "Wraps",     "~11 oz",   580, 25,  8, 0.0,  70, 1550, 52, 3,  5, 33),
            _item("Cobb Salad (Grilled Chicken)",  "Salads",    "~15 oz",   430, 24,  8, 0.0, 180,  910, 19, 4,  7, 38),
            _item("Spicy Southwest Salad",         "Salads",    "~14 oz",   450, 21,  6, 0.0, 120, 1180, 35, 7, 14, 33),
            _item("Side Salad",                    "Sides",     "~3.5 oz",   80,  5,  2, 0.0,  15,  110,  6, 2,  4,  5),
            _item("Mac & Cheese (Large)",          "Sides",     "~8 oz",    690, 41, 19, 0.0,  95, 1460, 59, 2,  7, 25),
            _item("Chicken Tortilla Soup (Med)",   "Soups",     "~11 oz",   260, 10,  3, 0.0,  65, 1160, 26, 3,  5, 22),
            _item("Hash Brown Scramble Burrito",   "Breakfast", "~9.7 oz",  700, 34, 14, 0.0, 480, 1380, 63, 3,  4, 37),
            _item("Egg White Grill",               "Breakfast", "~6.9 oz",  300,  7,  3, 0.0, 260, 970,  28, 1,  5, 26),
            _item("Sausage Biscuit",               "Breakfast", "~4.4 oz",  500, 28, 11, 0.0,  40, 1100, 47, 2,  4, 15),
            _item("Greek Yogurt Parfait",          "Breakfast", "~6.9 oz",  230,  3,  1, 0.0,  10,   80, 43, 1, 32, 12),
            _item("Brownie",                       "Desserts",  "~3.2 oz",  370, 19, 11, 0.0,  55,  200, 47, 2, 31,  4),
        ],
    },

    # ── KFC ──────────────────────────────────────────────────────────────────
    "kfc": {
        "chain": dict(name="KFC", slug="kfc",
                      website="https://www.kfc.com", cuisine_type="Fast Food"),
        "items": [
            _item("Original Recipe Drumstick",    "Chicken",   "~3 oz",    150,  8,  2, 0.0,  75,  400,  4, 0,  0, 17),
            _item("Original Recipe Wing",         "Chicken",   "~1.7 oz",  130,  8,  2, 0.0,  60,  330,  4, 0,  0, 11),
            _item("Extra Crispy Thigh",           "Chicken",   "~4.4 oz",  380, 26,  6, 0.0,  95,  740,  9, 0,  0, 27),
            _item("Extra Crispy Drumstick",       "Chicken",   "~2.4 oz",  190, 11,  3, 0.0,  60,  390,  8, 0,  0, 15),
            _item("Kentucky Grilled Breast",      "Grilled",   "~5.6 oz",  210,  7,  2, 0.0, 130,  710,  0, 0,  0, 38),
            _item("Kentucky Grilled Thigh",       "Grilled",   "~3.8 oz",  160,  8,  2, 0.0,  95,  540,  0, 0,  0, 21),
            _item("8pc Chicken Nuggets",          "Nuggets",   "~4 oz",    260, 16,  3, 0.0,  35,  690, 14, 1,  0, 14),
            _item("Popcorn Chicken (Small)",      "Chicken",   "~3.5 oz",  370, 22,  5, 0.0,  50, 1090, 26, 1,  1, 17),
            _item("KFC Wrap",                     "Sandwiches","~6.8 oz",  490, 23,  5, 0.0,  55, 1300, 49, 2,  5, 24),
            _item("Corn on the Cob",              "Sides",     "~5.7 oz",  140,  3,  0, 0.0,   0,   0,  26, 2,  5,  4),
            _item("Green Beans",                  "Sides",     "~4.6 oz",   25,  0,  0, 0.0,   0,  260,   4, 2,  2,  1),
            _item("Coleslaw",                     "Sides",     "~4 oz",    150,  9,  1, 0.0,   0,  160,  17, 2,  7,  1),
            _item("Potato Wedges (Small)",        "Sides",     "~3 oz",    290, 14,  3, 0.0,   0,  740,  38, 4,  2,  5),
        ],
    },

    # ── TACO BELL ────────────────────────────────────────────────────────────
    "taco-bell": {
        "chain": dict(name="Taco Bell", slug="taco-bell",
                      website="https://www.tacobell.com", cuisine_type="Mexican"),
        "items": [
            _item("Soft Taco Supreme",            "Tacos",     "~4.5 oz",  210, 10,  4, 0.0,  35,  560, 20, 2,  3, 10),
            _item("Crunchy Taco Supreme",         "Tacos",     "~3.8 oz",  200, 11,  4, 0.0,  30,  390, 15, 3,  2,  9),
            _item("Spicy Potato Soft Taco",       "Tacos",     "~4.6 oz",  230,  9,  2, 0.0,   0,  460, 31, 4,  2,  5),
            _item("Doritos Locos Taco Supreme",   "Tacos",     "~3.9 oz",  200, 11,  4, 0.0,  30,  430, 15, 2,  2,  9),
            _item("Chicken Quesadilla",           "Quesadillas","~5.7 oz", 470, 24,  9, 0.0,  80, 1050, 38, 3,  3, 26),
            _item("Steak Quesadilla",             "Quesadillas","~6 oz",   480, 25, 10, 0.0,  65, 1130, 38, 3,  4, 24),
            _item("7-Layer Burrito",              "Burritos",  "~10 oz",   490, 15,  5, 0.0,  20, 1280, 68,12,  5, 18),
            _item("Burrito Supreme (Beef)",       "Burritos",  "~9.5 oz",  400, 15,  6, 0.5,  40, 1010, 51, 7,  5, 17),
            _item("Burrito Supreme (Chicken)",    "Burritos",  "~9 oz",    370, 10,  4, 0.0,  55, 1070, 49, 6,  4, 22),
            _item("Steak Grilled Cheese Burrito", "Burritos",  "~8.5 oz",  700, 34, 13, 0.5,  80, 1600, 69, 5,  6, 29),
            _item("Power Bowl (Chicken)",         "Bowls",     "~11 oz",   470, 19,  7, 0.0,  70, 1300, 48, 8,  5, 27),
            _item("Taco Salad",                   "Salads",    "~17 oz",   750, 34, 13, 1.5,  65, 1660, 81, 13, 7, 25),
            _item("Chips & Nacho Cheese",         "Sides",     "~3.5 oz",  220, 10,  2, 0.0,   0,  430, 28, 1,  1,  3),
            _item("Black Beans & Rice",           "Sides",     "~4.4 oz",  180,  4,  1, 0.0,   0,  390, 31, 4,  1,  5),
            _item("Cinnabon Delights (2pk)",      "Desserts",  "~1.4 oz",  160,  9,  4, 2.0,   5,   90, 18, 0,  8,  2),
        ],
    },

    # ── SUBWAY ───────────────────────────────────────────────────────────────
    "subway": {
        "chain": dict(name="Subway", slug="subway",
                      website="https://www.subway.com", cuisine_type="Sandwiches"),
        "items": [
            _item("Black Forest Ham (6\")",       "Subs",      "~7.5 oz",  310,  6,  2, 0.0,  45,  850, 44, 3,  8, 19),
            _item("Rotisserie-Style Chicken (6\")","Subs",     "~9 oz",    350,  7,  2, 0.0,  60,  710, 40, 3,  6, 30),
            _item("Roast Beef (6\")",             "Subs",      "~8 oz",    320,  6,  2, 0.0,  45,  650, 41, 3,  7, 22),
            _item("Sweet Onion Chicken Teriyaki (6\")","Subs", "~9 oz",    370,  5,  1, 0.0,  50,  760, 53, 3, 17, 25),
            _item("Subway Club (6\")",            "Subs",      "~9 oz",    310,  5,  1, 0.0,  50,  820, 42, 3,  7, 23),
            _item("BLT (6\")",                    "Subs",      "~6.5 oz",  320, 10,  3, 0.0,  30,  620, 40, 3,  6, 16),
            _item("Cold Cut Combo (6\")",         "Subs",      "~7.5 oz",  360, 12,  4, 0.0,  60, 1110, 42, 3,  7, 19),
            _item("Spicy Italian (6\")",          "Subs",      "~7 oz",    480, 24,  9, 0.0,  65, 1600, 40, 3,  6, 22),
            _item("Chicken & Bacon Ranch (6\")",  "Subs",      "~9 oz",    510, 22,  7, 0.0,  80, 1240, 41, 3,  6, 33),
            _item("Buffalo Chicken (6\")",        "Subs",      "~8.5 oz",  390, 10,  3, 0.0,  55,  950, 44, 3,  6, 28),
            _item("Steak & Cheese (6\")",         "Subs",      "~8 oz",    380, 11,  5, 0.0,  60,  910, 40, 3,  6, 28),
            _item("Pizza Sub (6\")",              "Subs",      "~6.5 oz",  430, 17,  6, 0.0,  40, 1040, 46, 3,  7, 19),
            _item("Footlong Turkey Breast",       "Footlongs", "~14 oz",   560,  8,  2, 0.0,  50, 1520, 80, 6, 12, 40),
            _item("Footlong Italian BMT",         "Footlongs", "~14 oz",   820, 36, 12, 1.0, 110, 2620, 80, 6, 12, 44),
            _item("Apple Slices",                 "Sides",     "~3 oz",     35,  0,  0, 0.0,   0,    0,  9, 1,  7,  0),
        ],
    },

    # ── SONIC ────────────────────────────────────────────────────────────────
    "sonic": {
        "chain": dict(name="Sonic Drive-In", slug="sonic",
                      website="https://www.sonicdrivein.com", cuisine_type="Fast Food"),
        "items": [
            _item("Double Classic Cheeseburger",  "Burgers",   "~8.5 oz",  800, 50, 17, 2.0, 160, 1160, 47, 2,  9, 40),
            _item("Jr. Double Cheeseburger",      "Burgers",   "~5.6 oz",  530, 33, 11, 1.5,  95,  750, 31, 2,  6, 25),
            _item("Jr. Breakfast Burrito",        "Breakfast", "~5.2 oz",  440, 27,  9, 0.0, 265,  910, 32, 1,  3, 20),
            _item("Breakfast Toaster (Bacon)",    "Breakfast", "~7.3 oz",  530, 29, 10, 0.0, 245, 1290, 42, 2,  5, 25),
            _item("Super Sonic Bacon Double Cheeseburger","Burgers","~11 oz",980,63,22,2.5,195,1460,47,2,9,55),
            _item("Chicken Strips (3pc)",         "Chicken",   "~4.5 oz",  370, 20,  4, 0.0,  35, 1040, 28, 1,  0, 19),
            _item("Popcorn Chicken (Small)",      "Chicken",   "~3.5 oz",  280, 15,  3, 0.0,  25,  820, 25, 1,  0, 11),
            _item("Large Tater Tots",             "Sides",     "~5.3 oz",  460, 24,  4, 0.0,   0,  870, 55, 5,  0,  6),
            _item("Small Tater Tots",             "Sides",     "~2.4 oz",  200, 11,  2, 0.0,   0,  380, 24, 2,  0,  3),
            _item("Large Onion Rings",            "Sides",     "~4.8 oz",  500, 27,  5, 5.5,   0,  580, 60, 3,  4,  6),
            _item("Large Vanilla Shake",          "Shakes",    "20 fl oz", 790, 34, 22, 0.5, 120,  400,110, 0, 86, 13),
            _item("Large Cherry Limeade",         "Drinks",    "32 fl oz", 400,  0,  0, 0.0,   0,   40,104, 0,101,  0),
            _item("Footlong Quarter Pound Coney", "Hot Dogs",  "~7.5 oz",  690, 42, 17, 1.0, 115, 2060, 48, 2, 10, 27),
            _item("Jr. Banana Split Blast",       "Desserts",  "~10 oz",   470, 12,  7, 0.0,  45,  170, 83, 1, 60,  8),
        ],
    },

    # ── PANERA BREAD ─────────────────────────────────────────────────────────
    "panera": {
        "chain": dict(name="Panera Bread", slug="panera",
                      website="https://www.panerabread.com", cuisine_type="Bakery / Café"),
        "items": [
            _item("Chicken Noodle Soup (Cup)",    "Soups",     "~6 oz",    90,  2,  0, 0.0,  30,  820, 12, 1,  1,  7),
            _item("Tomato Soup (Bowl)",            "Soups",     "~12 oz",  250,  8,  3, 0.0,  20, 1090, 34, 4, 17,  7),
            _item("Clam Chowder (Bowl)",           "Soups",     "~12 oz",  430, 24, 15, 0.0,  90, 1090, 38, 1,  4, 16),
            _item("Green Goddess Salad w/Chicken","Salads",    "~13 oz",  540, 30,  6, 0.0, 100,  870, 32, 5, 14, 36),
            _item("Greek Salad",                  "Salads",    "~10 oz",  370, 27,  9, 0.0,  55,  990, 18, 4,  9, 13),
            _item("Napa Almond Chicken Salad",    "Sandwiches","~12 oz",  810, 44, 10, 0.0,  75, 1450, 69, 5, 18, 36),
            _item("Smokehouse BBQ Chicken",       "Sandwiches","~11 oz",  720, 26,  8, 0.0,  90, 1660, 81, 4, 21, 41),
            _item("Toasted Steak & White Cheddar","Sandwiches","~10 oz",  760, 37, 14, 1.0, 115, 1490, 62, 3,  9, 45),
            _item("Grilled Cheese",               "Sandwiches","~6 oz",   610, 30, 17, 0.5,  75, 1110, 60, 3,  5, 24),
            _item("Mac & Cheese (Cup)",           "Mac",       "~6 oz",   480, 29, 16, 0.0,  85,  780, 48, 2,  6, 17),
            _item("Frontega Chicken Flatbread",   "Flatbreads","~9 oz",   540, 21,  8, 0.0, 100, 1140, 51, 2,  4, 36),
            _item("Everything Bagel",             "Bakery",    "~4 oz",   290,  2,  0, 0.0,   0,  490, 56, 2,  6, 10),
            _item("Plain Bagel",                  "Bakery",    "~4 oz",   290,  2,  0, 0.0,   0,  490, 57, 2,  5, 10),
            _item("Pecan Roll",                   "Bakery",    "~4.8 oz", 680, 33, 11, 0.0,  40,  640, 90, 3, 48,  9),
        ],
    },

    # ── PANDA EXPRESS ────────────────────────────────────────────────────────
    "panda-express": {
        "chain": dict(name="Panda Express", slug="panda-express",
                      website="https://www.pandaexpress.com", cuisine_type="Asian"),
        "items": [
            _item("Sweetfire Chicken Breast",     "Entrees",   "5.7 oz",  380, 13,  3, 0.0,  65,  330, 43, 2, 20, 25),
            _item("Mushroom Chicken",             "Entrees",   "5.5 oz",  220, 13,  2, 0.0,  55,  760, 13, 2,  6, 16),
            _item("String Bean Chicken Breast",   "Entrees",   "5.5 oz",  190,  9,  2, 0.0,  55,  520, 13, 2,  5, 16),
            _item("Black Pepper Angus Steak",     "Entrees",   "5.5 oz",  200, 10,  3, 0.0,  60,  720, 10, 2,  4, 19),
            _item("Grilled Teriyaki Chicken",     "Entrees",   "5.5 oz",  300, 13,  3, 0.0, 110,  530,  8, 0,  7, 36),
            _item("Vegetable Spring Roll (2pc)",  "Appetizers","3.0 oz",  190,  9,  2, 0.0,   0,  340, 24, 2,  3,  4),
            _item("Apple Pie Roll (2pc)",         "Desserts",  "2.4 oz",  150,  5,  2, 0.0,   0,  115, 26, 0, 11,  2),
            _item("Bowl (1 Side + 1 Entree)",     "Combos",    "~14 oz",  890, 26,  5, 0.0, 165, 1640,108, 3,  6, 38),
            _item("Plate (1 Side + 2 Entrees)",   "Combos",    "~22 oz", 1130, 37,  7, 0.0, 175, 2030,134, 5, 10, 50),
        ],
    },

    # ── POPEYES ──────────────────────────────────────────────────────────────
    "popeyes": {
        "chain": dict(name="Popeyes", slug="popeyes",
                      website="https://www.popeyes.com", cuisine_type="Fast Food"),
        "items": [
            _item("Wing (Mild/Spicy)",            "Chicken",   "~1.8 oz",  150, 10,  3, 0.0,  55,  490,  7, 0,  0,  9),
            _item("Leg (Mild/Spicy)",             "Chicken",   "~2.4 oz",  190, 12,  4, 0.0,  80,  560,  9, 0,  0, 15),
            _item("Nuggets (4pc Mild)",           "Nuggets",   "~3 oz",    170,  9,  2, 0.0,  30,  460, 12, 0,  0, 11),
            _item("Shrimp (4pc)",                 "Seafood",   "~2.7 oz",  260, 14,  4, 0.0,  80,  680, 22, 1,  0, 11),
            _item("Mac & Cheese",                 "Sides",     "~5.3 oz",  220, 11,  7, 0.0,  35,  490, 23, 1,  3,  9),
            _item("Corn on the Cob",              "Sides",     "~5 oz",    190,  5,  1, 0.0,   0,    5, 32, 3,  8,  5),
            _item("Handcrafted Chicken Tender (1pc)","Tenders","~1.9 oz",  120,  6,  2, 0.0,  25,  310,  8, 0,  0, 10),
            _item("Chicken Sandwich (Blackened)", "Sandwiches","~7 oz",    400, 15,  5, 0.0,  85, 1320, 44, 2,  7, 27),
        ],
    },

    # ── FIVE GUYS ────────────────────────────────────────────────────────────
    "five-guys": {
        "chain": dict(name="Five Guys", slug="five-guys",
                      website="https://www.fiveguys.com", cuisine_type="Fast Food"),
        "items": [
            _item("Little Cheeseburger",          "Burgers",   "~6.3 oz",  620, 37, 16, 1.5, 100,  660, 39, 2,  9, 29),
            _item("Veggie Sandwich",              "Sandwiches","~6 oz",    440, 15,  7, 0.5,  30,  710, 60, 5,  9, 17),
            _item("BLT",                          "Sandwiches","~5 oz",    580, 38, 19, 0.5, 100,  760, 41, 2,  9, 17),
            _item("Grilled Cheese",               "Sandwiches","~4.5 oz",  430, 26, 14, 0.5,  55,  700, 35, 2,  8, 14),
            _item("Hot Dog",                      "Hot Dogs",  "~5.5 oz",  580, 36, 15, 0.5, 100, 1170, 46, 2,  9, 22),
            _item("Cheese Dog",                   "Hot Dogs",  "~6.3 oz",  710, 48, 22, 0.5, 125, 1590, 47, 2,  9, 29),
            _item("Small Cajun Fries",            "Fries",     "~8.5 oz",  476, 21,  4, 0.0,   0,  941, 65, 4,  0,  7),
            _item("Chocolate Milkshake",          "Milkshakes","24 fl oz", 840, 24, 15, 0.0,  90,  510,136, 2,121, 18),
            _item("Strawberry Milkshake",         "Milkshakes","24 fl oz", 760, 20, 12, 0.0,  80,  490,127, 1,115, 17),
        ],
    },

    # ── CHIPOTLE ─────────────────────────────────────────────────────────────
    "chipotle": {
        "chain": dict(name="Chipotle", slug="chipotle",
                      website="https://www.chipotle.com", cuisine_type="Mexican"),
        "items": [
            _item("Barbacoa Burrito Bowl",        "Bowls",     "~15 oz",  615, 23,  7, 0.5,  70, 1530, 68, 11, 4, 43),
            _item("Carnitas Burrito Bowl",        "Bowls",     "~15 oz",  560, 19,  7, 0.0,  70, 1440, 68, 11, 4, 38),
            _item("Veggie Burrito Bowl",          "Bowls",     "~14 oz",  480, 17,  5, 0.0,   0, 1280, 69, 12, 4, 19),
            _item("Barbacoa Tacos (3)",           "Tacos",     "~11 oz",  395, 14,  5, 0.5,  60, 1095, 42,  7, 3, 33),
            _item("Sofritas Tacos (3)",           "Tacos",     "~11 oz",  370, 14,  4, 0.0,   0, 1010, 44,  8, 3, 17),
            _item("Quesadilla (Chicken)",         "Quesadillas","~11 oz", 850, 49, 22, 1.0, 195, 1900, 64, 4,  3, 51),
            _item("Carnitas",                     "Ingredients","~4 oz",  210, 12,  4, 0.0,  65,  450,  0, 0,  0, 23),
            _item("Barbacoa",                     "Ingredients","~4 oz",  170,  7,  3, 0.5,  65,  540,  2, 0,  0, 24),
            _item("Sofritas",                     "Ingredients","~4 oz",  150,  9,  1, 0.0,   0,  420,  9, 3,  1,  8),
            _item("Fajita Veggies",               "Ingredients","~2.5 oz", 20,  1,  0, 0.0,   0,  175,  4, 1,  2,  1),
            _item("Tomatillo Green-Chili Salsa",  "Ingredients","~3.5 oz", 30,  1,  0, 0.0,   0,  260,  4, 1,  2,  1),
            _item("Corn Salsa",                   "Ingredients","~3.5 oz", 80,  1,  0, 0.0,   0,  410, 15, 2,  5,  2),
            _item("Chips & Tomatillo Green Salsa","Sides",     "~6 oz",   620, 25,  4, 0.0,   0,  750, 89, 7,  5,  9),
        ],
    },

    # ── DAIRY QUEEN ──────────────────────────────────────────────────────────
    "dairy-queen": {
        "chain": dict(name="Dairy Queen", slug="dairy-queen",
                      website="https://www.dairyqueen.com", cuisine_type="Fast Food"),
        "items": [
            _item("Bacon Double Cheeseburger",    "Burgers",   "~9.2 oz",  720, 43, 17, 2.0, 145, 1240, 38, 2,  9, 43),
            _item("FlameThrower GrillBurger",     "Burgers",   "~9.5 oz",  800, 47, 18, 2.0, 150, 1530, 52, 2, 10, 39),
            _item("Crispy Chicken BLT Salad",     "Salads",    "~11 oz",   460, 26, 10, 0.0,  80, 1260, 28, 4,  7, 28),
            _item("Chicken Strip Basket (2pc)",   "Chicken",   "~5.5 oz",  560, 27,  7, 0.0,  40, 1350, 55, 3,  6, 21),
            _item("Blizzard Brownie Batter (Med)","Blizzards", "15 fl oz", 840, 32, 20, 0.5,  75,  430,123, 2, 97, 14),
            _item("Blizzard Choco Brownie Xtreme","Blizzards", "15 fl oz", 800, 30, 18, 0.5,  75,  360,119, 2, 96, 14),
            _item("Blizzard Mint Choco Chip (Med)","Blizzards","15 fl oz", 760, 29, 19, 0.5,  75,  280,114, 0, 99, 13),
            _item("Banana Split",                 "Sundaes",   "~13 oz",   490, 12,  8, 0.0,  40,  170, 86, 2, 65,  9),
            _item("Small French Fries",           "Sides",     "~2.5 oz",  220,  9,  2, 0.0,   0,  490, 31, 2,  0,  3),
            _item("Large French Fries",           "Sides",     "~5.2 oz",  470, 20,  4, 0.0,   0, 1040, 66, 5,  0,  6),
            _item("Hot Dog",                      "Hot Dogs",  "~4.5 oz",  340, 21,  8, 0.0,  50,  930, 25, 1,  5, 13),
            _item("Pretzel Sticks w/Cheese (5pc)","Sides",     "~4.5 oz",  390, 10,  3, 0.0,  10,  920, 59, 3,  6, 14),
        ],
    },

    # ── JIMMY JOHN'S ─────────────────────────────────────────────────────────
    "jimmy-johns": {
        "chain": dict(name="Jimmy John's", slug="jimmy-johns",
                      website="https://www.jimmyjohns.com", cuisine_type="Sandwiches"),
        "items": [
            _item("Pepe (8\")",                   "Subs",      "~9 oz",   530, 22,  8, 0.0,  75, 1600, 50, 2,  4, 28),
            _item("Big John (8\")",               "Subs",      "~9 oz",   490, 17,  5, 0.0,  75, 1150, 51, 2,  4, 32),
            _item("Totally Tuna (8\")",           "Subs",      "~10 oz",  690, 43,  7, 0.0,  45,  970, 47, 2,  4, 28),
            _item("Country Club (8\")",           "Subs",      "~10 oz",  570, 27,  8, 0.0,  75, 1810, 48, 2,  4, 30),
            _item("Hunter's Club (8\")",          "Subs",      "~10 oz",  540, 21,  6, 0.0,  75, 1540, 50, 2,  4, 30),
            _item("Club Lulu (8\")",              "Subs",      "~9 oz",   490, 17,  5, 0.0,  75, 1450, 51, 2,  4, 30),
            _item("Unwich (Turkey Tom)",          "Unwiches",  "~7 oz",   180,  9,  3, 0.0,  30,  800,  7, 2,  3, 18),
            _item("Unwich (Italian Night Club)",  "Unwiches",  "~8 oz",   340, 25,  9, 0.5,  70, 1570, 10, 2,  3, 21),
        ],
    },

    # ── WINGSTOP ─────────────────────────────────────────────────────────────
    "wingstop": {
        "chain": dict(name="Wingstop", slug="wingstop",
                      website="https://www.wingstop.com", cuisine_type="Wings"),
        "items": [
            _item("Classic Wings Garlic Parmesan","Wings",     "~6 oz",   470, 34,  9, 0.0, 120, 1070,  8, 0,  1, 37),
            _item("Classic Wings Mango Habanero", "Wings",     "~6 oz",   460, 29,  8, 0.0, 120, 1060, 12, 0,  9, 37),
            _item("Classic Wings Hawaiian",       "Wings",     "~6 oz",   450, 28,  8, 0.0, 120,  570, 11, 0,  9, 37),
            _item("Boneless Wings Garlic Parm",   "Wings",     "~6 oz",   430, 26,  6, 0.0,  60, 1870, 27, 1,  1, 21),
            _item("Chicken Tenders Lemon Pepper","Tenders",    "~5.5 oz", 490, 26,  5, 0.0,  75, 1540, 34, 1,  2, 30),
            _item("Veggie Sticks & Ranch",        "Sides",     "~4 oz",   220, 22,  4, 0.0,  10,  260,  5, 2,  3,  2),
            _item("Small Seasoned Fries",         "Sides",     "~3.5 oz", 290, 14,  3, 0.0,   0,  940, 39, 3,  0,  4),
            _item("Cajun Fried Corn",             "Sides",     "~4 oz",   290, 17,  3, 0.0,   0,  490, 31, 3,  7,  4),
        ],
    },

    # ── RAISING CANE'S ───────────────────────────────────────────────────────
    "raising-canes": {
        "chain": dict(name="Raising Cane's", slug="raising-canes",
                      website="https://www.raisingcanes.com", cuisine_type="Fast Food"),
        "items": [
            _item("3pc Finger Combo",             "Combos",    "~12 oz",  670, 36,  7, 0.0, 100, 1310, 60, 2,  5, 28),
            _item("Sandwich Combo",               "Combos",    "~14 oz",  740, 37,  7, 0.0, 110, 1600, 71, 3,  7, 30),
            _item("Large Crinkle Cut Fries",      "Sides",     "~6 oz",   490, 21,  4, 0.0,   0,  660, 70, 5,  0,  8),
            _item("Chicken Sandwich",             "Sandwiches","~7 oz",   420, 19,  4, 0.0,  70,  950, 43, 2,  5, 22),
            _item("Sweet Tea (22 oz)",            "Drinks",    "22 fl oz",160,  0,  0, 0.0,   0,   15, 43, 0, 43,  0),
        ],
    },

    # ── SHAKE SHACK ──────────────────────────────────────────────────────────
    "shake-shack": {
        "chain": dict(name="Shake Shack", slug="shake-shack",
                      website="https://www.shakeshack.com", cuisine_type="Fast Food"),
        "items": [
            _item("Double ShackBurger",           "Burgers",   "~9.3 oz",  780, 49, 21, 2.5, 155, 1200, 33, 1,  9, 45),
            _item("Shack Stack",                  "Burgers",   "~10 oz",   760, 47, 17, 2.0, 130, 1160, 44, 2, 10, 35),
            _item("'Shroom Burger",               "Burgers",   "~7.8 oz",  590, 33, 15, 0.5,  75,  820, 48, 4,  9, 22),
            _item("Chicken Shack",                "Chicken",   "~7.5 oz",  590, 32,  7, 0.0,  75, 1120, 47, 2,  6, 26),
            _item("Avocado Bacon Burger",         "Burgers",   "~8.5 oz",  640, 39, 14, 1.5, 100, 1050, 35, 3,  8, 32),
            _item("Chocolate Shake",              "Shakes",    "16 fl oz", 710, 38, 25, 0.0, 155,  410, 80, 1, 70, 14),
            _item("Strawberry Shake",             "Shakes",    "16 fl oz", 660, 34, 22, 0.0, 145,  310, 79, 0, 70, 13),
            _item("Black & White Cookie Shake",   "Shakes",    "16 fl oz", 790, 40, 26, 0.0, 155,  500,100, 0, 84, 14),
        ],
    },

    # ── CULVER'S ─────────────────────────────────────────────────────────────
    "culvers": {
        "chain": dict(name="Culver's", slug="culvers",
                      website="https://www.culvers.com", cuisine_type="Fast Food"),
        "items": [
            _item("Triple ButterBurger w/Cheese", "Burgers",   "~12.5 oz",960, 60, 28, 1.5, 210, 1310, 37, 1,  6, 59),
            _item("Mushroom & Swiss ButterBurger","Burgers",   "~8.6 oz",  620, 34, 14, 1.0, 110,  910, 40, 2,  7, 33),
            _item("Bacon Deluxe ButterBurger",    "Burgers",   "~9 oz",    650, 36, 14, 1.0, 120, 1140, 38, 1,  7, 36),
            _item("North Atlantic Cod Sandwich",  "Seafood",   "~6.5 oz",  540, 25,  4, 0.0,  65,  740, 51, 3,  5, 24),
            _item("Chicken Tenders (2pc)",        "Chicken",   "~3 oz",    290, 14,  2, 0.0,  45,  680, 23, 1,  0, 19),
            _item("Chicken Tenders (4pc)",        "Chicken",   "~6 oz",    580, 28,  5, 0.0,  90, 1360, 46, 2,  0, 37),
            _item("Cheese Curds (Large)",         "Sides",     "~8 oz",    960, 62, 29, 0.0, 160, 1000, 64, 1,  5, 38),
            _item("Onion Rings (Regular)",        "Sides",     "~4 oz",    380, 18,  4, 4.0,   0,  670, 49, 2,  5,  5),
            _item("Coleslaw",                     "Sides",     "~4 oz",    220, 15,  2, 0.0,  15,  260, 20, 2,  9,  2),
            _item("Concrete Mixer Turtle (Small)","Frozen Custard","12 oz",640, 34, 18, 0.0, 120,  330, 79, 1, 62, 12),
            _item("Strawberry Shake (Small)",     "Shakes",    "12 fl oz", 530, 25, 15, 0.0, 105,  240, 68, 0, 57, 10),
        ],
    },

    # ── WHATABURGER ──────────────────────────────────────────────────────────
    "whataburger": {
        "chain": dict(name="Whataburger", slug="whataburger",
                      website="https://whataburger.com", cuisine_type="Fast Food"),
        "items": [
            _item("Triple Whataburger",           "Burgers",   "~14 oz", 1140, 71, 27, 2.0, 230, 1520, 59, 2, 10, 69),
            _item("Bacon & Cheese Whataburger",   "Burgers",   "~10.7 oz",730, 38, 14, 1.0, 110, 1390, 58, 2,  9, 40),
            _item("Jalapeño & Cheese Whataburger","Burgers",   "~9.9 oz", 630, 31, 12, 1.0,  85, 1250, 57, 2,  8, 32),
            _item("Grilled Chicken Sandwich",     "Chicken",   "~8.5 oz", 430, 14,  3, 0.0,  90, 1160, 44, 2,  7, 31),
            _item("Crispy Chicken Sandwich",      "Chicken",   "~7.5 oz", 530, 22,  4, 0.0,  65, 1230, 52, 2,  7, 26),
            _item("Whatachick'n Strips (3pc)",    "Chicken",   "~5 oz",   390, 19,  4, 0.0,  60, 1050, 28, 1,  0, 27),
            _item("Garden Salad",                 "Salads",    "~10 oz",   60,  3,  1, 0.0,  10,  130,  7, 2,  4,  3),
            _item("Apple & Cranberry Chicken Salad","Salads",  "~13 oz",  400, 14,  4, 0.0,  80,  950, 36, 4, 21, 35),
            _item("Large French Fries",           "Sides",     "~5 oz",   500, 23,  5, 0.0,   0,  540, 65, 5,  0,  7),
            _item("Onion Rings (Medium)",         "Sides",     "~4 oz",   410, 21,  5, 4.0,   0,  540, 51, 3,  5,  5),
            _item("Cinnamon Roll",                "Breakfast", "~4 oz",   490, 19,  4, 3.0,  20,  560, 73, 2, 31,  8),
            _item("Breakfast Platter",            "Breakfast", "~13 oz",  740, 45, 17, 0.5, 585, 1890, 49, 3,  4, 34),
        ],
    },

    # ── IN-N-OUT BURGER ──────────────────────────────────────────────────────
    "in-n-out": {
        "chain": dict(name="In-N-Out Burger", slug="in-n-out",
                      website="https://www.in-n-out.com", cuisine_type="Fast Food"),
        "items": [
            _item("3×3 Burger",                   "Burgers",   "~14 oz",  950, 60, 27, 0.0, 180, 2070, 39, 3,  5, 55),
            _item("4×4 Burger",                   "Burgers",   "~17 oz", 1150, 74, 36, 0.0, 240, 2550, 40, 3,  5, 73),
            _item("Double-Double Animal Style",   "Burgers",   "~12 oz",  760, 50, 22, 0.0, 120, 1440, 40, 3, 11, 38),
            _item("Veggie Burger",                "Burgers",   "~5 oz",   300, 11,  5, 0.0,  25,  550, 40, 3,  8,  9),
            _item("Neapolitan Shake",             "Shakes",    "15 fl oz",660, 29, 19, 0.0, 100,  340, 88, 0, 83, 12),
            _item("Vanilla Shake",                "Shakes",    "15 fl oz",580, 27, 19, 0.0,  95,  280, 73, 0, 68, 11),
            _item("Lemonade",                     "Drinks",    "16 fl oz",180,  0,  0, 0.0,   0,   25, 45, 0, 44,  0),
            _item("Iced Tea",                     "Drinks",    "16 fl oz",  0,  0,  0, 0.0,   0,   10,  0, 0,  0,  0),
        ],
    },

    # ── STARBUCKS ────────────────────────────────────────────────────────────
    "starbucks": {
        "chain": dict(name="Starbucks", slug="starbucks",
                      website="https://www.starbucks.com", cuisine_type="Coffee / Café"),
        "items": [
            _item("Nitro Cold Brew (Venti)",      "Cold Coffees","24 fl oz", 30,  0,  0, 0.0,  0,   25,  5, 0,  4,  1),
            _item("Iced Brown Sugar Oat Latte",   "Cold Coffees","Grande",  260,  7,  1, 0.0,  0,  170, 44, 1, 42,  4),
            _item("Iced Matcha Latte (Grande)",   "Cold Coffees","Grande",  200,  5,  3, 0.0, 20,  135, 30, 1, 27,  7),
            _item("Chai Tea Latte (Grande)",      "Hot Coffees","Grande",   240,  5,  3, 0.0, 20,  115, 42, 0, 42,  8),
            _item("White Chocolate Mocha (Grande)","Hot Coffees","Grande",  430, 15, 10, 0.0, 40,  250, 61, 0, 58, 14),
            _item("Iced Caramel Macchiato (Grande)","Cold Coffees","Grande",250, 7, 4, 0.0, 30,  150, 34, 0, 32, 10),
            _item("Pink Drink (Grande)",          "Cold Coffees","Grande",  140,  2,  2, 0.0,  5,   65, 27, 0, 24,  2),
            _item("Dragon Drink (Grande)",        "Cold Coffees","Grande",  130,  3,  2, 0.0,  5,   80, 28, 0, 25,  1),
            _item("Bacon Gouda Sandwich",         "Snacks & Sandwiches","~4.3 oz",370,19,8,0.0,155,840,32,0,4,19),
            _item("Spinach Feta Wrap",            "Snacks & Sandwiches","~3.9 oz",290,10,3,0.0,15,830,33,3,3,19),
            _item("Tomato & Mozzarella Sandwich", "Snacks & Sandwiches","~5 oz",380,15,6,0.0,25,510,44,2,7,18),
            _item("Iced Lemon Loaf",              "Bakery",    "~4.3 oz",  490, 22,  3, 0.0, 70,  410, 67, 1, 44,  6),
            _item("Pumpkin Cream Cheese Muffin",  "Bakery",    "~4.7 oz",  410, 20,  6, 0.0, 70,  440, 53, 1, 35,  5),
            _item("Butter Croissant",             "Bakery",    "~2.7 oz",  260, 14,  8, 0.5, 45,  290, 29, 1,  4,  5),
        ],
    },

    # ── DUNKIN' ───────────────────────────────────────────────────────────────
    "dunkin": {
        "chain": dict(name="Dunkin'", slug="dunkin",
                      website="https://www.dunkindonuts.com", cuisine_type="Coffee / Café"),
        "items": [
            _item("Pumpkin Spice Latte (Med)",    "Hot Drinks","16 fl oz", 350, 11,  7, 0.0, 45,  200, 53, 0, 48, 12),
            _item("Frozen Coffee (Med)",          "Frozen","24 fl oz",     480, 14,  9, 0.0, 50,  260, 79, 0, 72, 10),
            _item("Strawberry Coolatta (Med)",    "Frozen","32 fl oz",     490,  0,  0, 0.0,  0,   45,122, 0,115,  0),
            _item("Chocolate Glazed Donut",       "Donuts","~2.5 oz",      310, 16,  7, 0.0,  0,  310, 39, 1, 20,  4),
            _item("Blueberry Donut",              "Donuts","~2 oz",        260, 12,  5, 0.0,  0,  260, 35, 1, 15,  3),
            _item("Glazed Munchkins (5pc)",       "Donuts","~2 oz",        220, 10,  5, 0.0,  0,  210, 31, 1, 14,  3),
            _item("Sausage Egg & Cheese Bagel",   "Sandwiches","~7 oz",   590, 27, 10, 0.0,235, 1360, 60, 3,  8, 28),
            _item("Egg & Cheese English Muffin",  "Sandwiches","~4.5 oz", 310, 11,  4, 0.0,195,  750, 38, 2,  4, 16),
            _item("Wake-Up Wrap (Egg & Cheese)",  "Wraps","~3 oz",        190,  9,  4, 0.0,165,  480, 18, 1,  2,  9),
            _item("Avocado Toast",                "Snacks","~5 oz",        350, 13,  2, 0.0,  0,  560, 49, 7,  3, 10),
            _item("Hash Browns (6pc)",            "Sides","~3 oz",         200, 10,  2, 0.0,  0,  360, 24, 2,  0,  2),
        ],
    },

    # ── IHOP ─────────────────────────────────────────────────────────────────
    "ihop": {
        "chain": dict(name="IHOP", slug="ihop",
                      website="https://www.ihop.com", cuisine_type="Breakfast"),
        "items": [
            _item("New York Cheesecake Pancakes (5pc)","Pancakes","~13 oz",1090,41,21,0.5,230,2020,156,4,60,22),
            _item("Harvest Grain & Nut Pancakes (3pc)","Pancakes","~9 oz", 590,25, 5, 0.0,130,1150, 77,7,16,16),
            _item("Stuffed French Toast (Original)","French Toast","~9 oz",870,42,22,0.5,170,1360, 99,4,49,20),
            _item("Chicken & Pancakes",           "Combos",    "~14 oz", 1000,43,12, 0.0,130,2250, 98,4, 9,57),
            _item("Eggs Benedict",                "Breakfast", "~12 oz",  680,41,16, 0.5,510,1740, 47,3, 5,32),
            _item("Spinach & Mushroom Omelette",  "Omelettes", "~14 oz",  440,33,13, 0.0,690,1020, 10,2, 4,34),
            _item("Bacon Temptation Omelette",    "Omelettes", "~14 oz",  610,45,20, 0.5,790,1680, 13,1, 3,44),
            _item("Buttermilk Crispy Chicken",    "Chicken",   "~14 oz",  900,41,10, 0.0,115,2320, 85,5, 7,50),
            _item("Sirloin Tips & Eggs",          "Entrees",   "~13 oz",  490,25, 9, 0.5,490,1300, 14,2, 3,51),
            _item("Fresh Strawberry Crepes",      "Crepes",    "~9 oz",   490,14, 7, 0.0,150,1010, 74,3,33,18),
        ],
    },

    # ── DENNY'S ───────────────────────────────────────────────────────────────
    "dennys": {
        "chain": dict(name="Denny's", slug="dennys",
                      website="https://www.dennys.com", cuisine_type="Breakfast"),
        "items": [
            _item("Super Slam",                   "Slams",     "~16 oz",  1150,67,25, 0.5,720,2980, 87,4,16,50),
            _item("All-American Slam",            "Slams",     "~14 oz",   820,51,19, 0.5,645,1980, 55,3,12,41),
            _item("Fit Fare Omelette",            "Omelettes", "~14 oz",   380,20, 6, 0.0,510,1340, 20,4, 5,32),
            _item("Denver Omelette",              "Omelettes", "~14 oz",   650,42,14, 0.5,660,1570, 31,3, 5,41),
            _item("Chicken Avocado BLT",          "Sandwiches","~13 oz",   830,46,11, 0.0,115,2090, 64,6, 9,44),
            _item("Bacon BBQ Burger",             "Burgers",   "~11 oz",   940,56,22, 1.5,165,1880, 57,3,15,47),
            _item("Philly Cheesesteak Omelette",  "Omelettes", "~14 oz",   740,48,18, 0.5,680,1580, 28,3, 4,49),
            _item("Loaded Veggie Omelette",       "Omelettes", "~14 oz",   510,35,13, 0.0,550,1070, 22,4, 6,31),
            _item("Strawberry Pancakes (2pc)",    "Pancakes",  "~6 oz",    340, 5,  1, 0.0,  0,  880, 63,3, 14, 7),
            _item("Cheesy Grits",                 "Sides",     "~6 oz",    210,11, 6, 0.0, 30,  460, 24,1,  1, 7),
            _item("Veggie Burger",                "Burgers",   "~10 oz",   590,23, 8, 0.0, 45, 1260, 70,7, 12,22),
        ],
    },

    # ── JACK IN THE BOX ──────────────────────────────────────────────────────
    "jack-in-the-box": {
        "chain": dict(name="Jack in the Box", slug="jack-in-the-box",
                      website="https://www.jackinthebox.com", cuisine_type="Fast Food"),
        "items": [
            _item("Bacon Ultimate Cheeseburger",  "Burgers",   "~11 oz",  890, 61, 24, 2.5, 185, 1580, 41, 2,  9, 48),
            _item("Double Jack",                  "Burgers",   "~9.6 oz", 730, 50, 19, 2.0, 125, 840,  41, 2,  9, 37),
            _item("Jr. Jack",                     "Burgers",   "~3.9 oz", 350, 19,  7, 0.5,  45, 590,  30, 1,  7, 15),
            _item("Chicken Sandwich",             "Chicken",   "~6.7 oz", 420, 17,  4, 0.0,  40, 740,  42, 2,  5, 20),
            _item("Chicken Strips (4pc)",         "Chicken",   "~6 oz",   500, 27,  6, 0.0,  60, 1290, 34, 2,  0, 27),
            _item("Large Curly Fries",            "Sides",     "~5.4 oz", 580, 30,  8, 0.0,   0, 1620, 73, 6,  0,  7),
            _item("Egg Rolls (3pc)",              "Sides",     "~5.4 oz", 400, 21,  5, 0.0,  15, 750,  41, 4,  3, 11),
            _item("Stuffed Jalapeños (3pc)",      "Sides",     "~3.1 oz", 230, 13,  5, 0.0,  20, 400,  22, 1,  3,  8),
            _item("Breakfast Jack",               "Breakfast", "~4 oz",   270, 11,  4, 0.0, 195, 700,  28, 1,  6, 13),
            _item("Loaded Breakfast Sandwich",    "Breakfast", "~6.7 oz", 670, 41, 14, 0.5, 380, 1450, 40, 2,  5, 35),
            _item("Oreo Cookie Ice Cream Shake",  "Shakes",    "16 fl oz",740, 33, 21, 0.0,  95, 440, 101, 1, 80, 12),
        ],
    },

    # ── QDOBA ────────────────────────────────────────────────────────────────
    "qdoba": {
        "chain": dict(name="Qdoba", slug="qdoba",
                      website="https://www.qdoba.com", cuisine_type="Mexican"),
        "items": [
            _item("Steak Burrito",                "Burritos",  "~15 oz",  870, 36, 12, 0.5,  85, 2180, 89, 9, 10, 45),
            _item("Impossible Burrito",           "Burritos",  "~15 oz",  820, 29,  9, 0.0,   0, 2110, 97,12, 11, 28),
            _item("Pulled Pork Bowl",             "Bowls",     "~14 oz",  570, 21,  6, 0.0,  75, 1930, 59, 7,  7, 35),
            _item("Ground Beef Taco (per taco)",  "Tacos",     "~4 oz",   240, 10,  4, 0.0,  35,  590, 24, 2,  2, 13),
            _item("Veggie Bowl",                  "Bowls",     "~14 oz",  490, 15,  5, 0.0,   0, 1390, 66, 9,  6, 18),
            _item("Loaded Taco (Chicken)",        "Tacos",     "~5 oz",   290, 13,  4, 0.0,  50,  690, 27, 3,  2, 17),
            _item("Breakfast Burrito (Egg & Cheese)","Burritos","~11 oz", 680, 27,  9, 0.0, 425, 1390, 77, 5,  5, 28),
        ],
    },

    # ── BUFFALO WILD WINGS ───────────────────────────────────────────────────
    "buffalo-wild-wings": {
        "chain": dict(name="Buffalo Wild Wings", slug="buffalo-wild-wings",
                      website="https://www.buffalowildwings.com", cuisine_type="Wings"),
        "items": [
            _item("Traditional Wings (12pc)",     "Wings",     "~14 oz",  860, 54, 18, 0.0, 290,  980,  0, 0,  0, 82),
            _item("Boneless Wings (12pc)",        "Wings",     "~12 oz",  760, 44, 10, 0.0, 110, 2200, 40, 2,  2, 46),
            _item("Cauliflower Wings (8pc)",      "Wings",     "~8 oz",   490, 28,  4, 0.0,   0, 1860, 51, 5,  9, 11),
            _item("Ultimate Nachos (Chicken)",    "Appetizers","~20 oz", 1640,100,36, 1.0, 195, 3680,127, 13,14, 65),
            _item("Avocado Chicken Burger",       "Burgers",   "~11 oz",  820, 51, 16, 1.0, 125, 1480, 47, 4,  9, 45),
            _item("Grilled Chicken Salad",        "Salads",    "~13 oz",  450, 27, 10, 0.0, 100, 1180, 19, 3,  6, 37),
            _item("Cheese Quesadilla",            "Appetizers","~7 oz",   710, 40, 19, 0.5,  85, 1230, 56, 3,  5, 29),
            _item("Large Steak Fries",            "Sides",     "~8 oz",   680, 33,  7, 0.0,   0, 1540, 88, 9,  2, 11),
            _item("Onion Rings",                  "Sides",     "~5 oz",   540, 26,  5, 4.0,   0,  970, 68, 4, 11,  7),
        ],
    },
}
