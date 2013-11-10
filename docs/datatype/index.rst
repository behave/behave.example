.. _id.datatype:

==============================================================================
Data Types and User-defined Types
==============================================================================

.. index:: data type

The following sections describe in more detail how user-defined data types
are used in `behave`_. The type-converter functionality, that is described here,
is only supported by the:

  * "parse" matcher (based on: `parse`_ module)
  * "cfparse" matcher (based on: `parse_type`_ module)

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

    Part of the functionality, that is described here, is based on
    `parse_type`_, an extension of the excellent `parse`_ module.

    The `parse`_ module is the inverse of Python `string.format`_ function.
    The `parse_type`_ module extends it to simplify the generation of types
    (actually type converter functions for types).

    .. index:: parse extensions

    `parse`_ *features*:

      * Optional :py:attr:`pattern` attribute (for regex) in user-defined type converters.
      * The :py:func:`with_pattern()` decorator for type-converters.

    `parse_type`_ *features*:

      * Simplifies the creation of type converters for some common cases
      * Creates type converter variants based on cardinality
      * :py:mod:`parse_type` extensions (:py:class:`TypeBuilder` functionality).
      * Provides an extended parser with **cardinality field** support.
        A cardinality field is a type suffix in parse expression, like:

        ============  ==================== ===================================
        Cardinality    Example             Description
        ============  ==================== ===================================
           0..1       "{person:Person?}"   Zero or one:  For optional parts.
           0..*       "{persons:Person*}"  Zero or more: For list<T> (many0).
           1..*       "{persons:Person+}"  One  or more: For list<T> (many).
        ============  ==================== ===================================

.. _behave: http://pypi.python.org/pypi/behave
.. _parse:  http://pypi.python.org/pypi/parse
.. _parse_type: https://github.com/jenisys/parse_type
.. _string.format: http://docs.python.org/library/string.html#format-string-syntax
