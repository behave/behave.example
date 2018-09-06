.. raw:: pdf

    PageBreak

.. _id.tutorial06:

Tutorial 6: Setup Table
==============================================================================

.. index:: setup-table, use-table, table

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
    :start-after: @mark.steps

.. literalinclude:: ../../features/steps/testutil.py
    :prepend:   # file:features/steps/testutil.py
    :language: python
    :start-after: @mark.test_support


Provide the Domain Model
-----------------------------

.. literalinclude:: ../../features/steps/company_model.py
    :prepend:   # file:features/steps/company_model.py
    :language: python
    :start-after: @mark.domain_model


Run the Feature Test
-----------------------------

When you run the feature file from above:

.. ifconfig:: ansiterm_supported

    .. command-output:: behave ../features/tutorial06_step_setup_table.feature
        :shell:

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c ../features/tutorial06_step_setup_table.feature
        :shell:
