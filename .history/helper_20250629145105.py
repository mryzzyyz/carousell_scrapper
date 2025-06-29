import re
import sqlite3
import os
import pandas as pd
from datetime import datetime

def validate_listing(listing):
    """Validate required fields in a listing"""
    required_fields = ['listing_date', 'title', 'price', 'condition', 'url']
    return all(field in listing and listing[field] for field in required_fields)


def extract_price(price_str):
    if not price_str:
        return None
    # Extract digits and remove S$, commas, etc.
    cleaned = re.sub(r"[^\d]", "", price_str)
    return int(cleaned) if cleaned.isdigit() else None

def extract_listing_id(url: str) -> str:
    match = re.search(r'/p/[^/]+-(\d+)', url)
    return match.group(1) if match else None

def save_to_sqlite(listings):

    conn = sqlite3.connect('carousell_laptops.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS listings (
        id INTEGER PRIMARY KEY AUTOINCREMENT, -- unique id for each listing
        datetime TEXT, -- timestamp of when the listing was scraped
        title TEXT, -- laptop title
        price REAL,  -- in SGD
        condition TEXT, -- brand new, like new, lightly used, well used, heavily used
        likes INTEGER, -- number of likes
        listing_url TEXT, -- listing url 
        sold_status INTEGER, -- 0 for available, 1 for sold/reserved
        sold_datetime TEXT, -- timestamp when the laptop was sold
        description TEXT, -- laptop description
        grading REAL, -- laptop grading
        seller_name TEXT,
        seller_url TEXT,
        seller_rating REAL,
        review_count INTEGER,
        years_on_carousell REAL,
        time_to_sell INTEGER,
        thumbnail_url TEXT,
        category TEXT, -- laptop category
        brand TEXT, -- laptop brand
        model TEXT, -- laptop model
        specifications TEXT, -- laptop specifications
        features TEXT, -- laptop features
        processor TEXT, -- laptop processor
        ram TEXT, -- laptop RAM
        storage TEXT, -- laptop storage
        screen_size TEXT, -- laptop screen size
        display_size TEXT, -- laptop display size
        battery_life TEXT, -- laptop battery life
        operating_system TEXT, -- laptop operating system
        camera TEXT, -- laptop camera
        dimensions TEXT, -- laptop dimensions
        item_weight TEXT, -- laptop weight
        warranty TEXT, -- laptop warranty
        warranty_duration TEXT, -- laptop warranty duration
        warranty_type TEXT, -- laptop warranty type
        warranty_coverage TEXT, -- laptop warranty coverage
        delivery_method TEXT, -- laptop delivery method
        return_policy TEXT, -- laptop return policy
        shipping_charge TEXT, -- laptop shipping charge
        shipping_terms TEXT -- laptop shipping terms
    )
    ''')

    c.execute('''
    CREATE VIEW IF NOT EXISTS enriched_listings AS
    SELECT *,
        CAST(JULIANDAY(sold_datetime) - JULIANDAY(datetime) AS INTEGER) AS time_to_sell,
        CAST(JULIANDAY('now') - JULIANDAY(datetime) AS INTEGER) AS days_since_posted,
        LENGTH(title) AS title_length,
        LENGTH(description) AS desc_length,
        CASE WHEN seller_rating >= 4.5 AND review_count > 30 THEN 1 ELSE 0 END AS is_premium_seller,
        CASE WHEN price < 500 THEN 1 ELSE 0 END AS is_cheap,
        CASE
            WHEN condition = 'Brand new' THEN 5
            WHEN condition = 'Like new' THEN 4
            WHEN condition = 'Lightly used' THEN 3
            WHEN condition = 'Well used' THEN 1
            WHEN condition = 'Heavily used' THEN 0
            ELSE 0
        END AS condition_score
    FROM listings
    WHERE sold_status = 1 AND sold_datetime IS NOT NULL
    ''')

    # Convert to DataFrame and filter valid listings
    valid_listings = [listing for listing in listings if validate_listing(listing)]

    # Insert data
    for item in valid_listings:
        c.execute('''
            INSERT INTO listings 
            (datetime, title, price, condition, likes, listing_url, sold_status, thumbnail_url)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            timestamp.isoformat(),
            item['title'],
            item['price'],
            item['condition'],
            item['likes'],
            item['url'],
            0,
            item['img']
        ))

    conn.commit()
    print(f"Successfully saved {len(valid_listings)} listings to database")

    with open('carousell_dump.sql', 'w', encoding='utf-8') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
    print("Dumped database to carousell_dump.sql")

    with open(os.path.join('backup', f'backup_{timestamp.strftime("%Y-%m-%d_%H-%M-%S")}.sql'), 'w', encoding='utf-8') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
    print(f"Backup saved to backup/backup_{timestamp.strftime("%Y-%m-%d_%H-%M-%S")}.sql")
    conn.close()


def save_to_csv(listings):
    df = pd.DataFrame(listings)
    csv_file = f"laptops_history.csv"
    if os.path.exists(csv_file):
        df.to_csv(csv_file, mode='a', index=True, header=False)
    else:
        df.to_csv(csv_file, mode='w', index=True, header=[ "date","title", "price", "condition", "likes", "url"])
    print("Appended today's listings to:", csv_file)