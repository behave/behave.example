.. _id.tutorial11:

Tutorial 11: Use Tags
==============================================================================

:Goal: Understand the usage of tags to organize the testsuite.


Write the Feature Test
------------------------

.. literalinclude:: ../features/tutorial11_tags.feature
    :prepend:   # file:features/tutorial11_tags.feature
    :language: gherkin


Run the Feaure Test
-------------------------

When you run the feature file with disabled tag @wip,
then marked feature is skipped as well as all its scenarios.

.. command-output:: behave --format=plain --tags ~@wip ../features/tutorial11_tags.feature
    :shell:

.. note::

    Check the test summary for the skipped count for features and scenarios.


When you run the feature file with enabled tag @ninja.chuck,
then only the second scenario is executed and the first one is skipped.

.. command-output:: behave -c --tags @ninja.chuck ../features/tutorial11_tags.feature
    :shell:

.. note::

    Check the test summary for the skipped count for scenarios
    and the expansion of the scenario.

