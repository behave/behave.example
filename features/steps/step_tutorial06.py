# -*- coding: UTF-8 -*-
"""
Based on ``behave tutorial``

Feature: Step Setup Table

   Scenario: Setup Table
     Given a set of specific users
        | name      | department  |
        | Barry     | Beer Cans   |
        | Pudey     | Silly Walks |
        | Two-Lumps | Silly Walks |

    When we count the number of people in each department
    Then we will find two people in "Silly Walks"
     But we will find one person in "Beer Cans"
"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave   import given, when, then
from hamcrest import assert_that, equal_to
from testutil import NamedNumber
from company_model import CompanyModel

@given('a set of specific users')
def step_impl(context):
    model = getattr(context, "model", None)
    if not model:
        context.model = CompanyModel()
    for row in context.table:
        context.model.add_user(row["name"], deparment=row["department"])

@when('we count the number of people in each department')
def step_impl(context):
    context.model.count_persons_per_department()

@then('we will find {count} people in "{department}"')
def step_impl(context, count, department):
    count_ = NamedNumber.from_string(count)
    assert_that(count_, equal_to(context.model.get_headcount_for(department)))

@then('we will find one person in "{department}"')
def step_impl(context, department):
    assert_that(1, equal_to(context.model.get_headcount_for(department)))
