.. _id.datatype.cardinality_one_or_more:

Cardinality: One or More (List of Type)
==============================================================================

.. index:: Cardinality: One or more, many

Sometimes a solution is needed where list of one or more items need to be parsed.
Initially, we want process a comma-separated list, like:

.. code-block:: gherkin

    Scenario:
        When I meet Alice
         And I meet Alice, Bob, Charly

Then, we want process a list that is separated by the word "and", like:

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
    :lines:  33-47

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
    :lines:  48-


Run the Test
-----------------------------

Now we run this example with ``behave``:

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

