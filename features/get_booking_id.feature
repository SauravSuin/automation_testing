@getbookingid
Feature: Get Booking API

  @get_booking_id
  Scenario: Fetch all booking IDs
    When I send a GET request to the booking IDs endpoint
    Then the response status code should be 200
    And the response should contain a list of booking IDs
