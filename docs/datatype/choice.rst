.. _id.user_defined_types.choice:

Choice (Word/String Alternatives)
==============================================================================

Assume you need a user-defined data type with the following features:

  * Only a limited number of words (or strings) should be matched
  * All values are pre-defined (before the test)

Then the **Choice** type is a solution for your problem.
Common use cases for the choice type are:

  * text-based enumerations (string enum)
  * color names
  * ...


Feature Example
-----------------------------

Assuming you want to write something like this:

.. literalinclude:: ../../datatype.features/choice.feature
    :prepend:   # file:datatype.features/choice.feature
    :language: gherkin
    :lines:  1-10

Define the Data Type
-----------------------------

.. literalinclude:: ../../datatype.features/steps/step_choice.py
    :prepend:   # file:datatype.features/steps/step_choice.py
    :language: python
    :lines:  16-26

.. note::

    The ``TypeBuilder.make_choice()`` function performs the magic.
    It computes a regular expression pattern for the given choice of
    words/strings and stores them in ``parse_shop_item.pattern`` attribute.
    This optional attribute is used by the ``parse`` module to improve
    pattern matching for user-defined types.

.. hidden:
    :emphasize-lines: 22-25

Provide the Step Definitions
-----------------------------

.. literalinclude:: ../../datatype.features/steps/step_choice.py
    :prepend:   # file:datatype.features/steps/step_choice.py
    :language: python
    :lines:  28-


Run the Test
-----------------------------

Now we run this example with ``behave`` (and all steps are matched):

.. command-output:: behave --tags=-xfail --no-skipped ../datatype.features/choice.feature
    :shell:
    :returncode: 0


SAD Feature Example
------------------------------------------------------------------------------

The following feature example shows that only supported choice values
are matched.

.. literalinclude:: ../../datatype.features/choice.feature
    :prepend:   # file:datatype.features/choice.feature
    :language: gherkin
    :lines:  1, 10-


When you run this example with ``behave`` the last step is not matched:

.. command-output:: behave --tags=xfail --no-skipped ../datatype.features/choice.feature
    :shell:
    :returncode: 1


The Complete Picture
------------------------------------------------------------------------------

.. literalinclude:: ../../datatype.features/choice.feature
    :prepend:   # file:datatypes.features/choice.feature
    :language: gherkin

.. literalinclude:: ../../datatype.features/steps/step_choice.py
    :prepend:   # file:datatype.features/steps/step_choice.py
    :language: python
    :lines:  1,16-
