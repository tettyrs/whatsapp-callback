import os
# from dotenv import load_dotenv

# load_dotenv()

class Config():
   EXPECTED_VERIFY_TOKEN = os.getenv("TOKEN_CONNECT")
   WHATSAPP_BLAST_ENDPOINT = os.getenv("BLAST_ENDPOINT")
   WHATSAPP_TEMPLATE_NAME = os.getenv("TEMPLATE_NAME")
   PARAM1 = os.getenv("PARAM1")