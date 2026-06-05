from chains._generic_table import GenericTableScraper


class BurgerKingScraper(GenericTableScraper):
    name         = "Burger King"
    slug         = "burger-king"
    website      = "https://www.bk.com"
    cuisine_type = "Fast Food"
    url          = "https://www.bk.com/pdfs/nutrition.pdf"

    async def scrape_menu(self):
        # BK uses a navigable web menu rather than a static table
        self.url = "https://www.bk.com/menu/burgers"
        from playwright.async_api import async_playwright
        from bs4 import BeautifulSoup
        from base_scraper import MenuItemData

        items = []
        categories = [
            ("Burgers", "https://www.bk.com/menu/burgers"),
            ("Chicken & Fish", "https://www.bk.com/menu/chicken-fish"),
            ("Sides", "https://www.bk.com/menu/sides"),
            ("Beverages", "https://www.bk.com/menu/beverages"),
            ("Breakfast", "https://www.bk.com/menu/breakfast"),
            ("Salads & Wraps", "https://www.bk.com/menu/salads-wraps"),
            ("Desserts", "https://www.bk.com/menu/desserts"),
        ]
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page    = await browser.new_page()
            for cat_name, url in categories:
                await page.goto(url, wait_until="domcontentloaded", timeout=30000)
                await self.polite_delay()
                html = await page.content()
                soup = BeautifulSoup(html, "lxml")
                for card in soup.select("[class*='menu-item'], [data-testid*='menu']"):
                    name_el = card.select_one("h2, h3, [class*='title'], [class*='name']")
                    cal_el  = card.select_one("[class*='calorie'], [class*='cal']")
                    if not name_el:
                        continue
                    items.append(MenuItemData(
                        name=name_el.get_text(strip=True),
                        category=cat_name,
                        calories=self.safe_int(cal_el.get_text(strip=True) if cal_el else None),
                    ))
            await browser.close()
        return items
