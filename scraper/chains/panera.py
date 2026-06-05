"""Panera Bread — uses their public menu JSON API."""
import httpx
from base_scraper import BaseScraper, MenuItemData


class PaneraScraper(BaseScraper):
    name         = "Panera Bread"
    slug         = "panera"
    website      = "https://www.panerabread.com"
    cuisine_type = "Bakery / Café"

    API_URL = "https://www.panerabread.com/api/v1/menuapi/get-menu?method=getEntireMenu&channelType=2"

    async def scrape_menu(self) -> list[MenuItemData]:
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json",
            "Referer": "https://www.panerabread.com/en-us/menu.html",
        }
        async with httpx.AsyncClient(headers=headers, follow_redirects=True, timeout=30) as client:
            resp = await client.get(self.API_URL)

        if resp.status_code != 200:
            return await self._playwright_fallback()

        data = resp.json()
        items = []
        for cat in data.get("menuGroups", []):
            cat_name = cat.get("name", "Menu")
            for item in cat.get("items", []):
                n = item.get("nutritionalInformation", {})
                items.append(MenuItemData(
                    name=item.get("name", ""),
                    category=cat_name,
                    serving_size=item.get("servingSize", ""),
                    calories=self.safe_int(n.get("calories")),
                    total_fat_g=self.safe_float(n.get("fat")),
                    saturated_fat_g=self.safe_float(n.get("saturatedFat")),
                    trans_fat_g=self.safe_float(n.get("transFat")),
                    cholesterol_mg=self.safe_int(n.get("cholesterol")),
                    sodium_mg=self.safe_int(n.get("sodium")),
                    total_carbs_g=self.safe_float(n.get("carbohydrates")),
                    dietary_fiber_g=self.safe_float(n.get("dietaryFiber")),
                    total_sugars_g=self.safe_float(n.get("sugars")),
                    protein_g=self.safe_float(n.get("protein")),
                ))
        return items

    async def _playwright_fallback(self) -> list[MenuItemData]:
        from chains._generic_table import GenericTableScraper
        fallback = GenericTableScraper.__new__(GenericTableScraper)
        fallback.url = "https://www.panerabread.com/en-us/menu.html"
        BaseScraper.__init__(fallback)
        return await fallback.scrape_menu()
