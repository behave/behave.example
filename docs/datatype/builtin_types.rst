.. _id.datatype.builtin_types:

Predefined Data Types in ``parse``
==============================================================================

:pypi:`behave` uses the :pypi:`parse` module (inverse of Python `string.format`_)
under the hoods to parse parameters in step definitions.
This leads to rather simple and readable parse expressions for step parameters.

Therefore, the following ``parse types`` are already supported
in step definitions without registration of any *user-defined type*:

===== =========================================== ========
Type  Characters Matched                          Output
===== =========================================== ========
l     Letters (ASCII)                             str
w     Letters, numbers and underscore             str
W     Not letters, numbers and underscore         str
s     Whitespace                                  str
S     Non-whitespace                              str
d     Digits (effectively integer numbers)        int
D     Non-digit                                   str
n     Numbers with thousands separators (, or .)  int
%     Percentage (converted to value/100.0)       float
f     Fixed-point numbers                         float
F     Decimal numbers                             Decimal
e     Floating-point numbers with exponent        float
      e.g. 1.1e-10, NAN (all case insensitive)
g     General number format (either d, f or e)    float
b     Binary numbers                              int
o     Octal numbers                               int
x     Hexadecimal numbers (lower and upper case)  int
ti    ISO 8601 format date/time                   datetime
      e.g. 1972-01-20T10:21:36Z ("T" and "Z"
      optional)
te    RFC2822 e-mail format date/time             datetime
      e.g. Mon, 20 Jan 1972 10:21:36 +1000
tg    Global (day/month) format date/time         datetime
      e.g. 20/1/1972 10:21:36 AM +1:00
ta    US (month/day) format date/time             datetime
      e.g. 1/20/1972 10:21:36 PM +10:30
tc    ctime() format date/time                    datetime
      e.g. Sun Sep 16 01:03:52 1973
th    HTTP log format date/time                   datetime
      e.g. 21/Nov/2011:00:07:11 +0000
ts    Linux system log format date/time           datetime
      e.g. Nov  9 03:37:44
tt    Time                                        time
      e.g. 10:21:36 PM -5:30
===== =========================================== ========


.. _string.format: https://docs.python.org/3/library/string.html#format-string-syntax
