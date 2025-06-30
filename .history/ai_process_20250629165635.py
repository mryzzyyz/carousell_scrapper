import subprocess
import json
from helper import load_from_db

def ask_deepseek(prompt):
    result = subprocess.run(
        ["ollama", "run", "deepseek-chat"],
        input=prompt.encode(),
        capture_output=True
    )
    return result.stdout.decode()

data = load_from_db(None)

prompt = f"""You are an expert on second-hand laptop deals.
Give this listing a score from 1 to 10 for how worth it is:

{listing_summary}

Score:"""

print(ask_deepseek(prompt))
