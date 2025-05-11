from behave import given, when, then
import requests
from utils.api_helpers import create_booking
from hamcrest import assert_that, equal_to, is_not, none, empty
import json
import allure


# Get booking IDs GET - https://restful-booker.herokuapp.com/booking

BASE_URL = "https://restful-booker.herokuapp.com"

@when("I send a GET request to the booking IDs endpoint")
def step_impl(context):
    context.response = requests.get(f"{BASE_URL}/booking", verify=False)
    print("GET /booking Response:", context.response.text) # Use to Print out in console, but it is not working and i am not able to see in console

@then("the response status code should be 200")
def step_impl(context):
    assert_that(context.response.status_code, equal_to(200))

@then("the response should contain a list of booking IDs")
def step_impl(context):
    data = context.response.json()         # it's a pythn object having list of ID's from API response
    
    # Assert that the response is a list
    # If data is not a list, the assert statement will raise an AssertionError, causing the test to fail.
    assert isinstance(data, list)

    # Checks to make sure each item in the list contains a "bookingid"
    # Check and ensures that every items in the data list contain either "bookingid" or "id" field. 
    # If the 'data list' have multiple data in it then it will check for all data list that it would have 'bookingid' or 'id' field or not.
    # Once all the item and found 'bookingid' or 'id' field in it, then 'assert all()' function return TRUE which will pass the test.
    # I it's FALSE, then the test fail.  
    assert all("bookingid" in item or "id" in item for item in data)
    
    # Print to console, but it is not working and i am not able to see in console
    print("List of Booking IDs:", data)

    # Attach to Allure report
    # data --> Python object having list of ID's which is coming from API response.
    # json.dumps(data, indent=2) --> Convert the python object (i.e. data) to Json formatted string.
    # indent=2 --> It's use for formetting the Json data by providint 2 spaces.
    # name = "List of Booking ID's" --> Name of the attachment that will appear in Allure report under the step.
    # attachment_type=allure.attachment_type.JSON --> Tells Allure that the attached content is of type JSON, so it formats it accordingly in the report.
    allure.attach(json.dumps(data, indent=2), name="List of Booking IDs", attachment_type=allure.attachment_type.JSON)

