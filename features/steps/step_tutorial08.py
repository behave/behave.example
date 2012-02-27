# -*- coding: UTF-8 -*
"""
Based on ``behave tutorial``

Feature: Step executes other Steps

   Scenario: Step by Step
     Given I start a new game
     When  I press the big red button
      And  I duck
     Then  I reach the next level

   Scenario: Execute multiple Steps in middle Step
     Given I start a new game
     When  I do the same thing as before
     Then  I reach the next level
"""

from behave   import given, when, then
from hamcrest import assert_that, greater_than

# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
@given('I start a new game')
def step(context):
    context.duck_count = 0
    context.red_button_pressed = 0

@when('I press the big red button')
def step(context):
    context.red_button_pressed += 1

@when('I duck')
def step(context):
    context.duck_count += 1

@when('I do the same thing as before')
def step(context):
    context.execute_steps(u"""
        when I press the big red button
         and I duck
    """)

@then('I reach the next level')
def step(context):
    assert_that(context.duck_count, greater_than(0))
    assert_that(context.red_button_pressed, greater_than(0))
