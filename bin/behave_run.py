#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# =============================================================================
# REUSE LOCAL BEHAVE, if available
# =============================================================================

import os.path
import sys

# ----------------------------------------------------------------------------
# SETUP PATHS:
# ----------------------------------------------------------------------------
# HERE = os.path.dirname(sys.argv[0])
HERE = os.path.dirname(__file__)
BEHAVE_HOME = os.path.normpath(os.path.join(HERE, "..", "..", "behave"))
BEHAVE_HOME = os.path.abspath(BEHAVE_HOME)

DEBUG = False
if DEBUG:
    print "BEHAVE: HERE=%s" % HERE
    print "BEHAVE: BEHAVE_HOME=%s" % BEHAVE_HOME

if os.path.isdir(BEHAVE_HOME):
    sys.path.insert(0, os.path.abspath(os.path.join(BEHAVE_HOME)))

# ----------------------------------------------------------------------------
# PREPARE BEHAVE:
# ----------------------------------------------------------------------------
from behave.formatter.pretty1 import Pretty1AsPrettyFormatter
from behave.formatter.pretty1 import SimplePrettyAsPrettyFormatter
from behave.reporter.summary import SummaryReporter
from behave.formatter import ansi_escapes

def monkeypatch_behave():
    """
    Apply patches to "behave" to make documenation runs work.
    """
    SummaryReporter.use_output_stream = "stdout"  #< BETTER: For examples.
    ansi_escapes.colors["grey"] = ansi_escapes.colors["blue"]

if __name__ == "__main__":
    from behave.__main__ import main
    from behave.reporter.summary import SummaryReporter
    from behave.formatter import ansi_escapes
    from behave.formatter import formatters
    monkeypatch_behave()
    formatters.register(Pretty1AsPrettyFormatter)
    # XXX formatters.register(SimplePrettyAsPrettyFormatter)
    sys.exit(main())
