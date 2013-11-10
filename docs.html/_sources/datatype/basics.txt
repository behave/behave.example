.. _id.datatype.basics:

Type Definition Basics
==============================================================================

Workflow
---------------------

Preparation/setup phase:

    0. The user registers a data type, for example in ``environment.py``.

The :pypi:`parse` module is the workhorse:

    1. The :py:class:`parse.Parser` class matches a string for a data type.

    2. Then it calls the type-converter function to convert the
       matched text into an object of this data type.


Simple Example
---------------------

The following example shows how a user-defined type can be provided.

.. literalinclude:: ../../features/steps/step_tutorial10.py
    :prepend:   # file:features/steps/step_tutorial10.py
    :language: python
    :start-after: @mark.user_defined_types
    :end-before:  @mark.steps

.. seealso::

    :ref:`id.tutorial10` for more information on this example.


Example with Regular Expression Pattern
----------------------------------------

For better matching of user-defined data types, the :pypi:`parse` supports
an optional ``pattern`` attribute for type-converter functions.
If this attribute is provided, it contains a textual regular expression
for this data type. This regular expression pattern is used to match
the data type.

The regular expression pattern can be defined by using the
:py:func:`parse.with_pattern` function decorator:

.. literalinclude:: ../../step_matcher.features/steps/step_optional_part.py
    :prepend:   # file:step_matcher.features/steps/step_optional_part.py
    :language: python
    :start-after: @mark.user_defined_types
    :end-before:  @mark.steps

or by assigning the :py:attr:`pattern` attribute, like:

.. code-block:: python

    parse_word_a.pattern = r"a\s+"
