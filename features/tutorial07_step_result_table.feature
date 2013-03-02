Feature: Step Result Table (tutorial07)

   Scenario: Unordered Result Table Comparison (RowFixture Table)
     Given a set of specific users:
        | name      | department  |
        | Alice     | Beer Cans   |
        | Bob       | Beer Cans   |
        | Charly    | Silly Walks |
        | Dodo      | Silly Walks |
    Then we will have the following people in "Silly Walks":
        | name    |
        | Charly  |
        | Dodo    |
    And we will have the following people in "Beer Cans":
        | name    |
        | Bob     |
        | Alice   |


   Scenario: Subset Result Table Comparison
     Given a set of specific users:
        | name      | department       |
        | Alice     | Super-sonic Cars |
        | Bob       | Super-sonic Cars |
    Then we will have at least the following people in "Super-sonic Cars":
        | name    |
        | Alice   |
