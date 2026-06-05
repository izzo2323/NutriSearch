from __future__ import annotations
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict


class NutritionSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    calories:          Optional[int]     = None
    calories_from_fat: Optional[int]     = None
    total_fat_g:       Optional[Decimal] = None
    saturated_fat_g:   Optional[Decimal] = None
    trans_fat_g:       Optional[Decimal] = None
    cholesterol_mg:    Optional[int]     = None
    sodium_mg:         Optional[int]     = None
    total_carbs_g:     Optional[Decimal] = None
    dietary_fiber_g:   Optional[Decimal] = None
    total_sugars_g:    Optional[Decimal] = None
    added_sugars_g:    Optional[Decimal] = None
    protein_g:         Optional[Decimal] = None
    vitamin_d_mcg:     Optional[Decimal] = None
    calcium_mg:        Optional[Decimal] = None
    iron_mg:           Optional[Decimal] = None
    potassium_mg:      Optional[Decimal] = None
    health_score:      Optional[Decimal] = None


class MenuCategorySchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id:   int
    name: str


class ChainSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id:           int
    name:         str
    slug:         str
    cuisine_type: Optional[str] = None
    logo_url:     Optional[str] = None


class MenuItemSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id:           int
    name:         str
    description:  Optional[str]             = None
    serving_size: Optional[str]             = None
    image_url:    Optional[str]             = None
    chain:        Optional[ChainSummary]    = None
    category:     Optional[MenuCategorySchema] = None
    nutrition:    Optional[NutritionSchema] = None


class LocationSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id:          int
    chain_id:    int
    address:     Optional[str]     = None
    city:        Optional[str]     = None
    state:       Optional[str]     = None
    zip:         Optional[str]     = None
    lat:         Optional[Decimal] = None
    lon:         Optional[Decimal] = None
    distance_km: Optional[float]   = None
    chain:       Optional[ChainSummary] = None


class ChainDetailSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id:              int
    name:            str
    slug:            str
    website:         Optional[str] = None
    logo_url:        Optional[str] = None
    cuisine_type:    Optional[str] = None
    location_count:  int = 0
    item_count:      int = 0


class MealItem(BaseModel):
    menu_item_id: int
    quantity:     int = 1


class MealRequest(BaseModel):
    items: list[MealItem]


class MealTotals(BaseModel):
    calories:        int
    total_fat_g:     float
    saturated_fat_g: float
    trans_fat_g:     float
    cholesterol_mg:  int
    sodium_mg:       int
    total_carbs_g:   float
    dietary_fiber_g: float
    total_sugars_g:  float
    protein_g:       float


class DailyValuePct(BaseModel):
    calories:        float
    total_fat:       float
    saturated_fat:   float
    cholesterol:     float
    sodium:          float
    total_carbs:     float
    dietary_fiber:   float
    protein:         float


class MealResponse(BaseModel):
    items:      list[MenuItemSchema]
    totals:     MealTotals
    daily_pct:  DailyValuePct


class PresetMealItemSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    menu_item: MenuItemSchema
    quantity:  int


class PresetMealSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id:           int
    name:         str
    description:  Optional[str]           = None
    category:     str                     = "popular"
    chain:        Optional[ChainSummary]  = None
    items:        list[PresetMealItemSchema]
    totals:       Optional[MealTotals]    = None
