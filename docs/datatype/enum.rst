.. _id.datatype.enum:

Enumeration (String-to-Value Mapping)
==============================================================================

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
    :lines:  27-35

.. note::

    The ``TypeBuilder.make_enum()`` function performs the magic.
    It computes a regular expression pattern for the given enumeration of
    words/strings and stores them in ``parse_yesno.pattern`` attribute.


Provide the Step Definitions
-----------------------------

.. literalinclude:: ../../datatype.features/steps/step_enum.py
    :prepend:   # file:datatype.features/steps/step_enum.py
    :language: python
    :lines:  36-


Run the Test
-----------------------------

Now we run this example with ``behave`` (and all steps are matched):

.. command-output:: behave ../datatype.features/enum.feature
    :shell:
    :returncode: 0


The Complete Picture
------------------------------------------------------------------------------

.. literalinclude:: ../../datatype.features/steps/step_enum.py
    :prepend:   # file:datatype.features/steps/step_enum.py
    :language: python
