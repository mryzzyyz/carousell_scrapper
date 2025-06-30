import ollama
from helper import load_from_db
import re

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
        if line.startswith("id:"):
            current['id'] = int(line.split(":")[1].strip())
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
        f"id: {d['id']}, price: {d['price']}, title: {d['title']}, condition: {d['condition']}" for d in data
    )

    prompt = f"""
        You are a resale laptop expert. Given the listing below, find the top {targeted_num} deals.

        For the top {targeted_num} deals, rate each on a scale of 0 to 10. Return only:

        id:
        score:

        {feeding_data}
    """
    print("asking AI...")
    raw_output = ask_ai(prompt)
    print(raw_output)
    return parse_ai_response(raw_output)