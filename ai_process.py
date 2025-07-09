import ollama
import re
import json
from openai import OpenAI
import os
from dotenv import load_dotenv 

load_dotenv() 


MODEL = "deepseek-r1:7b"

system_prompt = """   
    You are a resale laptop expert. Your task is to identify the top best-value laptop deals from the listings below.

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

    Return only the top deals in **strict JSON format** as shown below. Do not include any explanation or extra text.

    [
    {{
        "temp_id": "<temp_id>",
        "score": <score_integer_0_to_10>
    }},
    ...
    ]
    """

def ask_api_ai(prompt):
    client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"),base_url=os.getenv("DEEPSEEK_API_URL"))

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        temperature=1.0,
        stream=False,
    )
    return response.choices[0].message.content



def ask_ai(prompt):
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
            {"temperature": 1.0}
        ],
        think=False,
        options={"num_predict": 100,"temperature": 1.0, "stop": ["]"]}
    )
    return response['message']['content']


def parse_ai_response(response):
    # Try to recover the JSON list from incomplete output
    try:
        temp_ids = re.findall(r'"?temp_id"?\s*:\s*"?(?P<temp_id>\d+)"?', response)
        scores = re.findall(r'"?score"?\s*:\s*"?(?P<score>\d+(?:\.\d+)?)"?', response)
        results = []

        if len(temp_ids) != len(scores):
            print("❌ Failed to parse response: temp_id and score count mismatch")
            return []
        
        for i in range(len(temp_ids)):
            data = {
                "temp_id": int(temp_ids[i]),
                "score": float(scores[i])
            }
            results.append(data)
        return results

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
    Your task is to identify the top {targeted_num} best-value laptop deals from the listings below.

    Listings:
    {feeding_data}
    """


    print("asking AI...")
    # print(prompt)
    # raw_output = ask_ai(prompt)
    raw_output = ask_api_ai(prompt)
    print(raw_output)
    return parse_ai_response(raw_output)

def chunk_ai_process(data, chunk_size=30, max_chunk_size=40):
    if len(data) > max_chunk_size:
        results = []
        for i in range(0, len(data), chunk_size):
            chunk = data[i:i+chunk_size]
            chunk_result = ai_filter(chunk)  # ask AI and parse
            if not chunk_result:
                print(f"❌ AI failed on batch starting at index {i}")
                return None  # This triggers a retry in the outer function
            results.extend(chunk_result)
            print(f"✅ Done with batch {i}")
        return results if results else None
    else:
        result = ai_filter(data)
        return result if result else None

# def try_ask_api_ai():
#     client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"),base_url=os.getenv("DEEPSEEK_API_URL"))

#     response = client.chat.completions.create(
#         model="deepseek-chat",
#         messages=[
#             {"role": "system", "content": "you are a helpful assistance"},
#             {"role": "user", "content": "how can you analysis if a secondhand market product is worth or not"},
#         ],
#         temperature=1.0,
#         stream=False,
#     )
#     return response.choices[0].message.content


