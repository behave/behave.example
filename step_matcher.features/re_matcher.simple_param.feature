Feature: Use "re" Step Matcher with Simple Parameters

    Scenario: Match simple parameter
        Given I use the regular expression step matcher
        When I try to match "foo"
        Then the parameter "foo" is "foo"
        And  the parameter "bar" is none

    Scenario: Match two simple parameters
        Given I use the regular expression step matcher
        When I try to match "foo"
         And I try to match "bar"
        Then the parameter "foo" is "foo"
        And  the parameter "bar" is "bar"
