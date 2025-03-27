import schedule
import time
from src.api import get_fixtures, get_results
from src.formatter import format_fixture, format_result
from bot import send_message

def post_fixtures():
    matches = get_fixtures()
    for match in matches:
        message = format_fixture(match)
        send_message(message)

def post_results():
    matches = get_results()
    for match in matches:
        message = format_result(match)
        send_message(message)

def start_scheduler():
    schedule.every().day.at("14:00").do(post_fixtures)
    schedule.every(1).minutes.do(post_results)
