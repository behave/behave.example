.. _id.tutorial10:

Tutorial 10: User-defined Datatype
==============================================================================

:Goal: Show how used-defined datatypes can be used in step parameters.

User-defined datatypes simplify the processing in step definitions.
The string parameters are automatically parsed and converted into the
specific datatype.


Write the Feature Test
------------------------

.. literalinclude:: ../features/tutorial10_step_usertype.feature
    :prepend:   # file:features/tutorial10_step_usertype.feature
    :language: gherkin


Provide the Test Automation
-----------------------------

.. literalinclude:: ../features/steps/step_tutorial10.py
    :prepend:   # file:features/steps/step_tutorial10.py
    :language: python
    :lines:  1, 19-22, 38-

Provide the Domain Model
-----------------------------

.. literalinclude:: ../features/steps/step_tutorial10.py
    :prepend:   # file:features/steps/step_tutorial10.py
    :language: python
    :lines:  23-36


