import os
import sys
import psutil
import asyncio
import requests
from xml.etree import ElementTree
from typing import List
import pandas as pd
import sqlite3
from datetime import datetime
from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode

FETCH_UNTIL = 3


__location__ = os.path.dirname(os.path.abspath(__file__))
__output__ = os.path.join(__location__, "output")

# Append parent directory to system path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)


def load_url_list(fetch_until):
    # Connect to the database, fetch urls and return a list of urls
    conn = sqlite3.connect('carousell_laptops.db')
    c = conn.cursor()
    c.execute(f"SELECT listing_url, datetime FROM listings WHERE DATE(datetime) >= DATE('now', '-{fetch_until} days')")
    rows = [row[0] for row in c.fetchall()]
    conn.close()
    return rows

def parse_listing_fields(result):
    try:
        # print("Type:", type(result._results[0]))
        # print("Attributes:", dir(result._results[0]))

        html = result._results[0].page_content
        soup = BeautifulSoup(result._results[0].html, "html.parser")

        # Example extraction (adjust selectors as needed):
        description = soup.find("meta", {"name": "description"})
        seller_name = soup.select_one('[data-testid="seller-name"]')  # placeholder selector
        seller_url = soup.select_one('[data-testid="seller-profile-link"]')  # placeholder
        seller_rating_elem = soup.select_one('[data-testid="seller-rating"]')  # placeholder

        return {
            "sold_status": 1 if "Reserved" in result.page_content or "Sold" in result.page_content else 0,
            "sold_datetime": datetime.now().isoformat() if "Sold" in result.page_content else None,
            "description": description["content"] if description else "",
            "grading": None,  # Placeholder; can be added by AI scoring
            "seller_name": seller_name.text.strip() if seller_name else "",
            "seller_url": "https://www.carousell.sg" + seller_url['href'] if seller_url else "",
            "seller_rating": float(seller_rating_elem.text.strip()) if seller_rating_elem else None,
        }
    except Exception as e:
        print("❌ Parsing error:", e)
        return {}

# List of URLs to crawl
urls = load_url_list(FETCH_UNTIL)

async def crawl_parallel(urls: List[str], max_concurrent: int = 3):
    print("\n=== Parallel Crawling with Browser Reuse + Memory Check ===")

    # We'll keep track of peak memory usage across all tasks
    peak_memory = 0
    process = psutil.Process(os.getpid())

    def log_memory(prefix: str = ""):
        nonlocal peak_memory
        current_mem = process.memory_info().rss  # in bytes
        if current_mem > peak_memory:
            peak_memory = current_mem
        print(f"{prefix} Current Memory: {current_mem // (1024 * 1024)} MB, Peak: {peak_memory // (1024 * 1024)} MB")

    # Minimal browser config
    browser_config = BrowserConfig(
        headless=True,
        verbose=False,  # corrected from 'verbos=False'
        extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
    )
    crawl_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS)

    # Create the crawler instance
    crawler = AsyncWebCrawler(config=browser_config)
    await crawler.start()

    try:
        # We'll chunk the URLs in batches of 'max_concurrent'
        success_count = 0
        fail_count = 0
        for i in range(0, len(urls), max_concurrent):
            batch = urls[i : i + max_concurrent]
            tasks = []

            for j, url in enumerate(batch):
                # Unique session_id per concurrent sub-task
                session_id = f"parallel_session_{i + j}"
                task = crawler.arun(url=url, config=crawl_config, session_id=session_id)
                tasks.append(task)

            # Check memory usage prior to launching tasks
            log_memory(prefix=f"Before batch {i//max_concurrent + 1}: ")

            # Gather results
            results = await asyncio.gather(*tasks, return_exceptions=True)
            parsed_listings = []
            
            # Check memory usage after tasks complete
            log_memory(prefix=f"After batch {i//max_concurrent + 1}: ")

            # Evaluate results
            for url, result in zip(batch, results):
                if isinstance(result, Exception):
                    print(f"Error crawling {url}: {result}")
                    fail_count += 1
                elif result.success:
                    success_count += 1
                else:
                    fail_count += 1
                    # Build final record (add your scraped values too: title, price, likes, etc.)
                parsed = parse_listing_fields(result)
                listing = {
                    "date": datetime.today().strftime("%Y-%m-%d"),
                    "title": result.meta.get("title", ""),
                    "price": result.meta.get("price", ""),
                    "condition": result.meta.get("condition", ""),
                    "likes": result.meta.get("likes", 0),
                    "url": url,
                    **parsed  # unpacks sold_status, desc, seller_name, etc.
                }

                parsed_listings.append(listing)

        print(f"\nSummary:")
        print(f"  - Successfully crawled: {success_count}")
        print(f"  - Failed: {fail_count}")

    finally:
        print("\nClosing crawler...")
        await crawler.close()
        # Final memory log
        log_memory(prefix="Final: ")
        print(f"\nPeak memory usage (MB): {peak_memory // (1024 * 1024)}")

# Create SQLite database and table for listings
def create_db():
    conn = sqlite3.connect('carousell_listings.db')  # Create or connect to the database
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS listings (
            date TEXT,
            title TEXT,
            price TEXT,
            condition TEXT,
            likes INTEGER,
            url TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Call this function once to set up the database
create_db()



def save_to_db(listings):
    conn = sqlite3.connect('carousell_listings.db')
    cursor = conn.cursor()

    # Insert listings into the database
    for listing in listings:
        cursor.execute('''
            INSERT INTO listings (date, title, price, condition, likes, url)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (listing['date'], listing['title'], listing['price'], listing['condition'], listing['likes'], listing['url']))

    conn.commit()
    conn.close()
    print("Saved today's listings to the database.")

async def main():
    if urls:
        print(f"Found {len(urls)} URLs to crawl")
        await crawl_parallel(urls, max_concurrent=3)
    else:
        print("No URLs found to crawl")

if __name__ == "__main__":
    asyncio.run(main())
