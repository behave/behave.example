Feature: Use "re" Step Matcher with Optional Parameters

    Scenario: Optional parameter 1 is missing
        Given I use the regular expression step matcher
        When I try to match optional "foo"
        Then the parameter "foo" is "foo"
        And  the parameter "an_" is none

    Scenario: Optional parameter 1 is provided
        Given I use the regular expression step matcher
        When I try to match an optional "foo"
        Then the parameter "foo" is "foo"
        And  the parameter "an_" is "an "

    Scenario: Optional parameter 2 is missing
        Given I use the regular expression step matcher
        When I try to match optional "bar"
        Then the parameter "bar" is "bar"

    Scenario: Optional parameter 2 is provided (not captured)
        Given I use the regular expression step matcher
        When I try to match an optional "bar"
        Then the parameter "bar" is "bar"
