import ollama
from helper import load_from_db
import re
from datetime import datetime

sample_listings = [
    {
        "timestamp": '2025-06-29T14:55:50.371928',
        "listing_date": "2 days ago",
        "title": "MacBook Pro 2019 i7 16GB 512GB",
        "price": 850,
        "condition": "Lightly used",
        "likes": 12,
        "sold_status": "Available",
        "url": "https://carousell.sg/p/macbook-pro-2019",
        "img": "img_001.jpg"
    },
    {
        "timestamp": datetime.now().isoformat(),
        "listing_date": "1 day ago",
        "title": "ASUS Vivobook i5 8GB 256GB SSD",
        "price": 420,
        "condition": "Well used",
        "likes": 5,
        "sold_status": "Available",
        "url": "https://carousell.sg/p/asus-vivobook",
        "img": "img_002.jpg"
    },
    {
        "timestamp": datetime.now().isoformat(),
        "listing_date": "Today",
        "title": "MacBook Air M1 2020 8GB 256GB",
        "price": 780,
        "condition": "Like new",
        "likes": 22,
        "sold_status": "Available",
        "url": "https://carousell.sg/p/macbook-air-m1",
        "img": "img_003.jpg"
    },
    {
        "timestamp": datetime.now().isoformat(),
        "listing_date": "3 days ago",
        "title": "Dell XPS 13, 11th Gen i5, 16GB",
        "price": 640,
        "condition": "Lightly used",
        "likes": 18,
        "sold_status": "Available",
        "url": "https://carousell.sg/p/dell-xps-13",
        "img": "img_004.jpg"
    },
    {
        "timestamp": datetime.now().isoformat(),
        "listing_date": "Today",
        "title": "HP Envy Ryzen 5 8GB 512GB SSD",
        "price": 560,
        "condition": "Lightly used",
        "likes": 9,
        "sold_status": "Available",
        "url": "https://carousell.sg/p/hp-envy",
        "img": "img_005.jpg"
    },
    {
        "timestamp": datetime.now().isoformat(),
        "listing_date": "Yesterday",
        "title": "Acer Swift 3, i3, 4GB, 128GB SSD",
        "price": 270,
        "condition": "Well used",
        "likes": 4,
        "sold_status": "Available",
        "url": "https://carousell.sg/p/acer-swift-3",
        "img": "img_006.jpg"
    },
    {
        "timestamp": datetime.now().isoformat(),
        "listing_date": "2 days ago",
        "title": "MacBook Pro 2021 M1 Pro 16GB",
        "price": 1700,
        "condition": "Like new",
        "likes": 45,
        "sold_status": "Available",
        "url": "https://carousell.sg/p/macbook-pro-m1-pro",
        "img": "img_007.jpg"
    },
    {
        "timestamp": datetime.now().isoformat(),
        "listing_date": "Today",
        "title": "Lenovo IdeaPad 3 Ryzen 3",
        "price": 330,
        "condition": "Brand new",
        "likes": 3,
        "sold_status": "Available",
        "url": "https://carousell.sg/p/lenovo-ideapad-3",
        "img": "img_008.jpg"
    },
    {
        "timestamp": datetime.now().isoformat(),
        "listing_date": "Yesterday",
        "title": "Surface Laptop 4 i5 8GB 256GB",
        "price": 690,
        "condition": "Lightly used",
        "likes": 11,
        "sold_status": "Available",
        "url": "https://carousell.sg/p/surface-laptop-4",
        "img": "img_009.jpg"
    },
    {
        "timestamp": datetime.now().isoformat(),
        "listing_date": "Today",
        "title": "MSI Gaming Laptop i7 GTX1650",
        "price": 870,
        "condition": "Well used",
        "likes": 17,
        "sold_status": "Available",
        "url": "https://carousell.sg/p/msi-gaming-laptop",
        "img": "img_010.jpg"
    }
]



FETCH_UNTIL = 3 

def ask_ai(prompt):
    response = ollama.chat(
        model='phi',
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['message']['content']

def parse_ai_response(response):
    lines = response.strip().split('\n')
    parsed = []
    current = {}
    for line in lines:
        if line.startswith("timestamp:"):
            current['timestamp'] = int(line.split(":")[1].strip())
        elif line.startswith("score:"):
            current['score'] = float(line.split(":")[1].strip())
            parsed.append(current)
            current = {}
    return parsed

def ai_filter(data):
    if not data:
        return []

    data_length = len(data)
    targeted_num = max(1, int(data_length * 0.15))

    feeding_data = "\n".join(
        f"timestamp: {d['timestamp']}, price: {d['price']}, title: {d['title']}, condition: {d['condition']}" for d in data
    )

    prompt = f"""
        You are a resale laptop expert. Given the listing below, find the top {targeted_num} deals.

        For the top {targeted_num} deals, rate each on a scale of 0 to 10. Return only:

        timestamp:
        score:

        {feeding_data}
    """
    print("asking AI...")
    print(prompt)
    raw_output = ask_ai(prompt)
    print(raw_output)
    return parse_ai_response(raw_output)

ai_filtered_listings = ai_filter(sample_listings)

print(ai_filtered_listings)