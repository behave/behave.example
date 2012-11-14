.. _id.datatype.cardinality_one_or_more:

Cardinality: One or More (List of Type)
==============================================================================

.. index:: Cardinality: One or more, many

Sometimes a solution is needed where a list of one or more items needs
to be parsed. Initially, this should be a comma-separated list, like:

.. code-block:: gherkin

    Scenario:
        When I meet Alice
         And I meet Alice, Bob, Charly

Then, a list should be processed that is separated by the word "and", like:

.. code-block:: gherkin

    Scenario:
        When I meet Alice and Bob and Charly


Feature Example
-----------------------------

.. literalinclude:: ../../datatype.features/cardinality.one_or_more.feature
    :prepend:   # file:datatype.features/cardinality.one_or_more.feature
    :language: gherkin


Define the Data Type
-----------------------------

.. literalinclude:: ../../datatype.features/steps/step_cardinality_one_or_more.py
    :prepend:   # file:datatype.features/steps/step_cardinality_one_or_more.py
    :language: python
    :start-after: @mark.user_defined_types
    :end-before:  @mark.steps

.. note::

    The :py:meth:`TypeBuilder.with_many()` function performs the magic.
    It computes a regular expression pattern for the list of items.
    Then it generates a type-converter function that processes the list of
    items by using the type-converter for one item ("Person").


Provide the Step Definitions
-----------------------------

.. literalinclude:: ../../datatype.features/steps/step_cardinality_one_or_more.py
    :prepend:   # file:datatype.features/steps/step_cardinality_one_or_more.py
    :language: python
    :start-after: @mark.steps


Run the Test
-----------------------------

Now we run this example with :py:mod:`behave`:

.. ifconfig:: ansiterm_supported

    .. command-output:: behave ../datatype.features/cardinality.one_or_more.feature
        :shell:
        :returncode: 0

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c ../datatype.features/cardinality.one_or_more.feature
        :shell:
        :returncode: 0


The Complete Picture
------------------------------------------------------------------------------

.. literalinclude:: ../../datatype.features/steps/step_cardinality_one_or_more.py
    :prepend:   # file:datatype.features/steps/step_cardinality_one_or_more.py
    :language: python

