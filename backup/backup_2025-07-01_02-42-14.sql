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
INSERT INTO "listings" VALUES(1,'2025-07-01T02:32:14.436363','MacBook Air M1 8GB 256GB 13" 2020 (with box)',600.0,'Like new',1,'https://www.carousell.sg/p/macbook-air-m1-8gb-256gb-13-2020-with-box-1377930405/?t-id=SIxc4sIlt9_1751308356967&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=lNl2nODN1BwKV_1U&t-referrer_sort_by=popular&t-tap_index=1',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(2,'2025-07-01T02:32:14.436363','M1 MacBook Air 500gb',550.0,'Like new',0,'https://www.carousell.sg/p/m1-macbook-air-500gb-1377928550/?t-id=SIxc4sIlt9_1751308356967&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=lNl2nODN1BwKV_1U&t-referrer_sort_by=popular&t-tap_index=3',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(3,'2025-07-01T02:36:04.722905','MacBook Air M1 8GB 256GB 13" 2020 (with box)',600.0,'Like new',1,'https://www.carousell.sg/p/macbook-air-m1-8gb-256gb-13-2020-with-box-1377930405/?t-id=V_wn6SluHA_1751308596147&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=N4qjfHZSt5Jm3UOp&t-referrer_sort_by=popular&t-tap_index=2',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(4,'2025-07-01T02:36:04.722905','M1 MacBook Air 500gb',550.0,'Like new',0,'https://www.carousell.sg/p/m1-macbook-air-500gb-1377928550/?t-id=V_wn6SluHA_1751308596147&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=N4qjfHZSt5Jm3UOp&t-referrer_sort_by=popular&t-tap_index=5',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(5,'2025-07-01T02:42:14.621119','HP i7 LAPTOP - 16/512GB RAM - With Warranty',496.0,'Like new',0,'https://www.carousell.sg/p/hp-i7-laptop-16-512gb-ram-with-warranty-1377934005/?t-id=ouwM79W01F_1751308957109&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=sTekU2J0QHLA8sdr&t-referrer_sort_by=popular&t-tap_index=1',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(6,'2025-07-01T02:42:14.621119','MacBook Air M1 8GB 256GB 13" 2020 (with box)',600.0,'Like new',1,'https://www.carousell.sg/p/macbook-air-m1-8gb-256gb-13-2020-with-box-1377930405/?t-id=ouwM79W01F_1751308957109&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=sTekU2J0QHLA8sdr&t-referrer_sort_by=popular&t-tap_index=3',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
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
INSERT INTO "sqlite_sequence" VALUES('listings',6);
COMMIT;
