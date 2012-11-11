.. _id.tutorial05:

Tutorial 5: Multi-line Text (Step Data)
==============================================================================

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
    :lines:  1, 16-19, 42-

Provide the Domain Model
-----------------------------

.. literalinclude:: ../../features/steps/step_tutorial05.py
    :prepend:   # file:features/steps/step_tutorial05.py
    :language: python
    :lines:  20-41


Run the Feature Test
-----------------------------

When you run the feature file from above (with coloring enabled):

.. command-output:: behave ../features/tutorial05_step_data.feature
    :shell:
