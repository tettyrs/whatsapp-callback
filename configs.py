import os
from dotenv import load_dotenv

load_dotenv()

class Config():
   EXPECTED_VERIFY_TOKEN = os.getenv("TOKEN_CONNECT")
   PHONE_NUMBER_ID = os.getenv("ACCOUNT_PHONE_NUMBER_ID")
   ACCESS_TOKEN = os.getenv("META_ACCESS_TOKEN")
   


