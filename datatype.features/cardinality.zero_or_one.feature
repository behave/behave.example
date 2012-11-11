Feature: Data Type with Cardinality 0..1 (Optional Part)

  Scenario: Case1 "When attacked by a ..."
    Given the ninja has a black-belt
    When attacked by a samurai

  Scenario: Case2 "When attacked by ..."
    Given the ninja has a black-belt
    When attacked by Chuck Norris

# -- DESCRIPTION:
# "When attacked by ...": Once with "a ", once without it.
# Only one step should be used.
