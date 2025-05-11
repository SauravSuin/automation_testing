from behave import given, when, then
import requests
from utils.api_helpers import create_booking
from hamcrest import assert_that, equal_to, is_not, none, empty
import json
import allure


# Get booking details by ID GET - https://restful-booker.herokuapp.com/booking

BASE_URL = "https://restful-booker.herokuapp.com"

@given("I have a valid booking ID")
def step_impl(context):
    # Get any booking ID (existing one)
    response = requests.get(f"{BASE_URL}/booking", verify=False)   # Get API call 
    booking_list = response.json()                                 # List of booking return by the API
    assert_that(booking_list, is_not(empty()))                     # Check if the list is empty or not, if empty then error.
    context.booking_id = booking_list[0]["bookingid"]              # capture the booking id from the 1st value from the booking list. And stores the extracted bookingid into the context object. This allows it to be reused in later steps of the scenario. 
    allure.attach(str(context.booking_id), name="Booking ID", attachment_type=allure.attachment_type.TEXT)  #Capture the Booking id in Allure report.

@when("I send a GET request to fetch the booking")
def step_impl(context):
    response = requests.get(f"{BASE_URL}/booking/{context.booking_id}", verify=False) # Get API called with captured bookingID.
    context.response = response                                                       # API response store in 'context' object which can be used in later step.
    context.response_json = response.json()                                           # Store the retured json response.
    allure.attach(json.dumps(context.response_json, indent=2), name="Get Booking Response", attachment_type=allure.attachment_type.JSON)   #Capture the response as JSON in Allure report.

@then("the api response code should be 200")
def step_impl(context):
    assert_that(context.response.status_code, equal_to(200))         # Check if the status code = 200, if not test failed.

@then("the booking details should be returned")
def step_impl(context):
    assert_that(context.response_json, is_not(none()))                 # This assertion checks that the parsed JSON response from the API is not None, meaning a valid JSON object was returned.
    assert_that("firstname" in context.response_json, equal_to(True))  # This assertion checks if the key "firstname" exists in the JSON response stored in context.response_json. If the "firstname" key is found, the assertion passes; otherwise, it fails.
    assert_that("lastname" in context.response_json, equal_to(True))   # This assertion checks if the key "firstname" exists in the JSON response stored in context.response_json. If the "lastname" key is found, the assertion passes; otherwise, it fails.

