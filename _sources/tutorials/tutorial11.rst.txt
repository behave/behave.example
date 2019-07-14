.. raw:: pdf

    PageBreak

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

    ================== =============== ============================================
    Tag                 Kind            Description
    ================== =============== ============================================
    @wip                predefined      "Work in Process" (under development).
    @xfail              predefined      Tests that are (currently) expected to fail.
    @not_implemented    user-defined    Marks a test that is not implemented yet.
    @slow               user-defined    Mark slow, long-running tests.
    @glacier            user-defined    Mark even slower, longer running tests.
    ================== =============== ============================================


.. hint:: Tag Logic v2: Using :pypi:`cucumber-tag-expressions`

    ================== ============================ ========================================
    Logic Operation    Command Options              Description
    ================== ============================ ========================================
    select/enable      ``--tags=@one``              Only items with this tag.
    not                ``--tags="not @one"``        Only items without this tag.
    logical-or         ``--tags="@one or @two"``    If @one or @two is present.
    logical-and        ``--tags="@one and @two"``   If both @one and @two are present.
    match-substring    ``--tags="@one.*"``          Matches all tags that start with "one."
    ================== ============================ ========================================

    Notes:

    * The tag name prefix '@' (AT) is optional in tag options
    * Use ``--tags-help`` for a short description of the tag logic.
    * Use parenthesis to group tag expressions, like: ``@one and (@two or @three)``

    See also `behave tags documentation`_ for more information on tags.


.. hint: HIDDEN: Tag Logic v1 (deprecated):

    ================== ============================ ==================================
    Logic Operation    Command Options              Description
    ================== ============================ ==================================
    select/enable      ``--tags=@one``              Only items with this tag.
    not (tilde/minus)  ``--tags="~@one``             Only items without this tag.
    logical-or         ``--tags=@one,@two``         If @one or @two is present.
    logical-and        ``--tags=@one --tags=@two``  If both @one and @two are present.
    ================== ============================ ==================================



Write the Feature Test
------------------------

.. literalinclude:: ../../features/tutorial11_tags.feature
    :prepend:   # file:features/tutorial11_tags.feature
    :language: gherkin


Run the Feature Test
-------------------------

When you run the feature file by **excluding** the tag ``@wip``,
then any feature marked with this tag is skipped as well as all of its scenarios.

.. ifconfig:: ansiterm_supported

    .. command-output:: behave --tags="not wip" ../features/tutorial11_tags.feature
        :shell:

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c --tags="not wip" ../features/tutorial11_tags.feature
        :shell:

.. note::

    Check the test summary for the skipped count for features and scenarios.


Case: Select-by-tag
-----------------------------------------------------------------------------------

When you **enable the tag** ``@ninja.chuck``:

.. ifconfig:: ansiterm_supported

    .. command-output:: behave --tags=ninja.chuck ../features/tutorial11_tags.feature
        :shell:

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c --tags=ninja.chuck ../features/tutorial11_tags.feature
        :shell:

.. note::

    Now only the second scenario is executed and the first one is skipped.


Case: Exclude-by-tag (Logical-not)
-----------------------------------------------------------------------------------

When you **disable the tag** ``@ninja.chuck``:

.. ifconfig:: ansiterm_supported

    .. command-output:: behave --tags="not ninja.chuck" ../features/tutorial11_tags.feature
        :shell:

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c --tags="not ninja.chuck" ../features/tutorial11_tags.feature
        :shell:

.. note::

    Now only the first scenario is executed and the second one is now skipped.


Case: Select Combinations (Logical-or)
-----------------------------------------------------------------------------------

When you select items with **either tag** ``@ninja.any`` **or** the tag
``@ninja.chuck`` (**tag-or**):

.. ifconfig:: ansiterm_supported

    .. command-output:: behave --tags="@ninja.any or @ninja.chuck" ../features/tutorial11_tags.feature
        :shell:

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c --tags="@ninja.any or @ninja.chuck" ../features/tutorial11_tags.feature
        :shell:

.. note::

    Now both scenarios are executed.


Case: Logical-and
-----------------------------------------------------------------------------------

When you select items that have the **tag** ``@ninja.any``
**and** the tag ``@ninja.chuck`` (**tag-and**):

.. ifconfig:: ansiterm_supported

    .. command-output:: behave --tags="@ninja.any and @ninja.chuck" ../features/tutorial11_tags.feature
        :shell:

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c --tags="@ninja.any and @ninja.chuck" ../features/tutorial11_tags.feature
        :shell:

.. note::

    Now no scenario is executed, all are skipped.


Case: Match Tag Names by using Wildcards
-----------------------------------------------------------------------------------

When you select items that have a **tag** that starts with "``@ninja.``" prefix:

.. ifconfig:: ansiterm_supported

    .. command-output:: behave --tags="@ninja.*" ../features/tutorial11_tags.feature
        :shell:

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c --tags="@ninja.*" ../features/tutorial11_tags.feature
        :shell:

.. note::

    Again, both scenarios marked with ``@ninja.any`` and ``@ninja.chuck`` are executed.


.. _py.test markers:    http://docs.pytest.org/en/latest/example/markers.html
.. _TestNG test groups: https://testng.org/
.. _JUnit Categories:   https://github.com/junit-team/junit4/wiki/Categories
.. _NUnit CategoryAttribute:   https://nunit.org/index.php?p=category&r=2.4
.. _JUnit:  http://junit.org/
.. _behave tags documentation: https://behave.readthedocs.io/en/latest/tutorial.html#controlling-things-with-tags

