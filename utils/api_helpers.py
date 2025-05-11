import requests

BASE_URL = "https://restful-booker.herokuapp.com"

def create_booking(data):
    headers = {"Content-Type": "application/json"}
    return requests.post(f"{BASE_URL}/booking", json=data, headers=headers)
