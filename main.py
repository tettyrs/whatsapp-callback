import json, json, os
from fastapi import FastAPI, Request, Query
from fastapi.responses import PlainTextResponse
from datetime import datetime
from dotenv import load_dotenv
from blastMessage import send_message
from configs import Config


load_dotenv()

app = FastAPI()
CONFIG = Config()

# Verify Token yang harus sesuai dengan token yang digunakan oleh pengirim request


@app.get("/webhooks", response_class=PlainTextResponse)
async def verify_webhook(
    hub_mode: str = Query(..., alias="hub.mode"),
    hub_verify_token: str = Query(..., alias="hub.verify_token"),
    hub_challenge: str = Query(..., alias="hub.challenge")
):
    """
    Endpoint untuk memverifikasi webhook. 
    Jika verify_token cocok, balas dengan hub_challenge.
    """
    if hub_mode == "subscribe" and hub_verify_token == CONFIG.EXPECTED_VERIFY_TOKEN:
        # Mengembalikan hub.challenge jika token cocok
        return hub_challenge
    else:
        # Mengembalikan error jika token tidak cocok
        return PlainTextResponse("Forbidden", status_code=403)


@app.post("/webhooks")
async def receive_message(request: Request):
    data = await request.json()
    print("Data diterima:", json.dumps(data, indent=4))

    # Periksa apakah ini adalah pesan baru
    if data.get("object") == "whatsapp_business_account":
        entry = data.get("entry", [])[0]
        changes = entry.get("changes", [])[0]
        value = changes.get("value", {})
        messages = value.get("messages", [])

        if messages:
            # Ambil detail pesan
            message = messages[0]
            sender = message["from"]  # Nomor pengirim
            text = message["text"]["body"]  # Isi pesan

            print(f"Pesan dari {sender}: {text}")

            # Kirim balasan otomatis
            await send_message(sender, "Terima kasih telah menghubungi kami! Pesan Anda telah diterima.")

        return {"status": "EVENT_RECEIVED"}, 200

    return {"status": "Not a valid message"}, 404

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)