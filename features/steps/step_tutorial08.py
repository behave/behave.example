# -*- coding: UTF-8 -*-
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

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave   import given, when, then
from hamcrest import assert_that, greater_than

@given('I start a new game')
def step_impl(context):
    context.duck_count = 0
    context.red_button_pressed = 0

@when('I press the big red button')
def step_impl(context):
    context.red_button_pressed += 1

@when('I duck')
def step_impl(context):
    context.duck_count += 1

@when('I do the same thing as before')
def step_impl(context):
    context.execute_steps(u"""
        when I press the big {button_color} button
         and I duck
    """.format(button_color="red"))

@then('I reach the next level')
def step_impl(context):
    assert_that(context.duck_count, greater_than(0))
    assert_that(context.red_button_pressed, greater_than(0))
