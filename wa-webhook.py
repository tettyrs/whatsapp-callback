from fastapi import FastAPI, Request, Query
from fastapi.responses import PlainTextResponse
from datetime import datetime
from dotenv import load_dotenv
import os


load_dotenv()

app = FastAPI()

# Verify Token yang harus sesuai dengan token yang digunakan oleh pengirim request
EXPECTED_VERIFY_TOKEN = os.getenv("TOKEN_CONNECT")

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
    if hub_mode == "subscribe" and hub_verify_token == EXPECTED_VERIFY_TOKEN:
        # Mengembalikan hub.challenge jika token cocok
        return hub_challenge
    else:
        # Mengembalikan error jika token tidak cocok
        return PlainTextResponse("Forbidden", status_code=403)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)