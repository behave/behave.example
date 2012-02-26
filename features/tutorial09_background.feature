Feature: Using Background -- Fight or Flight (Natural Language Part2, tutorial09)

    Background: Ninja fight setup
        Given the ninja encounters another opponent

    Scenario: Weaker opponent
        Given the ninja has a third level black-belt
        When attacked by a samurai
        Then the ninja should engage the opponent

    Scenario: Stronger opponent
        Given the ninja has a second level black-belt
        When attacked by Chuck Norris
        Then the ninja should run for his life
