import requests
from config import API_URL

def get_fixtures():
    response = requests.get(f"{API_URL}/fixtures")
    return response.json() if response.status_code == 200 else None

def get_results():
    response = requests.get(f"{API_URL}/results")
    return response.json() if response.status_code == 200 else None
