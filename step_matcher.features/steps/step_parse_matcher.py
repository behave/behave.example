# -*- coding: UTF-8 -*-

from behave import given, then, use_step_matcher
from hamcrest import assert_that, equal_to, is_, none

# @mark.steps
# -----------------------------------------------------------------------------
# MORE STEPS: With "parse" matcher
# -----------------------------------------------------------------------------
use_step_matcher("parse")

@given(u'I use the regular expression step matcher')
def step_given_I_use_regex_matcher(context):
    pass

@then(u'the parameter "{name}" is "{expected_value}"')
def step_then_parameter_is_equal_to(context, name, expected_value):
    actual_value = getattr(context, name, None)
    assert_that(actual_value, equal_to(expected_value))

@then(u'the parameter "{name}" is none')
def step_then_parameter_is_none(context, name):
    actual_value = getattr(context, name, None)
    assert_that(actual_value, is_(none()))
