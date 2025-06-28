import os
import sys
import psutil
import asyncio
import requests
from xml.etree import ElementTree
from typing import List
import os
import pandas as pd
import sqlite3
from datetime import datetime
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode


__location__ = os.path.dirname(os.path.abspath(__file__))
__output__ = os.path.join(__location__, "output")

# Append parent directory to system path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)


def load_db():
    # Connect to the database, fetch urls and return a list of urls
    conn = sqlite3.connect('carousell_laptops.db')
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    c.execute("SELECT listing_url FROM listings")
    rows = [row[0] for row in c.fetchall()]
    conn.close()


# List of URLs to crawl
urls = [
    "https://www.carousell.sg/p/amazon-kindle-1376801060/?t-id=_7BW4jCbxI_1750788643825&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=MhDE8S_5hq6d65KU&t-referrer_sort_by=popular&t-tap_index=0",
    "https://www.carousell.sg/p/amazon-kindle-1376801060/?t-id=Q4CvTieSb0_1750788909645&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=CjpWhbLj9Lq0I6YI&t-referrer_sort_by=popular&t-tap_index=0",
    "https://www.carousell.sg/p/amazon-kindle-1376801060/?t-id=XIhNmy7ySR_1750789072392&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=r4BCS2Q7rrxtc1Vh&t-referrer_sort_by=popular&t-tap_index=0",
    "https://www.carousell.sg/p/amazon-kindle-1376801060/?t-id=xDE4GVIOVS_1750789578018&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=gHPfM3K9U8UPEtvB&t-referrer_sort_by=popular&t-tap_index=0",
    "https://www.carousell.sg/p/asus-laptop-windows-10-1376799626/?t-id=xDE4GVIOVS_1750789578018&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=gHPfM3K9U8UPEtvB&t-referrer_sort_by=popular&t-tap_index=1",
    "https://www.carousell.sg/p/hp-stream-11-ak0xxx-in-white-1376799193/?t-id=xDE4GVIOVS_1750789578018&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=gHPfM3K9U8UPEtvB&t-referrer_sort_by=popular&t-tap_index=2",
    "https://www.carousell.sg/p/lenovo-i5-10th-gen-16gb-ram-512gb-ssd-1376796269/?t-id=xDE4GVIOVS_1750789578018&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=gHPfM3K9U8UPEtvB&t-referrer_sort_by=popular&t-tap_index=3",
    "https://www.carousell.sg/p/yoga-lenovo-l13-touchscreen-with-stylus-2-in-1-laptop-1376796219/?t-id=xDE4GVIOVS_1750789578018&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=gHPfM3K9U8UPEtvB&t-referrer_sort_by=popular&t-tap_index=5",
    "https://www.carousell.sg/p/2025-asus-tuf-a16-amd-ryzen-9-8940hx-rtx-5070-32gb-ddr5-ram-2-5k-2560-x-1600-wqxga-qhd-165hz-screen-1tb-ssd-jaeger-grey-gaming-laptop-notebook-1308525888/?t-id=xDE4GVIOVS_1750789578018&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=gHPfM3K9U8UPEtvB&t-referrer_sort_by=popular&t-tap_index=6",
    "https://www.carousell.sg/p/wts-asus-tuf-f15-rtx-3050-i7-12th-gen-gaming-laptop-warranty-2027-1376795730/?t-id=xDE4GVIOVS_1750789578018&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=gHPfM3K9U8UPEtvB&t-referrer_sort_by=popular&t-tap_index=7"
]

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
            print(results[0])

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
