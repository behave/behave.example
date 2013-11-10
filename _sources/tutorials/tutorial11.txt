.. _id.tutorial11:

Tutorial 11: Use Tags
==============================================================================

.. index:: tags, use-tags

:Goal: Understand the usage of tags to organize the testsuite and optimize test runs.

Several test frameworks support a concept of tags to mark a number of tests
(`py.test markers`_, `TestNG test groups`_, `JUnit Categories`_,
`NUnit CategoryAttribute`_).
This provides a simple, flexible and effective mechanism to:

  * select  a number of tests
  * exclude a number of tests

for a test run. This mechanism is orthogonal to the
static test package structure.


.. hint:: Predefined or often used tags:

    ======= =============== ============================================
    Tag     Kind            Description
    ======= =============== ============================================
    @wip    predefined      "Work in Process" (under development).
    @skip   predefined      Skip/disable a feature, scenario, ...
    @slow   user-defined    Mark slow, long-running tests.
    ======= =============== ============================================


.. hint:: Tag Logic:

    ================== ============================ ==================================
    Logic Operation    Command Options              Description
    ================== ============================ ==================================
    select/enable      ``--tags=@one``              Only items with this tag.
    not (tilde/minus)  ``--tags=~@one``             Only items without this tag.
    logical-or         ``--tags=@one,@two``         If @one or @two is present.
    logical-and        ``--tags=@one --tags=@two``  If both @one and @two are present.
    ================== ============================ ==================================

    Notes:

      * The tag name prefix '@' (AT) is optional in tag options
      * Use ``--tags-help`` for a short description of the tag logic.

    See also `behave tags documentation`_ for more information on tags.


Write the Feature Test
------------------------

.. literalinclude:: ../../features/tutorial11_tags.feature
    :prepend:   # file:features/tutorial11_tags.feature
    :language: gherkin


Run the Feature Test
-------------------------

When you run the feature file by excluding the tag @wip,
then any feature marked with this tag is skipped as well as all of its scenarios.

.. ifconfig:: ansiterm_supported

    .. command-output:: behave --tags=-wip ../features/tutorial11_tags.feature
        :shell:

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c --tags=-wip ../features/tutorial11_tags.feature
        :shell:

.. note::

    Check the test summary for the skipped count for features and scenarios.


When you **enable the tag** @ninja.chuck:

.. ifconfig:: ansiterm_supported

    .. command-output:: behave --tags=ninja.chuck ../features/tutorial11_tags.feature
        :shell:

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c --tags=ninja.chuck ../features/tutorial11_tags.feature
        :shell:

.. note::

    Now only the second scenario is executed and the first one is skipped.

When you **disable the tag** @ninja.chuck:

.. ifconfig:: ansiterm_supported

    .. command-output:: behave --tags=-ninja.chuck ../features/tutorial11_tags.feature
        :shell:

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c --tags=-ninja.chuck ../features/tutorial11_tags.feature
        :shell:

.. note::

    Now only the first scenario is executed and the second one is now skipped.

When you select items with **either tag** @ninja.any **or** the tag
@ninja.chuck (**tag-or**):

.. ifconfig:: ansiterm_supported

    .. command-output:: behave --tags=@ninja.any,@ninja.chuck ../features/tutorial11_tags.feature
        :shell:

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c --tags=@ninja.any,@ninja.chuck ../features/tutorial11_tags.feature
        :shell:

.. note::

    Now both scenarios are executed.

When you select items that have the **tag** @ninja.any **and** the
tag @ninja.chuck (**tag-and**):

.. ifconfig:: ansiterm_supported

    .. command-output:: behave --tags=@ninja.any --tags=@ninja.chuck ../features/tutorial11_tags.feature
        :shell:

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c --tags=@ninja.any --tags=@ninja.chuck ../features/tutorial11_tags.feature
        :shell:

.. note::

    Now no scenario is executed, all are skipped.


.. _py.test markers:    http://pytest.org/latest/example/markers.html
.. _TestNG test groups: http://testng.org/
.. _JUnit Categories:   https://github.com/junit-team/junit/wiki/Categories
.. _NUnit CategoryAttribute:   http://www.nunit.org/index.php?p=category&r=2.4
.. _JUnit:  http://junit.org/
.. _behave tags documentation: http://packages.python.org/behave/tutorial.html#controlling-things-with-tags
