Feature: Search word in Jisho dictionary

  Scenario Outline: Search for "computer" in Jisho
    Given I open the Jisho website in "<browser>"
    When I search for the word "computer"
    Then I should see at least one result

    Examples:
    | browser |
    | chrome |
    | firefox|