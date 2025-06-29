import re

def extract_price(price_str):
    if not price_str:
        return None
    # Extract digits and remove S$, commas, etc.
    cleaned = re.sub(r"[^\d]", "", price_str)
    return int(cleaned) if cleaned.isdigit() else None

def extract_listing_id(url: str) -> str:
    match = re.search(r'/p/[^/]+-(\d+)', url)
    return match.group(1) if match else None