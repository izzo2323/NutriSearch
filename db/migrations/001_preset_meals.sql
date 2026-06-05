-- Run this if you already have a database from before the preset meals feature.
-- docker-compose exec db psql -U nutrition -d nutrition -f /docker-entrypoint-initdb.d/migrations/001_preset_meals.sql

CREATE TABLE IF NOT EXISTS preset_meals (
    id            SERIAL PRIMARY KEY,
    chain_id      INTEGER REFERENCES restaurant_chains(id) ON DELETE CASCADE,
    name          VARCHAR(255) NOT NULL,
    description   TEXT,
    display_order INTEGER DEFAULT 0,
    created_at    TIMESTAMP DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS preset_meals_chain_idx ON preset_meals(chain_id);

CREATE TABLE IF NOT EXISTS preset_meal_items (
    id             SERIAL PRIMARY KEY,
    preset_meal_id INTEGER REFERENCES preset_meals(id) ON DELETE CASCADE,
    menu_item_id   INTEGER REFERENCES menu_items(id)   ON DELETE CASCADE,
    quantity       INTEGER DEFAULT 1
);
