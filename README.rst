behave.example: Examples and Tutorials
==============================================================================

:Date: 2016-10-22
:Category: BDD, testing
:License:  BSD

`behave`_ is a BDD test framework and cucumber-clone for Python.
This project provides tutorials and examples how to use `behave`_.
It should extends the excellent documentation of `behave`_.

SEE ALSO:
  * https://github.com/behave/behave.example
  * behave:  http://pypi.python.org/pypi/behave/
  * cucumber: http://cucumber.io/

DOCUMENTATION:
  * http://behave.github.com/behave.example (latest version)

REPOSITORIES:
  * https://github.com/behave/behave
  * https://github.com/behave/parse_type


.. _behave: https://github.com/behave/behave
.. _parse_type:  https://github.com/jenisys/parse_type
.. _invoke: http://www.pyinvoke.org
.. _sphinxcontrib-ansi: http://bitbucket.org/birkenfeld/sphinx-contrib
.. _sphinxcontrib-programoutput: https://github.com/lunaryorn/sphinxcontrib-programoutput


INSTALL
------------------------------------------------------------------------------

The project provides tutorials and examples.
Therefore, it should not be installed.
To prepare the local installation, use the following command to install
all prerequisites::

    pip install -r requirements.txt

Snapshots of the `behave`_ and `parse_type`_ implementations
are provided in the directory ``lib/python/``.  This directory is
automatically used when you use ``bin/behave`` to run `behave`_.


HOWTO
------------------------------------------------------------------------------

Cleanup local workspace::

    invoke clean

Run `behave`_ tests::

    invoke test

or::

    bin/behave features/
    bin/behave datatype.features/
    bin/behave step_matcher.features/


Build Sphinx-based documentation with tutorials::

    invoke docs

If `invoke`_ is not installed, use the following canned script instead::

    bin/invoke command ...


SPECIAL CONFIGURATION
------------------------------------------------------------------------------

* The `behave`_ PrettyFormatter is replaced with ``pretty2.SimplePrettyFormatter``.

  This formatter implementation avoids cursor-ups while processing steps.
  ANSI escape cursor-up sequences do not work with `sphinxcontrib-ansi`_
  when the sphinx-based documentation is generated
  (experimental feature for colorized behave output support).

* `sphinxcontrib-ansi`_ does not process the following ANSI escape sequences
  correctly (set-color, set-bold)::

    CSI{color_code}mCSI1m

  The color is reset in HTML output when set-bold is detected.
  The following ANSI escape sequence should be used instead::

    CSI{color_code};1m

  The behave runner, that is used here, patches the original functionality
  to use the second solution ("use_ansi_escape_colorbold_composites()").

* The coloring schema in `behave`_ is adapted by setting the environment
  variable ("grey" is replaced with "white")::

    GHERKIN_COLORS="executing=white:comments=white"

* To disable "ANSI coloring" support for Sphinx,
  set "ansiterm_supported = False" in "docs/conf.py".
  Note that this is not necessary on Windows.
