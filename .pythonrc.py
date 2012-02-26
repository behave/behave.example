#!/usr/bin/env python
#=============================================================================
# PROJECT-SPECIFIC: Setup PYTHONPATH
#=============================================================================
# AUTHOR:    Jens Engel
# LANGUAGE:  Python >= 2.5
# ENVIRONMENT: Multi-Environment (Win32, Cygwin, UNIX).
# DESCRIPTION:
#    This file provides a project-specific pyth init for Python.
#
#=============================================================================
#           COPYRIGHT (c) 2010 by Jens Engel, ALL RIGHTS RESERVED
#=============================================================================

# -- IMPORTS:
import os.path
import sys

HERE  = os.path.dirname(__file__)
HEREA = os.path.abspath(HERE)
PYTHONPATH = [
    os.curdir,
    os.path.normpath(HEREA),
    os.path.normpath(os.path.join(HEREA, "tests")),
]

if os.path.exists(PYTHONPATH[0]) and PYTHONPATH[0] not in sys.path:
    # -- SETUP SEARCH PATH for PROJECT:
    sys.path = PYTHONPATH + sys.path
