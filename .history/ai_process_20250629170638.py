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



prompt = f"""You are an expert on second-hand laptop deals.
Give this listing a score from 1 to 10 for how worth it is:

{data}

Score:"""

print(ask_deepseek(prompt))
