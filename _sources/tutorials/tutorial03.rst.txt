.. raw:: pdf

    PageBreak

.. _id.tutorial03:

Tutorial 3: Step Parameters
==============================================================================

.. index:: step parameters

:Goal: Use step parameter to handover parameters to step functions.

Write the Feature Test
------------------------

.. literalinclude:: ../../features/tutorial03_step_parameters.feature
    :language: gherkin
    :prepend: # file:features/tutorial03_step_parameters.feature

The feature description contains a number of parameters,
where different values can be filled in. This also makes the test automation
layer much simpler, because the number of step definitions is reduced.

.. hint::

    **BEST PRACTICE:** Put parameters in **double-quoted text** to make
    variation-points visible. The test runner output does not have
    this problem, because it often marks these parameters as **bold text**.

Provide the Test Automation
-----------------------------

.. literalinclude:: ../../features/steps/step_tutorial03.py
    :prepend:   # file:features/steps/step_tutorial03.py
    :language: python
    :start-after: @mark.steps


Provide the Domain Model
-----------------------------

.. literalinclude:: ../../features/steps/blender.py
    :prepend:   # file:features/steps/blender.py
    :language: python
    :start-after: @mark.domain_model


Run the Feature Test
-----------------------------

When you run the feature file from above:

.. ifconfig:: ansiterm_supported

    .. command-output:: behave ../features/tutorial03_step_parameters.feature
        :shell:

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c ../features/tutorial03_step_parameters.feature
        :shell:
