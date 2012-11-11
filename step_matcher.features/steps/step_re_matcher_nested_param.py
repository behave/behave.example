# -*- coding: UTF-8 -*-
"""
Nested parameter examples with "re" matcher (regular expression step matcher).
"""

from behave import step_matcher, when

# -----------------------------------------------------------------------------
# STEPS: With "re" matcher
# -----------------------------------------------------------------------------
step_matcher("re")

# -- NESTED GROUP:
@when(u'I try to match nested "(?P<foo>foo(?P<bar>bar)?)"')
def step_when_I_try_to_match_nested_foobar(context, foo, bar):
    context.foo = foo
    context.bar = bar

# -- SIMPLE GROUP: anything else
@when(u'I try to match nested "(?P<anything>.*)"')
def step_when_I_try_to_match_anything_else(context, anything):
    context.anything = anything
