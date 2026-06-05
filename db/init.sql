CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- ────────────────────────────────────────────────
-- Restaurant chains
-- ────────────────────────────────────────────────
CREATE TABLE restaurant_chains (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(255) NOT NULL,
    slug        VARCHAR(255) UNIQUE NOT NULL,
    website     VARCHAR(500),
    logo_url    VARCHAR(500),
    cuisine_type VARCHAR(100),
    is_chain    BOOLEAN DEFAULT true,
    created_at  TIMESTAMP DEFAULT NOW(),
    updated_at  TIMESTAMP DEFAULT NOW()
);

CREATE INDEX restaurant_chains_name_trgm ON restaurant_chains USING GIN (name gin_trgm_ops);

-- ────────────────────────────────────────────────
-- Physical restaurant locations
-- ────────────────────────────────────────────────
CREATE TABLE restaurant_locations (
    id          SERIAL PRIMARY KEY,
    chain_id    INTEGER REFERENCES restaurant_chains(id) ON DELETE CASCADE,
    address     VARCHAR(500),
    city        VARCHAR(100),
    state       VARCHAR(50),
    zip         VARCHAR(20),
    country     VARCHAR(50) DEFAULT 'US',
    lat         NUMERIC(10,7),
    lon         NUMERIC(10,7),
    geom        GEOGRAPHY(POINT, 4326),
    osm_id      BIGINT,
    phone       VARCHAR(30),
    created_at  TIMESTAMP DEFAULT NOW(),
    updated_at  TIMESTAMP DEFAULT NOW()
);

CREATE INDEX restaurant_locations_geom_idx  ON restaurant_locations USING GIST(geom);
CREATE INDEX restaurant_locations_chain_idx ON restaurant_locations(chain_id);

-- ────────────────────────────────────────────────
-- Menu categories
-- ────────────────────────────────────────────────
CREATE TABLE menu_categories (
    id            SERIAL PRIMARY KEY,
    chain_id      INTEGER REFERENCES restaurant_chains(id) ON DELETE CASCADE,
    name          VARCHAR(255) NOT NULL,
    display_order INTEGER DEFAULT 0
);

-- ────────────────────────────────────────────────
-- Menu items
-- ────────────────────────────────────────────────
CREATE TABLE menu_items (
    id            SERIAL PRIMARY KEY,
    chain_id      INTEGER REFERENCES restaurant_chains(id) ON DELETE CASCADE,
    category_id   INTEGER REFERENCES menu_categories(id) ON DELETE SET NULL,
    name          VARCHAR(500) NOT NULL,
    description   TEXT,
    serving_size  VARCHAR(100),
    image_url     VARCHAR(500),
    is_available  BOOLEAN DEFAULT true,
    created_at    TIMESTAMP DEFAULT NOW(),
    updated_at    TIMESTAMP DEFAULT NOW()
);

CREATE INDEX menu_items_chain_idx    ON menu_items(chain_id);
CREATE INDEX menu_items_category_idx ON menu_items(category_id);
CREATE INDEX menu_items_name_trgm    ON menu_items USING GIN (name gin_trgm_ops);

-- ────────────────────────────────────────────────
-- Nutrition information
-- health_score: lower = healthier
-- formula: calories + sat_fat*9 + sodium*0.1 - protein*4 - fiber*5
-- ────────────────────────────────────────────────
CREATE TABLE nutrition_info (
    id                  SERIAL PRIMARY KEY,
    menu_item_id        INTEGER UNIQUE REFERENCES menu_items(id) ON DELETE CASCADE,
    calories            INTEGER,
    calories_from_fat   INTEGER,
    total_fat_g         NUMERIC(8,2),
    saturated_fat_g     NUMERIC(8,2),
    trans_fat_g         NUMERIC(8,2),
    cholesterol_mg      INTEGER,
    sodium_mg           INTEGER,
    total_carbs_g       NUMERIC(8,2),
    dietary_fiber_g     NUMERIC(8,2),
    total_sugars_g      NUMERIC(8,2),
    added_sugars_g      NUMERIC(8,2),
    protein_g           NUMERIC(8,2),
    vitamin_d_mcg       NUMERIC(8,2),
    calcium_mg          NUMERIC(8,2),
    iron_mg             NUMERIC(8,2),
    potassium_mg        NUMERIC(8,2),
    health_score        NUMERIC(10,2) GENERATED ALWAYS AS (
        COALESCE(calories,0)
        + COALESCE(saturated_fat_g,0) * 9
        + COALESCE(sodium_mg,0)       * 0.1
        - COALESCE(protein_g,0)       * 4
        - COALESCE(dietary_fiber_g,0) * 5
    ) STORED,
    created_at          TIMESTAMP DEFAULT NOW(),
    updated_at          TIMESTAMP DEFAULT NOW()
);

CREATE INDEX nutrition_health_score_idx ON nutrition_info(health_score);
CREATE INDEX nutrition_calories_idx     ON nutrition_info(calories);
CREATE INDEX nutrition_protein_idx      ON nutrition_info(protein_g DESC NULLS LAST);
CREATE INDEX nutrition_sodium_idx       ON nutrition_info(sodium_mg);

-- ────────────────────────────────────────────────
-- Preset / popular meals
-- ────────────────────────────────────────────────
CREATE TABLE preset_meals (
    id            SERIAL PRIMARY KEY,
    chain_id      INTEGER REFERENCES restaurant_chains(id) ON DELETE CASCADE,
    name          VARCHAR(255) NOT NULL,
    description   TEXT,
    category      VARCHAR(50) DEFAULT 'popular',
    display_order INTEGER DEFAULT 0,
    created_at    TIMESTAMP DEFAULT NOW()
);

CREATE INDEX preset_meals_chain_idx ON preset_meals(chain_id);

CREATE TABLE preset_meal_items (
    id             SERIAL PRIMARY KEY,
    preset_meal_id INTEGER REFERENCES preset_meals(id) ON DELETE CASCADE,
    menu_item_id   INTEGER REFERENCES menu_items(id)   ON DELETE CASCADE,
    quantity       INTEGER DEFAULT 1
);
