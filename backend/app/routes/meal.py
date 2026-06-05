from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.database import get_db
from app.models import MenuItem
from app.schemas import (
    MealRequest, MealResponse, MealTotals, DailyValuePct, MenuItemSchema
)

router = APIRouter(prefix="/meal", tags=["meal"])

# FDA 2000-calorie daily reference values
DAILY_VALUES = {
    "calories":      2000,
    "total_fat_g":   78,
    "saturated_fat_g": 20,
    "cholesterol_mg": 300,
    "sodium_mg":     2300,
    "total_carbs_g": 275,
    "dietary_fiber_g": 28,
    "protein_g":     50,
}


def _f(val) -> float:
    return float(val) if val is not None else 0.0


@router.post("/analyze", response_model=MealResponse)
async def analyze_meal(body: MealRequest, db: AsyncSession = Depends(get_db)):
    ids = [i.menu_item_id for i in body.items]
    qty_map = {i.menu_item_id: i.quantity for i in body.items}

    stmt = (
        select(MenuItem)
        .where(MenuItem.id.in_(ids))
        .options(
            selectinload(MenuItem.chain),
            selectinload(MenuItem.category),
            selectinload(MenuItem.nutrition),
        )
    )
    db_items = {row.id: row for row in (await db.execute(stmt)).scalars().all()}

    missing = set(ids) - set(db_items.keys())
    if missing:
        raise HTTPException(status_code=404, detail=f"Menu items not found: {missing}")

    totals = MealTotals(
        calories=0, total_fat_g=0, saturated_fat_g=0, trans_fat_g=0,
        cholesterol_mg=0, sodium_mg=0, total_carbs_g=0,
        dietary_fiber_g=0, total_sugars_g=0, protein_g=0,
    )

    items_out = []
    for item_id in ids:
        item = db_items[item_id]
        qty  = qty_map[item_id]
        n    = item.nutrition
        if n:
            totals.calories        += int(_f(n.calories)        * qty)
            totals.total_fat_g     += _f(n.total_fat_g)         * qty
            totals.saturated_fat_g += _f(n.saturated_fat_g)     * qty
            totals.trans_fat_g     += _f(n.trans_fat_g)         * qty
            totals.cholesterol_mg  += int(_f(n.cholesterol_mg)  * qty)
            totals.sodium_mg       += int(_f(n.sodium_mg)       * qty)
            totals.total_carbs_g   += _f(n.total_carbs_g)       * qty
            totals.dietary_fiber_g += _f(n.dietary_fiber_g)     * qty
            totals.total_sugars_g  += _f(n.total_sugars_g)      * qty
            totals.protein_g       += _f(n.protein_g)           * qty
        items_out.append(MenuItemSchema.model_validate(item))

    def pct(actual, key):
        dv = DAILY_VALUES.get(key, 1)
        return round(actual / dv * 100, 1)

    daily_pct = DailyValuePct(
        calories=pct(totals.calories, "calories"),
        total_fat=pct(totals.total_fat_g, "total_fat_g"),
        saturated_fat=pct(totals.saturated_fat_g, "saturated_fat_g"),
        cholesterol=pct(totals.cholesterol_mg, "cholesterol_mg"),
        sodium=pct(totals.sodium_mg, "sodium_mg"),
        total_carbs=pct(totals.total_carbs_g, "total_carbs_g"),
        dietary_fiber=pct(totals.dietary_fiber_g, "dietary_fiber_g"),
        protein=pct(totals.protein_g, "protein_g"),
    )

    return MealResponse(items=items_out, totals=totals, daily_pct=daily_pct)
