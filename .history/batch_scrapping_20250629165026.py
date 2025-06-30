import os
import sys
import psutil
import asyncio
from typing import List
import sqlite3
from datetime import datetime
from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from helper import extract_price, load_url_ids_list
import re

FETCH_UNTIL = 3 # Fetch listings from the last 3 days

__location__ = os.path.dirname(os.path.abspath(__file__))
__output__ = os.path.join(__location__, "output")

# Append parent directory to system path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

# Extract the listing fields from the HTML
def parse_listing_fields(result):
    try:
        html = result._results[0].html
        soup = BeautifulSoup(html, "html.parser")

        # --- Description ---
        description = ""
        try:
            meta_desc = soup.find("meta", {"name": "description"})
            description = meta_desc["content"] if meta_desc else ""
        except Exception as e:
            print("❌ Description error:", e)

        # --- Price (fallback to None if extract fails) ---
        updated_price = None
        try:
            price_elem = soup.find("meta", {"name": "twitter:data1"})
            if price_elem and price_elem.has_attr("content"):
                match = re.search(r"[\d,]+", price_elem["content"])
                if match:
                    updated_price = float(match.group(0).replace(",", ""))
        except Exception as e:
            print("❌ Price parsing failed:", e)

        # --- Review count ---
        review_count = None
        try:
            review_elem = soup.find("p", string=lambda t: t and "review" in t.lower())
            if review_elem:
                match = re.search(r"\((\d+)\s+reviews?\)", review_elem.text)
                if match:
                    review_count = int(match.group(1))
        except Exception as e:
            print("❌ Review count error:", e)

        # --- Seller info block ---
        seller_rating = None
        years_on_carousell = None
        try:
            seller_siblings = soup.find('p', string='Meet the seller').parent.find_next_siblings()
            if seller_siblings:
                seller_block = seller_siblings[0]

                # Seller rating
                rating_elem = seller_block.find('p', class_=re.compile("D_bMw.*D_bMx.*"))
                if rating_elem:
                    match = re.search(r"[\d.]+", rating_elem.get_text(strip=True))
                    if match:
                        seller_rating = float(match.group(0))

                # Years on Carousell
                years_elem = seller_block.find('p', class_=re.compile("D_bMw.*D_lI"))
                if years_elem:
                    text = years_elem.get_text(strip=True)
                    if "years" in text:
                        match = re.search(r"(\d+)", text)
                        years_on_carousell = int(match.group(1)) if match else None
                    elif "months" in text:
                        match = re.search(r"(\d+)", text)
                        years_on_carousell = round(int(match.group(1)) / 12, 2) if match else None
        except Exception as e:
            print("❌ Seller info block error:", e)

        # --- Seller URL ---
        seller_url = ""
        try:
            seller_url_elem = soup.find("a", href=lambda x: x and "/u/" in x)
            if seller_url_elem:
                seller_url = "https://www.carousell.sg" + seller_url_elem.get("href", "")
            else:
                print("❌ Seller URL not found")
        except Exception as e:
            print("❌ Seller URL error:", e)

        return {
            "sold_status": 1 if "Reserved" in html or "Sold" in html else 0,
            "sold_datetime": datetime.now().isoformat() if "Sold" in html else None,
            "description": description,
            "price": updated_price,
            "grading": None,
            "seller_url": seller_url,
            "seller_rating": seller_rating,
            "review_count": review_count,
            "years_on_carousell": years_on_carousell
        }

    except Exception as e:
        print("❌ Parsing failed completely:", e)
        return None

# List of URLs to crawl
urls = [row[0] for row in load_url_ids_list(FETCH_UNTIL)]
ids = [row[1] for row in load_url_ids_list(FETCH_UNTIL)]

# Crawl URL in batches
async def crawl_parallel(urls: List[str], max_concurrent: int = 3):
    print("\n=== Parallel Crawling with Browser Reuse + Memory Check ===")
    parsed_listings = []
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
        count = 0
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
            
                # Parse listing fields and store in a list
                parsed = parse_listing_fields(result)
                listing = {
                    "id": ids[count],  # unique id for each listing
                    **parsed
                }
                parsed_listings.append(listing)
                count += 1

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

# Update the database with the listings
def update_db(listings):
    conn = sqlite3.connect('carousell_laptops.db')
    cursor = conn.cursor()

    # Insert listings into the database
    for listing in listings:
        print(f"Updating listing {listing['id']} into the database...")

        cursor.execute('''
            UPDATE listings
            SET price = ?, sold_status =?, sold_datetime =?, description =?, grading =?, seller_url =?, seller_rating =?, review_count =?, years_on_carousell =?
            WHERE id = ?
        ''', (listing['price'], listing['sold_status'], listing['sold_datetime'], listing['description'], listing['grading'], listing['seller_url'], listing['seller_rating'], listing['review_count'], listing['years_on_carousell'], listing['id']))

    conn.commit()
    conn.close()
    print(f"Updated {len(listings)} listings in the database.")


async def main():
    if urls:
        print(f"Found {len(urls)} URLs to crawl")
        listings = await crawl_parallel(urls, max_concurrent=3)

        print(f"Updated {len(listings)} listings in the database.")
        update_db(listings)

    else:
        print("No URLs found to crawl")


if __name__ == "__main__":
    asyncio.run(main())
