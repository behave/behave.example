.. raw:: pdf

    PageBreak

.. _id.tutorial02:

Tutorial 2: Natural Language
==============================================================================

:Goal: Use natural language when writing tests.

.. hint::
    This example is based on the `Ninja Survival Rate`_ examples
    from [SecretNinja10]_.

.. _`Ninja Survival Rate`: https://github.com/davedf/cuke4ninja/tree/master/src/ruby/NinjaSurvivalRate/features


Write the Feature Test
------------------------

.. literalinclude:: ../../features/tutorial02_natural_language.feature
    :prepend:   # file:features/tutorial02_natural_language.feature
    :language: gherkin


Provide the Test Automation
---------------------------------

.. literalinclude:: ../../features/steps/step_tutorial02.py
    :prepend:   # file:features/steps/step_tutorial02.py
    :language: python
    :start-after: @mark.steps
    :end-before:  @mark.background_steps


Provide the Domain Model
-----------------------------

Normally, the **domain model** is the

* *class-under-test* (CUT)
* *subsystem-under-test*
* *system-under-test* (SUT)

It contains the *business logic* that describes the behaviour of the system.
The thin test automation layer from above (step definitions) just interacts
with it.
The *domain model* normally preexists (in another Python module/package)
and you do not have to write it.

.. literalinclude:: ../../features/steps/step_tutorial02.py
    :prepend:   # file:features/steps/step_tutorial02.py
    :language: python
    :start-after: @mark.domain_model
    :end-before:  @mark.steps


Run the Feature Test
-----------------------------

When you run the feature file from above:

.. ifconfig:: ansiterm_supported

    .. command-output:: behave ../features/tutorial02_natural_language.feature
        :shell:

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c ../features/tutorial02_natural_language.feature
        :shell:


The Complete Picture
-----------------------------

.. literalinclude:: ../../features/steps/step_tutorial02.py
    :prepend:   # file:features/steps/step_tutorial02.py
    :language: python
    :end-before: @mark.background_steps


