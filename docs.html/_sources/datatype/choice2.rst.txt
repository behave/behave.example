.. _id.datatype.choice2:

Choice2 (Word/String Alternatives)
==============================================================================

.. index:: Choice2, data type

This basically the same as :ref:`id.datatype.choice`,
but the generated type-converter function (parse_choice2) returns a
tuple::

    (selected_index, selected_text)

instead of ``selected_text`` (as string).
This is sometimes useful in step definitions if you need to use the
selected item index for other operations.


Define the Data Type
-----------------------------

.. code-block:: python

    # -- FILE: features/environment.py (location 1, global types)
    #    FILE: features/steps/step.py  (location 2, more locally used types)
    # ------------------------------------------------------------------------
    # USER-DEFINED TYPES:
    # ------------------------------------------------------------------------
    from behave import register_type
    from parse_type import TypeBuilder

    # -- CHOICE2: Constrain to a list of supported items (as string).
    offered_shop_items = [ "apples", "beef", "potatoes", "pork" ]
    parse_shop_item2 = TypeBuilder.make_choice2(offered_shop_items)
    register_type(ShopItem2=parse_shop_item2)

.. note::

    The :py:func:`TypeBuilder.make_choice2()` function performs the magic,
    as before.


Provide the Step Definitions
-----------------------------

.. code-block:: python

    # -- FILE: features/steps/step.py
    # ------------------------------------------------------------------------
    # STEPS:
    # ------------------------------------------------------------------------
    from behave import given, when, then

    @given("I buy {shop_item:ShopItem2}")
    def step_impl(context, shop_item):
        # EXAMPLE: "potatoes" => (selected_index=2, selected_text="potatoes")
        selected_index, selected_text = shop_item
        assert 0 <= select_index < len(offered_shop_items)
        shop_item_id = context.shop.shop_item_index2id(selected_index)
        context.shopping_cart.append(shop_item_id)
