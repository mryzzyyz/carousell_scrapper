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


def ai_filter(data):
    if not data:
        return []

    data_length = len(data)
    targeted_num = max(1, int(data_length * 0.15))

    feeding_data = "\n".join(
        f"id: {d['id']}, price: {d['price']}, title: {d['title']}, url: {d['url']}" for d in data
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