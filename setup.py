# -*- coding: utf-8 -*-
import os.path
import sys

# -- AUTO-DISCOVER: paver-minilib.zip
for searchpath in (".", "bin"):
    paver_minilib_zip = os.path.join(searchpath, "paver-minilib.zip")
    if os.path.exists(paver_minilib_zip):
        sys.path.insert(0, paver_minilib_zip)
        break

# -- SETUP-MAIN:
import paver.tasks
paver.tasks.main()
