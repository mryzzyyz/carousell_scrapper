import subprocess
import json

def ask_deepseek(prompt):
    result = subprocess.run(
        ["ollama", "run", "deepseek-chat"],
        input=prompt.encode(),
        capture_output=True
    )
    return result.stdout.decode()

listing_summary = """
Title: MacBook Pro 16-inch M2
Price: 1400 SGD
Condition: Like new
Seller rating: 4.9
Review count: 120
Description: Used only 3 months. Comes with original charger. Battery cycle: 12.
"""

prompt = f"""You are an expert on second-hand laptop deals.
Give this listing a score from 1 to 10 for how worth it is:

{listing_summary}

Score:"""

print(ask_deepseek(prompt))
