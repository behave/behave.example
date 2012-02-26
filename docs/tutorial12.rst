.. _id.tutorial12:

Tutorial 12: Use another Spoken Language
==============================================================================

:Goal: XXX Use step parameter to handover parameters to step functions.

XXX (Internationalisation)

Write the Feature Test
------------------------

.. literalinclude:: ../features/tutorial12_spoken_language.feature
    :prepend:   # file:features/tutorial12_stoken_language.feature
    :language: gherkin
    :lines:  1, 24-


Provide the Test Automation
-----------------------------

.. literalinclude:: ../features/steps/step_tutorial01.py
    :prepend:   # file:features/steps/step_tutorial01.py
    :language: python
    :lines:  1, 5-

.. literalinclude:: ../features/steps/step_tutorial12.py
    :prepend:   # file:features/steps/step_tutorial12.py
    :language: python
    :lines:  1-2, 18-

Execute the Feature Test
-----------------------------

Automatic language selection (via feature-file language marker):

.. command-output:: behave --format=plain ../features/tutorial12_spoken_language.feature
    :shell:

Explicit language selection via command-line usage of ``--lang=${lang}``:

.. command-output:: behave --lang=de --format=plain ../features/tutorial12_spoken_language.feature
    :shell:
