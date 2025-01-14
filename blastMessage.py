import httpx
# from fastapi import requests
from configs import Config

CONFIG = Config()

async def send_message(recipient):
    url = CONFIG.WHATSAPP_BLAST_ENDPOINT
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
	    "phone_number":recipient,
        "template_name":CONFIG.WHATSAPP_TEMPLATE_NAME,
        "param1":CONFIG.PARAM1
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=payload, headers=headers)
        print(response.text)

    if response.status_code == 200:
        print("Pesan berhasil dikirim:", response.json())
    else:
        print("Gagal mengirim pesan:", response.status_code, response.text)