behave.example: Examples and Tutorials
==============================================================================

:Date: 2012-01-28
:Category: BDD, testing
:License:  BSD

``behave`` is a BDD test framework and cucumber-clone for Python.
This project provides tutorials and examples how to use ``behave``.
It should extend the otherwise excellent document of ``behave``.


SEE ALSO:
  * behave:  http://pypi.python.org/pypi/behave/
  * cucumber: http://cukes.info/

REPOSITORIES:
  * https://github.com/jeamland/behave (master)
  * https://github.com/jenisys/behave

DOCUMENTATION:
  * http://jenisys.github.com/behave.example (latest version)


INSTALL
------------------------------------------------------------------------------

The project provides only examples. Therefore, it should not be installed.
To prepare the local installation, use the following command to install
all prerequisites::

    pip install -r requirements.txt


HOWTO
------------------------------------------------------------------------------

Cleanup local workspace::

    paver clean

Run ``behave`` tests::

    paver test

or::

    behave features/


Build Sphinx-based documentation with tutorials::

    paver docs

If ``paver`` is not installed, use the following canned script instead::

    bin/paver command ...

