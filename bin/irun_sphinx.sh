#!/bin/sh
# ==========================================================================
# INCREMENTAL SPHINX-BUILD
# ==========================================================================
# BASED-ON: http://jacobian.org/writing/auto-building-sphinx/
# REQUIRES: watchdog, for watchmedo
# DESCRIPTION:
#  Runs sphinx-build incrementally when files change.
#
# ==========================================================================
# watchmedo shell-command \
#    --patterns='*.rst;*.py' \
#    --ignore-pattern='docs/build/*;*flymake*' \
#    --recursive \
#    --command='python setup.py build_sphinx'
#    --ignore-directories \

set -x
FOCUS_ON_DIRS="docs *features datatype.features step_matcher.features"

watchmedo shell-command \
    --patterns='*.rst;*.py;*.feature' \
    --ignore-pattern='build/*;.tox/*;__WORKDIR__/*;paver_ext/*' \
    --recursive --timeout=3 --wait \
    --command='paver docs' ${FOCUS_ON_DIRS}

#    --command='echo "${watch_src_path}"' ${FOCUS_ON_DIRS}
