.. _id.introduction:

Introduction
==============================================================================

Read the Documentation
------------------------

Before you start reading this manual, you should have read the
`behave documentation`_ to understand how :pypi:`behave` works.

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



Select an Assertion Matcher Library
-----------------------------------------

Before you start to use :pypi:`behave` (or any other :term:`BDD` framework)
you should select an assertion matcher library that you want to use
in your project.

Python has a growing number of assertion *matcher libraries* by now.
Here is the list of some of these:

================ ===============================================================
Matcher Library  Description
================ ===============================================================
Native assert    Starting point, but not enough information when assert fails.
`hamcrest`_      First assertion matcher library, now part of `JUnit4`_.
                 Supports several programming languages:
                 https://github.com/hamcrest/PyHamcrest
`nose.tools`_    Part of the :pypi:`nose` test framework
`should-dsl`_    An interesting small matcher library,
                 https://pypi.python.org/pypi/should_dsl
:pypi:`sure`     Provided by the maker of :pypi:`lettuce`,
                 :github:`gabrielfalcao/sure`
:pypi:`compare`  https://pypi.python.org/pypi/compare
:pypi:`describe` https://pypi.python.org/pypi/describe
================ ===============================================================

.. note::

    `hamcrest`_ is used as *assertion matcher library* in the examples
    presented here.

.. _behave documentation:  http://pythonhosted.org/behave/
.. _hamcrest:   https://github.com/hamcrest/
.. _JUnit4:     http://junit.org/
.. _nose.tools: http://nose.readthedocs.io/en/latest/testing_tools.html
.. _should-dsl: https://pypi.python.org/pypi/should_dsl

.. _cucumber: https://cucumber.io/
.. _jbehave:  http://jbehave.org/

