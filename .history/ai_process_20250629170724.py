import subprocess
import json
from helper import load_from_db

FETCH_UNTIL = 3 

def ask_deepseek(prompt):
    result = subprocess.run(
        ["ollama", "run", "deepseek-chat"],
        input=prompt.encode(),
        capture_output=True
    )
    return result.stdout.decode()

data = load_from_db(FETCH_UNTIL)[0]



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
