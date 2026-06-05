from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func, select, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db
from app.models import RestaurantChain, RestaurantLocation, MenuItem
from app.schemas import ChainDetailSchema, ChainSummary, LocationSchema

router = APIRouter(prefix="/restaurants", tags=["restaurants"])


@router.get("", response_model=list[ChainDetailSchema])
async def list_chains(
    q: Optional[str] = Query(None, description="Search by name"),
    cuisine: Optional[str] = None,
    limit: int = Query(50, le=200),
    offset: int = 0,
    db: AsyncSession = Depends(get_db),
):
    stmt = (
        select(
            RestaurantChain,
            func.count(RestaurantLocation.id.distinct()).label("location_count"),
            func.count(MenuItem.id.distinct()).label("item_count"),
        )
        .outerjoin(RestaurantLocation, RestaurantLocation.chain_id == RestaurantChain.id)
        .outerjoin(MenuItem, MenuItem.chain_id == RestaurantChain.id)
        .group_by(RestaurantChain.id)
        .order_by(RestaurantChain.name)
        .limit(limit)
        .offset(offset)
    )
    if q:
        stmt = stmt.where(RestaurantChain.name.ilike(f"%{q}%"))
    if cuisine:
        stmt = stmt.where(RestaurantChain.cuisine_type.ilike(f"%{cuisine}%"))

    rows = (await db.execute(stmt)).all()
    result = []
    for chain, loc_count, item_count in rows:
        d = ChainDetailSchema.model_validate(chain)
        d.location_count = loc_count
        d.item_count = item_count
        result.append(d)
    return result


@router.get("/near", response_model=list[LocationSchema])
async def restaurants_near(
    lat: float = Query(..., description="Latitude"),
    lon: float = Query(..., description="Longitude"),
    radius_km: float = Query(25.0, le=100),
    limit: int = Query(50, le=200),
    db: AsyncSession = Depends(get_db),
):
    point = f"SRID=4326;POINT({lon} {lat})"
    stmt = (
        select(
            RestaurantLocation,
            (
                func.ST_Distance(
                    RestaurantLocation.geom,
                    func.ST_GeogFromText(point),
                ) / 1000
            ).label("distance_km"),
        )
        .where(
            func.ST_DWithin(
                RestaurantLocation.geom,
                func.ST_GeogFromText(point),
                radius_km * 1000,
            )
        )
        .order_by(text("distance_km"))
        .limit(limit)
    )
    rows = (await db.execute(stmt)).all()
    result = []
    for loc, dist in rows:
        s = LocationSchema.model_validate(loc)
        s.distance_km = round(dist, 2)
        result.append(s)
    return result


@router.get("/{chain_id}", response_model=ChainDetailSchema)
async def get_chain(chain_id: int, db: AsyncSession = Depends(get_db)):
    stmt = (
        select(
            RestaurantChain,
            func.count(RestaurantLocation.id.distinct()).label("location_count"),
            func.count(MenuItem.id.distinct()).label("item_count"),
        )
        .outerjoin(RestaurantLocation, RestaurantLocation.chain_id == RestaurantChain.id)
        .outerjoin(MenuItem, MenuItem.chain_id == RestaurantChain.id)
        .where(RestaurantChain.id == chain_id)
        .group_by(RestaurantChain.id)
    )
    row = (await db.execute(stmt)).first()
    if not row:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    chain, loc_count, item_count = row
    d = ChainDetailSchema.model_validate(chain)
    d.location_count = loc_count
    d.item_count = item_count
    return d
