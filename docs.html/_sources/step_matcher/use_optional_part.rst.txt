.. _id.step_matcher.use_optional_part:

==============================================================================
Use Optional Part in Step Definitions
==============================================================================

.. index:: optional part

It is a common case that optional parts occur in steps and step definitions.
This happens often when you start writing steps and step definitions.

**EXAMPLE**:

.. code-block:: gherkin

    Feature:
        Scenario: Case 1
            When attacked by a samurai
            ...

        Scenario: Case 2
            When attacked by Chuck Norris
            ...


It would be nice if only one step definition would be sufficient for both cases.
An other point is that the step definition implementation is also identical.


Variant 1: Use Cardinality Field
===============================================================================

The :pypi:`parse` expression format provides an optional cardinality field part
after the type field. The '?' character is used to mark a step parameter
as optional (cardinality: 0..1).

.. note::

    You need to use the "cfparse" step matcher (:pypi:`parse` with cardinality field
    support based on a :pypi:`parse-type` parser) to use this functionality.
    The cardinality field is optional and follows the type field "Person"
    in a parse expression, like:

    ============  ==================== ========================================
    Cardinality    Example             Description
    ============  ==================== ========================================
       1          {person:Person}      One, implicit without cardinality field.
       0..1       {person:Person?}     **Zero or one:  For optional parts**.
       0..*       {persons:Person*}    Zero or more: For list<T> (many0).
       1..*       {persons:Person+}    One  or more: For list<T> (many).
    ============  ==================== ========================================

    Using the cardinality field in a parse expression is the
    preferred solution for the optional parameter problem.


Provide the Step Definitions
-----------------------------

.. literalinclude:: ../../step_matcher.features/steps/step_optional_part.py
    :prepend:   # file:step_matcher.features/steps/step_optional_part.py
    :language: python
    :start-after: @mark.steps
    :end-before:  @mark.more_steps

Define the Data Type
-----------------------------

.. literalinclude:: ../../step_matcher.features/steps/step_optional_part.py
    :prepend:   # file:step_matcher.features/steps/step_optional_part.py
    :language: python
    :start-after: @mark.user_defined_types
    :end-before:  @mark.steps


Run the Test
-----------------------------

Now we run this example with :py:mod:`behave`:

.. ifconfig:: ansiterm_supported

    .. command-output:: behave ../step_matcher.features/use_optional_part.feature
        :shell:
        :returncode: 0

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c ../step_matcher.features/use_optional_part.feature
        :shell:
        :returncode: 0


The Complete Picture
------------------------------------------------------------------------------

.. literalinclude:: ../../step_matcher.features/steps/step_optional_part.py
    :prepend:   # file:step_matcher.features/steps/step_optional_part.py
    :language: python


Variant 2: Use Data Type with Cardinality 0..1
===============================================================================

A special data type must be defined and registered that has the cardinality
*zero or one (0..1)*. This is similar to the solution above. But it requires
that the developer performs this work. In the case above this task is
implicitly done by :pypi:`parse` when it was needed
(triggered by the cardinality field).

.. hint::

    See also :ref:`id.datatype.cardinality_zero_or_one` for more information.

