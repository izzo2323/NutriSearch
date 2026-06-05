from typing import Literal, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models import MenuItem, NutritionInfo, MenuCategory
from app.schemas import MenuItemSchema

router = APIRouter(prefix="/menu-items", tags=["menu-items"])

SortField = Literal[
    "healthiest", "unhealthiest",
    "calories_asc", "calories_desc",
    "protein_desc", "carbs_asc",
    "sodium_asc", "fat_asc",
]

SORT_MAP: dict[str, tuple[object, str]] = {
    "healthiest":    (NutritionInfo.health_score,   "asc"),
    "unhealthiest":  (NutritionInfo.health_score,   "desc"),
    "calories_asc":  (NutritionInfo.calories,       "asc"),
    "calories_desc": (NutritionInfo.calories,       "desc"),
    "protein_desc":  (NutritionInfo.protein_g,      "desc"),
    "carbs_asc":     (NutritionInfo.total_carbs_g,  "asc"),
    "sodium_asc":    (NutritionInfo.sodium_mg,      "asc"),
    "fat_asc":       (NutritionInfo.total_fat_g,    "asc"),
}


@router.get("", response_model=list[MenuItemSchema])
async def list_menu_items(
    q: Optional[str] = Query(None, description="Search item name"),
    chain_id: Optional[int] = None,
    category_id: Optional[int] = None,
    sort: SortField = "healthiest",
    max_calories: Optional[int] = None,
    limit: int = Query(50, le=200),
    offset: int = 0,
    db: AsyncSession = Depends(get_db),
):
    sort_col, sort_dir = SORT_MAP[sort]
    order = sort_col.asc() if sort_dir == "asc" else sort_col.desc()

    stmt = (
        select(MenuItem)
        .join(NutritionInfo, NutritionInfo.menu_item_id == MenuItem.id)
        .options(
            selectinload(MenuItem.chain),
            selectinload(MenuItem.category),
            selectinload(MenuItem.nutrition),
        )
        .where(MenuItem.is_available == True)
        .order_by(order)
        .limit(limit)
        .offset(offset)
    )

    if q:
        stmt = stmt.where(MenuItem.name.ilike(f"%{q}%"))
    if chain_id:
        stmt = stmt.where(MenuItem.chain_id == chain_id)
    if category_id:
        stmt = stmt.where(MenuItem.category_id == category_id)
    if max_calories is not None:
        stmt = stmt.where(NutritionInfo.calories <= max_calories)

    rows = (await db.execute(stmt)).scalars().all()
    return [MenuItemSchema.model_validate(r) for r in rows]


@router.get("/{item_id}", response_model=MenuItemSchema)
async def get_menu_item(item_id: int, db: AsyncSession = Depends(get_db)):
    stmt = (
        select(MenuItem)
        .where(MenuItem.id == item_id)
        .options(
            selectinload(MenuItem.chain),
            selectinload(MenuItem.category),
            selectinload(MenuItem.nutrition),
        )
    )
    item = (await db.execute(stmt)).scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return MenuItemSchema.model_validate(item)


@router.get("/chain/{chain_id}/categories", response_model=list[dict])
async def get_chain_categories(chain_id: int, db: AsyncSession = Depends(get_db)):
    stmt = (
        select(MenuCategory)
        .where(MenuCategory.chain_id == chain_id)
        .order_by(MenuCategory.display_order)
    )
    rows = (await db.execute(stmt)).scalars().all()
    return [{"id": r.id, "name": r.name} for r in rows]
