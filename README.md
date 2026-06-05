# NutriSearch 🥗

A full-stack restaurant nutrition database web app for searching, comparing, and planning meals across 50+ restaurant chains. Features an ingredient-level meal builder for build-your-own chains like Chipotle and Subway, location-based restaurant search powered by OpenStreetMap, and pre-built popular and healthy meal presets.

---

## Features

- **50+ Restaurant Chains** — Browse complete menus with full nutrition facts (calories, protein, carbs, fat, sugar, sodium, and more)
- **Category-First Navigation** — Every restaurant opens with a visual category grid (🍔 Burgers, 🌮 Tacos, 🥗 Salads, etc.)
- **Ingredient Builder** — Build-your-own chains (Chipotle, Qdoba, Subway, Jimmy John's, Jersey Mike's, Firehouse Subs) let you pick each ingredient step by step with a live running nutrition total
- **Meal Builder** — Combine items from any restaurant and get a complete macro breakdown with % Daily Value bars and a Recharts chart. Built meals group as a single entry (e.g., "🥣 Chipotle Bowl") rather than individual ingredients
- **Popular Combos** — Pre-built popular meals (e.g., "Big Mac Large Combo" = Big Mac + Large Fries + Large Dr Pepper) across 17+ chains
- **Healthiest Options** — Auto-generated per chain: Healthiest Overall, Lowest Calorie, and Highest Protein presets, computed from the database health score
- **Health Score Sorting** — Sort any menu by healthiest first using the formula: `calories + sat_fat×9 + sodium×0.1 − protein×4 − fiber×5`
- **Item Detail Page** — Click any item to see its full FDA-style nutrition label plus Add a Side / Add a Drink dropdowns with live nutrition totals
- **Location Search** — Find restaurants near you via GPS or city/zip code using OpenStreetMap and the Overpass API, displayed on a Leaflet map

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Next.js 14 (App Router), TypeScript, Tailwind CSS, React Query, Leaflet, Recharts |
| Backend | Python, FastAPI, SQLAlchemy (async), asyncpg |
| Database | PostgreSQL 16 + PostGIS |
| Scraper | Python, Playwright, BeautifulSoup |
| Location | OpenStreetMap Nominatim + Overpass API |
| Infrastructure | Docker Compose |

---

## Getting Started

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Git

### 1. Clone and configure

```bash
git clone https://github.com/izzo2323/NutriSearch.git
cd NutriSearch
cp .env.example .env
```

### 2. Start the app

```bash
docker-compose up
```

- Frontend → http://localhost:3000
- API → http://localhost:8000
- API docs → http://localhost:8000/docs

The database initializes automatically on first run.

### 3. Populate the database

The app needs seed data before anything shows up. Run these commands in order:

```bash
# Core menu data for all 50+ chains
docker-compose run --rm scraper python main.py --seed

# Extended menu data (more items per chain)
docker-compose run --rm scraper python main.py --seed-extended

# Ingredient-level data for build-your-own chains (Chipotle, Subway, etc.)
docker-compose run --rm scraper python main.py --seed-builder

# Popular meal combos (Big Mac Meal, Chicken Sandwich Combo, etc.)
docker-compose run --rm scraper python main.py --presets

# Auto-generate Healthiest/Lowest Calorie/High Protein presets
docker-compose run --rm scraper python main.py --healthy-presets

# Restaurant locations for Omaha, NE and Wichita, KS
docker-compose run --rm scraper python main.py --locations
```

Or run everything in one shot:

```bash
docker-compose run --rm scraper python main.py \
  --seed --seed-extended --seed-builder --presets --healthy-presets --locations
```

---

## Project Structure

```
NutriSearch/
├── docker-compose.yml
├── .env.example
│
├── backend/                    # FastAPI application
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── main.py
│       ├── models.py           # SQLAlchemy ORM models
│       ├── schemas.py          # Pydantic schemas
│       ├── builder_config.py   # Ingredient builder configs per chain
│       └── routes/
│           ├── restaurants.py  # Chain search + nearby
│           ├── menu_items.py   # Item search + sorting
│           ├── locations.py    # Geocoding + chain locations
│           ├── meal.py         # Meal nutrition analysis
│           ├── preset_meals.py # Popular + healthy presets
│           └── builder.py      # Ingredient builder config endpoint
│
├── frontend/                   # Next.js application
│   ├── Dockerfile
│   ├── package.json
│   └── src/
│       ├── app/
│       │   ├── page.tsx                        # Home / location search
│       │   ├── restaurants/[id]/page.tsx        # Restaurant detail
│       │   ├── menu-items/[id]/page.tsx         # Item detail + meal add-ons
│       │   └── meal-builder/page.tsx            # Meal builder
│       ├── components/
│       │   ├── IngredientBuilder.tsx            # Step-by-step ingredient picker
│       │   ├── PresetMealCard.tsx               # Popular/healthy combo card
│       │   ├── MenuItemCard.tsx                 # Item list card
│       │   ├── NutritionFacts.tsx               # FDA-style nutrition label
│       │   ├── LocationMap.tsx                  # Leaflet map
│       │   └── CalorieBadge.tsx                 # Color-coded calorie pill
│       └── lib/
│           ├── api.ts                           # API client
│           └── types.ts                         # TypeScript interfaces
│
├── scraper/                    # Data collection
│   ├── Dockerfile
│   ├── main.py                 # CLI orchestrator
│   ├── base_scraper.py         # Abstract base class
│   ├── db_writer.py            # Upsert logic
│   ├── osm_locations.py        # OpenStreetMap location fetcher
│   ├── seed_data.py            # Base nutrition seed data (50 chains)
│   ├── seed_data_extended.py   # Extended menu items (29 chains)
│   ├── seed_data_builder.py    # Ingredient data (build-your-own chains)
│   ├── preset_meals.py         # Popular combos + healthy preset seeder
│   └── chains/                 # Per-chain live scrapers (50 chains)
│
└── db/
    ├── init.sql                # Schema + PostGIS setup
    └── migrations/
        ├── 001_preset_meals.sql
        └── 002_preset_meal_category.sql
```

---

## Ingredient Builder Chains

The following chains support step-by-step ingredient selection with live nutrition totals:

| Chain | Meal Types | Customisation Steps |
|---|---|---|
| Chipotle | Bowl, Burrito, Crispy Tacos, Soft Tacos, Salad, Quesadilla | Protein → Rice → Beans → Salsa → Extras |
| Qdoba | Bowl, Burrito, Tacos, Salad, Quesadilla | Protein → Rice → Beans → Salsa → Toppings |
| Subway | 6-inch, Footlong, Wrap, Salad | Bread → Protein → Cheese → Vegetables → Sauce |
| Jimmy John's | 8" Sub, Slim, Unwich | Bread → Protein → Vegetables → Sauce |
| Jersey Mike's | Regular, Giant, Lettuce Wrap | Bread → Protein → Cheese → Vegetables → Condiments |
| Firehouse Subs | Medium, Large | Bread → Protein → Cheese → Vegetables → Sauce |

---

## Database Schema

```
restaurant_chains       — Chain info (name, slug, website, cuisine type)
restaurant_locations    — Physical locations with PostGIS geography column
menu_categories         — Category groupings per chain
menu_items              — Individual menu items
nutrition_info          — Full nutrition facts + computed health_score
preset_meals            — Popular combos and healthy option presets
preset_meal_items       — Junction: which items belong to each preset
```

Health score is a PostgreSQL generated column:
```sql
health_score = calories + sat_fat*9 + sodium*0.1 - protein*4 - fiber*5
```
Lower score = healthier item.

---

## Scraper Commands Reference

```bash
# Seed data (no network required)
python main.py --seed                  # Base data for all 50+ chains
python main.py --seed-extended         # Extended menus (more items per chain)
python main.py --seed-builder          # Ingredient data for build-your-own chains

# Presets
python main.py --presets               # Popular meal combos
python main.py --healthy-presets       # Auto-generate healthy presets from DB scores

# Locations
python main.py --locations             # Omaha NE + Wichita KS via OpenStreetMap
python main.py --locations --cities omaha wichita denver  # Custom cities

# Live scraping (hits real restaurant websites)
python main.py --chains mcdonalds chipotle panera
python main.py --chains all

# Filter any command to specific chains
python main.py --seed --chains mcdonalds arbys
```

---

## API Endpoints

| Method | Path | Description |
|---|---|---|
| GET | `/api/restaurants` | List/search chains |
| GET | `/api/restaurants/near` | Chains near lat/lon |
| GET | `/api/restaurants/{id}` | Chain detail |
| GET | `/api/menu-items` | Search items with sort/filter |
| GET | `/api/menu-items/{id}` | Item with full nutrition |
| GET | `/api/menu-items/chain/{id}/categories` | Categories for a chain |
| GET | `/api/locations/geocode` | City/zip → lat/lon |
| GET | `/api/locations/chain/{id}` | All locations for a chain |
| POST | `/api/meal/analyze` | Analyze a list of item IDs |
| GET | `/api/preset-meals` | List presets (filter by chain + category) |
| GET | `/api/builder/{chain_id}` | Ingredient builder config + item data |

Full interactive docs available at http://localhost:8000/docs when running.

---

## Applying Migrations

If you have an existing database volume and need to apply schema changes:

```bash
docker-compose exec db psql -U nutrition -d nutrition -f /migrations/001_preset_meals.sql
docker-compose exec db psql -U nutrition -d nutrition -f /migrations/002_preset_meal_category.sql
```

---

## Environment Variables

Copy `.env.example` to `.env` and update as needed:

```env
POSTGRES_DB=nutrition
POSTGRES_USER=nutrition
POSTGRES_PASSWORD=nutrition
NEXT_PUBLIC_API_URL=http://localhost:8000
```
