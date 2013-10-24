# -*- coding: UTF-8 -*-
"""
Feature: User-Defined Enum Type (Name-to-Value Mapping)

    Scenario:
        When Romeo asks Julia: "Do you love me?"
        Then the answer is "yes"

    Scenario:
        When Romeo asks Julia: "Do you hate me?"
        Then the answer is "no"

    Scenario:
        When Romeo asks Julia: "Do you kiss me?"
        Then the answer is "silence"
"""

# ------------------------------------------------------------------------
# DOMAIN MODEL:
# ------------------------------------------------------------------------
answer_oracle = {
    "Do you love me?": True,
    "Do you hate me?": False,
    "Do you kiss me?": True,
}

# @mark.user_defined_types
# ------------------------------------------------------------------------
# USER-DEFINED TYPES:
# ------------------------------------------------------------------------
from behave import register_type
from parse_type import TypeBuilder

# -- ENUM: Returns True (for "yes" and "jubilee"), False (for "no")
parse_yesno = TypeBuilder.make_enum({"yes": True, "no": False, "jubilee": True })
register_type(YesNo=parse_yesno)

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import when, then
from hamcrest import assert_that, equal_to

@when(u'Romeo asks Julia: "{question}"')
def step_when_romeo_asks_julia(context, question):
    context.question = question

@then(u'the answer is "{answer:YesNo}"')
def step_then_the_answer_is(context, answer):
    assert_that(answer, equal_to(answer_oracle.get(context.question, None)))
