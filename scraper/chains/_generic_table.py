"""
Generic HTML-table scraper.
Many chains publish a simple nutrition table at a static URL.
Subclasses only need to set url and column_map.
"""
import httpx
from bs4 import BeautifulSoup
from base_scraper import BaseScraper, MenuItemData

# Standard column order for most chains (0-indexed after the name column)
DEFAULT_COLS = {
    "serving_size":   1,
    "calories":       2,
    "total_fat_g":    3,
    "saturated_fat_g":4,
    "trans_fat_g":    5,
    "cholesterol_mg": 6,
    "sodium_mg":      7,
    "total_carbs_g":  8,
    "dietary_fiber_g":9,
    "total_sugars_g": 10,
    "protein_g":      11,
}


class GenericTableScraper(BaseScraper):
    url: str            # Nutrition table URL
    column_map: dict = DEFAULT_COLS
    name_col: int = 0
    category_header_cols: int = 1  # rows with this many cells are category headers

    async def scrape_menu(self) -> list[MenuItemData]:
        from playwright.async_api import async_playwright

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            # domcontentloaded is far more reliable than networkidle on SPAs
            try:
                await page.goto(self.url, wait_until="domcontentloaded", timeout=45000)
            except Exception:
                await browser.close()
                return []
            # Brief wait for any JS-driven content to render
            await self.polite_delay(1.5, 2.5)
            html = await page.content()
            await browser.close()

        soup = BeautifulSoup(html, "lxml")
        items = []
        current_category = "Menu"

        for row in soup.select("tr"):
            cells = [c.get_text(strip=True) for c in row.find_all(["th", "td"])]
            if not cells:
                continue
            if len(cells) <= self.category_header_cols:
                current_category = cells[0] or current_category
                continue
            name = cells[self.name_col] if len(cells) > self.name_col else ""
            if not name or name.lower() in ("item", "menu item", "food"):
                continue

            def get(key):
                col = self.column_map.get(key)
                return cells[col] if col is not None and len(cells) > col else None

            try:
                items.append(MenuItemData(
                    name=name,
                    category=current_category,
                    serving_size=get("serving_size") or "",
                    calories=self.safe_int(get("calories")),
                    total_fat_g=self.safe_float(get("total_fat_g")),
                    saturated_fat_g=self.safe_float(get("saturated_fat_g")),
                    trans_fat_g=self.safe_float(get("trans_fat_g")),
                    cholesterol_mg=self.safe_int(get("cholesterol_mg")),
                    sodium_mg=self.safe_int(get("sodium_mg")),
                    total_carbs_g=self.safe_float(get("total_carbs_g")),
                    dietary_fiber_g=self.safe_float(get("dietary_fiber_g")),
                    total_sugars_g=self.safe_float(get("total_sugars_g")),
                    protein_g=self.safe_float(get("protein_g")),
                ))
            except Exception:
                continue

        return items
