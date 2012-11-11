Feature: Use "re" Step Matcher with Nested Parameters

    Scenario: Nested parameter with nested match
        Given I use the regular expression step matcher
        When I try to match nested "foobar"
        Then the parameter "foo" is "foobar"
        And  the parameter "bar" is "bar"
        And  the parameter "anything" is none

    Scenario: Nested parameter with nested anything-else match
        Given I use the regular expression step matcher
        When I try to match nested "foo bar"
        Then the parameter "foo" is none
        And  the parameter "bar" is none
        And  the parameter "anything" is "foo bar"
