from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
from geopy.geocoders import Nominatim
import folium
import time

geolocator = Nominatim(user_agent="housing_scraper")

def get_coordinates(address):
    try:
        location = geolocator.geocode(address + ", Singapore")
        return (location.latitude, location.longitude) if location else (None, None)
    except Exception as e:
        print(f"Geocoding error: {str(e)}")
        return (None, None)

def main():
    driver = webdriver.Chrome()
    driver.get("https://hz.ziroom.com/z/q1123223475194343425/?sort=2&isOpen=1")
    
    locations = []
    
    try:
        while True:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, "listing"))
            )
            
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            listings = soup.find_all('div', class_='item')
            
            for listing in listings:
                # Extract listing details
                title = listing.find('h5', class_='title').get_text(strip=True)
                desc = listing.select('.desc div:first-child')[0].get_text(strip=True, separator='|').split('|')
                area = desc[0].strip() if len(desc) > 0 else ''
                floor = desc[1].strip() if len(desc) > 1 else ''
                orientation = desc[2].strip() if len(desc) > 2 else ''
                location = listing.select('.location')[0].get_text(strip=True)
                
                # Extract numeric price from background positions
                price_els = listing.select('.underline_price .s_num')
                # Map sprite positions to actual numbers
                POSITION_MAP = {
                    '0': '0', '21': '1', '42': '2', '64': '3', '85': '4',
                    '107': '5', '128': '6', '149': '7', '171': '8', '192': '9'
                }
                price_digits = []
                for el in price_els:
                    match = re.search(r'-(\d+)px', el['style'])
                    if match:
                        pos = match.group(1)
                        price_digits.append(POSITION_MAP.get(pos, ''))
                price = int(''.join(price_digits)) if price_digits else 0
                
                tags = [tag.get_text(strip=True) for tag in listing.select('.tag span')]
                
                locations.append({
                    'title': title,
                    'area': area,
                    'floor': floor,
                    'orientation': orientation,
                    'location': location,
                    'price': price,
                    'tags': ', '.join(tags)
                })
            
            try:
                next_btn = driver.find_element(By.XPATH, "//a[contains(text(), '下一页')]")
                next_btn.click()
                time.sleep(2)
            except:
                break
                
    finally:
        driver.quit()
    
    # Create interactive map
    m = folium.Map(location=[1.3521, 103.8198], zoom_start=12)
    
    for addr in locations:
        lat, lng = get_coordinates(addr)
        if lat and lng:
            folium.Marker(
                [lat, lng],
                popup=addr,
                icon=folium.Icon(color='green', icon='home')
            ).add_to(m)
    
    m.save('housing_map.html')
    print(f"Saved {len(locations)} locations to housing_map.html")

if __name__ == "__main__":
    main()
