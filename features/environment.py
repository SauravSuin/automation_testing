# environment.py

import requests

BASE_URL = "https://restful-booker.herokuapp.com"

def get_token():
    url = f"{BASE_URL}/auth"
    payload = {
        "username": "admin",
        "password": "password123"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers, verify=False)
    response.raise_for_status()
    return response.json()["token"]

def before_all(context):
    print("Fetching authentication token...")
    context.token = get_token()
    print(f"Auth token acquired: {context.token}")
