import requests

BOT_TOKEN = "7249244277:AAHzUNPnXpM2Bhz6OgqvW-BzDIYu0Hm3r2I"
CHAT_ID = '7658586331'

def send_ai_results_to_telegram(listings):

    # Prepare message
    lines = []
    for l in listings:
        title = l.get("title", "No title")
        price = l.get("price", "N/A")
        url = l.get("url", "")
        lines.append(f"{title}\n💰 ${price}\n🔗 {url}\n")

    message = "\n".join(lines)

    # Send message (split if too long)
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    for i in range(0, len(message), 4000):  # Telegram limit is 4096 chars
        payload = {
            "chat_id": CHAT_ID,
            "text": message[i:i+4000]
        }
        requests.post(url, data=payload)

def send_debug_message_to_telegram(message: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        response = requests.post(url, data=payload)
        if response.ok:
            print("✅ Telegram sent.")
        else:
            print("❌ Telegram error:", response.text)
    except Exception as e:
        print("❌ Telegram failed:", e)


