.. raw:: pdf

    PageBreak

.. _id.tutorial04:

Tutorial 4: Scenario Outline
==============================================================================

.. index:: Scenario Outline

:Goal: Use scenario outline as a parametrized template (avoid too many similar scenarios).

A ``Scenario Outline`` provides a ``parametrized scenario script`` (or template)
for the feature file writer. The ``Scenario Outline`` is executed for each
example row in the ``Examples`` section below the ``Scenario Outline``.

Write the Feature Test
------------------------

.. literalinclude:: ../../features/tutorial04_scenario_outline.feature
    :language: gherkin
    :prepend: # file:features/tutorial04_scenario_outline.feature


Provide the Test Automation
-----------------------------

.. literalinclude:: ../../features/steps/step_tutorial03.py
    :prepend:   # file:features/steps/step_tutorial03.py
    :language: python
    :start-after: @mark.steps

.. note::

    Test automation layer reused from :ref:`id.tutorial03`.


Provide the Domain Model
-----------------------------

.. literalinclude:: ../../features/steps/blender.py
    :prepend:   # file:features/steps/blender.py
    :language: python
    :start-after: @mark.domain_model

.. note::

    Domain model reused from :ref:`id.tutorial03`.

Run the Feature Test
-----------------------------

When you run the feature file from above (with plain formatting):

.. ifconfig:: ansiterm_supported

    .. command-output:: behave ../features/tutorial04_scenario_outline.feature
        :shell:

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -f plain ../features/tutorial04_scenario_outline.feature
        :shell:

