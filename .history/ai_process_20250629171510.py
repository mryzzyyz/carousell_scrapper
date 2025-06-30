import subprocess
import json
from helper import load_from_db

FETCH_UNTIL = 3 

def ask_deepseek(prompt):
    response = ollama.chat(
        model='deepseek-r1:7b',
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response['message']['content']



prompt = f"""You are a resale laptop expert. Given the listing below, evaluate how good the deal is.

{data}

Your tasks:
1. Estimate the current market price for this laptop.
2. Say whether this is a good, fair, or bad deal.
3. Give it a score from 0 to 10 (10 = amazing deal).

Format your response as:
Estimated Market Price: ...
Verdict: ...
Score: ...
"""

print(ask_deepseek(prompt))
