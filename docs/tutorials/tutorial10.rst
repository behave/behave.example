.. _id.tutorial10:

Tutorial 10: User-defined Data Type
==============================================================================

:Goal: Show how user-defined datatypes can be used in step parameters.

User-defined datatypes simplify the processing in step definitions.
The string parameters are automatically parsed and converted into
specific datatypes.

.. note::

    Besides conversion into a user-defined type,
    this mechanism can also be used for text transformations
    that occurs before the parameter is handed to the step definition function.

Write the Feature Test
------------------------

.. literalinclude:: ../../features/tutorial10_step_usertype.feature
    :prepend:   # file:features/tutorial10_step_usertype.feature
    :language: gherkin


Provide the Test Automation
-----------------------------

.. literalinclude:: ../../features/steps/step_tutorial10.py
    :prepend:   # file:features/steps/step_tutorial10.py
    :language: python
    :lines:  1, 19-

Provide the Domain Model
-----------------------------

.. literalinclude:: ../../features/steps/calculator.py
    :prepend:   # file:features/steps/calculator.py
    :language: python


.. note::

    **Predefined Types**

    `behave`_ uses the `parse`_ module (inverse of Python `string.format`_)
    under the hoods to parse parameters in step definitions.
    This leads to rather simple and readable parse expressions for step parameters.

    See also :ref:`id.data_types.builtin_types` for more information.
    In addition, see also :ref:`id.data_types` for more information on
    defining and using user-defined data types.

.. _behave: http://pypi.python.org/pypi/behave
.. _parse:  http://pypi.python.org/pypi/parse
.. _string.format: http://docs.python.org/library/string.html#format-string-syntax