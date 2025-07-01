BEGIN TRANSACTION;
CREATE TABLE listings (
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
    );
INSERT INTO "listings" VALUES(1,'2025-07-01T02:50:31.759260','HP i7 LAPTOP - 16/512GB RAM - With Warranty',496.0,'Like new',0,'https://www.carousell.sg/p/hp-i7-laptop-16-512gb-ram-with-warranty-1377934005/?t-id=l7XuLOIh93_1751309454231&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=E_QeZ7_82-L0pluS&t-referrer_sort_by=popular&t-tap_index=1',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
CREATE VIEW enriched_listings AS
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
    WHERE sold_status = 1 AND sold_datetime IS NOT NULL;
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('listings',1);
COMMIT;
