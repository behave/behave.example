.. _id.tutorial01:

Tutorial 1: First Steps
==============================================================================

:Goal: Show basics, make first steps

Write the Feature Test
------------------------

The following feature file provides a simple feature with one scenario
in the known ``Given ... When ... Then ...`` language style (BDD).

.. literalinclude:: ../../features/tutorial01_basics.feature
    :prepend:   # file:features/tutorial01_basics.feature
    :language: gherkin


Provide the Test Automation
-----------------------------

To be able to execute the feature file, you need to provide a thin
automation layer that represents the steps in the feature file
with Python functions. These step functions provide the test automation layer
(fixture code) that interacts with the ``system-under-test`` (SUT).

.. literalinclude:: ../../features/steps/step_tutorial01.py
    :prepend:   # file:features/steps/step_tutorial01.py
    :language: python
    :start-after: @mark.steps


Run the Feature Test
-----------------------------

.. ifconfig:: ansiterm_supported

    When you run the feature file from above (with coloring enabled):

    .. command-output:: behave ../features/tutorial01_basics.feature
        :shell:

.. ifconfig:: not ansiterm_supported

    When you run the feature file from above (with coloring disabled):

    .. command-output:: behave -c ../features/tutorial01_basics.feature
        :shell:

As alternative you can run the feature with plain formatting
(or another formatter):

.. command-output:: behave --format=plain --show-timings ../features/tutorial01_basics.feature
    :shell:

