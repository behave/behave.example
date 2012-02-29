.. _id.tutorial09:

Tutorial 9: Use Background
==============================================================================

:Goal: Use the ``Background`` concept to execute a number of steps before each scenario.


Write the Feature Test
------------------------

.. literalinclude:: ../features/tutorial09_background.feature
    :language: gherkin
    :prepend: # file:features/tutorial09_background.feature


Provide the Test Automation
-----------------------------

.. literalinclude:: ../features/steps/step_tutorial02.py
    :prepend:   # file:features/steps/step_tutorial02.py
    :append:    ...
    :language: python
    :lines:  1, 22-25, 52-65


Provide the Domain Model
-----------------------------

.. literalinclude:: ../features/steps/step_tutorial02.py
    :prepend:   # file:features/steps/step_tutorial02.py
    :language: python
    :lines:  26-51

Run the Feature Test
-----------------------------

When you run this feature test with the background functionality:

.. command-output:: behave --format=plain ../features/tutorial09_background.feature
    :shell:
