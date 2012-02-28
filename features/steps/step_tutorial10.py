# -*- coding: UTF-8 -*-
"""
Based on ``behave tutorial``

Feature: A Step uses a User-Defined Type as Step Parameter (tutorial10)

  Scenario Outline: Calculator
    Given I have a calculator
    When I add "<x>" and "<y>"
    Then the calculator returns "<sum>"

    Examples: Add Numbers
        |  x  |  y | sum |
        |  1  |  1 |  2  |
        |  1  |  2 |  3  |
        |  2  |  1 |  3  |
        |  2  |  7 |  9  |
"""

from behave   import given, when, then, matchers
from hamcrest import assert_that, equal_to

# ----------------------------------------------------------------------------
# Domain Model:
# ----------------------------------------------------------------------------
class Calculator(object):
    def __init__(self, value=0):
        self.result = value

    def reset(self):
        self.result = 0

    def add2(self, x, y):
        self.result += (x + y)
        return self.result


# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
# -- REGISTER USER-TYPE PARSER/CONVERTER:
matchers.register_type(Number=int)

@given('I have a calculator')
def step(context):
    context.calculator = Calculator()

@when('I add "{x:Number}" and "{y:Number}"')
def step(context, x, y):
    assert isinstance(x, int)
    assert isinstance(y, int)
    context.calculator.add2(x, y)

@then('the calculator returns "{expected:Number}"')
def step(context, expected):
    assert isinstance(expected, int)
    assert_that(context.calculator.result, equal_to(expected))
