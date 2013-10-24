#!/bin/sh
# =============================================================================
# BOOTSTRAP PROJECT: Download all requirements
# =============================================================================
# test ${PIP_DOWNLOADS_DIR} || mkdir -p ${PIP_DOWNLOADS_DIR}
# tox -e init

set -e

# -- CONFIGURATION:
HERE=`dirname $0`
TOP="${HERE}/.."
: ${PIP_INDEX_URL="http://pypi.python.org/simple"}
: ${PIP_DOWNLOAD_DIR:="${TOP}/downloads"}
export PIP_INDEX_URL PIP_DOWNLOADS_DIR

# -- EXECUTE STEPS:
${HERE}/toxcmd.py mkdir ${PIP_DOWNLOAD_DIR}
pip install --use-mirrors --download=${PIP_DOWNLOAD_DIR} -r ${TOP}/requirements.txt
${HERE}/make_localpi.py ${PIP_DOWNLOAD_DIR}

