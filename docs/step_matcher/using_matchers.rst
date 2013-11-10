.. _id.step_matcher.using_matchers:

==============================================================================
Using the Step Matchers
==============================================================================

.. index:: step matcher, step_matcher()

Default Matcher Strategy
-------------------------

The "parse" matcher is used per default.


Defining an own Default Matcher
-----------------------------------

Use the ``environment.py`` file to define an own default matcher
that is used for all features in the ``features/`` directory.

.. code-block:: python

    # -- FILE: features/environment.py
    from behave import use_step_matcher

    # -- SELECT DEFAULT STEP MATCHER: Use "re" matcher as default.
    # use_step_matcher("parse")
    # use_step_matcher("cfparse")
    use_step_matcher("re")

.. note::

    The step matcher strategy is reset to the default step matcher
    before each step is loaded. Therefore, if you use only one step matcher,
    it is sufficient to define it in the "environment.py" file.


Switch between Step Matcher Strategy in a Step Definition File
----------------------------------------------------------------

It is possible to switch the step matcher several times in a *step definition*.
But normally you group the step definitions according to their step matcher.

.. code-block:: python

    # -- FILE: features/steps/step.py
    from behave import given, when, then, use_step_matcher
    from hamcrest import assert_that, equal_to

    # ------------------------------------------------------------------------
    # STEPS with Regular Expression Matcher ("re")
    # ------------------------------------------------------------------------
    # -- SELECT STEP MATCHER: Before using it in step definitions.
    use_step_matcher("re")

    @when(u'I meet with "(?P<person>Alice|Bob)"')
    def step_when_I_meet(context, person):
        context.person = person

    # ------------------------------------------------------------------------
    # STEPS with Parse Matcher ("parse")
    # ------------------------------------------------------------------------
    use_step_matcher("parse")

    @then(u'I have a lot of fun with "{person}"')
    def step_then_I_have_fun_with(context, person):
        assert_that(person, equal_to(context.person))

