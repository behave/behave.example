.. _id.datatype.cardinality_zero_or_one:

Cardinality: Zero or One (Optional)
==============================================================================

.. index:: Cardinality: Zero or one, optional part

There are some cases, when a text part may be present or not.
Therefore, this text part is an optional and has cardinality zero or one (0..1).

The :py:class:`parse_type.TypeBuilder` can be used to compute the type with
cardinality zero or one based on data type with cardinality one.

.. seealso::

    :ref:`id.step_matcher.use_optional_part` for a simpler solution
    to this problem by using the **cardinality field** in parse expressions.


Feature Example
-----------------------------

Assuming you want to write something like this:

.. literalinclude:: ../../datatype.features/cardinality.zero_or_one.feature
    :prepend:   # file:datatype.features/cardinality.zero_or_one.feature
    :language: gherkin


Define the Data Type
-----------------------------

.. literalinclude:: ../../datatype.features/steps/step_cardinality_zero_or_one.py
    :prepend:   # file:datatype.features/steps/step_cardinality_zero_or_one.py
    :language: python
    :start-after: @mark.user_defined_types
    :end-before:  @mark.steps

.. note::

    The :py:meth:`TypeBuilder.with_optional()` function performs the magic.
    It computes a regular expression pattern for the given choice of
    words/strings and stores them in :py:attr:`parse_optional_word_a.pattern`
    attribute.


Provide the Step Definitions
-----------------------------

.. literalinclude:: ../../datatype.features/steps/step_cardinality_zero_or_one.py
    :prepend:   # file:datatype.features/steps/step_cardinality_zero_or_one.py
    :language: python
    :start-after: @mark.steps


Run the Test
-----------------------------

Now we run this example with :py:mod:`behave`:

.. ifconfig:: ansiterm_supported

    .. command-output:: behave ../datatype.features/cardinality.zero_or_one.feature
        :shell:

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c ../datatype.features/cardinality.zero_or_one.feature
        :shell:


The Complete Picture
------------------------------------------------------------------------------

.. literalinclude:: ../../datatype.features/steps/step_cardinality_zero_or_one.py
    :prepend:   # file:datatype.features/steps/step_cardinality_zero_or_one.py
    :language: python
