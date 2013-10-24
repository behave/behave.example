# -*- coding: UTF-8 -*-
"""
Feature: Data Type with Cardinality one or more (MANY, List<T>)

  Scenario:
    Given I go to a meeting
    When I meet Alice, Bob, Charly
    And  I meet Dodo
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
      | Bob    |
      | Alice  |
      | Charly |
"""

# ----------------------------------------------------------------------------
# DOMAIN MODEL:
# ----------------------------------------------------------------------------
class Meeting(object):
    def __init__(self):
        self.persons = set()


# @mark.user_defined_types
# ------------------------------------------------------------------------
# USER-DEFINED TYPES:
# ------------------------------------------------------------------------
from behave import register_type
from parse_type import TypeBuilder

company_persons = [ "Alice", "Bob", "Charly", "Dodo" ]
parse_person = TypeBuilder.make_choice(company_persons)
register_type(Person=parse_person)

# -- MANY-TYPE: Persons := list<Person> with list-separator = "and"
# parse_persons = TypeBuilder.with_one_or_more(parse_person, listsep="and")
parse_persons = TypeBuilder.with_many(parse_person, listsep="and")
register_type(PersonAndMore=parse_persons)

# -- NEEDED-UNTIL: parse_type.cfparse.Parser is used by behave.
# parse_persons2 = TypeBuilder.with_many(parse_person)
# type_dict = {"Person+": parse_persons2}
# register_type(**type_dict)


# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then

# -- MANY-VARIANT 1: Use Cardinality field in parse expression (comma-separated)
@when('I meet {persons:Person+}')
def step_when_I_meet_persons(context, persons):
    for person in persons:
        context.meeting.persons.add(person)

# -- MANY-VARIANT 2: Use special many data type ("and"-separated)
@when('I meet {persons:PersonAndMore}')
def step_when_I_meet_person_and_more(context, persons):
    for person in persons:
        context.meeting.persons.add(person)

# ----------------------------------------------------------------------------
# MORE STEPS:
# ----------------------------------------------------------------------------
from hamcrest import assert_that, contains

@given('I go to a meeting')
def step_given_I_go_to_meeting(context):
    context.meeting = Meeting()

@then('the following persons are present')
def step_following_persons_are_present(context):
    assert context.table, "table<Person> is required"
    actual_persons   = sorted(context.meeting.persons)
    expected_persons = [ row["name"]  for row in context.table ]

    # -- LIST-COMPARISON:
    assert_that(actual_persons, contains(*expected_persons))
