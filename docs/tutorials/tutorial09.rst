.. raw:: pdf

    PageBreak

.. _id.tutorial09:

Tutorial 9: Use Background
==============================================================================

.. index:: use-background, Background

:Goal: Use the ``Background`` concept to execute a number of steps before each scenario.

.. hint::
    This example is based on the `Ninja Survival Rate`_ examples
    from [SecretNinja10]_.

.. _`Ninja Survival Rate`: https://github.com/davedf/cuke4ninja/tree/master/src/ruby/NinjaSurvivalRate/features


Write the Feature Test
------------------------

.. literalinclude:: ../../features/tutorial09_background.feature
    :language: gherkin
    :prepend: # file:features/tutorial09_background.feature


Provide the Test Automation
-----------------------------

.. literalinclude:: ../../features/steps/step_tutorial02.py
    :prepend:  # file:features/steps/step_tutorial02.py
    :language: python
    :start-after: @mark.background_steps

.. literalinclude:: ../../features/steps/step_tutorial02.py
    :prepend:  # file:features/steps/step_tutorial02.py
    :language: python
    :start-after: @mark.steps
    :end-before:  @mark.background_steps

Provide the Domain Model
-----------------------------

.. literalinclude:: ../../features/steps/step_tutorial02.py
    :prepend:  # file:features/steps/step_tutorial02.py
    :language: python
    :start-after: @mark.domain_model
    :end-before:  @mark.steps


Run the Feature Test
-----------------------------

When you run this feature test with the background functionality:

.. ifconfig:: ansiterm_supported

    .. command-output:: behave ../features/tutorial09_background.feature
        :shell:

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -f plain ../features/tutorial09_background.feature
        :shell:
