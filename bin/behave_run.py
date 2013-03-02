#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# =============================================================================
# REUSE LOCAL BEHAVE, if available
# =============================================================================

import os.path
import sys

DEBUG = False
USE_LOCAL_BEHAVE = False

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
if USE_LOCAL_BEHAVE and os.path.isdir(BEHAVE_HOME):
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

def use_ansi_escape_colorbold_composites():
    """
    Patch for "sphinxcontrib-ansi" to process the following ANSI escapes
    correctly (set-color set-bold sequences):

        ESC[{color}mESC[1m  => ESC[{color};1m

    Reapply aliases to ANSI escapes mapping.
    """
    colors  = ansi_escapes.colors
    aliases = ansi_escapes.aliases
    color_codes = {}
    for color_name, color_escape in colors.items():
        color_code = color_escape.replace(u"\x1b[", u"").replace(u"m", u"")
        color_codes[color_name] = color_code

    for alias in aliases:
        parts = [ color_codes[c] for c in aliases[alias].split(',') ]
        # DIAG: print "alias {0}: {1}:".format(alias, ";".join(parts))
        composite_escape = u"\x1b[{0}m".format(u";".join(parts))
        ansi_escapes.escapes[alias] = composite_escape

        arg_alias = alias + '_arg'
        arg_seq = aliases.get(arg_alias, aliases[alias] + ',bold')
        parts = [ color_codes[c] for c in arg_seq.split(',') ]
        # DIAG: print "alias {0}: {1}:".format(arg_alias, ";".join(parts))
        composite_escape = u"\x1b[{0}m".format(u";".join(parts))
        ansi_escapes.escapes[arg_alias] = composite_escape

def monkeypatch_behave():
    """
    Apply patches to "behave" to make documenation runs work.
    """
    SummaryReporter.use_output_stream = "stdout"  #< BETTER: For examples.
    ansi_escapes.colors["grey"] = ansi_escapes.colors["white"]
    use_ansi_escape_colorbold_composites()
    formatters.register(Pretty1AsPrettyFormatter)

# ----------------------------------------------------------------------------
# MAIN:
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    from behave.__main__ import main
    monkeypatch_behave()
    sys.exit(main())
