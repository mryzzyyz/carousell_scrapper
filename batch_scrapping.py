import os
import sys
import psutil
import asyncio
from typing import List
import sqlite3
from datetime import datetime
from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from helper import extract_price
import re
from telebot import send_debug_message_to_telegram

FETCH_UNTIL = 3 # Fetch listings from the last 3 days

__location__ = os.path.dirname(os.path.abspath(__file__))
__output__ = os.path.join(__location__, "output")

# Append parent directory to system path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

# Load the list of URLs to crawl from the database
def load_url_ids_list(fetch_until):
    # Connect to the database, fetch urls and return a list of urls
    conn = sqlite3.connect('carousell_laptops.db')
    c = conn.cursor()
    c.execute(f"""SELECT listing_url, id
              FROM listings WHERE sold_status = 0 
              AND DATE(datetime) >= DATE('now', '-{fetch_until} days')""")
    rows = c.fetchall()
    conn.close()
    return rows

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

        # -- Seller info block --
        seller_rating = None
        years_on_carousell = None
        try:
            seller_marker = soup.find('p', string='Meet the seller')
            if seller_marker:
                siblings = seller_marker.parent.find_next_siblings()
                if siblings:
                    seller_block = siblings[0]

                    # Seller rating
                    rating_elem = seller_block.find('p', class_=re.compile("D_bMw.*D_bMx.*"))
                    if rating_elem:
                        match = re.search(r"[\d.]+", rating_elem.get_text(strip=True))
                        if match:
                            seller_rating = float(match.group(0))

                    # Extract all <p> tags in that block
                    all_p_tags = seller_block.find_all('p')

                    for p in all_p_tags:
                        text = p.get_text(strip=True).lower()

                        # Years on Carousell
                        if "year" in text or "month" in text:
                            match = re.search(r"(\d+)", text)
                            if match:
                                value = int(match.group(1))
                                if "year" in text:
                                    years_on_carousell = value
                                elif "month" in text:
                                    years_on_carousell = round(value / 12, 2)
        except Exception as e:
            print("❌ Seller info block error:", e)

        # --- Rating + Review Count ---
        review_count = None
        try:
            rating_review_p = soup.find('p', string=lambda text: text and "review" in text.lower() and re.search(r"\d+(\.\d+)?", text))
            if rating_review_p:
                text = rating_review_p.get_text(strip=True)

                # Rating (e.g., 5.0)
                rating_match = re.search(r"(\d+\.\d+|\d+)", text)
                if rating_match:
                    review_count = float(rating_match.group(1))

        except Exception as e:
            print("❌ Rating/Review block error:", e)

        seller_rating = None
        try:
            # Look for div with aria-label like "5 stars"
            star_block = soup.find("div", attrs={"aria-label": re.compile(r"\d+(\.\d+)?\s+stars")})
            if star_block:
                # Extract rating from aria-label
                label = star_block["aria-label"]
                match = re.search(r"(\d+(\.\d+)?)", label)
                if match:
                    seller_rating = float(match.group(1))
        except Exception as e:
            print("❌ Review extraction error:", e)

        

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
                print(f"Parsed listing {listing['id']} from {url}: {listing}")

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
            SET price = ?, sold_status =?, sold_datetime =?, description =?, seller_url =?, seller_rating =?, review_count =?, years_on_carousell =?
            WHERE id = ?
        ''', (listing['price'], listing['sold_status'], listing['sold_datetime'], listing['description'], listing['seller_url'], listing['seller_rating'], listing['review_count'], listing['years_on_carousell'], listing['id']))

    conn.commit()
    conn.close()
    print(f"Updated {len(listings)} listings in the database.")


async def main():
    if urls:
        print(f"Found {len(urls)} URLs to crawl")
        listings = await crawl_parallel(urls, max_concurrent=3)
        send_debug_message_to_telegram(f"{len(listings)} listings crawled successfully.")


        print(f"Updated {len(listings)} listings in the database.")
        update_db(listings)

    else:
        print("No URLs found to crawl")
        send_debug_message_to_telegram("No URLs found to crawl.")


if __name__ == "__main__":
    asyncio.run(main())
