Feature: Use Multi-Methods in Step Definitions
  Scenario:
    Given I go to a shop
    When I buy 2 cucumbers
     And I buy 3 apples
     And I buy 4 diamonds

# @mark.description
# Different step definition implementations are needed for different types.
# But the text of these steps should be the same.
# Data type cases are: vegetable, fruit, "anything else".
