.. raw:: pdf

    PageBreak

.. _id.tutorial05:

Tutorial 5: Multi-line Text (Step Data)
==============================================================================

.. index:: multi-line text, docstring, step data

:Goal: Use multi-line text (with tripple-quoted text) for large text sections.

Triple-quoted strings (ala Python docstrings) provide a possible to use
large text section as step parameter. Normally, so much text would not fit
on one line.

Write the Feature Test
------------------------

.. literalinclude:: ../../features/tutorial05_step_data.feature
    :prepend:   # file:features/tutorial05_step_data.feature
    :language: gherkin


Provide the Test Automation
-----------------------------

.. literalinclude:: ../../features/steps/step_tutorial05.py
    :prepend:   # file:features/steps/step_tutorial05.py
    :language: python
    :start-after: @mark.steps

Provide the Domain Model
-----------------------------

.. literalinclude:: ../../features/steps/step_tutorial05.py
    :prepend:   # file:features/steps/step_tutorial05.py
    :language: python
    :start-after: @mark.domain_model
    :end-before:  @mark.steps


Run the Feature Test
-----------------------------

When you run the feature file from above:

.. ifconfig:: ansiterm_supported

    .. command-output:: behave ../features/tutorial05_step_data.feature
        :shell:

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c ../features/tutorial05_step_data.feature
        :shell:
