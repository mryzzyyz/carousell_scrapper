import ollama
import re
import json


MODEL = "deepseek-r1:7b"



# sample_listings = [
#     {
#         "temp_id": 1,
#         "timestamp": datetime.now().isoformat(),
#         "listing_date": "2 days ago",
#         "title": "MacBook Pro 2019 i7 16GB 512GB",
#         "price": 850,
#         "condition": "Lightly used",
#         "likes": 12,
#         "sold_status": "Available",
#         "url": "https://carousell.sg/p/macbook-pro-2019",
#         "img": "img_001.jpg"
#     },
#     {
#         "temp_id": 2,
#         "timestamp": datetime.now().isoformat(),
#         "listing_date": "1 day ago",
#         "title": "ASUS Vivobook i5 8GB 256GB SSD",
#         "price": 420,
#         "condition": "Well used",
#         "likes": 5,
#         "sold_status": "Available",
#         "url": "https://carousell.sg/p/asus-vivobook",
#         "img": "img_002.jpg"
#     },
#     {
#         "temp_id": 3,
#         "timestamp": datetime.now().isoformat(),
#         "listing_date": "Today",
#         "title": "MacBook Air M1 2020 8GB 256GB",
#         "price": 780,
#         "condition": "Like new",
#         "likes": 22,
#         "sold_status": "Available",
#         "url": "https://carousell.sg/p/macbook-air-m1",
#         "img": "img_003.jpg"
#     },
#     {
#         "temp_id": 4,
#         "timestamp": datetime.now().isoformat(),
#         "listing_date": "3 days ago",
#         "title": "Dell XPS 13, 11th Gen i5, 16GB",
#         "price": 640,
#         "condition": "Lightly used",
#         "likes": 18,
#         "sold_status": "Available",
#         "url": "https://carousell.sg/p/dell-xps-13",
#         "img": "img_004.jpg"
#     },
#     {
#         "temp_id": 5,
#         "timestamp": datetime.now().isoformat(),
#         "listing_date": "Today",
#         "title": "HP Envy Ryzen 5 8GB 512GB SSD",
#         "price": 560,
#         "condition": "Lightly used",
#         "likes": 9,
#         "sold_status": "Available",
#         "url": "https://carousell.sg/p/hp-envy",
#         "img": "img_005.jpg"
#     },
#     {
#         "temp_id": 6,
#         "timestamp": datetime.now().isoformat(),
#         "listing_date": "Yesterday",
#         "title": "Acer Swift 3, i3, 4GB, 128GB SSD",
#         "price": 270,
#         "condition": "Well used",
#         "likes": 4,
#         "sold_status": "Available",
#         "url": "https://carousell.sg/p/acer-swift-3",
#         "img": "img_006.jpg"
#     },
#     {
#         "temp_id": 7,
#         "timestamp": datetime.now().isoformat(),
#         "listing_date": "2 days ago",
#         "title": "MacBook Pro 2021 M1 Pro 16GB",
#         "price": 1700,
#         "condition": "Like new",
#         "likes": 45,
#         "sold_status": "Available",
#         "url": "https://carousell.sg/p/macbook-pro-m1-pro",
#         "img": "img_007.jpg"
#     },
#     {
#         "temp_id": 8,
#         "timestamp": datetime.now().isoformat(),
#         "listing_date": "Today",
#         "title": "Lenovo IdeaPad 3 Ryzen 3",
#         "price": 330,
#         "condition": "Brand new",
#         "likes": 3,
#         "sold_status": "Available",
#         "url": "https://carousell.sg/p/lenovo-ideapad-3",
#         "img": "img_008.jpg"
#     },
#     {
#         "temp_id": 9,
#         "timestamp": datetime.now().isoformat(),
#         "listing_date": "Yesterday",
#         "title": "Surface Laptop 4 i5 8GB 256GB",
#         "price": 690,
#         "condition": "Lightly used",
#         "likes": 11,
#         "sold_status": "Available",
#         "url": "https://carousell.sg/p/surface-laptop-4",
#         "img": "img_009.jpg"
#     },
#     {
#         "temp_id": 10,
#         "timestamp": datetime.now().isoformat(),
#         "listing_date": "Today",
#         "title": "MSI Gaming Laptop i7 GTX1650",
#         "price": 870,
#         "condition": "Well used",
#         "likes": 17,
#         "sold_status": "Available",
#         "url": "https://carousell.sg/p/msi-gaming-laptop",
#         "img": "img_010.jpg"
#     }
# ]


def ask_ai(prompt):
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ],
        think=False,
        options={"num_predict": 100,"temperature": 0.2, "stop": ["]"]}
    )
    return response['message']['content']


def parse_ai_response(response):
    # Try to recover the JSON list from incomplete output
    try:
        # Find the start of the list
        start = response.find('[')
        end = response.rfind('}')
        if start == -1 or end == -1:
            raise ValueError("Invalid format — missing brackets.")

        # Recover and fix the JSON
        json_text = response[start:end+1]
        if not json_text.strip().endswith(']'):
            json_text += ']'

        # Parse it
        raw_list = json.loads(json_text)

        # Normalize to int and float
        result = []
        for item in raw_list:
            temp_id = int(item["temp_id"])
            score = float(item["score"])
            result.append({"temp_id": temp_id, "score": score})

        return result

    except Exception as e:
        print("❌ Failed to parse response:", e)
        return []


def ai_filter(data, top_percent = 0.15):
    if not data:
        return []

    data_length = len(data)
    targeted_num = max(1, int(data_length * top_percent))

    feeding_data = "\n".join(
        f"temp_id: {d['temp_id']}, price: {d['price']}, title: {d['title']}, condition: {d['condition']}" for d in data
    )

    prompt = f"""
    You are a resale laptop expert. Your task is to identify the top {targeted_num} best-value laptop deals from the listings below.

    Each listing includes:
    - `temp_id`: unique identifier
    - `price`: lower is better
    - `condition`: prioritize 'like new' > 'lightly used' > 'well used'
    - `title`: includes model and specs (e.g., RAM, CPU, storage)

    Evaluate based on:
    1. Price-to-spec ratio
    2. Condition
    3. Brand/model desirability (e.g., MacBook M1 > older Intel models)
    4. RAM and SSD capacity
    5. CPU generation and performance

    Return only the top {targeted_num} deals in **strict JSON format** as shown below. Do not include any explanation or extra text.

    [
    {{
        "temp_id": "<temp_id>",
        "score": <score_integer_0_to_10>
    }},
    ...
    ]
    Listings:
    {feeding_data}
    """


    print("asking AI...")
    # print(prompt)
    raw_output = ask_ai(prompt)
    print(raw_output)
    return parse_ai_response(raw_output)


