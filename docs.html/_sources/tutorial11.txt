.. _id.tutorial11:

Tutorial 11: Use Tags
==============================================================================

:Goal: Understand the usage of tags to organize the testsuite and optimize test runs.

Several test frameworks support a concept of tags to mark a number of tests
(`py.test markers`_, `TestNG test groups`_, `JUnit Categories`_,
`NUnit CategoryAttribute`_).
This provides a simple, flexible and effective mechanism to:

  * select  a number of tests
  * exclude a number of tests

for a test run. This mechanism is orthogonal to the
static test package structure.

.. _py.test markers:    http://pytest.org/latest/example/markers.html
.. _TestNG test groups: http://testng.org/
.. _JUnit Categories:   http://kentbeck.github.com/junit/javadoc/latest/org/junit/experimental/categories/Categories.html
.. _NUnit CategoryAttribute:   http://www.nunit.org/index.php?p=category&r=2.4
.. _JUnit:  http://junit.org/

.. hint:: Predefined or often used tags:

    ======= =============== ============================================
    Tag     Kind            Description
    ======= =============== ============================================
    @wip    predefined      "Work in Process" (under development).
    @skip   predefined      Skip/disable a feature, scenario, ...
    @slow   user-defined    Mark slow, long-running tests.
    ======= =============== ============================================

    Tags option:

      * Enable a tag, like: ``--tags=TAG``
      * Disable a tag by using a minus sign prefix: ``--tags=-TAG``
      * Select multiple tags by using a comma-separated list: ``--tags=TAG1,TAG2``
      * ALTERNATIVE: Use a sequence of tags options: ``--tags=TAG1 --tags=TAG2``

    .. seealso::
       `behave tags documentation`_

.. _behave tags documentation: http://packages.python.org/behave/tutorial.html#controlling-things-with-tags


Write the Feature Test
------------------------

.. literalinclude:: ../features/tutorial11_tags.feature
    :prepend:   # file:features/tutorial11_tags.feature
    :language: gherkin


Run the Feaure Test
-------------------------

When you run the feature file by excluding the tag @wip,
then any feature marked with this tag is skipped as well as all of its scenarios.

.. command-output:: behave --format=plain --tags=-wip ../features/tutorial11_tags.feature
    :shell:

.. note::

    Check the test summary for the skipped count for features and scenarios.


When you run the feature file by selecting the tag @ninja.chuck,
then only the second scenario is executed and the first one is skipped.

.. command-output:: behave -c --tags=ninja.chuck ../features/tutorial11_tags.feature
    :shell:

.. note::

    Check the test summary for the skipped count for scenarios
    and the expansion of the scenario.

