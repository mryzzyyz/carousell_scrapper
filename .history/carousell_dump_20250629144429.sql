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
        shipping_terms TEXT, -- laptop shipping terms
        );

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

INSERT INTO "listings" VALUES(1,'2025-06-29T01:35:14.920941','MacBook Pro M4 16G/512G with Apple care 14inch',1798.0,'Brand new',0,'https://www.carousell.sg/p/macbook-pro-m4-16g-512g-with-apple-care-14inch-1377544588/?t-id=ZxskKcYDHd_1751132112802&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=8mvfmjG_U2MCvPf4&t-referrer_sort_by=popular&t-tap_index=0',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(2,'2025-06-29T01:35:14.920941','Apple MacBook Air 13-inch (2018)',320.0,'Lightly used',0,'https://www.carousell.sg/p/apple-macbook-air-13-inch-2018-1377542876/?t-id=ZxskKcYDHd_1751132112802&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=8mvfmjG_U2MCvPf4&t-referrer_sort_by=popular&t-tap_index=1',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(3,'2025-06-29T01:35:14.920941','M1 MacBook Air - 16GB RAM 256GB SSD',700.0,'Lightly used',0,'https://www.carousell.sg/p/m1-macbook-air-16gb-ram-256gb-ssd-1377541117/?t-id=ZxskKcYDHd_1751132112802&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=8mvfmjG_U2MCvPf4&t-referrer_sort_by=popular&t-tap_index=2',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(4,'2025-06-29T01:35:14.920941','ASUS ZenBook Laptop - Navy Blue',1350.0,'Like new',0,'https://www.carousell.sg/p/asus-zenbook-laptop-navy-blue-1377540970/?t-id=ZxskKcYDHd_1751132112802&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=8mvfmjG_U2MCvPf4&t-referrer_sort_by=popular&t-tap_index=3',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(5,'2025-06-29T01:35:14.920941','Dell Latitude Entertainment Laptop, 15.6” LED, Intel Core i5 CPU, SSD & HDD Dual Storage, HDMI, HD Camera, Win11 Pro , Ms office 2021 , 4hour ++ battery.',139.0,'Lightly used',0,'https://www.carousell.sg/p/dell-latitude-entertainment-laptop-15-6%E2%80%9D-led-intel-core-i5-cpu-ssd-hdd-dual-storage-hdmi-hd-camera-win11-pro-ms-office-2021-4hour-battery-1377540841/?t-id=ZxskKcYDHd_1751132112802&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=8mvfmjG_U2MCvPf4&t-referrer_sort_by=popular&t-tap_index=5',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(6,'2025-06-29T01:35:14.920941','Dell XPS 9315 Laptop - Like New Condition',850.0,'Like new',0,'https://www.carousell.sg/p/dell-xps-9315-laptop-like-new-condition-1377540767/?t-id=ZxskKcYDHd_1751132112802&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=8mvfmjG_U2MCvPf4&t-referrer_sort_by=popular&t-tap_index=6',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(7,'2025-06-29T01:35:14.920941','Dell WD19S180W docking station',100.0,'Brand new',0,'https://www.carousell.sg/p/dell-wd19s180w-docking-station-1377539264/?t-id=ZxskKcYDHd_1751132112802&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=8mvfmjG_U2MCvPf4&t-referrer_sort_by=popular&t-tap_index=7',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(8,'2025-06-29T01:35:14.920941','Lenovo ThinkPad Laptop like Razer Alienware DELL Apple Macbook',250.0,'Well used',1,'https://www.carousell.sg/p/lenovo-thinkpad-laptop-like-razer-alienware-dell-apple-macbook-1377539169/?t-id=ZxskKcYDHd_1751132112802&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=8mvfmjG_U2MCvPf4&t-referrer_sort_by=popular&t-tap_index=8',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(9,'2025-06-29T01:35:14.920941','HP ZBook 14 (G2) Mobile Workstation - AMD FirePro M4150 GPU / 4G-LTE Module / 16GB Ram /14.0" HD+ Display / 128G SSD+500GB HDD / fast speed',199.0,'Well used',0,'https://www.carousell.sg/p/hp-zbook-14-g2-mobile-workstation-amd-firepro-m4150-gpu-4g-lte-module-16gb-ram-14-0-hd-display-128g-ssd-500gb-hdd-fast-speed-1377538456/?t-id=ZxskKcYDHd_1751132112802&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=8mvfmjG_U2MCvPf4&t-referrer_sort_by=popular&t-tap_index=9',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(10,'2025-06-29T01:35:14.920941','Lenovo Thinkpad thunderbolt 3 docking station/dock',150.0,'Brand new',0,'https://www.carousell.sg/p/lenovo-thinkpad-thunderbolt-3-docking-station-dock-1377538329/?t-id=ZxskKcYDHd_1751132112802&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=8mvfmjG_U2MCvPf4&t-referrer_sort_by=popular&t-tap_index=10',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(11,'2025-06-29T01:35:14.920941','2017 MacBook Air 13” 2017 128GB',250.0,'Well used',1,'https://www.carousell.sg/p/2017-macbook-air-13%E2%80%9D-2017-128gb-1377538161/?t-id=ZxskKcYDHd_1751132112802&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=8mvfmjG_U2MCvPf4&t-referrer_sort_by=popular&t-tap_index=11',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('listings',11);
COMMIT;
