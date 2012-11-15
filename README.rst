behave.example: Examples and Tutorials
==============================================================================

:Date: 2012-11-13
:Category: BDD, testing
:License:  BSD

`behave`_ is a BDD test framework and cucumber-clone for Python.
This project provides tutorials and examples how to use `behave`_.
It should extend the otherwise excellent document of `behave`_.


SEE ALSO:
  * https://github.com/jenisys/behave.example
  * behave:  http://pypi.python.org/pypi/behave/
  * cucumber: http://cukes.info/

DOCUMENTATION:
  * http://jenisys.github.com/behave.example (latest version)

REPOSITORIES:
  * https://github.com/jeamland/behave (master)
  * https://github.com/jenisys/behave
  * https://github.com/jenisys/parse


.. _behave: https://github.com/jeamland/behave
.. _parse:  https://github.com/jenisys/parse
.. _`jenisys/behave`: https://github.com/jenisys/behave
.. _`jenisys/parse`:  https://github.com/jenisys/parse
.. _paver: http://www.blueskyonmars.com/projects/paver/
.. _sphinxcontrib-ansi: http://bitbucket.org/birkenfeld/sphinx-contrib
.. _sphinxcontrib-programoutput: https://github.com/lunaryorn/sphinxcontrib-programoutput


INSTALL
------------------------------------------------------------------------------

The project provides only examples. Therefore, it should not be installed.
To prepare the local installation, use the following command to install
all prerequisites::

    pip install -r requirements.txt

Note that some new and experimental features/extensions of `behave`_ and
`parse`_ are currently used here. These features are not part of the official
distributions (and repositories), yet.

Use the `jenisys/behave`_ and `jenisys/parse`_ variants, if you want
to run the ``*.feature`` files provided here.
Snapshots of the `jenisys/behave`_ and `jenisys/parse`_ implementations
are provided in the directory ``lib/python2/``.  This directory is
automatically used when you use ``bin/behave`` to run `behave`_.


HOWTO
------------------------------------------------------------------------------

Cleanup local workspace::

    paver clean

Run `behave`_ tests::

    paver test

or::

    bin/behave features/
    bin/behave datatype.features/
    bin/behave step_matcher.features/


Build Sphinx-based documentation with tutorials::

    paver docs

If `paver`_ is not installed, use the following canned script instead::

    bin/paver command ...


SPECIAL:
------------------------------------------------------------------------------

* The `behave`_ PrettyFormatter formatter is replaced with Pretty1Formatter.

  This formatter implementation avoids cursor-ups while processing steps.
  ANSI escape cursor-up sequences do not work with `sphinxcontrib-ansi`_
  when the sphinx-based documentation is generated
  (experimental feature for colorized behave output support).

*  An adapted version of the SummaryReporter is used to select
   SummaryReporter.use_output_stream = "stdout".
   This improves output generation with `sphinxcontrib-programoutput`_,
   actually the subprocess.call() functionality with mixed
   stdout/stderr output collection.

* A patched version of `sphinxcontrib-ansi`_ is needed to overcome problems
  with the coloring schema in `behave`_. An alternative is to replace the
  usage of the color "grey" in styles "executing", "coments",
  by setting the environment variable::

    GHERKIN_COLORS="executing=white:comments=white"

* To disable "ANSI coloring" support for Sphinx, for example on Windows,
  set "ansiterm_supported = False" in "docs/conf.py".


KNOWN PROBLEMS
------------------------------------------------------------------------------

* `sphinxcontrib-ansi`_ does not process the following ANSI sequences
  correctly (set-color, set-bold):

    CSI{color}mCSI1m

  The color is reset in HTML output when set-bold is detected.
