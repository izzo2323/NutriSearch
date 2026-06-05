"""Persist scraped nutrition data to PostgreSQL."""
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy import select, text
from base_scraper import BaseScraper, MenuItemData

DATABASE_URL = os.environ["DATABASE_URL"]
engine = create_async_engine(DATABASE_URL)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def upsert_chain(session: AsyncSession, scraper: BaseScraper) -> int:
    row = (await session.execute(
        text("SELECT id FROM restaurant_chains WHERE slug = :slug"),
        {"slug": scraper.slug},
    )).fetchone()
    if row:
        return row[0]
    result = await session.execute(
        text("""
            INSERT INTO restaurant_chains (name, slug, website, cuisine_type)
            VALUES (:name, :slug, :website, :cuisine_type)
            RETURNING id
        """),
        {
            "name": scraper.name,
            "slug": scraper.slug,
            "website": scraper.website,
            "cuisine_type": scraper.cuisine_type,
        },
    )
    await session.commit()
    return result.fetchone()[0]


async def upsert_category(session: AsyncSession, chain_id: int, category_name: str) -> int:
    row = (await session.execute(
        text("SELECT id FROM menu_categories WHERE chain_id = :cid AND name = :name"),
        {"cid": chain_id, "name": category_name},
    )).fetchone()
    if row:
        return row[0]
    result = await session.execute(
        text("""
            INSERT INTO menu_categories (chain_id, name)
            VALUES (:cid, :name)
            RETURNING id
        """),
        {"cid": chain_id, "name": category_name},
    )
    await session.commit()
    return result.fetchone()[0]


async def upsert_item(
    session: AsyncSession,
    chain_id: int,
    category_id: int,
    item: MenuItemData,
):
    row = (await session.execute(
        text("SELECT id FROM menu_items WHERE chain_id = :cid AND name = :name"),
        {"cid": chain_id, "name": item.name},
    )).fetchone()

    if row:
        item_id = row[0]
    else:
        result = await session.execute(
            text("""
                INSERT INTO menu_items (chain_id, category_id, name, description, serving_size)
                VALUES (:cid, :catid, :name, :desc, :serving)
                RETURNING id
            """),
            {
                "cid": chain_id,
                "catid": category_id,
                "name": item.name,
                "desc": item.description,
                "serving": item.serving_size,
            },
        )
        item_id = result.fetchone()[0]

    await session.execute(
        text("""
            INSERT INTO nutrition_info (
                menu_item_id, calories, total_fat_g, saturated_fat_g, trans_fat_g,
                cholesterol_mg, sodium_mg, total_carbs_g, dietary_fiber_g,
                total_sugars_g, added_sugars_g, protein_g,
                vitamin_d_mcg, calcium_mg, iron_mg, potassium_mg
            ) VALUES (
                :mid, :cal, :fat, :sat, :trans,
                :chol, :sod, :carb, :fiber,
                :sugar, :added_sugar, :prot,
                :vd, :ca, :fe, :k
            )
            ON CONFLICT (menu_item_id) DO UPDATE SET
                calories        = EXCLUDED.calories,
                total_fat_g     = EXCLUDED.total_fat_g,
                saturated_fat_g = EXCLUDED.saturated_fat_g,
                trans_fat_g     = EXCLUDED.trans_fat_g,
                cholesterol_mg  = EXCLUDED.cholesterol_mg,
                sodium_mg       = EXCLUDED.sodium_mg,
                total_carbs_g   = EXCLUDED.total_carbs_g,
                dietary_fiber_g = EXCLUDED.dietary_fiber_g,
                total_sugars_g  = EXCLUDED.total_sugars_g,
                added_sugars_g  = EXCLUDED.added_sugars_g,
                protein_g       = EXCLUDED.protein_g,
                updated_at      = NOW()
        """),
        {
            "mid": item_id,
            "cal": item.calories,
            "fat": item.total_fat_g,
            "sat": item.saturated_fat_g,
            "trans": item.trans_fat_g,
            "chol": item.cholesterol_mg,
            "sod": item.sodium_mg,
            "carb": item.total_carbs_g,
            "fiber": item.dietary_fiber_g,
            "sugar": item.total_sugars_g,
            "added_sugar": item.added_sugars_g,
            "prot": item.protein_g,
            "vd": item.vitamin_d_mcg,
            "ca": item.calcium_mg,
            "fe": item.iron_mg,
            "k": item.potassium_mg,
        },
    )
    await session.commit()


async def persist(scraper: BaseScraper, items: list[MenuItemData]):
    async with SessionLocal() as session:
        chain_id = await upsert_chain(session, scraper)
        for item in items:
            category_id = await upsert_category(session, chain_id, item.category)
            await upsert_item(session, chain_id, category_id, item)
    print(f"  ✓ {scraper.name}: {len(items)} items saved")
