export interface Nutrition {
  calories:          number | null;
  calories_from_fat: number | null;
  total_fat_g:       number | null;
  saturated_fat_g:   number | null;
  trans_fat_g:       number | null;
  cholesterol_mg:    number | null;
  sodium_mg:         number | null;
  total_carbs_g:     number | null;
  dietary_fiber_g:   number | null;
  total_sugars_g:    number | null;
  added_sugars_g:    number | null;
  protein_g:         number | null;
  vitamin_d_mcg:     number | null;
  calcium_mg:        number | null;
  iron_mg:           number | null;
  potassium_mg:      number | null;
  health_score:      number | null;
}

export interface ChainSummary {
  id:           number;
  name:         string;
  slug:         string;
  cuisine_type: string | null;
  logo_url:     string | null;
}

export interface ChainDetail extends ChainSummary {
  website:        string | null;
  location_count: number;
  item_count:     number;
}

export interface MenuCategory {
  id:   number;
  name: string;
}

export interface MenuItem {
  id:           number;
  name:         string;
  description:  string | null;
  serving_size: string | null;
  image_url:    string | null;
  chain:        ChainSummary | null;
  category:     MenuCategory | null;
  nutrition:    Nutrition | null;
}

export interface Location {
  id:          number;
  chain_id:    number;
  address:     string | null;
  city:        string | null;
  state:       string | null;
  zip:         string | null;
  lat:         number | null;
  lon:         number | null;
  distance_km: number | null;
  chain:       ChainSummary | null;
}

export interface MealTotals {
  calories:        number;
  total_fat_g:     number;
  saturated_fat_g: number;
  trans_fat_g:     number;
  cholesterol_mg:  number;
  sodium_mg:       number;
  total_carbs_g:   number;
  dietary_fiber_g: number;
  total_sugars_g:  number;
  protein_g:       number;
}

export interface DailyValuePct {
  calories:      number;
  total_fat:     number;
  saturated_fat: number;
  cholesterol:   number;
  sodium:        number;
  total_carbs:   number;
  dietary_fiber: number;
  protein:       number;
}

export interface MealAnalysis {
  items:     MenuItem[];
  totals:    MealTotals;
  daily_pct: DailyValuePct;
}

// ── Ingredient Builder ────────────────────────────────────────────────────
export interface BuilderIngredientSlot {
  name: string;
  item: MenuItem | null;
}

export interface BuilderIngredientGroup {
  id:             string;
  name:           string;
  required:       boolean;
  max_selections: number;
  none_label:     string | null;
  items:          BuilderIngredientSlot[];
}

export interface BuilderMealType {
  id:          string;
  name:        string;
  icon:        string;
  description: string;
  base_items:  BuilderIngredientSlot[];
}

export interface BuilderConfig {
  has_builder:       boolean;
  meal_types?:       BuilderMealType[];
  ingredient_groups?: BuilderIngredientGroup[];
}

export interface PresetMealItem {
  menu_item: MenuItem;
  quantity:  number;
}

export interface PresetMeal {
  id:          number;
  name:        string;
  description: string | null;
  chain:       ChainSummary | null;
  items:       PresetMealItem[];
  totals:      MealTotals | null;
}

export type SortOption =
  | "healthiest"
  | "unhealthiest"
  | "calories_asc"
  | "calories_desc"
  | "protein_desc"
  | "carbs_asc"
  | "sodium_asc"
  | "fat_asc";
