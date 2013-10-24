# -*- coding: UTF-8 -*-
"""
Based on ``behave tutorial``

Feature: Step Parameters

  Scenario: Blenders
    Given I put "apples" in a blender
    When  I switch the blender on
    Then  it should transform into "apple juice".

Feature: Scenario Outline

  Scenario Outline: Blenders
     Given I put <thing> in a blender
     When I switch the blender on
     Then it should transform into <other thing>

   Examples: Amphibians
     | thing         | other thing |
     | Red Tree Frog | mush        |
     | apples        | apple juice |

   Examples: Consumer Electronics
     | thing         | other thing |
     | iPhone        | toxic waste |
     | Galaxy Nexus  | toxic waste |

"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave   import given, when, then
from hamcrest import assert_that, equal_to
from blender  import Blender

@given('I put "{thing}" in a blender')
def step_given_put_thing_into_blender(context, thing):
    context.blender = Blender()
    context.blender.add(thing)

@when('I switch the blender on')
def step_when_switch_blender_on(context):
    context.blender.switch_on()

@then('it should transform into "{other_thing}"')
def step_then_should_transform_into(context, other_thing):
    assert_that(context.blender.result, equal_to(other_thing))
