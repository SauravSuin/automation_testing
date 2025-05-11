@booking
Feature: Booking API

  @create_booking
  Scenario Outline: Successfully create a new booking
    Given I have booking data with "<firstname>", "<lastname>", "<price>", "<deposit>", "<checkin>", "<checkout>", "<additionalneeds>"
    When I send a create booking request
    Then the response code should be 200
    And the booking ID should be present in the response

    Examples:
      | firstname | lastname | price | deposit | checkin    | checkout   | additionalneeds |
      | Sam       | sui      |   500 | true    | 2025-05-12 | 2025-05-20 | Breakfast       |
      | suin      | sam      |   150 | false   | 2025-06-10 | 2025-06-15 | Breakfast       |



  @update_booking
  Scenario: Update booking firstname
    Given I have booking data with "Monu", "Suin", "1000", "true", "2025-05-12", "2025-05-20", "Lunch"
    When I send a create booking request
    And I send an update request with new firstname 'Saurav'
    Then the updated firstname should be 'Saurav'
