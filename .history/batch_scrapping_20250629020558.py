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
import re

FETCH_UNTIL = 3


__location__ = os.path.dirname(os.path.abspath(__file__))
__output__ = os.path.join(__location__, "output")

# Append parent directory to system path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)


def load_url_ids_list(fetch_until):
    # Connect to the database, fetch urls and return a list of urls
    conn = sqlite3.connect('carousell_laptops.db')
    c = conn.cursor()
    c.execute(f"SELECT listing_url, datetime FROM listings WHERE DATE(datetime) >= DATE('now', '-{fetch_until} days')")
    rows = c.fetchall()
    conn.close()
    return rows

def parse_listing_fields(result):
    try:
        html = result._results[0].html
        soup = BeautifulSoup(html, "html.parser")
        description = soup.find("meta", {"name": "description"})

        review_elem = soup.find("p", string=lambda t: "review" in t.lower())  # finds first <p> with "review"
        
        seller_rating_elem = soup.find("span", string=lambda t: t and re.match(r"^\d\.\d$", t.strip()))
        seller_rating = float(seller_rating_elem.text.strip()) if seller_rating_elem else None
        print(seller_rating)

        years_elem = soup.find("span", string=lambda t: t and "year" in t.lower() and "carousell" in t.lower())
        years_on_carousell = int(re.search(r"\d+", years_elem.text).group()) if years_elem else None
        print(years_on_carousell)
                
        seller_url_elem = soup.find("a", href=lambda x: x and "/u/" in x)
        if seller_url_elem:
            seller_url = "https://www.carousell.sg" + seller_url_elem.get("href", "")
        else:
            print("❌ Could not find seller URL. Dumping HTML:")
            print(soup.prettify()[:2000])
            seller_url = ""


        return {
            "sold_status": 1 if "Reserved" in html or "Sold" in html else 0,
            "sold_datetime": datetime.now().isoformat() if "Sold" in html else None,
            "description": description["content"] if description else "",
            "grading": None,  # Placeholder; can be added by AI scoring
            "seller_url": seller_url,
            "seller_rating": seller_rating,
            "review_count": int(review_elem.text.split()[0]) if review_elem else None,
            "years_on_carousell": years_on_carousell
        }
    except Exception as e:
        print("❌ Parsing error:", e)
        return {}

# List of URLs to crawl
urls = [row[0] for row in load_url_ids_list(FETCH_UNTIL)]
ids = [row[1] for row in load_url_ids_list(FETCH_UNTIL)]

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
                    "id": ids[i],  # unique id for each listing
                    **parsed
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
        return parsed_listings

def update_db(listings):
    conn = sqlite3.connect('carousell_laptops.db')
    cursor = conn.cursor()

    # Insert listings into the database
    for listing in listings:
        cursor.execute('''
            UPDATE listings
            SET sold_status =?, sold_datetime =?, description =?, grading =?, seller_url =?, seller_rating =?, review_count =?, years_on_carousell =?
            WHERE id = ?
        ''', (listing['sold_status'], listing['sold_datetime'], listing['description'], listing['grading'], listing['seller_url'], listing['seller_rating'], listing['review_count'], listing['years_on_carousell'], listing['id']))

    conn.commit()
    conn.close()
    print(f"Updated {len(listings)} in the database.")

async def main():
    if urls:
        print(f"Found {len(urls)} URLs to crawl")
        listings = await crawl_parallel(urls, max_concurrent=3)
        print(listings)
        update_db(listings)

    else:
        print("No URLs found to crawl")

if __name__ == "__main__":
    asyncio.run(main())
