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
INSERT INTO "listings" VALUES(1,'2025-06-29T14:55:50.371928','Lenovo ThinkPad X12 Detachable Gen 1(Japan Keyboard) | Intel Core i5-1140G7/16GB Ram/256GB SSD | Windows 11 Pro + MS Office 2021 | 1 Month Shop Warranty',499.0,'Like new',67,'https://www.carousell.sg/p/lenovo-thinkpad-x12-detachable-gen-1-japan-keyboard-intel-core-i5-1140g7-16gb-ram-256gb-ssd-windows-11-pro-ms-office-2021-1-month-shop-warranty-1255133393/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=0',0,NULL,'Buy Lenovo ThinkPad X12 Detachable Gen 1(Japan Keyboard) | Intel Core i5-1140G7/16GB Ram/256GB SSD | Windows 11 Pro + MS Office 2021 | 1 Month Shop Warranty  in Singapore,Singapore. Rare model on second hand market. Item is heavily utilised by previous user.

➡   Working Condition: 10/10
➡   Physical Condition: 7/10
➡   Model: Lenovo Th Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/recirculateit',5.0,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(2,'2025-06-29T14:55:50.371928','Apple MacBook Pro 14 M4 Pro 12 Core CPU (2024) - Silver',2599.0,'Like new',0,'https://www.carousell.sg/p/apple-macbook-pro-14-m4-pro-12-core-cpu-2024-silver-1377620399/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=1',0,NULL,'Buy Apple MacBook Pro 14 M4 Pro 12 Core CPU (2024) - Silver in Singapore,Singapore. Only used for college use but realized I need x86 hardware.

The specs are:
12 Core CPU 
16 Core GPU
24GB Unified RAM
512GB SSD Storage

Comes with:
-Original B Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/skysaph',4.9,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(3,'2025-06-29T14:55:50.371928','MacBook Air A2337 M1/8Gb/256Gb',649.0,'Lightly used',0,'https://www.carousell.sg/p/macbook-air-a2337-m1-8gb-256gb-1377619856/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=2',0,NULL,'Buy MacBook Air A2337 M1/8Gb/256Gb in Singapore,Singapore. Brand : Apple
Model : A2337
CPU : M1
Ram : 8Gb
Ssd : 256Gb
Size : 13”
Condition : 9~9.5/10
Warranty : 1 month

*no box  Get great deals on Laptops & Notebooks Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/astore2000',4.9,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(4,'2025-06-29T14:55:50.371928','Aftershock Forge 15R Gaming Laptop - Ryzen 5, RTX 2060',950.0,'Lightly used',0,'https://www.carousell.sg/p/aftershock-forge-15r-gaming-laptop-ryzen-5-rtx-2060-1377618538/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=3',0,NULL,'Buy Aftershock Forge 15R Gaming Laptop - Ryzen 5, RTX 2060 in Singapore,Singapore. - Aftershock Forge 15R gaming laptop
- AMD Ryzen 5 3600 6-Core processor
- 16GB RAM
- NVIDIA GeForce RTX 2060 graphics card
- 466GB SSD
- Customizable RGB keybo Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/eesmokee',5.0,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(5,'2025-06-29T14:55:50.371928','Brand New and Sealed! 14-inch Macbook Pro M4 Chip',1900.0,'Brand new',0,'https://www.carousell.sg/p/brand-new-and-sealed-14-inch-macbook-pro-m4-chip-1377617984/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=5',0,NULL,'Buy Brand New and Sealed! 14-inch Macbook Pro M4 Chip in Singapore,Singapore. Selling BRAND NEW and SEALED Apple Macbook Pro. 

- Space Black color
- 16gb RAM 
- 512gb SSD Storage
- 10-core CPU
- M4 chip
- 14” display
- In original packag Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/rejpleo',5.0,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(6,'2025-06-29T14:55:50.371928','Dell Gaming Laptop',330.0,'Lightly used',0,'https://www.carousell.sg/p/dell-gaming-laptop-1377616782/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=6',0,NULL,'Buy Dell Gaming Laptop in Singapore,Singapore. 戴尔品牌笔记本电脑，游戏专用！高性能标压CPU，GTX1050独立显卡，无磕碰，基本全新！
具体配置：
CPU：i5-7300HQ（第七代），主频2.3GHz，睿频3.8GHz，4核8线程！
内存：16GB DDR4 2400核磁，品牌“三星”
硬盘：128GB东芝SSD固态硬盘 NV协议+512GB机械硬盘
显卡（G Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/zhengjialong0517',5.0,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(7,'2025-06-29T14:55:50.371928','Apple MacBook Pro 13-inch (2017)',330.0,'Well used',0,'https://www.carousell.sg/p/apple-macbook-pro-13-inch-2017-1377616382/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=7',0,NULL,'Buy Apple MacBook Pro 13-inch (2017) in Singapore,Singapore. Apple MacBook Pro laptop with touch bar.
Space grey.
Well used.
13 inch, 3.1GHz dual-core Intel Core i5.
**No charger.
Meet up at Khatib MRT only.
No trades, ca Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/username_walker',5.0,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(8,'2025-06-29T14:55:50.371928','2021 Macbook Pro M1 14” mini led',1300.0,'Lightly used',0,'https://www.carousell.sg/p/2021-macbook-pro-m1-14%E2%80%9D-mini-led-1377616232/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=8',0,NULL,'Buy 2021 Macbook Pro M1  14” mini led in Singapore,Singapore. Good condition - no screen scratches, batt cycle count at 47 (see attached pic) 

For serious buyers. 

Comes with all standard accessories:-
65w charging brick Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/scottfree7',4.8,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(9,'2025-06-29T14:55:50.371928','Lenovo 14 Inch Laptop - Cheapest HBL Laptop - Good Condition - Good Battery Life - Offer Now !',99.0,'Like new',12,'https://www.carousell.sg/p/lenovo-14-inch-laptop-cheapest-hbl-laptop-good-condition-good-battery-life-offer-now-1364481875/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=9',0,NULL,'Buy Lenovo 14 Inch Laptop - Cheapest HBL Laptop - Good Condition - Good Battery Life - Offer Now ! in Singapore,Singapore. Click here for more special deal !!!
https://www.carousell.sg/u/buyatfuji/

👨‍🔧 FREE Additional 3 𝐌𝐨𝐧𝐭𝐡 𝐖𝐚𝐫𝐫𝐚𝐧𝐭𝐲 !! First 10 set only !!!

🎀𝐋𝐞𝐧𝐨𝐯𝐨 𝐈𝐧𝐭𝐞𝐥 𝐖𝐢 Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/buyatfuji',4.9,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(10,'2025-06-29T14:55:50.371928','Gaming X1 Yoga Laptop - Intel i7-11Th Generation Higher Configuration Like New Laptop - iRIS Xe Graphic Card (8GB) Super Fast 2 in 1 Laptop - With Warranty',888.0,'Like new',1,'https://www.carousell.sg/p/gaming-x1-yoga-laptop-intel-i7-11th-generation-higher-configuration-like-new-laptop-iris-xe-graphic-card-8gb-super-fast-2-in-1-laptop-with-warranty-1377611975/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=13',0,NULL,'Buy Gaming X1 Yoga Laptop - Intel i7-11Th Generation Higher Configuration Like New Laptop - iRIS Xe Graphic Card (8GB) Super Fast 2 in 1 Laptop - With Warranty in Singapore,Singapore. ✅ Specification: 
Windows 11 Pro , MS office 2021, Power point, Excel, Antivirus and All necessary software are installed.

✅Lenovo ThinkPad X1 Yoga Gen 6, ✅ Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/comlab',5.0,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(11,'2025-06-29T14:55:50.371928','Lenovo ThinkPad T14 Laptop',699.0,'Like new',0,'https://www.carousell.sg/p/lenovo-thinkpad-t14-laptop-1377611394/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=14',1,'2025-06-29T15:06:25.824593','Buy Lenovo ThinkPad T14 Laptop in Singapore,Singapore. Price fixed. no nego. Will block and ignore for nego. 

- Powerful Ryzen 7 Pro 5850U (8 core 16 thread)
- 512 GB nvme SSD
- LTE Module (just insert sim to use)
 Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/ting.preloved',5.0,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(12,'2025-06-29T14:55:50.371928','Apple MacBook Pro 14 Inch M2 Pro Chip | 512GB SSD | 16GB RAM',1800.0,'Like new',0,'https://www.carousell.sg/p/apple-macbook-pro-14-inch-m2-pro-chip-512gb-ssd-16gb-ram-1377611254/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=15',0,NULL,'Buy Apple MacBook Pro 14 Inch M2 Pro Chip | 512GB SSD | 16GB RAM in Singapore,Singapore. Selling a Apple Refurbished MacBook Pro, comes with original box and accessories. I have never used the official charging block and the MagSafe charging cable,  Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/nicholas8399',5.0,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(13,'2025-06-29T14:55:50.371928','iPad Pro 11" (4th Gen, M2, 256GB, WIFI) w/ Apple Pencil Gen 2',1100.0,'Lightly used',0,'https://www.carousell.sg/p/ipad-pro-11-4th-gen-m2-256gb-wifi-w-apple-pencil-gen-2-1377610553/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=16',0,NULL,'Buy iPad Pro 11" (4th Gen, M2, 256GB, WIFI) w/ Apple Pencil Gen 2 in Singapore,Singapore. Selling my well-maintained iPad Pro 11” 4th Generation (M2, 2022) – in excellent condition with no issues at all. Only used for Netflix. 

- comes with Apple Pe Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/akydaky',5.0,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(14,'2025-06-29T14:55:50.371928','🔋 100% MacBook Air M3 Chip 2024 15 inch',1280.0,'Like new',23,'https://www.carousell.sg/p/%F0%9F%94%8B-100-macbook-air-m3-chip-2024-15-inch-1376054996/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=17',0,NULL,'Buy 🔋 100% MacBook Air M3 Chip 2024 15 inch in Singapore,Singapore. Model : Apple MacBook Air M3 Chip 2024
Codition:Like new ,screen not scratch 
Memory:16GB 
Storage: 256SSD 
Battery 🔋:100% / Cycle Count-21
Colour:Starlight 

 Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/m.electronics',5.0,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(15,'2025-06-29T14:55:50.371928','LENOVO i7 - 11th Generation Higher Configuration Like New Laptop - RAM 16GB & SSD 512GB - Iris Xe Graphic Card - FHD 14 Inches Display - With Warranty',584.0,'Like new',0,'https://www.carousell.sg/p/lenovo-i7-11th-generation-higher-configuration-like-new-laptop-ram-16gb-ssd-512gb-iris-xe-graphic-card-fhd-14-inches-display-with-warranty-1377610152/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=18',0,NULL,'Buy LENOVO i7 - 11th Generation Higher Configuration Like New Laptop - RAM 16GB & SSD 512GB - Iris Xe Graphic Card - FHD 14 Inches Display - With Warranty in Singapore,Singapore. 



Specification: 
Windows 11 Pro , MS office 2021, Power point, Excel, Antivirus and All necessary software are installed.

LENOVO Thinkpad Ultraslim L Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/comlab',5.0,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(16,'2025-06-29T14:55:50.371928','Alienware m15 R3 (i7-10750H, RTX 2070 SUPER, 16GB RAM, 1TB Storage, FHD)',700.0,'Lightly used',1,'https://www.carousell.sg/p/alienware-m15-r3-i7-10750h-rtx-2070-super-16gb-ram-1tb-storage-fhd-1377609662/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=19',0,NULL,'Buy Alienware m15 R3 (i7-10750H, RTX 2070 SUPER, 16GB RAM, 1TB Storage, FHD) in Singapore,Singapore. Hi! Selling a used Alienware m15 R3 notebook. This notebook has spent the entirety of its life in a smoke-free, pet-free and child-free home and has been extrem Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/victoriavsx',4.9,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(17,'2025-06-29T14:55:50.371928','MacBook Pro (Retina, 13-inch, Early 2015)',200.0,'Well used',0,'https://www.carousell.sg/p/macbook-pro-retina-13-inch-early-2015-1377609489/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=20',0,NULL,'Buy MacBook Pro (Retina, 13-inch, Early 2015) in Singapore,Singapore. - MacBook Pro (Retina, 13-inch, Early 2015)
- 2.7 GHz Intel Core i5 processor
- 8GB RAM
- Intel Iris Graphics 6100 1536MB
- macOS Monterey
- Purchased July 2016 Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/bberry1106',5.0,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(18,'2025-06-29T14:55:50.371928','HP EliteBook 8470p Laptop',105.0,'Well used',12,'https://www.carousell.sg/p/hp-elitebook-8470p-laptop-1365840772/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=21',0,NULL,'Buy HP EliteBook 8470p Laptop in Singapore,Singapore. Selling a well-used HP EliteBook 8470p laptop. It''s a reliable workhorse with a sturdy build and a comfortable keyboard. The laptop has some signs of wear and t Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/blackmask34',4.4,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(19,'2025-06-29T14:55:50.371928','2 in 1 LAPTOP LENOVO X1 Yoga i7-11Th Generation - RAM 16GB - SSD 512GB - iRIS Xe Graphic Share 8171MB (8GB) - MS office 21 & Windows 11 Pro Already Installed - With Warranty',886.0,'Like new',0,'https://www.carousell.sg/p/2-in-1-laptop-lenovo-x1-yoga-i7-11th-generation-ram-16gb-ssd-512gb-iris-xe-graphic-share-8171mb-8gb-ms-office-21-windows-11-pro-already-installed-with-warranty-1377608684/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=22',0,NULL,'Buy 2 in 1 LAPTOP LENOVO X1 Yoga i7-11Th Generation - RAM 16GB - SSD 512GB - iRIS Xe Graphic Share 8171MB (8GB) - MS office 21 & Windows 11 Pro Already Installed - With Warranty in Singapore,Singapore. ✅ Specification: 
Windows 11 Pro , MS office 2021, Power point, Excel, Antivirus and All necessary software are installed.

✅Lenovo ThinkPad X1 Yoga Gen 6, ✅ Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/comlab',5.0,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(20,'2025-06-29T14:55:50.371928','Apple MacBook Air 13-inch (2019)',450.0,'Lightly used',0,'https://www.carousell.sg/p/apple-macbook-air-13-inch-2019-1377607787/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=26',0,NULL,'Buy Apple MacBook Air 13-inch (2019) in Singapore,Singapore. Selling off my beloved MacBook In a very good condition, no scratch

MacBook Air Retina, 2019
Processor:1.6Ghz Dual Core Intel Core i5
Storage 128 GB
Color: Ros Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/xuanyin118',4.9,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(21,'2025-06-29T14:55:50.371928','HP Elite x2 2-in-1 Laptop - 8GB RAM, 128GB SSD',280.0,'Lightly used',0,'https://www.carousell.sg/p/hp-elite-x2-2-in-1-laptop-8gb-ram-128gb-ssd-1377607341/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=27',0,NULL,'Buy HP Elite x2 2-in-1 Laptop - 8GB RAM, 128GB SSD in Singapore,Singapore. HP Elite x2 2-in-1 laptop with a detachable keyboard. Features an Intel i5-8250U CPU, 8GB RAM, and a 128GB SSD. It is running Windows 11 Pro. The laptop is in g Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/shopnyl',4.7,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(22,'2025-06-29T14:55:50.371928','Macbook Air 15 inch M3 16+512GB A3114',1388.0,'Like new',1,'https://www.carousell.sg/p/macbook-air-15-inch-m3-16-512gb-a3114-1377607064/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=28',0,NULL,'Buy Macbook Air 15 inch M3 16+512GB A3114 in Singapore,Singapore. Macbook Air M3 A3114 15" 
16GB RAM + 512GB SSD
starlight

Apple warranty till 13/02/2026

-Pristine condition 9.5/10 lightly used for 4 months 
-Flawless displa Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/hitecmobilesg',5.0,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(23,'2025-06-29T14:55:50.371928','Razer Blade 15 Base Model (2020) - RTX 2070',1000.0,'Lightly used',0,'https://www.carousell.sg/p/razer-blade-15-base-model-2020-rtx-2070-1377606170/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=30',0,NULL,'Buy Razer Blade 15 Base Model (2020) - RTX 2070 in Singapore,Singapore. Selling a Razer Blade 15 Base Model (2020). Features an Intel i7-10750H CPU, 16GB RAM, and a 476.9GB SSD. Equipped with an NVIDIA GeForce RTX 2070 with Max-Q De Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/wasabex',5.0,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(24,'2025-06-29T14:55:50.371928','Microsoft Surface Pro 9 - 256GB, 8GB RAM complete set',799.0,'Lightly used',3,'https://www.carousell.sg/p/microsoft-surface-pro-9-256gb-8gb-ram-complete-set-1377606077/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=31',0,NULL,'Buy Microsoft Surface Pro 9 - 256GB, 8GB RAM complete set in Singapore,Singapore. FOR SELL
COMPLETE SET
-Microsoft Surface Pro 9
- Includes tablet, keyboard, and box
- Blue color
- hardly used
-Lady user
-Bought from Challenger 7 Oct 2023
- G Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/cute_elephant',4.9,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(25,'2025-06-29T14:55:50.371928','Acer Laptop, Sound Burger, Hard Drives, Phone',100.0,'Well used',0,'https://www.carousell.sg/p/acer-laptop-sound-burger-hard-drives-phone-1377605617/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=32',0,NULL,'Buy Acer Laptop, Sound Burger, Hard Drives, Phone in Singapore,Singapore. - Acer laptop need to used chargers
- Sound Burger portable turntable
- Two external hard drives (WD and another brand)
- music player(power not coming)

All it Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/kyawaungwi36843',NULL,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(26,'2025-06-29T14:55:50.371928','Lenovo Thinkpad T14 Intel i7-10th Gen 16GB RAM 512GB SSD Windows 11 Pro Microsoft Office Preloaded 14.0" FHD Display Wifi 6 Slim light weight Laptop t14s t14 x1 carbon elitebook zenbook',450.0,'Like new',4,'https://www.carousell.sg/p/lenovo-thinkpad-t14-intel-i7-10th-gen-16gb-ram-512gb-ssd-windows-11-pro-microsoft-office-preloaded-14-0-fhd-display-wifi-6-slim-light-weight-laptop-t14s-t14-x1-carbon-elitebook-zenbook-1366194713/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=33',0,NULL,'Buy Lenovo Thinkpad T14 Intel i7-10th Gen 16GB RAM 512GB SSD Windows 11 Pro Microsoft Office Preloaded 14.0" FHD Display Wifi 6 Slim light weight Laptop t14s t14 x1 carbon elitebook zenbook in Singapore,Singapore. PRICE DROP FROM $529 to $479!
(Labour Day Sale Until 1 May)  

ONLY 10 SETS AVAILABLE

🔥Lenovo Thinkpad T14🔥    

Fast and Stable Slim Lightweight Lenovo Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/hypedemand2',5.0,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(27,'2025-06-29T14:55:50.371928','Samsung N148 Plus Laptop',60.0,'Well used',0,'https://www.carousell.sg/p/samsung-n148-plus-laptop-1377604286/?t-id=SQhdDpBxrh_1751180151386&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=x_aHvBnakjcjX7op&t-referrer_sort_by=popular&t-tap_index=34',0,NULL,'Buy Samsung N148 Plus Laptop in Singapore,Singapore. - Samsung N148 Plus laptop
- Intel Atom N450 processor
- 2GB RAM
- 32-bit operating system
- Includes original charger
- In good working condition Chat to Buy',NULL,NULL,'https://www.carousell.sg/u/ckkoffers',5.0,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(28,'2025-07-01T00:59:38.631917','MacBook Pro 16-inch (2019) – i7 | 16GB RAM | 500GB SSD | Excellent working Condition-no issue',699.0,'Like new',1,'https://www.carousell.sg/p/macbook-pro-16-inch-2019-%E2%80%93-i7-16gb-ram-500gb-ssd-excellent-working-condition-no-issue-1377924966/?t-id=olK7xSitYR_1751302811490&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=Hkx1V8R8F8TfIl_8&t-referrer_sort_by=popular&t-tap_index=2',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(29,'2025-07-01T00:59:38.631917','New In Box, Core i7, Radeon independent GPU,8GB Memory , 500GB, HDMI, Bluetooth, DVD-RW…DELL Latitude Business Laptop',19999.0,'Brand new',1,'https://www.carousell.sg/p/new-in-box-core-i7-radeon-independent-gpu-8gb-memory-500gb-hdmi-bluetooth-dvd-rw%E2%80%A6dell-latitude-business-laptop-1377924994/?t-id=olK7xSitYR_1751302811490&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=Hkx1V8R8F8TfIl_8&t-referrer_sort_by=popular&t-tap_index=1',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "listings" VALUES(30,'2025-07-01T00:59:38.631917','Lenovo Thinkpad Ryzen 5 pro, 16gb ram 512gb NVMe SSD Super fast like new laptop',420.0,'Like new',2,'https://www.carousell.sg/p/lenovo-thinkpad-ryzen-5-pro-16gb-ram-512gb-nvme-ssd-super-fast-like-new-laptop-1377919163/?t-id=olK7xSitYR_1751302811490&t-referrer_browse_type=categories&t-referrer_category_id=1793&t-referrer_page_type=category_browse&t-referrer_request_id=Hkx1V8R8F8TfIl_8&t-referrer_sort_by=popular&t-tap_index=8',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
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
INSERT INTO "sqlite_sequence" VALUES('listings',30);
COMMIT;
