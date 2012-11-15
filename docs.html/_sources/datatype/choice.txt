.. _id.datatype.choice:

Choice (Word/String Alternatives)
==============================================================================

.. index:: Choice, data type

Assume you need a user-defined data type with the following features:

  * Only a limited number of words (or strings) should be matched
  * All values are pre-defined (before the test)

Then the **Choice** type is a solution for your problem.
Common use cases for the choice type are:

  * text-based enumerations (string enum)
  * color names
  * ...


Feature Example
-----------------------------

Assuming you want to write something like this:

.. literalinclude:: ../../datatype.features/choice.feature
    :prepend:   # file:datatype.features/choice.feature
    :language: gherkin
    :end-before: @xfail


Define the Data Type
-----------------------------

.. literalinclude:: ../../datatype.features/steps/step_choice.py
    :prepend:   # file:datatype.features/steps/step_choice.py
    :language: python
    :start-after: @mark.user_defined_types
    :end-before:  @mark.steps

.. note::

    The :py:meth:`TypeBuilder.make_choice()` function performs the magic.
    It computes a regular expression pattern for the given choice of
    words/strings and stores them in :py:attr:`parse_shop_item.pattern` attribute.
    This optional attribute is used by the :py:mod:`parse` module to improve
    pattern matching for user-defined types.


Provide the Step Definitions
-----------------------------

.. literalinclude:: ../../datatype.features/steps/step_choice.py
    :prepend:   # file:datatype.features/steps/step_choice.py
    :language: python
    :start-after: @mark.steps


Run the Test
-----------------------------

Now we run this example with :py:mod:`behave` (and all steps are matched):

.. ifconfig:: ansiterm_supported

    .. command-output:: behave --tags=-xfail --no-skipped ../datatype.features/choice.feature
        :shell:
        :returncode: 0

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c --tags=-xfail --no-skipped ../datatype.features/choice.feature
        :shell:
        :returncode: 0


SAD Feature Example
------------------------------------------------------------------------------

The following feature example shows that only supported choice values
are matched.

.. literalinclude:: ../../datatype.features/choice.feature
    :prepend:
        # file:datatype.features/choice.feature
        Feature: User-Defined Choice Type
    :language: gherkin
    :start-after: @xfail


When you run this example with :py:mod:`behave` the last step is not matched:

.. ifconfig:: ansiterm_supported

    .. command-output:: behave --tags=xfail --no-skipped ../datatype.features/choice.feature
        :shell:
        :returncode: 1

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c --tags=xfail --no-skipped ../datatype.features/choice.feature
        :shell:
        :returncode: 1

.. seealso:: :ref:`id.step_matcher.use_multi_methods`

    For a solution of this problem.



The Complete Picture
------------------------------------------------------------------------------

.. literalinclude:: ../../datatype.features/choice.feature
    :prepend:   # file:datatypes.features/choice.feature
    :language: gherkin

.. literalinclude:: ../../datatype.features/steps/step_choice.py
    :prepend:   # file:datatype.features/steps/step_choice.py
    :language: python
