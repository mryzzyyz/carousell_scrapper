from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import dateparser
from datetime import datetime
import os
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
from config import CAROUSELL_CONFIG, DB_CONFIG
import re



# Configuration from config file
SCRAP_DURATION = ["1 day ago", "2 days ago", "3 days ago", "4 days ago", "week ago"]

options = Options()
options.add_argument('--log-level=3')  
options.add_experimental_option("excludeSwitches", ["enable-logging"]) 
service = Service()  
driver = webdriver.Chrome(service=service, options=options)
driver.get(CAROUSELL_CONFIG['url'])

listings = []
current_date = datetime.today().date()
timestamp = datetime.now()

def scroll_to_bottom():
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to the bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.2)  # Wait for content to load

        # Check new scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break  # Reached the bottom
        last_height = new_height

def scroll_to_top():
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)  

def extract_price(price_str):
    if not price_str:
        return None
    # Extract digits and remove S$, commas, etc.
    cleaned = re.sub(r"[^\d]", "", price_str)
    return int(cleaned) if cleaned.isdigit() else None

def extract_listing_id(url: str) -> str:
    match = re.search(r'/p/[^/]+-(\d+)', url)
    return match.group(1) if match else None

# ----------------------------------------------------------------------------------------------------------

# # Step 1: Click first "Next"
# next_button = driver.find_element(By.XPATH, '//button[.//div[text()="Next"]]')
# driver.execute_script("arguments[0].click();", next_button)
# print("Clicked first 'Next'")

# # Step 2: Click second "Next"
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[.//div[text()="Next"]]')))
# next_button = driver.find_element(By.XPATH, '//button[.//div[text()="Next"]]')
# driver.execute_script("arguments[0].click();", next_button)
# print("Clicked second 'Next'")

# # Step 3: Click "Continue"
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[.//div[contains(text(),"Continue")]]')))
# continue_button = driver.find_element(By.XPATH, '//button[.//div[contains(text(),"Continue")]]')
# driver.execute_script("arguments[0].click();", continue_button)
# print("Clicked 'Continue'")

# time.sleep(2)  # wait for content to load

# ------------------------------ Create Filter and Sorting ---------------------------------

# Filter Laptops "Like new"
filter_button = driver.find_element(By.XPATH, '//button[.//span[text()="More filters"]]')
driver.execute_script("arguments[0].click();", filter_button)

recent_button = driver.find_element(By.XPATH, '//label[.//p[text()="Recent"]]')
driver.execute_script("arguments[0].click();", recent_button)

scroll_to_bottom()

condition_button = driver.find_element(By.XPATH, '//button[.//span[text()="Condition"]]')
driver.execute_script("arguments[0].click();", condition_button)

like_new_button = driver.find_element(By.XPATH, '//label[.//p[text()="Like new"]]')
driver.execute_script("arguments[0].click();", like_new_button)

lightly_used_button = driver.find_element(By.XPATH, '//label[.//p[text()="Lightly used"]]')
driver.execute_script("arguments[0].click();", lightly_used_button)

apply_button = driver.find_element(By.XPATH, '//button[text()="Apply"]')
driver.execute_script("arguments[0].click();", apply_button) 
print("All conditions set")
time.sleep(5) # Very needed to load new content

# sort_button = driver.find_element(By.XPATH, '//button[.//span[contains(text(),"Sort:")]]')
# driver.execute_script("arguments[0].click();", sort_button)


# ------------------------------ Loop through all listings -------------------------------------
card_num = 0
stop_scraping = False
stop_loading = False

while not stop_loading:
    cards = driver.find_elements(By.XPATH, '//div[starts-with(@data-testid, "listing-card-")]')
    for card in cards:
        card_num += 1
        try:
            driver.execute_script("arguments[0].scrollIntoView();", card)
            try:
                date_elem = card.find_element(By.XPATH, './/p[contains(., "ago")]').text
            except Exception as e:
                print("Could not find date for card")
                print("HTML:", card.get_attribute('outerHTML'))

            # Stop scrolling if it says "2 days ago" or more
            # print(date_elem, SCRAP_DURATION[CAROUSELL_CONFIG['scrap_days']-1], date_elem == SCRAP_DURATION[CAROUSELL_CONFIG['scrap_days']-1])
            try:
                if date_elem == "2 hours ago":
                    print("Stop scrolling — listing is too old:", date_elem)
                    stop_loading = True
                    break
            except Exception as e:
                print("Could not find date for card", card_num)

        except Exception as e:
            print("Skipped one listing:", e)
    try:
        more_button = driver.find_element(By.XPATH, '//button[contains(text(), "Show more results")]')
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", more_button)
        time.sleep(0.2)
        driver.execute_script("arguments[0].click();", more_button)
        time.sleep(0.5)

    except:
        print("No more results button.")
        break

print("Found", card_num, "listings.")
time.sleep(2)  # wait for content to load

# # ------------------------------ Extract data from each listing ----------

print("Extracting data from each listing...")
scroll_to_top()
# card_num = 30

cards = driver.find_elements(By.XPATH, '//div[starts-with(@data-testid, "listing-card-")]')
# Loop through all cards and extract data
for i in range(card_num):
    print( "Processing card", i)
    try:
        # Optional: scroll into view to load dynamic content like price
        driver.execute_script("arguments[0].scrollIntoView();", cards[i])
        time.sleep(0.1)

        # Find title by looping through all p element and check style is 2 lines
        link_elem = cards[i].find_element(By.XPATH, './/a[contains(@href, "/p/")]')
        title = link_elem.find_element(By.XPATH, './/p[@style="--max-line: 2;"]')
        url = link_elem.get_attribute('href')
        price_element = cards[i].find_element(By.XPATH, './/p[contains(text(),"$")]')
        price = extract_price(price_element.text) if price_element else "N/A"

        try:
            condition_elem = cards[i].find_element(
                By.XPATH,
                './/p[contains(text(), "Brand new") or contains(text(), "Like new") or contains(text(), "Lightly used") or contains(text(), "Well used") or contains(text(), "Heavily used")]'
            )
            condition = condition_elem.text
        except:
            print("Could not find condition for card", i)
            condition = "Unknown"

        try:
            like_element = cards[i].find_element(
                By.XPATH,
                './/button[@data-testid="listing-card-btn-like"]'
            )
            like_num = int(like_element.text.strip()) if like_element.text.strip().isdigit() else 0
        except: 
            print("Could not find like number for card", i)
            like_num = 0

        try:
            date_elem = cards[i].find_element(By.XPATH, './/p[contains(., "ago")]')
            listing_date = dateparser.parse(date_elem.text).date()
        except Exception as e:
            print("Could not find date for card", i)
            print("HTML:", cards[i].get_attribute('outerHTML'))
            listing_date = "Unknown"

        if (listing_date != current_date and listing_date != "Unknown")  or i >= card_num:
            print("Reached end of listings for today.")
            stop_scraping = True
            break  # Stop if listing date is not current date

        # print(f"Title: {title.text}, Price: {price}, Condition: {condition}, URL: {url}, Date: {listing_date}, Likes: {like_num}")

        if price and price >= 59:
            listings.append({
                "timestamp": timestamp,
                "listing_date": listing_date,
                "title": title.text,
                "price": price,
                "condition": condition,
                "likes": like_num,
                "sold_status": "Available",
                "url": url
            })

        else:
            print("Skipped listing due to likely false listing")

    except Exception as e:
        print("Skipped one listing:", e)

print("Reached end of listings for today.")
driver.quit()



# ------------------------------ Data Validation and Database Integration -----------------


def validate_listing(listing):
    """Validate required fields in a listing"""
    required_fields = ['listing_date', 'title', 'price', 'condition', 'url']
    return all(field in listing and listing[field] for field in required_fields)


def save_to_db(listings):
    """Save validated listings to PostgreSQL database"""
    
    # Create SQLAlchemy engine
    engine = create_engine(f"postgresql+psycopg2://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}")
    
    # Convert to DataFrame and filter valid listings
    valid_listings = [listing for listing in listings if validate_listing(listing)]
    df = pd.DataFrame(valid_listings)
    df['listing_id'] = df['url'].apply(extract_listing_id)
    df = df[df['listing_id'].notnull()]
    # df = df[df['price'].notnull()]
    # df = df[df['price'] >= 59]
    
    # Save to database
    try:
        df.to_sql('listings', engine, if_exists='append', index=False)
        print(f"Successfully saved {len(valid_listings)} listings to database")
    except Exception as e:
        print(f"Error saving to database: {str(e)}")

# Convert to DataFrame
def save_to_csv(listings):
    df = pd.DataFrame(listings)
    csv_file = f"{CAROUSELL_CONFIG['category']}_history.csv"
    if os.path.exists(csv_file):
        df.to_csv(csv_file, mode='a', index=True, header=False)
    else:
        df.to_csv(csv_file, mode='w', index=True, header=[ "date","title", "price", "condition", "likes", "url"])

    print("Appended today's listings to:", csv_file)

# Save listings to database
save_to_db(listings)
# save_to_csv(listings)
