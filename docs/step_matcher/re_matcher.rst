.. _id.step_matcher.re_matcher:

==============================================================================
Use the Regular Expression Matcher (re)
==============================================================================

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

.. literalinclude:: ../../step_matcher.features/steps/step_parse_matcher.py
    :prepend:   # file:step_matcher.features/steps/step_parse_matcher.py
    :language: python


Run the Test
-----------------------------

Now we run this example with ``behave``:

.. command-output:: behave --no-source ../step_matcher.features/re_matcher.simple_param.feature
    :shell:
    :returncode: 0


Optional Parameters
==============================================================================

Provide the Step Definitions
-----------------------------

.. literalinclude:: ../../step_matcher.features/steps/step_re_matcher_optional_param.py
    :prepend:   # file:step_matcher.features/steps/step_re_matcher_optional_param.py
    :language: python


Run the Test
-----------------------------

Now we run this example with ``behave``:

.. command-output:: behave --no-source ../step_matcher.features/re_matcher.optional_param.feature
    :shell:
    :returncode: 0


Nested Parameters
==============================================================================

Provide the Step Definitions
-----------------------------

.. literalinclude:: ../../step_matcher.features/steps/step_re_matcher_nested_param.py
    :prepend:   # file:step_matcher.features/steps/step_re_matcher_nested_param.py
    :language: python


Run the Test
-----------------------------

Now we run this example with ``behave``:

.. command-output:: behave ../step_matcher.features/re_matcher.nested_param.feature
    :shell:
    :returncode: 0

