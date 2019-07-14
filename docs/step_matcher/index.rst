.. raw:: pdf

    PageBreak

.. _id.step_matcher:

==============================================================================
Step Matchers
==============================================================================

:pypi:`behave` provides 3 step matchers:

  1. "parse" (ParseMatcher) by using the :pypi:`parse` module
  2. "cfparse" (extended ParseMatcher) that supports the cardinality field syntax
  3. "re" (RegexMatcher) that uses regular expressions for matching parameters

The "parse" matcher is the **default step matcher**.
It is more commonly used because it is:

  * easier to use, read and understand
  * provides data types support with predefined and user-defined types
  * reuses (hidden) regular expressions better by using data types (as alias)
  * hides regular expression complexity

The "cfparse" matcher extends the "parse" patcher (and is rather new).
It is intended to superceed the "parse" matcher as default matcher.
It has the following features:

  * extended parser that understands the cardinality field syntax
  * automatically creates missing type converters for fields
    with cardinality field part
  * based on :pypi:`parse-type`

The "re" matcher is used for the following reasons. It:

  * addresses some cases that cannot be solved otherwise (currently)
  * is backward compatible to `cucumber`_ (uses regular expressions)
  * is less ambiguous compared to the "parse" matcher (currently)

It should be noted that all step matchers use regular expressions.
But most of the regular expressions (and their complexity) is hidden
by the :pypi:`parse` module (or its cousin).

----

**Contents:**

.. toctree::
    :maxdepth: 1

    using_matchers
    parse_matcher
    re_matcher
    use_optional_part
    use_multi_methods
    regular_expressions


.. _cucumber: https://cucumber.io/
