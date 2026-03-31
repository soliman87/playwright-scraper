import asyncio
from playwright.async_api import async_playwright
from src.exporter import export_to_csv

URL = "https://quotes.toscrape.com/"

async def scrape():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        await page.goto(URL)

        quotes = await page.query_selector_all(".quote")

        data = []

        for q in quotes:
            text = await q.query_selector(".text")
            author = await q.query_selector(".author")

            data.append({
                "text": await text.inner_text(),
                "author": await author.inner_text()
            })

        await browser.close()
        return data


async def main():
    data = await scrape()
    export_to_csv(data)


if __name__ == "__main__":
    asyncio.run(main())
