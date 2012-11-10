.. _id.step_matcher.using_matchers:

==============================================================================
Using the Step Matchers
==============================================================================

Default Matcher Strategy
-------------------------

The "parse" matcher is used per default.


Defining an own Default Matcher
-----------------------------------

Use ``environment.py`` file to define an own default matcher
that is used for all features in the ``features/`` directory.

::

    set_step_matcher("re")
    set_step_matcher("parse")

Select a Step Matcher
-----------------------------------

XXX

::

    set_step_matcher("re")
    set_step_matcher("parse")


Switch between Step Matchers in a Step Definition File
-------------------------------------------------------

XXX

::

    set_step_matcher("re")
    set_step_matcher("parse")


