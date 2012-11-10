.. _id.step_matcher:

==============================================================================
Step Matchers
==============================================================================

`behave`_ provides 2 step matchers:

  1. "parse" (ParseMatcher) by using the `parse`_ module
  2. "re" (RegexMatcher) that uses regular expressions for matching parameters

The "parse" matcher is the **default step matcher**.
It is more commonly used because it is:

  * easier to use, read and understand
  * provides data types support with predefined and user-defined types
  * reuses (hidden) regular expressions better by using data types (as alias)
  * hides regular expression complexity

The "re" matcher is used for the following reasons. It:

  * addresses some cases that cannot be solved otherwise (currently)
  * is backward compatible to `cucumber`_ (uses regular expressions)
  * is less ambiguous compared to the "parse" matcher (currently)

It should be noted that both step matchers use regular expressions.
But most of the regular expressions (and their complexity) is hidden
by the `parse`_ module.

----

**Contents:**

.. toctree::
    :maxdepth: 1

    using_matchers
    parse_matcher
    re_matcher
    use_optional_part
    use_multi_methods


.. _behave: http://pypi.python.org/pypi/behave
.. _parse:  http://pypi.python.org/pypi/parse
.. _cucumber: http://cukes.info/
