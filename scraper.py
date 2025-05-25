# scraper.py
from playwright.sync_api import sync_playwright

def scrape_mytheresa():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.mytheresa.com/en-de/men/shoes.html")
        page.wait_for_selector(".product-tile")

        items = []
        product_tiles = page.query_selector_all(".product-tile")

        for tile in product_tiles[:20]:  # Adjust limit as needed
            name = tile.query_selector(".product-name")
            price = tile.query_selector(".price")
            img = tile.query_selector("img")

            item_data = {
                "name": name.inner_text().strip() if name else "N/A",
                "price": price.inner_text().strip() if price else "N/A",
                "image_url": img.get_attribute("src") if img else "N/A"
            }

            items.append(item_data)

        browser.close()
        return items