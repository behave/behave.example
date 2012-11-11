Feature: User-Defined Choice Type

    | The user-defined choice type supports only the following
    | choice of words:  apples, beef, potatoes, pork

    Scenario: Good Case
        Given I go to a shop to buy ingredients for a meal
        When I buy apples
         And I buy beef

    @xfail
    Scenario: Bad Case -- Undefined step definition for "diamonds"
        Given I go to a shop to buy ingredients for a meal
        When I buy apples
         And I buy pork
         And I buy diamonds
