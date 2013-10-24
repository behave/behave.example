# -*- coding: UTF-8 -*-
"""
Based on ``behave tutorial``

Feature: User-Defined Choice Type (advanced tutorial01: choice)

    | The user-defined choice type supports only the following words:
    |   apples, beef, potatoes, pork

    Scenario:
        Given I go to a shop to buy ingredients for a meal
        And I buy apples
        And I buy beef
"""

# @mark.user_defined_types
# ------------------------------------------------------------------------
# USER-DEFINED TYPES:
# ------------------------------------------------------------------------
from behave import register_type
from parse_type import TypeBuilder

# -- CHOICE: Constrain to a list of supported items (as string).
offered_shop_items = [ "apples", "beef", "potatoes", "pork" ]
parse_shop_item = TypeBuilder.make_choice(offered_shop_items)
register_type(ShopItem=parse_shop_item)

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then

@given(u"I go to a shop to buy ingredients for a meal")
def step_given_I_go_to_a_shop(context):
    context.shopping_cart = [ ]

@when(u"I buy {shop_item:ShopItem}")
def step_when_I_buy(context, shop_item):
    assert shop_item in offered_shop_items
    context.shopping_cart.append(shop_item)
