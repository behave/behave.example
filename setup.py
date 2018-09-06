# -*- coding: utf-8 -*
"""
Setup script for behave.example

USAGE:
    python setup.py install
    python setup.py behave_test     # -- XFAIL on Windows (currently).
    python setup.py nosetests
"""

import sys
import os.path

HERE0 = os.path.dirname(__file__) or os.curdir
os.chdir(HERE0)
HERE = os.curdir
sys.path.insert(0, os.path.abspath(HERE))

from setuptools import find_packages, setup
# -- PREPARED: from setuptools_behave import behave_test


# -----------------------------------------------------------------------------
# CONFIGURATION:
# -----------------------------------------------------------------------------
# REQUIRES: behave >= 1.2.6
python_version = float("%s.%s" % sys.version_info[:2])
requirements = [
    "behave>=1.2.6",
    "parse>=1.8.2", "parse_type>=0.4.2", "six>=1.11.0",
]
docs_requirements = [
    "Sphinx>=1.6",
    "sphinx_bootstrap_theme >= 0.4.12",
    "sphinxcontrib-ansi >= 0.6",
    "sphinxcontrib-programoutput >= 0.8",
    "PyHamcrest>=1.9",
]

# -- BEHAVE REQUIREMENTS:
behave_requirements = []
# -- DROP SUPPORT FOR: Python2.6 (soon)
if python_version < 2.7 or 3.0 <= python_version <= 3.1:
    behave_requirements.append("argparse")
if python_version < 2.7:
    behave_requirements.append("importlib")
    behave_requirements.append("ordereddict")

requirements.extend(docs_requirements)
requirements.extend(behave_requirements)

description = """\
Some tutorials and examples to explore behave, a BDD test tool for Python.
"""

# INSTALL_REQUIRES = read_requirements("requirements.txt")
INSTALL_REQUIRES = requirements

# -----------------------------------------------------------------------------
# SETUP:
# -----------------------------------------------------------------------------
setup(
    name="behave.example",
    version="1.2.6",
    url="http://github.com/behave/behave.example",
    author="Jens Engel",
    author_email="Jens_Engel@nowhere.net",
    license="BSD",
    description= description,
    keywords   = "utility",
    platforms  = [ 'any' ],
    install_requires= INSTALL_REQUIRES,
    include_package_data= True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Framework :: behave",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Testing",
        "Topic :: Documentation",
        "Topic :: Education",
    ],
    zip_safe = True,
    # -- PREPARED:
    # cmdclass = {
    #    "behave_test": behave_test,
    # },
)
