from abc import ABC, abstractmethod
from typing import Optional
import asyncio
import random


class MenuItemData:
    def __init__(
        self,
        name: str,
        category: str = "Menu",
        description: str = "",
        serving_size: str = "",
        calories: Optional[int] = None,
        total_fat_g: Optional[float] = None,
        saturated_fat_g: Optional[float] = None,
        trans_fat_g: Optional[float] = None,
        cholesterol_mg: Optional[int] = None,
        sodium_mg: Optional[int] = None,
        total_carbs_g: Optional[float] = None,
        dietary_fiber_g: Optional[float] = None,
        total_sugars_g: Optional[float] = None,
        added_sugars_g: Optional[float] = None,
        protein_g: Optional[float] = None,
        vitamin_d_mcg: Optional[float] = None,
        calcium_mg: Optional[float] = None,
        iron_mg: Optional[float] = None,
        potassium_mg: Optional[float] = None,
    ):
        self.name = name
        self.category = category
        self.description = description
        self.serving_size = serving_size
        self.calories = calories
        self.total_fat_g = total_fat_g
        self.saturated_fat_g = saturated_fat_g
        self.trans_fat_g = trans_fat_g
        self.cholesterol_mg = cholesterol_mg
        self.sodium_mg = sodium_mg
        self.total_carbs_g = total_carbs_g
        self.dietary_fiber_g = dietary_fiber_g
        self.total_sugars_g = total_sugars_g
        self.added_sugars_g = added_sugars_g
        self.protein_g = protein_g
        self.vitamin_d_mcg = vitamin_d_mcg
        self.calcium_mg = calcium_mg
        self.iron_mg = iron_mg
        self.potassium_mg = potassium_mg


class BaseScraper(ABC):
    # Subclasses must define these
    name: str         # Display name, e.g. "McDonald's"
    slug: str         # URL-safe slug, e.g. "mcdonalds"
    website: str
    cuisine_type: str

    async def polite_delay(self, min_s: float = 1.0, max_s: float = 3.0):
        await asyncio.sleep(random.uniform(min_s, max_s))

    @staticmethod
    def safe_float(value) -> Optional[float]:
        if value is None:
            return None
        try:
            cleaned = str(value).replace("g", "").replace("mg", "").strip()
            if cleaned in ("<1", "< 1"):
                return 0.5
            return float(cleaned)
        except (ValueError, TypeError):
            return None

    @staticmethod
    def safe_int(value) -> Optional[int]:
        if value is None:
            return None
        try:
            cleaned = str(value).strip()
            if cleaned in ("<1", "< 1"):
                return 0
            return int(float(cleaned))
        except (ValueError, TypeError):
            return None

    @abstractmethod
    async def scrape_menu(self) -> list[MenuItemData]:
        """Return all menu items with nutrition data."""
