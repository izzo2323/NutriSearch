"""Starbucks — scrapes their public menu page."""
import httpx
from bs4 import BeautifulSoup
from base_scraper import BaseScraper, MenuItemData


class StarbucksScraper(BaseScraper):
    name         = "Starbucks"
    slug         = "starbucks"
    website      = "https://www.starbucks.com"
    cuisine_type = "Coffee / Café"

    MENU_API = "https://www.starbucks.com/menu"

    async def scrape_menu(self) -> list[MenuItemData]:
        from playwright.async_api import async_playwright

        items = []
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()

            # Capture XHR calls that contain nutrition
            nutrition_data = {}

            async def handle_response(response):
                if "nutrition" in response.url and response.status == 200:
                    try:
                        body = await response.json()
                        nutrition_data[response.url] = body
                    except Exception:
                        pass

            page.on("response", handle_response)
            await page.goto(self.MENU_API, wait_until="domcontentloaded", timeout=60000)
            await self.polite_delay(2, 4)

            # Navigate through categories
            category_links = await page.query_selector_all("a[href*='/menu/']")
            category_urls = list({
                await link.get_attribute("href")
                for link in category_links
                if await link.get_attribute("href")
            })

            for url in category_urls[:20]:
                full_url = f"https://www.starbucks.com{url}" if url.startswith("/") else url
                await page.goto(full_url, wait_until="domcontentloaded", timeout=30000)
                await self.polite_delay(1, 2)

                html = await page.content()
                soup = BeautifulSoup(html, "lxml")

                category = soup.select_one("h1")
                cat_name = category.get_text(strip=True) if category else "Menu"

                for card in soup.select("[data-e2e='menu-item-tile'], .menu-item, [class*='menuItem']"):
                    name_el = card.select_one("h2, h3, [class*='name']")
                    cal_el  = card.select_one("[class*='calorie'], [data-e2e*='calorie']")
                    if not name_el:
                        continue
                    items.append(MenuItemData(
                        name=name_el.get_text(strip=True),
                        category=cat_name,
                        calories=self.safe_int(cal_el.get_text(strip=True) if cal_el else None),
                    ))

            await browser.close()

        # De-duplicate
        seen = set()
        unique = []
        for item in items:
            if item.name not in seen:
                seen.add(item.name)
                unique.append(item)
        return unique
