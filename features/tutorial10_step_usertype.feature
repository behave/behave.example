Feature: User-Defined Datatype as Step Parameter (tutorial10)

  As a test writer
  I want that a step parameter is converted into a specific datatype
  to simplify the programming of the step definition body.

  Scenario Outline: Calculator
    Given I have a calculator
    When I add "<x>" and "<y>"
    Then the calculator returns "<sum>"

    Examples:
        |  x  |  y | sum |
        |  1  |  1 |  2  |
        |  1  |  2 |  3  |
        |  2  |  1 |  3  |
        |  2  |  7 |  9  |
