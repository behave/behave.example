.. raw:: pdf

    PageBreak

.. _id.tutorial10:

Tutorial 10: User-defined Data Type
==============================================================================

.. index:: data type, user-defined data type

:Goal: Show how user-defined data types can be used in step parameters.

User-defined data types simplify the processing in step definitions.
The string parameters are automatically parsed and converted into
specific data types.

.. note::

    Besides conversion into a user-defined type,
    this mechanism can also be used for text transformations
    that occurs before the parameter is handed to the step definition function.

Write the Feature Test
------------------------

.. literalinclude:: ../../features/tutorial10_step_usertype.feature
    :prepend:  # file:features/tutorial10_step_usertype.feature
    :language: gherkin


Provide the Test Automation
-----------------------------

First you need to provide the type converter for ``Number`` and register it:

.. literalinclude:: ../../features/steps/step_tutorial10.py
    :prepend:  # file:features/steps/step_tutorial10.py
    :language: python
    :start-after: @mark.user_defined_types
    :end-before:  @mark.steps

Now you can use ``Number`` as type in step parameters for the step definitions:

.. literalinclude:: ../../features/steps/step_tutorial10.py
    :prepend:  # file:features/steps/step_tutorial10.py
    :language: python
    :start-after: @mark.steps



Provide the Domain Model
-----------------------------

.. literalinclude:: ../../features/steps/calculator.py
    :prepend:  # file:features/steps/calculator.py
    :language: python
    :start-after: @mark.domain_model


Run the Feature Test
-----------------------------

When you run the feature file from above:

.. ifconfig:: ansiterm_supported

    .. command-output:: behave ../features/tutorial10_step_usertype.feature
        :shell:

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -f plain ../features/tutorial10_step_usertype.feature
        :shell:


The Complete Picture
-----------------------------

.. literalinclude:: ../../features/steps/step_tutorial10.py
    :prepend:  # file:features/steps/step_tutorial10.py
    :language: python


.. note::

    **Predefined Types**

    :pypi:`behave` uses the :pypi:`parse` module (inverse of Python `string.format`_)
    under the hoods to parse parameters in step definitions.
    This leads to rather simple and readable parse expressions for step parameters.

    See also :ref:`id.datatype.builtin_types` for more information.
    In addition, see also :ref:`id.datatype` for more information on
    defining and using user-defined data types.

.. _string.format: https://docs.python.org/3/library/string.html#format-string-syntax

