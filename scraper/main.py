"""
Scraper orchestrator.

Usage:
    # Load seed data for all chains (fast, no network scraping)
    python main.py --seed

    # Load seed data for specific chains
    python main.py --seed --chains mcdonalds chipotle

    # Live-scrape specific chains (slower, may vary by site)
    python main.py --chains mcdonalds chipotle starbucks

    # Live-scrape all chains
    python main.py --chains all

    # OSM locations for Omaha + Wichita
    python main.py --locations

    # Recommended first run: seed everything + pull locations
    python main.py --seed --locations
"""
import asyncio
import argparse
import sys
import traceback

import db_writer
import osm_locations
from chains import ALL_SCRAPERS, SCRAPER_MAP
from seed_data import SEED
from seed_data_extended import EXTENDED
from seed_data_builder import BUILDER_INGREDIENTS
from preset_meals import seed_presets, seed_healthy_presets


async def run_scraper(scraper_cls):
    scraper = scraper_cls()
    print(f"→ Scraping {scraper.name} …")
    try:
        items = await scraper.scrape_menu()
        if items:
            await db_writer.persist(scraper, items)
        else:
            print(f"  ⚠ No items returned for {scraper.name}")
    except Exception as e:
        print(f"  ✗ {scraper.name} failed: {e}")
        traceback.print_exc()


async def load_seed(slugs: list[str] | None = None):
    """Write hardcoded nutrition data to the database."""
    targets = slugs if slugs else list(SEED.keys())
    for slug in targets:
        entry = SEED.get(slug)
        if not entry:
            print(f"  ⚠ No seed data for slug: {slug}")
            continue

        chain_info = entry["chain"]
        items      = entry["items"]

        # Build a minimal scraper-like object for db_writer
        class _Proxy:
            pass
        proxy = _Proxy()
        proxy.name         = chain_info["name"]
        proxy.slug         = chain_info["slug"]
        proxy.website      = chain_info.get("website", "")
        proxy.cuisine_type = chain_info.get("cuisine_type", "")

        print(f"→ Seeding {proxy.name} ({len(items)} items) …")
        await db_writer.persist(proxy, items)


async def main():
    parser = argparse.ArgumentParser(description="Restaurant nutrition scraper")
    parser.add_argument(
        "--seed", action="store_true",
        help="Load hardcoded seed data (fast, no network scraping required)"
    )
    parser.add_argument(
        "--seed-extended", action="store_true",
        help="Load extended seed data — adds comprehensive menu items to each chain"
    )
    parser.add_argument(
        "--seed-builder", action="store_true",
        help="Load ingredient-level data for build-your-own chains (Subway, Qdoba, etc.)"
    )
    parser.add_argument(
        "--chains", nargs="+", default=[],
        help="Chain slugs for live scraping or seed filtering, or 'all'"
    )
    parser.add_argument(
        "--presets", action="store_true",
        help="Seed popular preset meal combos (requires --seed data already loaded)"
    )
    parser.add_argument(
        "--healthy-presets", action="store_true",
        help="Auto-generate healthiest/lowest-calorie/high-protein presets from DB health scores"
    )
    parser.add_argument(
        "--locations", action="store_true",
        help="Fetch OSM locations for Omaha and Wichita"
    )
    parser.add_argument(
        "--cities", nargs="+", default=["omaha", "wichita"],
        help="Cities to fetch locations for"
    )
    args = parser.parse_args()

    if not args.seed and not getattr(args, 'seed_extended', False) and not getattr(args, 'seed_builder', False) and not args.chains and not args.locations and not args.presets and not getattr(args, 'healthy_presets', False):
        parser.print_help()
        sys.exit(1)

    # ── Seed data (fast path) ─────────────────────────────────────────────
    if args.seed:
        slugs = None
        if args.chains and args.chains != ["all"]:
            slugs = args.chains
        await load_seed(slugs)

    # ── Extended seed data ────────────────────────────────────────────────
    if getattr(args, 'seed_extended', False):
        slugs = None
        if args.chains and args.chains != ["all"]:
            slugs = args.chains

        targets = slugs if slugs else list(EXTENDED.keys())
        for slug in targets:
            entry = EXTENDED.get(slug)
            if not entry:
                print(f"  ⚠ No extended data for: {slug}")
                continue
            class _Proxy:
                pass
            proxy = _Proxy()
            proxy.name         = entry["chain"]["name"]
            proxy.slug         = entry["chain"]["slug"]
            proxy.website      = entry["chain"].get("website", "")
            proxy.cuisine_type = entry["chain"].get("cuisine_type", "")
            print(f"→ Extended seed {proxy.name} ({len(entry['items'])} items) …")
            await db_writer.persist(proxy, entry["items"])

    # ── Builder ingredient seed ───────────────────────────────────────────
    if getattr(args, 'seed_builder', False):
        slugs = None
        if args.chains and args.chains != ["all"]:
            slugs = args.chains
        targets = slugs if slugs else list(BUILDER_INGREDIENTS.keys())
        for slug in targets:
            entry = BUILDER_INGREDIENTS.get(slug)
            if not entry:
                print(f"  ⚠ No builder data for: {slug}")
                continue
            class _Proxy:
                pass
            proxy = _Proxy()
            proxy.name         = entry["chain"]["name"]
            proxy.slug         = entry["chain"]["slug"]
            proxy.website      = entry["chain"].get("website", "")
            proxy.cuisine_type = entry["chain"].get("cuisine_type", "")
            print(f"→ Builder seed {proxy.name} ({len(entry['items'])} items) …")
            await db_writer.persist(proxy, entry["items"])

    # ── Live scraping ─────────────────────────────────────────────────────
    elif args.chains:
        if args.chains == ["all"]:
            scrapers_to_run = ALL_SCRAPERS
        else:
            scrapers_to_run = []
            for slug in args.chains:
                cls = SCRAPER_MAP.get(slug)
                if cls:
                    scrapers_to_run.append(cls)
                else:
                    print(f"Unknown chain: {slug}. Available: {list(SCRAPER_MAP.keys())}")

        for cls in scrapers_to_run:
            await run_scraper(cls)
            await asyncio.sleep(2)

    # ── Preset meals ──────────────────────────────────────────────────────
    if args.presets:
        print("\n→ Seeding preset meals …")
        slugs = None
        if args.chains and args.chains != ["all"]:
            slugs = args.chains
        await seed_presets(slugs)

    # ── Healthy presets ───────────────────────────────────────────────────
    if getattr(args, 'healthy_presets', False):
        print("\n→ Generating healthy presets …")
        slugs = None
        if args.chains and args.chains != ["all"]:
            slugs = args.chains
        await seed_healthy_presets(slugs)

    # ── OSM locations ─────────────────────────────────────────────────────
    if args.locations:
        print("\n→ Fetching OSM locations …")
        await osm_locations.run(cities=args.cities)

    print("\nDone.")


if __name__ == "__main__":
    asyncio.run(main())
