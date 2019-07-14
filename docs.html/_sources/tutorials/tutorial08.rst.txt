.. raw:: pdf

    PageBreak

.. _id.tutorial08:

Tutorial 8: Execute Other Steps in a Step
==============================================================================

.. index:: execute_steps()

:Goal: Reuse a sequence of existing steps as a step-macro.

In some case, you want to replace a number of steps in a scenario
by one simple **macro step** (*macro functionality*).
To avoid code duplication in the *test automation layer*,
the :term:`BDD` framework normally provides a functionality to easily call
these steps from within a step defintion.

Write the Feature Test
------------------------

.. literalinclude:: ../../features/tutorial08_step_executes_steps.feature
    :prepend:  # file:features/tutorial08_step_executes_steps.feature
    :language: gherkin


Provide the Test Automation
-----------------------------

.. literalinclude:: ../../features/steps/step_tutorial08.py
    :prepend:   # file:features/steps/step_tutorial08.py
    :language: python
    :start-after: @mark.steps

Run the Feature Test
-----------------------------

When you run the feature file from above:

.. ifconfig:: ansiterm_supported

    .. command-output:: behave ../features/tutorial08_step_executes_steps.feature
        :shell:

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -f plain ../features/tutorial08_step_executes_steps.feature
        :shell:

