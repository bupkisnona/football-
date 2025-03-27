import schedule
import time
from src.api import get_fixtures, get_results
from src.formatter import format_fixture, format_result
from src.scheduler import start_scheduler
from config import CHANNEL_ID
import requests

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    start_scheduler()
    while True:
        schedule.run_pending()
        time.sleep(30)
