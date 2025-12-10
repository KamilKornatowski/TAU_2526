Feature: PJATK contact page

  Scenario Outline: Verify correct address on contact page in different browsers
    Given I open the PJATK website in "<browser>"
    When I accept cookies if visible
    And I go to the contact page
    Then I should see the address "ul. Koszykowa 86, 02-008 Warszawa"

    Examples:
      | browser  |
      | chrome   |
      | firefox  |

