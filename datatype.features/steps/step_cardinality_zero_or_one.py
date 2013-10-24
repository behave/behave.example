# -*- coding: UTF-8 -*-
"""
Feature: Use Optional Part in Step Definitions

  Scenario: Case 1 with "a "
    Given ...
    When attacked by a samurai

  Scenario: Case 2 without "a "
    Given ...
    When attacked by Chuck Norris
"""

# @mark.user_defined_types
# ------------------------------------------------------------------------
# USER-DEFINED TYPES:
# ------------------------------------------------------------------------
from behave import register_type
from parse_type import TypeBuilder
import parse

@parse.with_pattern(r"a\s+")
def parse_word_a(text):
    """Type converter for "a " (followed by one/more spaces)."""
    return text.strip()

# -- SAME:
# parse_optional_word_a = TypeBuilder.with_zero_or_one(parse_word_a)
parse_optional_word_a   = TypeBuilder.with_optional(parse_word_a)
register_type(optional_a_=parse_optional_word_a)


# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then
from hamcrest import assert_that, equal_to, is_in

# -- OPTIONAL-PART: {:optional_a_}
# By using data type with cardinality zero or one (0..1, optional).
@when('attacked by {:optional_a_}{opponent}')
def step_attacked_by(context, a_, opponent):
    context.ninja_fight.opponent = opponent
    # -- VERIFY: Optional part feature.
    assert_that(a_, is_in(["a", None]))
    assert_that(opponent, is_in(["Chuck Norris", "samurai"]))

# ----------------------------------------------------------------------------
# MORE STEPS:
# ----------------------------------------------------------------------------
from ninja_fight import NinjaFight

@given('the ninja has a {achievement_level}')
def step_the_ninja_has_a(context, achievement_level):
    context.ninja_fight = NinjaFight(achievement_level)

@then('the ninja should {reaction}')
def step_the_ninja_should(context, reaction):
    assert_that(reaction, equal_to(context.ninja_fight.decision()))
