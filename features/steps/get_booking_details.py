from behave import given, when, then
import requests
from utils.api_helpers import create_booking
from hamcrest import assert_that, equal_to, is_not, none
import json
import allure


# Get booking details by ID GET - https://restful-booker.herokuapp.com/booking

BASE_URL = "https://restful-booker.herokuapp.com"

@given("I have a valid booking ID")
def step_impl(context):
    # Get any booking ID (existing one)
    response = requests.get(f"{BASE_URL}/booking", verify=False)
    booking_list = response.json()
    assert booking_list, "No bookings found"
    context.booking_id = booking_list[0]["bookingid"]
    allure.attach(str(context.booking_id), name="Booking ID", attachment_type=allure.attachment_type.TEXT)

@when("I send a GET request to fetch the booking")
def step_impl(context):
    response = requests.get(f"{BASE_URL}/booking/{context.booking_id}", verify=False)
    context.response = response
    context.response_json = response.json()
    allure.attach(json.dumps(context.response_json, indent=2), name="Get Booking Response", attachment_type=allure.attachment_type.JSON)

@then("the api response code should be 200")
def step_impl(context):
    assert_that(context.response.status_code, equal_to(200))

@then("the booking details should be returned")
def step_impl(context):
    assert_that(context.response_json, is_not(none()))
    assert_that("firstname" in context.response_json, equal_to(True))
    assert_that("lastname" in context.response_json, equal_to(True))

