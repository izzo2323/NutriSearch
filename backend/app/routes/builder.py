from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models import RestaurantChain, MenuItem, NutritionInfo
from app.schemas import MenuItemSchema
from app.builder_config import BUILDER_CONFIGS

router = APIRouter(prefix="/builder", tags=["builder"])


@router.get("/{chain_id}")
async def get_builder_config(chain_id: int, db: AsyncSession = Depends(get_db)):
    """
    Returns the ingredient-builder config for a chain, with full item+nutrition
    data attached to each ingredient slot. Returns null if the chain has no config.
    """
    stmt = select(RestaurantChain).where(RestaurantChain.id == chain_id)
    chain = (await db.execute(stmt)).scalar_one_or_none()
    if not chain:
        raise HTTPException(status_code=404, detail="Chain not found")

    config = BUILDER_CONFIGS.get(chain.slug)
    if not config:
        return {"has_builder": False}

    # Collect all item names referenced by the config
    all_names: set[str] = set()
    for mt in config["meal_types"]:
        all_names.update(mt["base_items"])
    for grp in config["ingredient_groups"]:
        all_names.update(grp["items"])

    # Fetch them all in one query
    stmt = (
        select(MenuItem)
        .where(MenuItem.chain_id == chain_id)
        .where(MenuItem.name.in_(all_names))
        .options(
            selectinload(MenuItem.nutrition),
            selectinload(MenuItem.category),
            selectinload(MenuItem.chain),
        )
    )
    rows = (await db.execute(stmt)).scalars().all()
    item_map: dict[str, dict] = {
        row.name: MenuItemSchema.model_validate(row).model_dump()
        for row in rows
    }

    # Attach item data into the config
    hydrated_groups = []
    for grp in config["ingredient_groups"]:
        hydrated_groups.append({
            **grp,
            "items": [
                {"name": n, "item": item_map.get(n)}
                for n in grp["items"]
            ],
        })

    hydrated_types = []
    for mt in config["meal_types"]:
        hydrated_types.append({
            **mt,
            "base_items": [
                {"name": n, "item": item_map.get(n)}
                for n in mt["base_items"]
            ],
        })

    return {
        "has_builder":        True,
        "meal_types":         hydrated_types,
        "ingredient_groups":  hydrated_groups,
    }
