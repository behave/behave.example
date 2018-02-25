.. _id.step_matcher.re_matcher:

==============================================================================
Use the Regular Expression Matcher (re)
==============================================================================

.. index:: re matcher, step matcher

This step matcher allows to use regular expressions in step definition.
The named parameter syntax ``(?P<name>...)`` should be used to extract
parameters from the step definition.

.. seealso::

    :ref:`id.step_matcher.regular_expressions` for more information
    on regular expressions.

Simple Parameters
==============================================================================

Provide the Step Definitions
-----------------------------

.. literalinclude:: ../../step_matcher.features/steps/step_re_matcher_simple_param.py
    :prepend:   # file:step_matcher.features/steps/step_re_matcher_simple_param.py
    :language: python
    :start-after: @mark.steps

.. literalinclude:: ../../step_matcher.features/steps/step_parse_matcher.py
    :prepend:   # file:step_matcher.features/steps/step_parse_matcher.py
    :language: python
    :start-after: @mark.steps


Run the Test
-----------------------------

Now we run this example with :py:mod:`behave`:

.. ifconfig:: ansiterm_supported

    .. command-output:: behave --no-source ../step_matcher.features/re_matcher.simple_param.feature
        :shell:
        :returncode: 0

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c ../step_matcher.features/re_matcher.simple_param.feature
        :shell:
        :returncode: 0


Optional Parameters
==============================================================================

.. index:: optional part (re)

Provide the Step Definitions
-----------------------------

.. literalinclude:: ../../step_matcher.features/steps/step_re_matcher_optional_param.py
    :prepend:   # file:step_matcher.features/steps/step_re_matcher_optional_param.py
    :language: python
    :start-after: @mark.steps


Run the Test
-----------------------------

Now we run this example with :py:mod:`behave`:

.. ifconfig:: ansiterm_supported

    .. command-output:: behave --no-source ../step_matcher.features/re_matcher.optional_param.feature
        :shell:
        :returncode: 0

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c ../step_matcher.features/re_matcher.optional_param.feature
        :shell:
        :returncode: 0


Nested Parameters
==============================================================================

.. index:: nested parameters (re)

Provide the Step Definitions
-----------------------------

.. literalinclude:: ../../step_matcher.features/steps/step_re_matcher_nested_param.py
    :prepend:   # file:step_matcher.features/steps/step_re_matcher_nested_param.py
    :language: python
    :start-after: @mark.steps


Run the Test
-----------------------------

Now we run this example with :py:mod:`behave`:

.. ifconfig:: ansiterm_supported

    .. command-output:: behave ../step_matcher.features/re_matcher.nested_param.feature
        :shell:
        :returncode: 0

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c ../step_matcher.features/re_matcher.nested_param.feature
        :shell:
        :returncode: 0
