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
INSERT INTO "listings" VALUES(1,'2025-07-01T04:11:06.100474','Lenovo ThinkPad X1 Carbon 8th Gen Ultrabook - 4K UHD - Intel Core i7',490.0,'Like new',0,'https://www.carousell.sg/p/lenovo-thinkpad-x1-carbon-8th-gen-ultrabook-4k-uhd-intel-core-i7-1377937444/?t-id=1uzQfqO2Gw_1751314297542&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=kVluYYOvfniXRMF8&t-referrer_sort_by=popular&t-tap_index=0',0,NULL,'Buy Lenovo ThinkPad X1 Carbon 8th Gen Ultrabook - 4K UHD - Intel Core i7 in Singapore,Singapore. 4.34.3 out of 5 stars(4)

Lenovo ThinkPad X1 Carbon 8th Gen 14" Ultrabook - 4K UHD - Intel Core i7 (8th Gen) i7-8650U Quad-core - 16GB RAM - 1TB SSD - Black - W Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/bestlaptopking',NULL,NULL,3.0,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(2,'2025-07-01T04:11:06.100474','Apple MacBook Air 13" M4 Midnight',1340.0,'Brand new',0,'https://www.carousell.sg/p/apple-macbook-air-13-m4-midnight-1377935978/?t-id=1uzQfqO2Gw_1751314297542&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=kVluYYOvfniXRMF8&t-referrer_sort_by=popular&t-tap_index=1',0,NULL,'Buy Apple MacBook Air 13" M4 Midnight in Singapore,Singapore. - Apple MacBook Air 13" M4 (Midnight)
- 10-Core CPU, 8-Core GPU
- 16GB Unified Memory
- 256GB SSD Storage
- 13.6-inch Liquid Retina display
- Magic Keyboard wit Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/guiffindor',5.0,NULL,5.0,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(3,'2025-07-01T17:37:02.054724','Lenovo 15” LOQ RTX 4060 Ryzen 7 7435HS|',950.0,'Like new',1,'https://www.carousell.sg/p/lenovo-15%E2%80%9D-loq-rtx-4060-ryzen-7-7435hs-1378043677/?t-id=vdz2lQDNLd_1751362644024&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=fcs3aqiYdn_QVEUs&t-referrer_sort_by=popular&t-tap_index=6',0,NULL,NULL,9.2,NULL,NULL,NULL,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(4,'2025-07-01T17:37:02.054724','Lenovo 14 Laptop - Lenovo N22 - Lenovo N42 - Superb Condition - Free MS Office - Free Windows 11 - Bag-ready - Air-light',99.0,'Like new',0,'https://www.carousell.sg/p/lenovo-14-laptop-lenovo-n22-lenovo-n42-superb-condition-free-ms-office-free-windows-11-bag-ready-air-light-1378046390/?t-id=vdz2lQDNLd_1751362644024&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=fcs3aqiYdn_QVEUs&t-referrer_sort_by=popular&t-tap_index=3',0,NULL,NULL,8.7,NULL,NULL,NULL,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(5,'2025-07-01T17:37:02.054724','HP 12 Intel Laptop - HP Laptop - Ideal for All Users - Fast Wi-Fi - Windows OS + MS Office- Bag-ready - Air-light',119.0,'Like new',0,'https://www.carousell.sg/p/hp-12-intel-laptop-hp-laptop-ideal-for-all-users-fast-wi-fi-windows-os-ms-office-bag-ready-air-light-1378046203/?t-id=vdz2lQDNLd_1751362644024&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=fcs3aqiYdn_QVEUs&t-referrer_sort_by=popular&t-tap_index=5',0,NULL,NULL,8.6,NULL,NULL,NULL,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(6,'2025-07-01T17:37:02.054724','Lenovo ThinkPad P16 G1 Mobile Workstation | 16” 4K Display | i9-12950HX vPro 64GB 1TB | NVIDIA RTX A5500 16GB VRAM | Windows 11 Pro |Lenovo Warranty',2599.0,'Like new',309,'https://www.carousell.sg/p/lenovo-thinkpad-p16-g1-mobile-workstation-16%E2%80%9D-4k-display-i9-12950hx-vpro-64gb-1tb-nvidia-rtx-a5500-16gb-vram-windows-11-pro-lenovo-warranty-1322947097/?t-id=vdz2lQDNLd_1751362644024&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=fcs3aqiYdn_QVEUs&t-referrer_sort_by=popular&t-tap_index=11',0,NULL,NULL,8.5,NULL,NULL,NULL,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
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
