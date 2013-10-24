# -*- coding: UTF-8 -*-
"""
Simple parameter examples with "re" matcher (regular expression step matcher).
"""

# @mark.steps
# -----------------------------------------------------------------------------
# STEPS: With "re" matcher
# -----------------------------------------------------------------------------
from behave import use_step_matcher, when
use_step_matcher("re")

# -- SIMPLE GROUP: foo
@when(u'I try to match "(?P<foo>foo)"')
def step_when_I_try_to_match_foo(context, foo):
    context.foo = foo

# -- SIMPLE GROUP: bar
@when(u'I try to match "(?P<bar>bar)"')
def step_when_I_try_to_match_bar(context, bar):
    context.bar = bar

# -- SIMPLE GROUP: anything else
@when(u'I try to match "(?P<anything>.*)"')
def step_when_I_try_to_match_anything_else(context, anything):
    context.anything = anything
