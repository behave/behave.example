.. raw:: pdf

    PageBreak

.. _id.tutorial12:

Tutorial 12: Use another Spoken Language
==============================================================================

.. index:: select-language

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
        # -- file:*.feature
        ...

    When this happens, the :term:`BDD` framework selects the keywords for
    this language.
    The default language can be defined in the configuration file.
    `behave`_ uses either ``behave.ini`` or ``.behaverc`` as
    configuration file::

        # -- file:behave.ini
        [behave]
        lang = de


.. _behave: http://behave.readthedocs.io/

Write the Feature Test
------------------------

.. literalinclude:: ../../features/tutorial12_spoken_language.feature
    :prepend:   # file:features/tutorial12_spoken_language.feature
    :language: gherkin
    :end-before:  @mark.description


Provide the Test Automation
-----------------------------

.. literalinclude:: ../../features/steps/step_tutorial01.py
    :prepend:  # file:features/steps/step_tutorial01.py
    :language: python
    :start-after: @mark.steps

.. literalinclude:: ../../features/steps/step_tutorial12.py
    :prepend:
        # file:features/steps/step_tutorial12.py
        # -*- coding: UTF-8 -*-
        # language: de
    :language: python
    :start-after: @mark.steps

Run the Feature Test
-----------------------------

Automatic language selection (via feature-file language marker):

.. ifconfig:: ansiterm_supported

    .. command-output:: behave ../features/tutorial12_spoken_language.feature
        :shell:

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -f plain ../features/tutorial12_spoken_language.feature
        :shell:

Explicit language selection via command-line usage of ``--lang=${lang}``:

.. ifconfig:: ansiterm_supported

    .. command-output:: behave --lang=de ../features/tutorial12_spoken_language.feature
        :shell:

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -f plain --lang=de ../features/tutorial12_spoken_language.feature
        :shell:
