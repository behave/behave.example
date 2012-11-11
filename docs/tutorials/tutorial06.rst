.. _id.tutorial06:

Tutorial 6: Setup Table
==============================================================================

:Goal: Use *setup tables* to simplify test setup.

Write the Feature Test
------------------------

.. literalinclude:: ../../features/tutorial06_step_setup_table.feature
    :prepend:   # file:features/tutorial06_step_setup_table.feature
    :language: gherkin


Provide the Test Automation
-----------------------------

.. literalinclude:: ../../features/steps/step_tutorial06.py
    :prepend:   # file:features/steps/step_tutorial06.py
    :language: python
    :lines:  1, 19-

.. literalinclude:: ../../features/steps/testutil.py
    :prepend:   # file:features/steps/testutil.py
    :language: python
    :lines:  1, 5-

Provide the Domain Model
-----------------------------

.. literalinclude:: ../../features/steps/company_model.py
    :prepend:   # file:features/steps/company_model.py
    :language: python
    :lines:  1, 19-


Run the Feature Test
-----------------------------

When you run the feature file from above (with coloring enabled):

.. command-output:: behave ../features/tutorial06_step_setup_table.feature
    :shell:
