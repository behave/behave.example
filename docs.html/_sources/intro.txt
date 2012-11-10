.. _id.introduction:

Introduction
==============================================================================

Read the Documentation
------------------------

Before you start reading this manual, you should have read the
`behave documentation`_ to understand how `behave` works.

.. hint::

    The `cucumber`_ and `jbehave`_ documentation might also be
    interesting for you, if you like to know where certain concepts originate.


Given, When, Then
------------------------

You should understand the :term:`BDD` concepts.

.. code-block:: gherkin

    Feature: Title (one line describing the story/feature)

        As a    [role]
        I want  [feature]
        So that [benefit]

        Scenario: Title1 (for Behaviour 1)

            Given [context or setup]
            And  [some more context]...
            When [event occurs]
            Then [expected outcome]
            And  [another outcome]...

        Scenario: Title2 (for Behaviour 2)
            ...



Select an Assertation Matcher Library
-----------------------------------------

Before you start to use `behave`_ (or any other :term:`BDD` framework)
you should select an assertation matcher library that you want to use
in your project.

Python has a growing number of assertation *matcher libraries* by now.
Here is the list of some of these:

=============== ===============================================================
Matcher Library Description
=============== ===============================================================
Native assert   Starting point, but not enough information when assert fails.
`hamcrest`_     First assertation matcher library, now part of `JUnit4`_.
                Supports several programming languages:
                http://code.google.com/p/hamcrest/
`nose.tools`_   Part of the `nose`_ test framework
`should-dsl`_   An interesting small matcher library,
                http://www.should-dsl.info/
`sure`_         Provided by the maker of `lettuce`_,
                https://github.com/gabrielfalcao/sure
`compare`_      http://pypi.python.org/pypi/compare
`describe`_     http://pypi.python.org/pypi/describe
=============== ===============================================================

.. note::

    `hamcrest`_ is used as *assertation matcher library* in the examples
    presented here.

.. _behave:   http://pypi.python.org/pypi/behave
.. _behave documentation:  http://packages.python.org/behave/
.. _hamcrest:   http://code.google.com/p/hamcrest/
.. _JUnit4:     http://junit.org/
.. _lettuce:    http://pypi.python.org/pypi/lettuce
.. _nose:       http://pypi.python.org/pypi/nose
.. _nose.tools: http://readthedocs.org/docs/nose/en/latest/testing_tools.html
.. _should-dsl: http://www.should-dsl.info/
.. _sure:       https://github.com/gabrielfalcao/sure
.. _compare:    http://pypi.python.org/pypi/compare
.. _describe:   http://pypi.python.org/pypi/describe

.. _cucumber: http://cukes.info/
.. _jbehave:  htpp://jbehave.org/


