#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PROJECT WORKSPACE-SPECIFIC SETUP:
---------------------------------

Adds project-specific local packages under library path as site-package dir.
See also :py:module:`site`.

REQUIREMENTS:
  * Must be colocated to the scripts in "bin/" directory to simplify import.
"""

# from __future__ import print_function
import os.path
import sys

# ----------------------------------------------------------------------------
# PROJECT-SPECIFIC PATHS:
# ----------------------------------------------------------------------------
py_version_major = sys.version_info[0]
HERE = os.path.dirname(__file__)
TOPA = os.path.abspath(os.path.join(HERE, ".."))
PYTHON_LIBDIR  = os.path.join(TOPA, "lib", "python%s" % py_version_major)

def print_(text):
    sys.stdout.write(text + "\n")

DEBUG = False
if DEBUG:
    print_("usercustomize: Use PYTHON_LIBDIR=%s" % PYTHON_LIBDIR)

# ----------------------------------------------------------------------------
# SETUP PATH UTILS:
# ----------------------------------------------------------------------------
def project_workspace_addsitedir(sitedir):
    """
    Similar to site.addsitedir() but prefers new sitedir over existing ones.
    Therefore, prefers local packages over installed packages.

    .. note::
        This allows to support *.pth files and zip-/egg-imports
        similar to an installed site-packages directory.
    """
    assert os.path.isdir(sitedir)
    try:
        from site import addsitedir
    except ImportError:
        # -- USE: Python2.7 site.py package
        from pysite import addsitedir
    next_package_pos = len(sys.path)
    addsitedir(sitedir)

    # -- POST-PROCESS: Move new packages from end to begin of sys.path list.
    pos = 0
    new_packages = sys.path[next_package_pos:]
    del sys.path[next_package_pos:]
    sys.path[pos:pos] = new_packages


# ----------------------------------------------------------------------------
# SETUP PATHS:
# ----------------------------------------------------------------------------
if os.path.isdir(PYTHON_LIBDIR):
    project_workspace_addsitedir(PYTHON_LIBDIR)
sys.path.insert(0, TOPA)

# ----------------------------------------------------------------------------
# DIAGNOSTIC MAIN:
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    print_("sys.path[%d]:" % len(sys.path))
    for index, p in enumerate(sys.path):
        print_("  %3d  %s" % (index, p))
