.. _id.tutorial12:

Tutorial 12: Use another Spoken Language
==============================================================================

:Goal: Use another spoken language for testing (other than English)

Most :term:`BDD` frameworks provide internationalisation support.
The key part (but only the first step) is that the ``Given ... When ... Then``
keywords are provided in the native language, for example French or German.
If this is the case, a developer can provide step definitions in another
spoken language.

.. hint::

    The list of supported languages can be displayed via::

        behave --lang-list

    Feature files can be tagged for a specific language, like::

        # language: de
        ...

    When this happens, the :term:`BDD` framework selects the keywords for
    this language.
    The default language can be defined in the configuration file.
    `behave`_ uses either ``behave.ini`` or ``.behaverc`` as
    configuration file::

        [behave]
        lang = de


.. _behave: http://packages.python.org/behave/

Write the Feature Test
------------------------

.. literalinclude:: ../../features/tutorial12_spoken_language.feature
    :prepend:   # file:features/tutorial12_stoken_language.feature
    :language: gherkin
    :lines:  1, 24-


Provide the Test Automation
-----------------------------

.. literalinclude:: ../../features/steps/step_tutorial01.py
    :prepend:   # file:features/steps/step_tutorial01.py
    :language: python
    :lines:  1, 5-

.. literalinclude:: ../../features/steps/step_tutorial12.py
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
