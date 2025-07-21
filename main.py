from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
WEBHOOK_SECRET = os.environ.get("WEBHOOK_SECRET")

WELCOME_MESSAGE = """
👋 Ku soo dhawoow Wararka Crypto Bot!

Magacaygu waa Ibrahiim. Bot-kan wuxuu kuu soo gudbinayaa wararka ugu saameynta badan suuqa crypto sida:

📊 GDP
📈 CPI (Sicir Barar)
💰 Dulsaarka (Interest Rate)
🗞️ Wararka waaweyn ee Bitcoin & Altcoins
📅 Jadwalka dhacdooyinka Crypto
📊 Warbixinada dhaqaalaha: NFP, Shaqada Mareykanka, iyo Q1-Q4 Earnings

🕓 War kasta waxaan kusoo ogeysiin doonaa 10 daqiiqo ka hor iyo marka xogta rasmiga ah la shaaciyo — waqtiga saxda ah ee Soomaaliya (GMT+3).

🟢 Saameyn togan | 🟡 Dhexdhexaad | 🔴 Saameyn xun
"""

@app.route(f"/{os.environ.get('WEBHOOK_SECRET', 'webhook')}", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data and "text" in data["message"]:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]

        if text.lower() == "/start":
            send_message(chat_id, WELCOME_MESSAGE)

    return {"ok": True}

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run()
