"""
Popular preset meal combinations.
Each combo references items by the exact names used in seed_data.py.
Run:  python main.py --presets
"""
import asyncio
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy import text

DATABASE_URL = os.environ["DATABASE_URL"]
engine = create_async_engine(DATABASE_URL)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

# ─────────────────────────────────────────────────────────────────────────────
# Format: chain_slug → list of combos
# Each combo: { "name": str, "description": str, "items": [(item_name, qty)] }
# ─────────────────────────────────────────────────────────────────────────────
PRESETS: dict[str, list[dict]] = {

    "mcdonalds": [
        {
            "name": "Big Mac Large Combo",
            "description": "Big Mac, Large Fries, Large Dr Pepper",
            "items": [("Big Mac", 1), ("Large French Fries", 1), ("Large Dr Pepper", 1)],
        },
        {
            "name": "Big Mac Medium Combo",
            "description": "Big Mac, Medium Fries, Medium Soft Drink",
            "items": [("Big Mac", 1), ("Medium French Fries", 1), ("Medium Soft Drink", 1)],
        },
        {
            "name": "Quarter Pounder Large Combo",
            "description": "Quarter Pounder with Cheese, Large Fries, Large Soft Drink",
            "items": [("Quarter Pounder w/Cheese", 1), ("Large French Fries", 1), ("Large Soft Drink", 1)],
        },
        {
            "name": "10pc McNuggets Meal",
            "description": "10pc Chicken McNuggets, Medium Fries, Medium Soft Drink",
            "items": [("10 pc Chicken McNuggets", 1), ("Medium French Fries", 1), ("Medium Soft Drink", 1)],
        },
        {
            "name": "McChicken Meal",
            "description": "McChicken, Medium Fries, Medium Soft Drink",
            "items": [("McChicken", 1), ("Medium French Fries", 1), ("Medium Soft Drink", 1)],
        },
        {
            "name": "Crispy Chicken Sandwich Meal",
            "description": "Crispy Chicken Sandwich, Medium Fries, Medium Soft Drink",
            "items": [("Crispy Chicken Sandwich", 1), ("Medium French Fries", 1), ("Medium Soft Drink", 1)],
        },
        {
            "name": "Egg McMuffin Breakfast",
            "description": "Egg McMuffin, Hash Browns, Medium McCafé Coffee",
            "items": [("Egg McMuffin", 1), ("Hash Browns", 1), ("Medium McCafé Coffee", 1)],
        },
        {
            "name": "Sausage McMuffin Breakfast Meal",
            "description": "Sausage McMuffin with Egg, Hash Browns, Medium Orange Juice",
            "items": [("Sausage McMuffin w/Egg", 1), ("Hash Browns", 1), ("Medium Orange Juice", 1)],
        },
    ],

    "burger-king": [
        {
            "name": "Whopper Large Combo",
            "description": "Whopper, Large Fries, Large Dr Pepper",
            "items": [("Whopper", 1), ("Medium French Fries", 1), ("Large Dr Pepper", 1)],
        },
        {
            "name": "Whopper Medium Combo",
            "description": "Whopper, Medium Fries, Medium Soft Drink",
            "items": [("Whopper", 1), ("Medium French Fries", 1), ("Medium Soft Drink", 1)],
        },
        {
            "name": "Double Whopper Meal",
            "description": "Double Whopper, Medium Fries, Medium Soft Drink",
            "items": [("Double Whopper", 1), ("Medium French Fries", 1), ("Medium Soft Drink", 1)],
        },
        {
            "name": "Chicken Sandwich Combo",
            "description": "Original Chicken Sandwich, Medium Fries, Medium Soft Drink",
            "items": [("Original Chicken Sandwich", 1), ("Medium French Fries", 1), ("Medium Soft Drink", 1)],
        },
        {
            "name": "BK Breakfast",
            "description": "Croissan'wich with Egg & Cheese, Medium Soft Drink",
            "items": [("Croissan'wich w/Egg & Cheese", 1), ("Medium Soft Drink", 1)],
        },
    ],

    "wendys": [
        {
            "name": "Dave's Single Large Combo",
            "description": "Dave's Single, Large Fries, Large Dr Pepper",
            "items": [("Dave's Single", 1), ("Medium French Fries", 1), ("Large Dr Pepper", 1)],
        },
        {
            "name": "Dave's Double Meal",
            "description": "Dave's Double, Medium Fries, Medium Soft Drink",
            "items": [("Dave's Double", 1), ("Medium French Fries", 1), ("Medium Soft Drink", 1)],
        },
        {
            "name": "Baconator Meal",
            "description": "Baconator, Medium Fries, Medium Soft Drink",
            "items": [("Baconator", 1), ("Medium French Fries", 1), ("Medium Soft Drink", 1)],
        },
        {
            "name": "Spicy Chicken Combo",
            "description": "Spicy Chicken Sandwich, Medium Fries, Medium Soft Drink",
            "items": [("Spicy Chicken Sandwich", 1), ("Medium French Fries", 1), ("Medium Soft Drink", 1)],
        },
        {
            "name": "Frosty Meal Deal",
            "description": "Dave's Single, Small Fries, Large Frosty",
            "items": [("Dave's Single", 1), ("Medium French Fries", 1), ("Large Frosty (Chocolate)", 1)],
        },
    ],

    "chick-fil-a": [
        {
            "name": "Chicken Sandwich Meal",
            "description": "Chicken Sandwich, Waffle Fries, Large Lemonade",
            "items": [("Chicken Sandwich", 1), ("Waffle Potato Fries (Medium)", 1), ("Large Lemonade", 1)],
        },
        {
            "name": "Spicy Deluxe Meal",
            "description": "Spicy Chicken Sandwich, Waffle Fries, Medium Lemonade",
            "items": [("Spicy Chicken Sandwich", 1), ("Waffle Potato Fries (Medium)", 1), ("Medium Lemonade", 1)],
        },
        {
            "name": "8pc Nugget Meal",
            "description": "8pc Chicken Nuggets, Waffle Fries, Medium Lemonade",
            "items": [("8 pc Chicken Nuggets", 1), ("Waffle Potato Fries (Medium)", 1), ("Medium Lemonade", 1)],
        },
        {
            "name": "Grilled Chicken Meal",
            "description": "Grilled Chicken Sandwich, Waffle Fries, Medium Sweet Tea",
            "items": [("Grilled Chicken Sandwich", 1), ("Waffle Potato Fries (Medium)", 1), ("Medium Sweet Tea", 1)],
        },
        {
            "name": "12pc Nugget Family Meal",
            "description": "12pc Nuggets, Waffle Fries, Mac & Cheese, Large Lemonade",
            "items": [("12 pc Chicken Nuggets", 1), ("Waffle Potato Fries (Medium)", 1),
                      ("Mac & Cheese (Medium)", 1), ("Large Lemonade", 1)],
        },
    ],

    "kfc": [
        {
            "name": "Classic Chicken Meal",
            "description": "Original Recipe Breast, Mashed Potatoes, Biscuit, Large Soft Drink",
            "items": [("Original Recipe Breast", 1), ("Mashed Potatoes w/Gravy", 1),
                      ("Biscuit", 1), ("Large Soft Drink", 1)],
        },
        {
            "name": "KFC Famous Bowl Meal",
            "description": "Famous Bowl, Biscuit, Large Dr Pepper",
            "items": [("Famous Bowl", 1), ("Biscuit", 1), ("Large Dr Pepper", 1)],
        },
        {
            "name": "Chicken Sandwich Meal",
            "description": "Chicken Sandwich, Mashed Potatoes, Large Soft Drink",
            "items": [("Chicken Sandwich", 1), ("Mashed Potatoes w/Gravy", 1), ("Large Soft Drink", 1)],
        },
    ],

    "popeyes": [
        {
            "name": "Classic Chicken Sandwich Meal",
            "description": "Classic Chicken Sandwich, Cajun Fries, Large Soft Drink",
            "items": [("Classic Chicken Sandwich", 1), ("Cajun Fries (Regular)", 1), ("Large Soft Drink", 1)],
        },
        {
            "name": "Spicy Chicken Sandwich Meal",
            "description": "Spicy Chicken Sandwich, Cajun Fries, Large Dr Pepper",
            "items": [("Spicy Chicken Sandwich", 1), ("Cajun Fries (Regular)", 1), ("Large Dr Pepper", 1)],
        },
        {
            "name": "3pc Tenders Meal",
            "description": "3pc Tenders, Red Beans & Rice, Biscuit, Medium Soft Drink",
            "items": [("Tenders (3pc Mild)", 1), ("Red Beans & Rice", 1),
                      ("Biscuit", 1), ("Medium Soft Drink", 1)],
        },
        {
            "name": "Breast Meal",
            "description": "Chicken Breast, Mashed Potatoes, Biscuit, Medium Soft Drink",
            "items": [("Breast (Mild/Spicy)", 1), ("Mashed Potatoes w/Gravy", 1),
                      ("Biscuit", 1), ("Medium Soft Drink", 1)],
        },
    ],

    "taco-bell": [
        {
            "name": "Crunchwrap Meal",
            "description": "Crunchwrap Supreme, Nacho Cheese Doritos Fries, Mountain Dew Baja Blast",
            "items": [("Crunchwrap Supreme", 1), ("Nacho Cheese Doritos Fries", 1),
                      ("Mountain Dew Baja Blast (20oz)", 1)],
        },
        {
            "name": "Taco Combo (3 Crunchy)",
            "description": "3 Crunchy Tacos, Mountain Dew Baja Blast",
            "items": [("Crunchy Taco", 3), ("Mountain Dew Baja Blast (20oz)", 1)],
        },
        {
            "name": "Chalupa Combo",
            "description": "Chalupa Supreme, Crunchy Taco, Mountain Dew Baja Blast",
            "items": [("Chalupa Supreme", 1), ("Crunchy Taco", 1), ("Mountain Dew Baja Blast (20oz)", 1)],
        },
        {
            "name": "Bean Burrito Meal",
            "description": "Bean Burrito, Crunchy Taco, Mountain Dew Baja Blast",
            "items": [("Bean Burrito", 1), ("Crunchy Taco", 1), ("Mountain Dew Baja Blast (20oz)", 1)],
        },
    ],

    "sonic": [
        {
            "name": "Classic Combo",
            "description": "Classic Cheeseburger, Medium Tater Tots, Medium Cherry Limeade",
            "items": [("Classic Cheeseburger", 1), ("Medium Tater Tots", 1), ("Medium Cherry Limeade", 1)],
        },
        {
            "name": "Crispy Chicken Combo",
            "description": "Crispy Chicken Sandwich, Medium Tater Tots, Medium Cherry Limeade",
            "items": [("Crispy Chicken Sandwich", 1), ("Medium Tater Tots", 1), ("Medium Cherry Limeade", 1)],
        },
        {
            "name": "Corn Dog Snack",
            "description": "Corn Dog, Medium Tater Tots, Medium Cherry Limeade",
            "items": [("Corn Dog", 2), ("Medium Tater Tots", 1), ("Medium Cherry Limeade", 1)],
        },
    ],

    "arbys": [
        {
            "name": "Classic Roast Beef Meal",
            "description": "Classic Roast Beef, Medium Curly Fries, Large Soft Drink",
            "items": [("Classic Roast Beef", 1), ("Curly Fries (Medium)", 1), ("Large Soft Drink", 1)],
        },
        {
            "name": "Beef 'n Cheddar Meal",
            "description": "Beef 'n Cheddar Classic, Curly Fries, Large Dr Pepper",
            "items": [("Beef 'n Cheddar Classic", 1), ("Curly Fries (Medium)", 1), ("Large Dr Pepper", 1)],
        },
        {
            "name": "French Dip Meal",
            "description": "French Dip & Swiss, Curly Fries, Large Soft Drink",
            "items": [("French Dip & Swiss", 1), ("Curly Fries (Medium)", 1), ("Large Soft Drink", 1)],
        },
    ],

    "five-guys": [
        {
            "name": "Cheeseburger & Fries",
            "description": "Cheeseburger, Little Fries, Medium Soft Drink",
            "items": [("Cheeseburger", 1), ("Little Fries", 1), ("Medium Soft Drink", 1)],
        },
        {
            "name": "Bacon Burger Meal",
            "description": "Bacon Burger, Regular Fries, Medium Soft Drink",
            "items": [("Bacon Burger", 1), ("Regular Fries", 1), ("Medium Soft Drink", 1)],
        },
        {
            "name": "Little Hamburger Meal",
            "description": "Little Hamburger, Little Fries, Medium Soft Drink",
            "items": [("Little Hamburger", 1), ("Little Fries", 1), ("Medium Soft Drink", 1)],
        },
    ],

    "chipotle": [
        {
            "name": "Chicken Burrito Bowl",
            "description": "Chicken Bowl, White Rice, Black Beans, Cheese, Mild Salsa",
            "items": [("Chicken Burrito Bowl", 1)],
        },
        {
            "name": "Chicken Burrito Meal",
            "description": "Chicken Burrito + Chips & Guac",
            "items": [("Chicken Burrito", 1), ("Chips", 1), ("Guacamole", 1)],
        },
        {
            "name": "Steak Bowl",
            "description": "Steak Bowl, Brown Rice, Black Beans, Sour Cream",
            "items": [("Steak Burrito Bowl", 1)],
        },
        {
            "name": "Chicken Tacos Meal",
            "description": "3 Chicken Tacos + Chips",
            "items": [("Chicken Tacos (3)", 1), ("Chips", 1)],
        },
    ],

    "panera": [
        {
            "name": "You Pick Two — Soup & Sandwich",
            "description": "Broccoli Cheddar Soup + Turkey Sandwich",
            "items": [("Broccoli Cheddar Soup (Bowl)", 1), ("Turkey Pesto Sandwich", 1)],
        },
        {
            "name": "Mac & Cheese Meal",
            "description": "Mac & Cheese + Broccoli Cheddar Soup + Lemonade",
            "items": [("Mac & Cheese (Bowl)", 1), ("Broccoli Cheddar Soup (Bowl)", 1),
                      ("Strawberry Banana Smoothie", 1)],
        },
        {
            "name": "Fuji Apple Salad Meal",
            "description": "Fuji Apple Chicken Salad + Blueberry Muffin",
            "items": [("Fuji Apple Chicken Salad", 1), ("Blueberry Muffin", 1)],
        },
    ],

    "dairy-queen": [
        {
            "name": "Cheeseburger Blizzard Combo",
            "description": "DQ Cheeseburger, Medium Fries, Oreo Blizzard",
            "items": [("DQ Cheeseburger", 1), ("Medium French Fries", 1), ("Blizzard Oreo (Medium)", 1)],
        },
        {
            "name": "1/4 lb Burger Meal",
            "description": "1/4 lb GrillBurger, Medium Fries, Medium Soft Drink",
            "items": [("1/4 lb GrillBurger", 1), ("Medium French Fries", 1), ("Medium Soft Drink", 1)],
        },
        {
            "name": "Chicken Strip Basket",
            "description": "4pc Chicken Strip Basket, Large Soft Drink",
            "items": [("Chicken Strip Basket (4pc)", 1), ("Large Soft Drink", 1)],
        },
    ],

    "culvers": [
        {
            "name": "ButterBurger Basket",
            "description": "ButterBurger The Original, Crinkle Cut Fries, Medium Soft Drink",
            "items": [("ButterBurger The Original", 1), ("Crinkle Cut Fries (Reg)", 1), ("Medium Soft Drink", 1)],
        },
        {
            "name": "Double ButterBurger Meal",
            "description": "Double ButterBurger w/Cheese, Crinkle Cut Fries, Large Soft Drink",
            "items": [("Double ButterBurger w/Cheese", 1), ("Crinkle Cut Fries (Reg)", 1), ("Large Soft Drink", 1)],
        },
        {
            "name": "Cheese Curd Snack Combo",
            "description": "Fresh Cheese Curds, Vanilla Dish Custard, Medium Soft Drink",
            "items": [("Fresh Cheese Curds", 1), ("Vanilla Dish", 1), ("Medium Soft Drink", 1)],
        },
    ],

    "whataburger": [
        {
            "name": "Whataburger Large Combo",
            "description": "Whataburger, Large Fries, Large Dr Pepper",
            "items": [("Whataburger", 1), ("Medium French Fries", 1), ("Large Dr Pepper", 1)],
        },
        {
            "name": "Double Whataburger Meal",
            "description": "Double Whataburger, Medium Fries, Medium Soft Drink",
            "items": [("Double Whataburger", 1), ("Medium French Fries", 1), ("Medium Soft Drink", 1)],
        },
        {
            "name": "Honey Butter Chicken Breakfast",
            "description": "Honey Butter Chicken Biscuit, Medium Soft Drink",
            "items": [("Honey Butter Chicken Biscuit", 1), ("Medium Soft Drink", 1)],
        },
    ],

    "shake-shack": [
        {
            "name": "ShackBurger Meal",
            "description": "ShackBurger, Crinkle Cut Fries, Vanilla Shake",
            "items": [("ShackBurger", 1), ("Crinkle Cut Fries", 1), ("Vanilla Shake", 1)],
        },
        {
            "name": "SmokeShack Combo",
            "description": "SmokeShack, Cheese Fries, Vanilla Shake",
            "items": [("SmokeShack", 1), ("Cheese Fries", 1), ("Vanilla Shake", 1)],
        },
        {
            "name": "Chick'n Shack Meal",
            "description": "Chick'n Shack, Crinkle Cut Fries, Vanilla Shake",
            "items": [("Chick'n Shack", 1), ("Crinkle Cut Fries", 1), ("Vanilla Shake", 1)],
        },
    ],

    "subway": [
        {
            "name": "Italian BMT Footlong Combo",
            "description": "Italian BMT Footlong, Chips, Medium Soft Drink",
            "items": [("Italian BMT (6\")", 2), ("Chips", 1)],
        },
        {
            "name": "Turkey Breast Meal",
            "description": "Turkey Breast 6-inch, Chips",
            "items": [("Turkey Breast (6\")", 1), ("Chips", 1)],
        },
        {
            "name": "Meatball Marinara Combo",
            "description": "Meatball Marinara Footlong, Chips",
            "items": [("Meatball Marinara (6\")", 2), ("Chips", 1)],
        },
    ],

    "in-n-out": [
        {
            "name": "Double-Double Combo",
            "description": "Double-Double, French Fries, Medium Soft Drink",
            "items": [("Double-Double", 1), ("French Fries", 1), ("Medium Soft Drink", 1)],
        },
        {
            "name": "Cheeseburger Combo",
            "description": "Cheeseburger, French Fries, Medium Soft Drink",
            "items": [("Cheeseburger", 1), ("French Fries", 1), ("Medium Soft Drink", 1)],
        },
        {
            "name": "Animal Style Combo",
            "description": "Animal Style Burger, Animal Style Fries, Medium Soft Drink",
            "items": [("Animal Style Burger", 1), ("Animal Style Fries", 1), ("Medium Soft Drink", 1)],
        },
        {
            "name": "Protein Style Meal",
            "description": "Protein Style Burger (no bun), French Fries, Lemonade",
            "items": [("Protein Style (no bun)", 1), ("French Fries", 1)],
        },
    ],

    "five-guys": [
        {
            "name": "Cheeseburger & Fries",
            "description": "Cheeseburger, Little Fries, Medium Soft Drink",
            "items": [("Cheeseburger", 1), ("Little Fries", 1), ("Medium Soft Drink", 1)],
        },
        {
            "name": "Bacon Burger Meal",
            "description": "Bacon Burger, Regular Fries, Medium Soft Drink",
            "items": [("Bacon Burger", 1), ("Regular Fries", 1), ("Medium Soft Drink", 1)],
        },
    ],
}


async def get_chain_id(session: AsyncSession, slug: str) -> int | None:
    row = (await session.execute(
        text("SELECT id FROM restaurant_chains WHERE slug = :slug"), {"slug": slug}
    )).fetchone()
    return row[0] if row else None


async def get_item_id(session: AsyncSession, chain_id: int, name: str) -> int | None:
    row = (await session.execute(
        text("SELECT id FROM menu_items WHERE chain_id = :cid AND name = :name"),
        {"cid": chain_id, "name": name},
    )).fetchone()
    return row[0] if row else None


async def seed_presets(slugs: list[str] | None = None):
    targets = slugs or list(PRESETS.keys())
    async with SessionLocal() as session:
        for slug in targets:
            combos = PRESETS.get(slug, [])
            if not combos:
                continue

            chain_id = await get_chain_id(session, slug)
            if not chain_id:
                print(f"  ⚠ Chain not found: {slug} — run --seed first")
                continue

            saved = 0
            for order, combo in enumerate(combos):
                # Skip if already exists
                exists = (await session.execute(
                    text("SELECT 1 FROM preset_meals WHERE chain_id = :cid AND name = :name"),
                    {"cid": chain_id, "name": combo["name"]},
                )).fetchone()
                if exists:
                    continue

                result = await session.execute(
                    text("""
                        INSERT INTO preset_meals (chain_id, name, description, category, display_order)
                        VALUES (:cid, :name, :desc, 'popular', :ord) RETURNING id
                    """),
                    {"cid": chain_id, "name": combo["name"],
                     "desc": combo.get("description", ""), "ord": order},
                )
                preset_id = result.fetchone()[0]

                for item_name, qty in combo["items"]:
                    item_id = await get_item_id(session, chain_id, item_name)
                    if not item_id:
                        print(f"    ⚠ Item not found: '{item_name}' in {slug}")
                        continue
                    await session.execute(
                        text("""
                            INSERT INTO preset_meal_items (preset_meal_id, menu_item_id, quantity)
                            VALUES (:pmid, :miid, :qty)
                        """),
                        {"pmid": preset_id, "miid": item_id, "qty": qty},
                    )
                saved += 1

            await session.commit()
            if saved:
                print(f"  ✓ {slug}: {saved} preset meals saved")


# ─────────────────────────────────────────────────────────────────────────────
# Healthy preset generator — queries health scores from DB automatically
# ─────────────────────────────────────────────────────────────────────────────

# Category name fragments that mark non-entree items
_SIDE_PAT    = r"side|fries|salad|soup|tots|coleslaw|ring|bread|biscuit|beans|rice|applesauce|fruit"
_DRINK_PAT   = r"drink|beverage|coffee|tea|lemonade|limeade|shake|frosty|smoothie|juice|cold brew|blast|frappuccino|milkshake|slushie|soda"
_DESSERT_PAT = r"dessert|cookie|cake|pie|sundae|brownie|muffin|donut|churro|cinnamon|blizzard|flurry|custard|concrete"
_EXCLUDE_PAT = (
    r"side|fries|salad|soup|tots|coleslaw|ring|bread|biscuit|beans|rice|fruit"
    r"|drink|beverage|coffee|tea|lemonade|limeade|shake|frosty|smoothie|juice|cold brew|blast|frappuccino|milkshake"
    r"|dessert|cookie|cake|pie|sundae|brownie|muffin|donut|churro|cinnamon|blizzard|flurry|custard|concrete"
    r"|sauce|condiment|ingredient|dip|dressing|snack|appetizer|bakery"
)


async def _query(session, sql: str, params: dict):
    return (await session.execute(text(sql), params)).fetchall()


async def _upsert_healthy_preset(
    session, chain_id: int, name: str, description: str,
    item_ids: list[tuple[int, int]], order: int,
):
    """Insert or skip if already exists (idempotent)."""
    exists = (await session.execute(
        text("SELECT 1 FROM preset_meals WHERE chain_id = :cid AND name = :name"),
        {"cid": chain_id, "name": name},
    )).fetchone()
    if exists:
        return False

    result = await session.execute(
        text("""
            INSERT INTO preset_meals (chain_id, name, description, category, display_order)
            VALUES (:cid, :name, :desc, 'healthy', :ord) RETURNING id
        """),
        {"cid": chain_id, "name": name, "desc": description, "ord": order},
    )
    preset_id = result.fetchone()[0]
    for item_id, qty in item_ids:
        await session.execute(
            text("INSERT INTO preset_meal_items (preset_meal_id, menu_item_id, quantity) VALUES (:pmid, :miid, :qty)"),
            {"pmid": preset_id, "miid": item_id, "qty": qty},
        )
    return True


async def seed_healthy_presets(slugs: list[str] | None = None):
    """
    Auto-generate three healthy preset types for every chain:
      1. Healthiest Overall  — lowest health_score entree + best side + diet/low-cal drink
      2. Lowest Calorie      — lowest calorie entree + lightest available side
      3. High Protein        — highest protein entree + highest protein side
    Uses health_score from the DB so it stays accurate as data is updated.
    """

    # SQL: N best items from a chain filtered by category pattern
    ENTREE_SQL = """
        SELECT mi.id, mi.name, mc.name AS cat, ni.health_score, ni.calories, ni.protein_g
        FROM menu_items mi
        JOIN nutrition_info ni ON ni.menu_item_id = mi.id
        LEFT JOIN menu_categories mc ON mc.id = mi.category_id
        WHERE mi.chain_id = :cid
          AND mi.is_available = true
          AND ni.calories >= 150
          AND NOT COALESCE(mc.name,'') ~* :exclude
        ORDER BY ni.health_score ASC
        LIMIT :n
    """
    ENTREE_CAL_SQL = ENTREE_SQL.replace("ORDER BY ni.health_score ASC", "ORDER BY ni.calories ASC")
    ENTREE_PROT_SQL = """
        SELECT mi.id, mi.name, mc.name AS cat, ni.health_score, ni.calories, ni.protein_g
        FROM menu_items mi
        JOIN nutrition_info ni ON ni.menu_item_id = mi.id
        LEFT JOIN menu_categories mc ON mc.id = mi.category_id
        WHERE mi.chain_id = :cid
          AND mi.is_available = true
          AND ni.calories >= 150
          AND NOT COALESCE(mc.name,'') ~* :exclude
        ORDER BY ni.protein_g DESC NULLS LAST
        LIMIT :n
    """
    SIDE_SQL = """
        SELECT mi.id, mi.name, ni.health_score, ni.calories, ni.protein_g
        FROM menu_items mi
        JOIN nutrition_info ni ON ni.menu_item_id = mi.id
        LEFT JOIN menu_categories mc ON mc.id = mi.category_id
        WHERE mi.chain_id = :cid
          AND mi.is_available = true
          AND COALESCE(mc.name,'') ~* :side_pat
          AND NOT COALESCE(mc.name,'') ~* :drink_pat
        ORDER BY ni.health_score ASC
        LIMIT :n
    """
    DRINK_SQL = """
        SELECT mi.id, mi.name, ni.calories
        FROM menu_items mi
        JOIN nutrition_info ni ON ni.menu_item_id = mi.id
        LEFT JOIN menu_categories mc ON mc.id = mi.category_id
        WHERE mi.chain_id = :cid
          AND mi.is_available = true
          AND COALESCE(mc.name,'') ~* :drink_pat
        ORDER BY ni.calories ASC
        LIMIT 1
    """

    params_base = {
        "exclude":   _EXCLUDE_PAT,
        "side_pat":  _SIDE_PAT,
        "drink_pat": _DRINK_PAT,
    }

    # Resolve which chains to process
    if slugs:
        chain_slugs = slugs
    else:
        async with SessionLocal() as s:
            rows = (await s.execute(text("SELECT slug FROM restaurant_chains ORDER BY name"))).fetchall()
        chain_slugs = [r[0] for r in rows]

    async with SessionLocal() as session:
        for slug in chain_slugs:
            chain_id = await get_chain_id(session, slug)
            if not chain_id:
                continue

            p = {**params_base, "cid": chain_id, "n": 3}

            entrees      = await _query(session, ENTREE_SQL,      p)
            entrees_cal  = await _query(session, ENTREE_CAL_SQL,  p)
            entrees_prot = await _query(session, ENTREE_PROT_SQL, p)
            sides        = await _query(session, SIDE_SQL,        {**params_base, "cid": chain_id, "n": 3})
            drinks       = await _query(session, DRINK_SQL,       {**params_base, "cid": chain_id})

            if not entrees:
                continue

            chain_name_row = (await session.execute(
                text("SELECT name FROM restaurant_chains WHERE id = :id"), {"id": chain_id}
            )).fetchone()
            chain_name = chain_name_row[0] if chain_name_row else slug
            saved = 0

            # ── 1. Healthiest Overall ─────────────────────────────────────
            entree = entrees[0]
            items  = [(entree[0], 1)]
            parts  = [entree[1]]
            if sides:
                items.append((sides[0][0], 1))
                parts.append(sides[0][1])
            if drinks:
                items.append((drinks[0][0], 1))
                parts.append(drinks[0][1])
            ok = await _upsert_healthy_preset(
                session, chain_id,
                f"Healthiest {chain_name} Meal",
                f"Lowest overall nutrition score: {', '.join(parts)}",
                items, order=0,
            )
            if ok: saved += 1

            # ── 2. Lowest Calorie ─────────────────────────────────────────
            if entrees_cal:
                entree_c = entrees_cal[0]
                items_c  = [(entree_c[0], 1)]
                parts_c  = [entree_c[1]]
                if sides:
                    items_c.append((sides[0][0], 1))
                    parts_c.append(sides[0][1])
                if drinks:
                    items_c.append((drinks[0][0], 1))
                    parts_c.append(drinks[0][1])
                ok = await _upsert_healthy_preset(
                    session, chain_id,
                    f"Lowest Calorie {chain_name} Meal",
                    f"Fewest calories: {', '.join(parts_c)}",
                    items_c, order=1,
                )
                if ok: saved += 1

            # ── 3. High Protein ───────────────────────────────────────────
            if entrees_prot:
                entree_p = entrees_prot[0]
                items_p  = [(entree_p[0], 1)]
                parts_p  = [entree_p[1]]
                # Pair with highest-protein side
                sides_prot = await _query(session, SIDE_SQL.replace(
                    "ORDER BY ni.health_score ASC",
                    "ORDER BY ni.protein_g DESC NULLS LAST"
                ), {**params_base, "cid": chain_id, "n": 1})
                if sides_prot:
                    items_p.append((sides_prot[0][0], 1))
                    parts_p.append(sides_prot[0][1])
                if drinks:
                    items_p.append((drinks[0][0], 1))
                    parts_p.append(drinks[0][1])
                ok = await _upsert_healthy_preset(
                    session, chain_id,
                    f"High Protein {chain_name} Meal",
                    f"Maximum protein: {', '.join(parts_p)}",
                    items_p, order=2,
                )
                if ok: saved += 1

            await session.commit()
            if saved:
                print(f"  ✓ {chain_name}: {saved} healthy presets saved")
