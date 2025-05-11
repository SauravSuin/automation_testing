@getbookingdetails
Feature: Get Booking details by ID API
  
  @get_booking_detailsByID
  Scenario: Fetch booking ID details
    Given I have a valid booking ID
    When I send a GET request to fetch the booking
    Then the api response code should be 200
    And the booking details should be returned