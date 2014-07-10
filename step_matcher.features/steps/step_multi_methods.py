# -*- coding: UTF-8 -*-
"""
Feature: Use Multi-Methods in Step Definitions

    Scenario:
        Given I go to a shop
        When I buy 2 cucumbers
         And I buy 3 apples
         And I buy 4 diamonds
"""

# @mark.domain_model
# ------------------------------------------------------------------------
# DOMAIN MODEL:
# ------------------------------------------------------------------------
class Shop(object):
    vegetable_price_list = {
        "cucumbers": 0.2,   # Dollars per piece.
        "lettuce":   0.8,   # Dollars per piece.
    }
    fruit_price_list = {
        "apples":     0.5,  # Dollars per piece.
        "pears":      0.6,  # Dollars per piece.
    }
    common_price_list = {
        "diamonds": 1000.    # Dollars for one with 10 karat (only 1 size).
    }

    def calculate_price_for_fruit(self, fruit, amount):
        price_per_unit = self.fruit_price_list[fruit]
        return price_per_unit*amount

    def calculate_price_for_vegetable(self, vegetable, amount):
        price_per_unit = self.vegetable_price_list[vegetable]
        return price_per_unit*amount

    def calculate_price_for(self, shop_item, amount):
        price_per_unit = self.common_price_list[shop_item]
        return price_per_unit*amount

# @mark.user_defined_types
# ------------------------------------------------------------------------
# USER-DEFINED TYPES:
# ------------------------------------------------------------------------
from behave import register_type
from parse_type import TypeBuilder

parse_vegetable = TypeBuilder.make_choice(["cucumbers", "lettuce"])
register_type(Vegetable=parse_vegetable)

parse_fruit = TypeBuilder.make_choice(["apples", "pears"])
register_type(Fruit=parse_fruit)

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then

@given(u"I go to a shop")
def step_given_I_go_to_a_shop(context):
    context.shop = Shop()
    context.shopping_cart = [ ]

# -- STEP-ORDERING-IMPORTANT: Else step must be last.
@when(u"I buy {amount:n} {vegetable:Vegetable}")
def step_when_I_buy_vegetable(context, amount, vegetable):
    price = context.shop.calculate_price_for_vegetable(vegetable, amount)
    context.shopping_cart.append((vegetable, amount, price))

@when(u"I buy {amount:n} {fruit:Fruit}")
def step_when_I_buy_fruit(context, amount, fruit):
    price = context.shop.calculate_price_for_fruit(fruit, amount)
    context.shopping_cart.append((fruit, amount, price))

@when(u"I buy {amount:n} {anything_else:w}")
def step_when_I_buy_anything_else(context, amount, anything_else):
    price = context.shop.calculate_price_for(anything_else, amount)
    context.shopping_cart.append((anything_else, amount, price))
