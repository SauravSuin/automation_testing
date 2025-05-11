# environment.py

import requests
from hamcrest import assert_that, equal_to, is_not, none, empty

BASE_URL = "https://restful-booker.herokuapp.com"

def get_token():
    url = f"{BASE_URL}/auth"
    payload = {
        "username": "admin",
        "password": "password123"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers, verify=False)  # Bypass SSL validation 
    assert_that(response.status_code, equal_to(200))                            # Check if the status code = 200, if not test failed.
    
    # Used to extract and return the token value from a JSON response after making an HTTP request, typically in API authentication.
    # response.json() --> converts the response body from JSON string to a Python dictionary.
    # ["token"] --> accesses the value associated with the "token" key.
    # return --> sends this token value back to the calling function.
    return response.json()["token"]

def before_all(context):
    print("Fetching authentication token...")
    context.token = get_token()   # context.token = get_token() is used in Behave BDD (Behavior-Driven Development) to retrieve and store an authentication token in the shared context object for use across multiple test steps.
    print(f"Auth token acquired: {context.token}")
