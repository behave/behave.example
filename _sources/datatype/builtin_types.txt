.. _id.datatype.builtin_types:

Predefined Data Types in ``parse``
==============================================================================

`behave`_ uses the `parse`_ module (inverse of Python `string.format`_)
under the hoods to parse parameters in step definitions.
This leads to rather simple and readable parse expressions for step parameters.

Therefore, the following ``parse types`` are already supported
in step definitions without registration of any *user-defined type*:

===== =========================================== ========
Type  Characters Matched                          Output
===== =========================================== ========
 w    Letters and underscore                      str
 W    Non-letter and underscore                   str
 s    Whitespace                                  str
 S    Non-whitespace                              str
 d    Digits (effectively integer numbers)        int
 D    Non-digit                                   str
 n    Numbers with thousands separators (, or .)  int
 %    Percentage (converted to value/100.0)       float
 f    Fixed-point numbers                         float
 e    Floating-point numbers with exponent        float
      e.g. 1.1e-10, NAN (all case insensitive)
 g    General number format (either d, f or e)    float
 b    Binary numbers                              int
 o    Octal numbers                               int
 x    Hexadecimal numbers (lower and upper case)  int
 ti   ISO 8601 format date/time                   datetime
      e.g. 1972-01-20T10:21:36Z
 te   RFC2822 e-mail format date/time             datetime
      e.g. Mon, 20 Jan 1972 10:21:36 +1000
 tg   Global (day/month) format date/time         datetime
      e.g. 20/1/1972 10:21:36 AM +1:00
 ta   US (month/day) format date/time             datetime
      e.g. 1/20/1972 10:21:36 PM +10:30
 tc   ctime() format date/time                    datetime
      e.g. Sun Sep 16 01:03:52 1973
 th   HTTP log format date/time                   datetime
      e.g. 21/Nov/2011:00:07:11 +0000
 tt   Time                                        time
      e.g. 10:21:36 PM -5:30
===== =========================================== ========

XXX

.. hidden:

    :Goal: Show how user-defined datatypes can be used in step parameters.

    User-defined datatypes simplify the processing in step definitions.
    The string parameters are automatically parsed and converted into
    specific datatypes.

    .. note::

        Besides conversion into a user-defined type,
        this mechanism can also be used for text transformations
        that occurs before the parameter is handed to the step definition function.

    Write the Feature Test
    ------------------------

    .. literalinclude:: ../features/tutorial10_step_usertype.feature
        :prepend:   # file:features/tutorial10_step_usertype.feature
        :language: gherkin


    Provide the Test Automation
    -----------------------------

    .. literalinclude:: ../features/steps/step_tutorial10.py
        :prepend:   # file:features/steps/step_tutorial10.py
        :language: python
        :lines:  1, 19-

    Provide the Domain Model
    -----------------------------

    .. literalinclude:: ../features/steps/calculator.py
        :prepend:   # file:features/steps/calculator.py
        :language: python



.. _behave: http://pypi.python.org/pypi/behave
.. _parse:  http://pypi.python.org/pypi/parse
.. _string.format: http://docs.python.org/library/string.html#format-string-syntax