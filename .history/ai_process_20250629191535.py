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
    feeding_data = ""
    data_length = len(data)
    targeted_num = int(data_length * 0.15)
    for i in range(len(data)):
        feeding_data+=(f"id: {data[i]['id']}, price: {data[i]['price']}, title: {data[i]['title']}, url: {data[i]['url']} \n")

    print(feeding_data)

    prompt = f"""
    You are a resale laptop expert. Given the listing below, find the top {targeted_num} of deals for you.

    For the top {targeted_num} deals, please rate each deal on a scale of 0 to 10 (inclusive), where 10 is excellent deal and 0 is terrible deal.
    Return the top {targeted_num} deals along with their ratings.

    Do not explain your answer. Do not include any text. Only return the top {targeted_num} deals and their ratings.

    Listing:
    {data}
    """
    print("asking AI...")

    filtered_data = ask_ai(prompt)
    print(filtered_data)
    return filtered_data
