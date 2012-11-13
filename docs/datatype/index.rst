.. _id.datatype:

==============================================================================
Data Types and User-defined Types
==============================================================================

.. index:: data type

The following sections describe in more detail how user-defined data types
are used in `behave`_. The type-converter functionality, that is described here,
is only supported by the "parse" matcher.

----

**Contents:**

.. toctree::
    :maxdepth: 1

    basics
    builtin_types
    cardinality_zero_or_one
    cardinality_one_or_more
    cardinality_zero_or_more
    choice
    choice2
    enum
    more_complex_types

.. important::

    Part of the functionality, that is described here, is **experimental**.
    It is currently not part of the official `parse`_ release.
    Use the `jenisys/parse`_ fork, if you want to try it out.

    The `parse`_ module is the inverse of Python `string.format`_ function.

    .. index:: parse extensions

    **NEW FEATURES** (in `parse`_):

      * Optional :py:attr:`pattern` attribute in user-defined type-converters.

            This :py:attr:`pattern` attribute contains a regular expression
            for better pattern matching of the user-defined type (if present).

      * The :py:func:`with_pattern()` decorator for type-converters.

      * :py:mod:`parse_type` extensions (:py:class:`TypeBuilder` functionality).

      * Optional **cardinality field** part after type part in parse expression,
        like:

        ============  ==================== ===================================
        Cardinality    Example             Description
        ============  ==================== ===================================
           0..1       "{person:Person?}"   Zero or one:  For optional parts.
           0..*       "{persons:Person*}"  Zero or more: For list<T> (many0).
           1..*       "{persons:Person+}"  One  or more: For list<T> (many).
        ============  ==================== ===================================


.. _behave: http://pypi.python.org/pypi/behave
.. _parse:  http://pypi.python.org/pypi/parse
.. _string.format: http://docs.python.org/library/string.html#format-string-syntax
.. _jenisys/parse: https://github.com/jenisys/parse
