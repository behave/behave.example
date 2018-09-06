.. _id.step_matcher.parse_matcher:

==============================================================================
Use the Parse Matcher (parse)
==============================================================================

.. index:: parse matcher, step matcher

The "parse" matcher is used in most examples that are provided here.
It uses the :pypi:`parse` for regular expressions matching and parsing.
It provides:

  * predefined types
  * used-defined types and type-converters

.. seealso::

    * :ref:`id.datatype.builtin_types`
    * :ref:`id.datatype`


Step Definitions Example
-------------------------------------------------------------------------------

.. literalinclude:: ../../step_matcher.features/steps/step_parse_matcher.py
    :prepend:   # file:step_matcher.features/steps/step_parse_matcher.py
    :language: python

