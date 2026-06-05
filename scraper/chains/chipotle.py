"""Chipotle — nutrition data from their public nutrition page (static HTML table)."""
import httpx
from bs4 import BeautifulSoup
from base_scraper import BaseScraper, MenuItemData


class ChipotleScraper(BaseScraper):
    name         = "Chipotle"
    slug         = "chipotle"
    website      = "https://www.chipotle.com"
    cuisine_type = "Mexican"

    URL = "https://www.chipotle.com/content/dam/chipotle/documents/chipotle-nutrition-en.pdf"
    # Fallback HTML page
    HTML_URL = "https://www.chipotle.com/nutrition"

    async def scrape_menu(self) -> list[MenuItemData]:
        """Chipotle publishes an HTML nutrition page with a structured table."""
        from playwright.async_api import async_playwright

        items = []
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            await page.goto(self.HTML_URL, wait_until="domcontentloaded", timeout=45000)
            await self.polite_delay()

            html = await page.content()
            await browser.close()

        soup = BeautifulSoup(html, "lxml")
        # Chipotle renders nutrition in table rows; each has category + item
        current_category = "Menu"
        for row in soup.select("tr"):
            cells = [c.get_text(strip=True) for c in row.find_all(["th", "td"])]
            if not cells:
                continue
            # Category header rows are single bold cells
            if len(cells) == 1:
                current_category = cells[0]
                continue
            if len(cells) < 4:
                continue
            name = cells[0]
            if not name or name.lower() in ("item", "food item"):
                continue
            try:
                items.append(MenuItemData(
                    name=name,
                    category=current_category,
                    serving_size=cells[1] if len(cells) > 1 else "",
                    calories=self.safe_int(cells[2]) if len(cells) > 2 else None,
                    total_fat_g=self.safe_float(cells[3]) if len(cells) > 3 else None,
                    saturated_fat_g=self.safe_float(cells[4]) if len(cells) > 4 else None,
                    trans_fat_g=self.safe_float(cells[5]) if len(cells) > 5 else None,
                    cholesterol_mg=self.safe_int(cells[6]) if len(cells) > 6 else None,
                    sodium_mg=self.safe_int(cells[7]) if len(cells) > 7 else None,
                    total_carbs_g=self.safe_float(cells[8]) if len(cells) > 8 else None,
                    dietary_fiber_g=self.safe_float(cells[9]) if len(cells) > 9 else None,
                    total_sugars_g=self.safe_float(cells[10]) if len(cells) > 10 else None,
                    protein_g=self.safe_float(cells[11]) if len(cells) > 11 else None,
                ))
            except (IndexError, ValueError):
                continue
        return items
