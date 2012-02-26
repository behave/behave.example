.. _id.tutorial04:

Tutorial 4: Scenario Outline
==============================================================================

:Goal: Use scenario outline to avoid writing too many similar scenarios.

Write the Feature Test
------------------------

.. literalinclude:: ../features/tutorial04_scenario_outline.feature
    :language: gherkin
    :prepend: # file:features/tutorial04_scenario_outline.feature


Provide the Test Automation
-----------------------------

.. literalinclude:: ../features/steps/step_tutorial03.py
    :prepend:   # file:features/steps/step_tutorial03.py
    :language: python
    :lines:  1, 31-

.. note::

    Test automation layer reused from :ref:`id.tutorial03`.


Provide the Domain Model
-----------------------------

.. literalinclude:: ../features/steps/blender.py
    :prepend:   # file:features/steps/blender.py
    :language: python
    :lines:  1, 21-

.. note::

    Domain model reused from :ref:`id.tutorial03`.
