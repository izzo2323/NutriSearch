-- Adds a category column to preset_meals so popular combos and healthy
-- options can be stored together but queried/displayed separately.
ALTER TABLE preset_meals ADD COLUMN IF NOT EXISTS category VARCHAR(50) DEFAULT 'popular';
CREATE INDEX IF NOT EXISTS preset_meals_category_idx ON preset_meals(chain_id, category);
