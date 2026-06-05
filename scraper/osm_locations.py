"""
Fetch restaurant locations from OpenStreetMap Overpass API and persist them.

Usage:
    python osm_locations.py --cities omaha wichita
    python osm_locations.py --lat 41.2565 --lon -95.9345 --radius 50
"""
import asyncio
import argparse
import os
import httpx
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy import text

DATABASE_URL = os.environ["DATABASE_URL"]
engine = create_async_engine(DATABASE_URL)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

OVERPASS_URL = "https://overpass-api.de/api/interpreter"

CITY_COORDS = {
    "omaha":   (41.2565, -95.9345, 40),   # lat, lon, radius_km
    "wichita": (37.6872, -97.3301, 40),
}

# Map OSM brand names → our chain slugs
BRAND_TO_SLUG = {
    "McDonald's":          "mcdonalds",
    "Burger King":         "burger-king",
    "Wendy's":             "wendys",
    "Taco Bell":           "taco-bell",
    "Chick-fil-A":         "chick-fil-a",
    "KFC":                 "kfc",
    "Popeyes":             "popeyes",
    "Subway":              "subway",
    "Jimmy John's":        "jimmy-johns",
    "Jersey Mike's":       "jersey-mikes",
    "Sonic":               "sonic",
    "Jack in the Box":     "jack-in-the-box",
    "Whataburger":         "whataburger",
    "Five Guys":           "five-guys",
    "Shake Shack":         "shake-shack",
    "Culver's":            "culvers",
    "Domino's":            "dominos",
    "Pizza Hut":           "pizza-hut",
    "Papa John's":         "papa-johns",
    "Little Caesars":      "little-caesars",
    "Starbucks":           "starbucks",
    "Dunkin'":             "dunkin",
    "IHOP":                "ihop",
    "Denny's":             "dennys",
    "Cracker Barrel":      "cracker-barrel",
    "Chipotle":            "chipotle",
    "Chipotle Mexican Grill": "chipotle",
    "Qdoba":               "qdoba",
    "Panda Express":       "panda-express",
    "Noodles & Company":   "noodles-and-company",
    "Buffalo Wild Wings":  "buffalo-wild-wings",
    "Wingstop":            "wingstop",
    "Raising Cane's":      "raising-canes",
    "Applebee's":          "applebees",
    "Chili's":             "chilis",
    "TGI Fridays":         "tgi-fridays",
    "Red Robin":           "red-robin",
    "Olive Garden":        "olive-garden",
    "Red Lobster":         "red-lobster",
    "Texas Roadhouse":     "texas-roadhouse",
    "Outback Steakhouse":  "outback",
    "Arby's":              "arbys",
    "Dairy Queen":         "dairy-queen",
    "Firehouse Subs":      "firehouse-subs",
    "Panera Bread":        "panera",
    "Zaxby's":             "zaxbys",
    "Bob Evans":           "bob-evans",
    "Hardee's":            "hardees",
    "Carl's Jr.":          "carls-jr",
    "Del Taco":            "del-taco",
    "El Pollo Loco":       "el-pollo-loco",
    "LongHorn Steakhouse": "longhorn",
    "In-N-Out Burger":     "in-n-out",
}


def build_overpass_query(lat: float, lon: float, radius_m: int) -> str:
    return f"""
[out:json][timeout:60];
(
  node["amenity"~"restaurant|fast_food|cafe"](around:{radius_m},{lat},{lon});
  way["amenity"~"restaurant|fast_food|cafe"](around:{radius_m},{lat},{lon});
);
out center tags;
"""


async def fetch_overpass(lat: float, lon: float, radius_km: float) -> list[dict]:
    query = build_overpass_query(lat, lon, int(radius_km * 1000))
    async with httpx.AsyncClient(timeout=90) as client:
        resp = await client.post(OVERPASS_URL, data={"data": query})
        resp.raise_for_status()
    elements = resp.json().get("elements", [])
    results = []
    for el in elements:
        tags = el.get("tags", {})
        # Get coordinates (nodes have lat/lon directly; ways have a center)
        lat_val = el.get("lat") or (el.get("center") or {}).get("lat")
        lon_val = el.get("lon") or (el.get("center") or {}).get("lon")
        if not lat_val or not lon_val:
            continue
        results.append({
            "osm_id":  el["id"],
            "name":    tags.get("name", ""),
            "brand":   tags.get("brand", tags.get("name", "")),
            "address": tags.get("addr:street", ""),
            "city":    tags.get("addr:city", ""),
            "state":   tags.get("addr:state", ""),
            "zip":     tags.get("addr:postcode", ""),
            "phone":   tags.get("phone", tags.get("contact:phone", "")),
            "lat":     lat_val,
            "lon":     lon_val,
        })
    return results


async def get_or_create_chain(session: AsyncSession, name: str, slug: str) -> int:
    row = (await session.execute(
        text("SELECT id FROM restaurant_chains WHERE slug = :slug"), {"slug": slug}
    )).fetchone()
    if row:
        return row[0]
    result = await session.execute(
        text("""
            INSERT INTO restaurant_chains (name, slug, is_chain)
            VALUES (:name, :slug, false)
            RETURNING id
        """),
        {"name": name, "slug": slug},
    )
    await session.commit()
    return result.fetchone()[0]


async def persist_locations(locations: list[dict]):
    async with SessionLocal() as session:
        saved = 0
        for loc in locations:
            brand = loc["brand"]
            slug  = BRAND_TO_SLUG.get(brand)

            if not slug:
                # Local/independent restaurant — use a slug from name
                if not loc["name"]:
                    continue
                slug = loc["name"].lower().replace(" ", "-").replace("'", "")[:80]

            chain_id = await get_or_create_chain(session, loc["name"] or brand, slug)

            exists = (await session.execute(
                text("SELECT 1 FROM restaurant_locations WHERE osm_id = :oid"), {"oid": loc["osm_id"]}
            )).fetchone()
            if exists:
                continue

            await session.execute(
                text("""
                    INSERT INTO restaurant_locations
                        (chain_id, address, city, state, zip, lat, lon, geom, osm_id, phone)
                    VALUES
                        (:cid, :addr, :city, :state, :zip, :lat, :lon,
                         ST_SetSRID(ST_MakePoint(:lon, :lat), 4326)::geography,
                         :osm_id, :phone)
                """),
                {
                    "cid":    chain_id,
                    "addr":   loc["address"],
                    "city":   loc["city"],
                    "state":  loc["state"],
                    "zip":    loc["zip"],
                    "lat":    loc["lat"],
                    "lon":    loc["lon"],
                    "osm_id": loc["osm_id"],
                    "phone":  loc["phone"],
                },
            )
            saved += 1

        await session.commit()
        print(f"  ✓ Saved {saved} new locations")


async def run(cities: list[str] = None, lat: float = None, lon: float = None, radius_km: float = 40):
    searches = []
    if cities:
        for city in cities:
            if city.lower() in CITY_COORDS:
                searches.append(CITY_COORDS[city.lower()])
            else:
                print(f"Unknown city: {city}. Add coordinates to CITY_COORDS.")
    if lat and lon:
        searches.append((lat, lon, radius_km))

    for lat_, lon_, radius_ in searches:
        print(f"Querying Overpass for ({lat_}, {lon_}) radius {radius_}km …")
        locs = await fetch_overpass(lat_, lon_, radius_)
        print(f"  Found {len(locs)} locations")
        await persist_locations(locs)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cities", nargs="+", default=["omaha", "wichita"])
    parser.add_argument("--lat",    type=float)
    parser.add_argument("--lon",    type=float)
    parser.add_argument("--radius", type=float, default=40)
    args = parser.parse_args()
    asyncio.run(run(args.cities, args.lat, args.lon, args.radius))
