.. _id.datatype.cardinality_zero_or_more:

Cardinality: Zero or More (List of Type)
==============================================================================

.. index:: Cardinality: Zero or more, many0

The solution to this problem is basically the same like with
:ref:`id.datatype.cardinality_one_or_more`.
Note that the case for zero or more items is not so often needed.

Initially, a comma-separated list is processed, like:

.. code-block:: gherkin

    Scenario:
        When I paint with red, green

Next, a list that is separated with the word "and" is processed, like:

.. code-block:: gherkin

    Scenario:
        When I paint with red and green


Feature Example
-----------------------------

.. literalinclude:: ../../datatype.features/cardinality.zero_or_more.feature
    :prepend:   # file:datatype.features/cardinality.zero_or_more.feature
    :language: gherkin


Define the Data Type
-----------------------------

.. literalinclude:: ../../datatype.features/steps/step_cardinality_zero_or_more.py
    :prepend:   # file:datatype.features/steps/step_cardinality_zero_or_more.py
    :language: python
    :start-after: @mark.user_defined_types
    :end-before:  @mark.steps

.. note::

    The :py:meth:`TypeBuilder.with_zero_and_more()` function performs the magic.
    It computes a regular expression pattern for the list of items.
    Then it generates a type-converter function that processes the list of
    items by using the type-converter for one item ("Color").


Provide the Step Definitions
-----------------------------

.. literalinclude:: ../../datatype.features/steps/step_cardinality_zero_or_more.py
    :prepend:   # file:datatype.features/steps/step_cardinality_zero_or_more.py
    :language: python
    :start-after: @mark.steps


Run the Test
-----------------------------

Now we run this example with :py:mod:`behave`:

.. ifconfig:: ansiterm_supported

    .. command-output:: behave ../datatype.features/cardinality.zero_or_more.feature
        :shell:
        :returncode: 0

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c ../datatype.features/cardinality.zero_or_more.feature
        :shell:
        :returncode: 0


The Complete Picture
------------------------------------------------------------------------------

.. literalinclude:: ../../datatype.features/steps/step_cardinality_zero_or_more.py
    :prepend:   # file:datatype.features/steps/step_cardinality_zero_or_more.py
    :language: python

