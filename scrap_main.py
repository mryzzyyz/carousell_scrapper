from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import dateparser
from datetime import datetime
import sys
from config import CAROUSELL_CONFIG
import sqlite3
from helper import extract_price, save_to_sqlite
from ai_process import ai_filter,chunk_ai_process
from telebot import send_ai_results_to_telegram, send_debug_message_to_telegram
from selenium.webdriver.common.proxy import Proxy, ProxyType
import random



# Configuration from config file
SCRAP_DURATION = "1 day ago" # ["12 hours ago, 1 day ago", "2 days ago", "3 days ago", "4 days ago", "week ago"]
TOP_FILTER_PERCENT = 0.3

listings = []
current_date = datetime.today().date()
timestamp = datetime.now()

# if 1 <= timestamp.hour < 7:
#     print("⏱️ Between midnight and 1 AM. Exiting...")
#     sys.exit()

options = Options()
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113 Safari/537.36"
]
options.add_argument(f'user-agent={random.choice(user_agents)}')
options.add_argument('--headless=new')  # Use 'new' headless mode
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--window-size=1920,1080')
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115 Safari/537.36')

service = Service()  

driver = webdriver.Chrome(service=service, options=options)
driver.get(CAROUSELL_CONFIG['url'])


def human_delay(a=0.5, b=1.5):
    time.sleep(random.uniform(a, b))


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

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//div[starts-with(@data-testid, "listing-card-")]'))
)

html = driver.page_source
if "Just a moment..." in html:
    print("⚠️ You are being blocked by Cloudflare.")
    print(driver.page_source[:1000])
    driver.quit()

# Filter Laptops "Like new"
filter_button = driver.find_element(By.XPATH, '//button[.//span[text()="More filters"]]')
driver.execute_script("arguments[0].click();", filter_button)

recent_button = driver.find_element(By.XPATH, '//label[.//p[text()="Recent"]]')
driver.execute_script("arguments[0].click();", recent_button)

price_input = driver.find_element(By.NAME, "field_price_start")
price_input.clear()  # Clear any existing text
price_input.send_keys("1800")

scroll_to_bottom()
human_delay()

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
    human_delay()
    cards = driver.find_elements(By.XPATH, '//div[starts-with(@data-testid, "listing-card-")]')
    for card in cards:
        card_num += 1
        try:
            driver.execute_script("arguments[0].scrollIntoView();", card)
            try:
                date_elem = card.find_element(By.XPATH, './/p[contains(., "ago")]').text
                listing_datetime = dateparser.parse(date_elem)

            except Exception as e:
                print("Could not find date for card")
                print("HTML:", card.get_attribute('outerHTML'))

            # Stop scrolling if it says "2 days ago" or more
            # print(date_elem, SCRAP_DURATION[CAROUSELL_CONFIG['scrap_days']-1], date_elem == SCRAP_DURATION[CAROUSELL_CONFIG['scrap_days']-1])
            try:
                threshold_datetime  = dateparser.parse(SCRAP_DURATION)
                if listing_datetime <= threshold_datetime :
                    print("Stop scrolling — listing is too old:", listing_datetime)
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
    human_delay()
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
        img = cards[i].find_element(By.XPATH, './/img[contains(@src, "https://")]')

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

        # print(f"Title: {title.text}, Price: {price}, Condition: {condition}, URL: {url}, Date: {listing_date}, Likes: {like_num}")

        if (price and price >= 59):
            listings.append({
                "temp_id": i,
                "timestamp": timestamp,
                "title": title.text,
                "price": price,
                "condition": condition,
                "likes": like_num,
                "sold_status": "Available",
                "url": url,
                "img": img.text,
                "grading": 0
            })

        else:
            print(f"Price: {price}")
            print("Skipped listing due to likely false listing")

    except Exception as e:
        print("Skipped one listing:", e)

print("Reached end of listings for today.")
driver.quit()


# ---------- AI Filtering -----------------

def run_ai_filter_with_retry(data, max_retries=3):
    retries = 0
    while retries < max_retries:
        result = chunk_ai_process(data)
        if result:  # success
            return result
        retries += 1
        print(f"⚠️ Retry {retries}/{max_retries}... AI response failed.")
    print("❌ AI failed after max retries.")
    send_debug_message_to_telegram(f"❌ AI failed after max retries.")
    return []

ai_filtered_listings = run_ai_filter_with_retry(listings, TOP_FILTER_PERCENT)
filtered_listings = []
for scored in ai_filtered_listings:
    for listing in listings:
        if scored['temp_id'] == listing['temp_id']:
            listing['grading'] = scored['score']
            print(f"Listing {listing['temp_id']} passed AI filter with score {listing['grading']}")
            filtered_listings.append(listing)
            break
send_ai_results_to_telegram(filtered_listings)


# ------------------------------ Data Validation and Database Integration -----------------

# Save listings to database
save_to_sqlite(filtered_listings)