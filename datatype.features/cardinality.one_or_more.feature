Feature: Data Type with Cardinality one or more (MANY, List<T>)

  Scenario: Many list, comma-separated
    Given I go to a meeting
    When I meet Alice, Bob, Dodo
    And  I meet Charly
    Then the following persons are present:
      | name   |
      | Alice  |
      | Bob    |
      | Charly |
      | Dodo   |

  Scenario: Many list with list-separator "and"
    Given I go to a meeting
    When I meet Alice and Bob and Charly
    Then the following persons are present:
      | name   |
      | Alice  |
      | Bob    |
      | Charly |
