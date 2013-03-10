#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# =============================================================================
# REUSE LOCAL BEHAVE, if available
# =============================================================================

import os.path
import sys

DEBUG = False
USE_COLOCATED_BEHAVE = False

# ----------------------------------------------------------------------------
# SETUP PATHS:
# ----------------------------------------------------------------------------
# HERE = os.path.dirname(sys.argv[0])
HERE = os.path.dirname(__file__)
PYTHON_LIBDIR = os.path.normpath(os.path.join(HERE, "..", "lib",
        "python%s" % sys.version_info[0] ))
BEHAVE_ZIP  = os.path.join(PYTHON_LIBDIR, "behave.zip")
BEHAVE_HOME = os.path.normpath(os.path.join(HERE, "..", "..", "behave"))

if DEBUG:
    print "BEHAVE: HERE=%s" % HERE
    print "BEHAVE: BEHAVE_HOME=%s" % BEHAVE_HOME

# -- LOCAL-PATH-SETUP: Use local libs if possible.
if os.path.isdir(PYTHON_LIBDIR):
    sys.path.insert(0, os.path.abspath(PYTHON_LIBDIR))
if os.path.exists(BEHAVE_ZIP):
    # sys.stdout.write("USING-BUNDLE: %s\n" % os.path.basename(BEHAVE_ZIP))
    if DEBUG: sys.stdout.write("USING-BUNDLE: %s\n" % BEHAVE_ZIP)
    sys.path.insert(0, os.path.realpath(BEHAVE_ZIP))
if USE_COLOCATED_BEHAVE and os.path.isdir(BEHAVE_HOME):
    if DEBUG: sys.stdout.write("USING-LOCAL: %s\n" % BEHAVE_HOME)
    sys.path.insert(0, os.path.abspath(os.path.join(BEHAVE_HOME)))

# ----------------------------------------------------------------------------
# BEHAVE-PATCHES:
# ----------------------------------------------------------------------------
# from behave.formatter.pretty1 import SimplePrettyAsPrettyFormatter
from behave.formatter.pretty1 import Pretty1AsPrettyFormatter
from behave.reporter.summary import SummaryReporter
from behave.formatter import ansi_escapes
from behave.formatter import formatters

def monkeypatch_behave():
    """
    Apply patches to "behave" to make documenation runs work.
    """
    SummaryReporter.use_output_stream = "stdout"  #< BETTER: For examples.
    ansi_escapes.colors["grey"] = ansi_escapes.colors["white"]
    ansi_escapes.use_ansi_escape_colorbold_composites()
    formatters.register(Pretty1AsPrettyFormatter)

# ----------------------------------------------------------------------------
# MAIN:
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    from behave.__main__ import main
    monkeypatch_behave()
    sys.exit(main())
