from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy import func, select, text
from sqlalchemy.ext.asyncio import AsyncSession
import httpx

from app.database import get_db
from app.models import RestaurantLocation
from app.schemas import LocationSchema

router = APIRouter(prefix="/locations", tags=["locations"])

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"


@router.get("/geocode")
async def geocode(q: str = Query(..., description="City, zip, or address")):
    """Convert a city/zip string to lat/lon using Nominatim."""
    async with httpx.AsyncClient(headers={"User-Agent": "NutritionApp/1.0 (personal)"}) as client:
        resp = await client.get(
            NOMINATIM_URL,
            params={"q": q, "format": "json", "limit": 1},
        )
        resp.raise_for_status()
        data = resp.json()
    if not data:
        return {"error": "Location not found"}
    return {"lat": float(data[0]["lat"]), "lon": float(data[0]["lon"]), "display_name": data[0]["display_name"]}


@router.get("/chain/{chain_id}", response_model=list[LocationSchema])
async def locations_for_chain(chain_id: int, db: AsyncSession = Depends(get_db)):
    stmt = (
        select(RestaurantLocation)
        .where(RestaurantLocation.chain_id == chain_id)
        .order_by(RestaurantLocation.state, RestaurantLocation.city)
    )
    rows = (await db.execute(stmt)).scalars().all()
    return [LocationSchema.model_validate(r) for r in rows]
