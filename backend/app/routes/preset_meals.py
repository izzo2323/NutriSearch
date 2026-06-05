from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import PresetMeal, PresetMealItem, MenuItem
from app.schemas import PresetMealSchema, MealTotals

router = APIRouter(prefix="/preset-meals", tags=["preset-meals"])


def _f(val) -> float:
    return float(val) if val is not None else 0.0


def _compute_totals(preset: PresetMeal) -> MealTotals:
    t = MealTotals(
        calories=0, total_fat_g=0, saturated_fat_g=0, trans_fat_g=0,
        cholesterol_mg=0, sodium_mg=0, total_carbs_g=0,
        dietary_fiber_g=0, total_sugars_g=0, protein_g=0,
    )
    for pmi in preset.items:
        n   = pmi.menu_item.nutrition
        qty = pmi.quantity
        if not n:
            continue
        t.calories        += int(_f(n.calories)        * qty)
        t.total_fat_g     += _f(n.total_fat_g)         * qty
        t.saturated_fat_g += _f(n.saturated_fat_g)     * qty
        t.trans_fat_g     += _f(n.trans_fat_g)         * qty
        t.cholesterol_mg  += int(_f(n.cholesterol_mg)  * qty)
        t.sodium_mg       += int(_f(n.sodium_mg)       * qty)
        t.total_carbs_g   += _f(n.total_carbs_g)       * qty
        t.dietary_fiber_g += _f(n.dietary_fiber_g)     * qty
        t.total_sugars_g  += _f(n.total_sugars_g)      * qty
        t.protein_g       += _f(n.protein_g)           * qty
    return t


@router.get("", response_model=list[PresetMealSchema])
async def list_preset_meals(
    chain_id: int | None = None,
    category: str | None = None,
    db: AsyncSession = Depends(get_db),
):
    stmt = (
        select(PresetMeal)
        .options(
            selectinload(PresetMeal.chain),
            selectinload(PresetMeal.items).selectinload(PresetMealItem.menu_item)
                .selectinload(MenuItem.nutrition),
            selectinload(PresetMeal.items).selectinload(PresetMealItem.menu_item)
                .selectinload(MenuItem.chain),
            selectinload(PresetMeal.items).selectinload(PresetMealItem.menu_item)
                .selectinload(MenuItem.category),
        )
        .order_by(PresetMeal.chain_id, PresetMeal.display_order)
    )
    if chain_id:
        stmt = stmt.where(PresetMeal.chain_id == chain_id)
    if category:
        stmt = stmt.where(PresetMeal.category == category)

    rows = (await db.execute(stmt)).scalars().all()

    result = []
    for preset in rows:
        s = PresetMealSchema.model_validate(preset)
        s.totals = _compute_totals(preset)
        result.append(s)
    return result
