"""
McDonald's scraper — uses their public nutrition JSON API.
Endpoint discovered via browser network inspection.
"""
import httpx
from base_scraper import BaseScraper, MenuItemData


class McDonaldsScraper(BaseScraper):
    name         = "McDonald's"
    slug         = "mcdonalds"
    website      = "https://www.mcdonalds.com"
    cuisine_type = "Fast Food"

    API_URL = "https://www.mcdonalds.com/us/en-us/about-our-food/nutrition-calculator.html"
    DATA_URL = "https://www.mcdonalds.com/bin/publishedCalcNutritionInfo.json"

    async def scrape_menu(self) -> list[MenuItemData]:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
            "Accept": "application/json",
            "Referer": self.API_URL,
        }
        async with httpx.AsyncClient(headers=headers, follow_redirects=True, timeout=30) as client:
            resp = await client.get(self.DATA_URL)
            if resp.status_code != 200:
                return await self._scrape_via_playwright()
            data = resp.json()

        items = []
        for category in data.get("Category", []):
            cat_name = category.get("Name", "Menu")
            for item in category.get("Item", []):
                nf = item.get("NutritionInfo", {})
                items.append(MenuItemData(
                    name=item.get("ItemName", ""),
                    category=cat_name,
                    serving_size=item.get("PortionSize", ""),
                    calories=self.safe_int(nf.get("Calories")),
                    total_fat_g=self.safe_float(nf.get("TotalFat")),
                    saturated_fat_g=self.safe_float(nf.get("SaturatedFat")),
                    trans_fat_g=self.safe_float(nf.get("TransFat")),
                    cholesterol_mg=self.safe_int(nf.get("Cholesterol")),
                    sodium_mg=self.safe_int(nf.get("Sodium")),
                    total_carbs_g=self.safe_float(nf.get("TotalCarbohydrate")),
                    dietary_fiber_g=self.safe_float(nf.get("DietaryFiber")),
                    total_sugars_g=self.safe_float(nf.get("Sugars")),
                    protein_g=self.safe_float(nf.get("Protein")),
                ))
        return items

    async def _scrape_via_playwright(self) -> list[MenuItemData]:
        """Playwright fallback if the JSON endpoint changes."""
        from playwright.async_api import async_playwright

        items = []
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(self.API_URL, wait_until="domcontentloaded")
            # Parse whatever table/list the page renders
            rows = await page.query_selector_all("[data-testid='menuItem']")
            for row in rows:
                name = await row.query_selector("[data-testid='itemName']")
                cal  = await row.query_selector("[data-testid='calories']")
                if name:
                    items.append(MenuItemData(
                        name=await name.inner_text(),
                        category="Menu",
                        calories=self.safe_int(await cal.inner_text() if cal else None),
                    ))
            await browser.close()
        return items
