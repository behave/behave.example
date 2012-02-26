.. _id.tutorial08:

Tutorial 8: Step executes Other Steps
==============================================================================

:Goal: Use step execution to avoid code duplication.

In some case, you want to replace a number of steps in a scenario
by one simple **macro step** (*macro functionality*).
To avoid code duplication in the *test automation layer*,
the :term:`BDD` framework normally provides a functionality to easily call
these steps from within a step defintion.

Write the Feature Test
------------------------

.. literalinclude:: ../features/tutorial08_step_executes_steps.feature
    :prepend:   # file:features/tutorial08_step_executes_steps.feature
    :language: gherkin


Provide the Test Automation
-----------------------------

.. literalinclude:: ../features/steps/step_tutorial08.py
    :prepend:   # file:features/steps/step_tutorial08.py
    :language: python
    :lines:  1, 19-


