from behave import given, when, then
import requests
from utils.api_helpers import create_booking
from hamcrest import assert_that, equal_to, is_not, none
import json
import allure


# Booking creation POST - https://restful-booker.herokuapp.com/booking

BASE_URL = "https://restful-booker.herokuapp.com"

@given('I have booking data with "{firstname}", "{lastname}", "{price}", "{deposit}", "{checkin}", "{checkout}", "{additionalneeds}"')
def step_impl(context, firstname, lastname, price, deposit, checkin, checkout, additionalneeds):
    context.booking_data = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": int(price),
        "depositpaid": deposit.lower() == "true",
        "bookingdates": {
            "checkin": checkin,
            "checkout": checkout
        },
        "additionalneeds": additionalneeds
    }

@when("I send a create booking request")
def step_impl(context):

    # Used 'f'- string to dynamically construct the URL. (i.e. Base URL + /booking).It supported by Python.
    url = f"{BASE_URL}/booking"
    headers = {"Content-Type": "application/json"}

    # It sends a POST request to create a booking, using booking data and headers, without validating the server's SSL certificate.
    response = requests.post(url, json=context.booking_data, headers=headers, verify=False)    #added verify = False --> this bypass SSL validation, it can be used in test/dev enviornment 
    
    # In Behave (a BDD framework for Python), the "context" object is used to share data between steps in a scenario. 
    # It's like a temporary memory space that persists for the duration of a single scenario.
    # use to check the response code = context.response.status_code
    # use to Inspect the response bodyd (eg. e.g., context.response.json() or context.response.tex)
    # Also used in Allure reporting. 
    context.response = response
    context.response_json = response.json()

    # Print to console , but it is not working and i am not able to see the ID in console
    print("Response Body:", context.response.json())  

    #Attach to Allure report
    allure.attach(json.dumps(context.booking_data, indent=2), name="Request Payload", attachment_type=allure.attachment_type.JSON)
    allure.attach(json.dumps(context.response_json, indent=2), name="Response Body", attachment_type=allure.attachment_type.JSON)


    # Capture the booking ID generated (single value)
    # This will retrieve the bookingid from the API response. If bookingid doesn't exist, it will return "Not Found".
    booking_id = context.response_json.get("bookingid", "Not Found")  
    
    # Add this to make booking_id accessible in update step
    context.booking_id = booking_id


    # Attach it to Allure
    # This will attach the booking_id which is generated and attached to the Allure report as a text attachment.
    # booking_id --> Having the single ID which is coming from API response.
    # str(booking_id) --> Convert the ID into string before attach it to allure, Allure attachments require string or byte data.
    # name = "Booking ID" --> Name of the attachment that will appear in Allure report under the step.
    # attachment_type=allure.attachment_type.TEXT --> Tells Allure that the attached content is a simple text, so it displayed as simple text in the report.
    allure.attach(str(booking_id), name="Booking ID", attachment_type=allure.attachment_type.TEXT)

    # Use to Print the ID in console, but it is not working and i am not able to see the ID in console
    print("Booking ID:", booking_id)


@then("the response code should be 200")
def step_impl(context):

    # It asserts that the response code from the API call is 200 OK (which indicates a successful HTTP request).
    # If the assertion fails: Test will be stop at that point, An error will be raised & Failure reported in Allure.
    # context.response.status_code --> Gets the HTTP status code from the response (e.g., 200, 404, 500).
    # equal_to(200) --> A Hamcrest matcher that checks if the value is exactly 200.
    # assert_that() --> The Hamcrest assertion function that compares the actual value (status_code) with the expected value (200).
    # Equality and Comparison --> equal_to(x), is_not(x), is_(x), greater_then(x), less_then(x)..etc.
    # String Matchers --> contains_string("string"), starts_with("string"), ends_with("string")
    # Collection Matchers --> has_length(x), has_item(x), has_items(x, y), contains(x, y, z)
    # Type Matchers --> instance_of(Class), none(), not_none()
    assert_that(context.response.status_code, equal_to(200))
    print("Status Code:", context.response.status_code) # Use to Print in console, but it is not working and i am not able to see the output in console


@then("the booking ID should be present in the response")
def step_impl(context):

    # This evaluates if "bookingid" tag is present in JSON response or not, if present then pass TRUE.
    assert_that("bookingid" in context.response_json, equal_to(True))
    # This assertion verifies that the "bookingid" value in the context.response_json is not None. 
    # In other words, it checks that the bookingid field exists and has a valid value.
    # assert_that(..., is_not(none())) --> This will pass if the value for "bookingid" is not None. If it is None, it will fail the test.
    assert_that(context.response_json["bookingid"], is_not(none()))

    # Capture the booking ID generated (single value)
    # This will retrieve the bookingid from the API response. If bookingid doesn't exist, it will return "Not Found".
    booking_id = context.response_json.get("bookingid", "Not Found")

    # Attach it to Allure
    # This will attach the booking_id which is generated and attached to the Allure report as a text attachment.
    allure.attach(str(booking_id), name="Booking ID", attachment_type=allure.attachment_type.TEXT)

    # Use to Print the ID in console, but it is not working and i am not able to see the ID in console
    print("Booking ID:", booking_id)
    
#-------------- Update details ---------------------------------

@when("I send an update request with new firstname '{new_firstname}'")
def step_impl(context, new_firstname):
    updated_data = context.booking_data.copy()
    updated_data["firstname"] = new_firstname
    context.updated_data = updated_data

    headers = {
        "Content-Type": "application/json",
        "Cookie": f"token={context.token}"
    }

    response = requests.put(
        f"{BASE_URL}/booking/{context.booking_id}",
        json=updated_data,
        headers=headers,
        verify=False
    )
    context.update_response = response
    context.update_json = response.json()

    allure.attach(json.dumps(context.update_json, indent=2), name="Update Response", attachment_type=allure.attachment_type.JSON)

@then("the updated firstname should be '{expected_name}'")
def step_impl(context, expected_name):
    assert_that(context.update_json["firstname"], equal_to(expected_name))
