#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Provides a paver script when paver is not installed.
Use the provided "paver-minilib.zip" distribution instead.
"""

import os.path
import sys

HERE = os.path.dirname(sys.argv[0])
PAVER_MINILIB_ZIP = os.path.join(HERE, "paver-minilib.zip")

try:
    import paver
except ImportError:
    if os.path.exists(PAVER_MINILIB_ZIP):
        sys.stdout.write("USING-BUNDLE: %s\n" % os.path.basename(PAVER_MINILIB_ZIP))
        sys.path.insert(0, os.path.realpath(PAVER_MINILIB_ZIP))

if __name__ == '__main__':
    import paver.tasks
    paver.tasks.main()
