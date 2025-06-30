import ollama
from helper import load_from_db

FETCH_UNTIL = 3 

def ask_ai(prompt):
    response = ollama.chat(
        model='phi',
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['message']['content']


def ai_filter(id, title, price, condition):
    feeding_data = 

    prompt = f"""
    You are a resale laptop expert. Given the listing below, evaluate how good the deal is.

    Return **only a single number** from 0 to 10 (inclusive), where:
    - 10 = excellent deal
    - 0 = terrible deal

    Do not explain your answer. Do not include any text. Only return the number.

    Listing:
    {data}
    """
    print("asking AI...")

    filtered_data = ask_ai(prompt)
    print(filtered_data)
    return filtered_data
