import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
API_URL = "https://unofficial-espn-api.com"
TIMEZONE = "Asia/Kolkata"
