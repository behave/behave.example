# -*- coding: UTF-8 -*-
"""
Optional parameter examples with "re" matcher (regular expression step matcher).
"""

# @mark.steps
# -----------------------------------------------------------------------------
# STEPS: With "re" matcher
# -----------------------------------------------------------------------------
from behave import step_matcher, when
step_matcher("re")

# -- OPTIONAL 1: Optional param is captured and provided as parameter "an_".
@when(u'I try to match (?P<an_>an )?optional "(?P<foo>foo)"')
def step_when_I_try_to_match_an_optional_foo(context, an_, foo):
    context.foo = foo
    context.an_ = an_

# -- OPTIONAL 2: Optional param is matched, but not captured.
@when(u'I try to match (?:an )?optional "(?P<bar>bar)"')
def step_when_I_try_to_match_an_optional_bar(context, bar):
    context.bar = bar
