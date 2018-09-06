.. _id.datatype.enum:

Enumeration (String-to-Value Mapping)
==============================================================================

.. index:: Enum, Enumeration, data type

An enumeration maps a number of unique string-based words/strings to values.

Feature Example
-----------------------------

Assuming you want to write something like this:

.. literalinclude:: ../../datatype.features/enum.feature
    :prepend:   # file:datatype.features/enum.feature
    :language: gherkin


Define the Data Type
-----------------------------

.. literalinclude:: ../../datatype.features/steps/step_enum.py
    :prepend:   # file:datatype.features/steps/step_enum.py
    :language: python
    :start-after: @mark.user_defined_types
    :end-before:  @mark.steps

.. note::

    The :py:func:`TypeBuilder.make_enum()` function performs the magic.
    It computes a regular expression pattern for the given enumeration of
    words/strings and stores them in :py:attr:`parse_yesno.pattern` attribute.


Provide the Step Definitions
-----------------------------

.. literalinclude:: ../../datatype.features/steps/step_enum.py
    :prepend:   # file:datatype.features/steps/step_enum.py
    :language: python
    :start-after:  @mark.steps


Run the Test
-----------------------------

Now we run this example with :py:mod:`behave` (and all steps are matched):

.. ifconfig:: ansiterm_supported

    .. command-output:: behave ../datatype.features/enum.feature
        :shell:
        :returncode: 0

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c ../datatype.features/enum.feature
        :shell:
        :returncode: 0


The Complete Picture
------------------------------------------------------------------------------

.. literalinclude:: ../../datatype.features/steps/step_enum.py
    :prepend:   # file:datatype.features/steps/step_enum.py
    :language: python
