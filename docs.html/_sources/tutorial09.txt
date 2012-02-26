.. _id.tutorial09:

Tutorial 9: Use Background
==============================================================================

:Goal: XXX Use step parameter to handover parameters to step functions.

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
    :lines:  1, 23-26, 53-68

Provide the Domain Model
-----------------------------

.. literalinclude:: ../features/steps/step_tutorial02.py
    :prepend:   # file:features/steps/step_tutorial02.py
    :language: python
    :lines:  27-51

Execute the Feature Test
-----------------------------

When you run this feature test with the background functionality:

.. command-output:: behave --format=plain ../features/tutorial09_background.feature
    :shell:
