.. _id.step_matcher.use_multi_methods:

==============================================================================
Use Multi-Methods in Step Definitions
==============================================================================

.. index:: multi-methods

Assume you have a number of rather similar steps, like:

.. hidden:
    .. code-block:: gherkin

        Feature:
            Scenario:
                Given I go to a shop
                When I buy 2 cucumbers
                 And I buy 3 apples
                 And I buy 4 diamonds

.. literalinclude:: ../../step_matcher.features/use_multi_methods.feature
    :prepend:   # file:step_matcher.features/use_multi_methods.feature
    :language: gherkin
    :end-before: @mark.description

But you need different step definition implementations for some cases
(data types, actually their regular expressions).
In this example, the following cases should be distinguished:

  * vegetables
  * fruits
  * anything else


There are 2 possible solutions how this problem can be mapped into
step definitions.


Variant 1: Use Single Method
==============================================================================

One step definition with a string-based data type is provided in this solution.
The step definition implementation contains the logic how to distinguish
between the different cases.

.. code-block:: python

    # -- FILE: step_matcher.features/steps/one_step.py
    from behave import given, when, then

    @when("I buy {amount:n} {shop_item:w}")
    def step_when_I_buy_shop_item(context, amount, shop_item):
        pass    # -- HERE comes the logic how to distinguish the cases.


Variant 2: Use Multi-Methods
==============================================================================

If different data types are needed in the step definitions, another solution
may be better. This solution, the **multi-methods** approach, is described here.

.. caution::

    This solution requires that each case uses a different regular expression
    for each data type (including the else-case).
    Otherwise, the step matcher algorithm will not be able to distinguish
    these cases.


Provide the Step Definitions
-----------------------------

.. literalinclude:: ../../step_matcher.features/steps/step_multi_methods.py
    :prepend:   # file:step_matcher.features/steps/step_multi_methods.py
    :language: python
    :start-after: @mark.steps

.. hidden:
    .. note::

        The ordering of the step definitions is important.
        The "anything else" step definition should be the last one.


Define the Data Types
-----------------------------

.. literalinclude:: ../../step_matcher.features/steps/step_multi_methods.py
    :prepend:   # file:step_matcher.features/steps/step_multi_methods.py
    :language: python
    :start-after: @mark.user_defined_types
    :end-before:  @mark.steps


Run the Test
-----------------------------

Now we run this example with :py:mod:`behave`:

.. ifconfig:: ansiterm_supported

    .. command-output:: behave ../step_matcher.features/use_multi_methods.feature
        :shell:
        :returncode: 0

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c ../step_matcher.features/use_multi_methods.feature
        :shell:
        :returncode: 0

.. note::
    Notice the difference in line numbers for each step.
    Each step matches a different step definition (implementation).


The Complete Picture
------------------------------------------------------------------------------

.. disabled:
    .. literalinclude:: ../../step_matcher.features/use_multi_methods.feature
        :prepend:   # file:step_matcher.features/use_multi_methods.feature
        :language: gherkin

.. literalinclude:: ../../step_matcher.features/steps/step_multi_methods.py
    :prepend:   # file:step_matcher.features/steps/step_multi_methods.py
    :language: python
    :linenos:

