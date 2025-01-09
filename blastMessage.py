import http
from fastapi import requests
from configs import Config

CONFIG = Config()

async def send_message(recipient, message):
    url = f"https://graph.facebook.com/v17.0/{CONFIG.PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {CONFIG.ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": recipient,
        "text": {"body": message}
    }

    async with http.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print("Pesan berhasil dikirim:", response.json())
    else:
        print("Gagal mengirim pesan:", response.status_code, response.text)