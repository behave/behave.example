# -*- coding: UTF-8 -*
"""
Setup script for behave.example

USAGE:
    python setup.py install
    python setup.py behave_test     # -- XFAIL on Windows (currently).
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
description = """\
Some tutorials and examples to explore behave, a BDD test tool for Python.
"""

# -----------------------------------------------------------------------------
# SETUP:
# -----------------------------------------------------------------------------
setup(
    name="behave.example",
    version="1.2.7",
    url="https://github.com/behave/behave.example",
    author="Jens Engel",
    author_email="Jens_Engel@nowhere.net",
    license="BSD",
    description= description,
    keywords   = "utility",
    platforms  = [ 'any' ],
    # -- REQUIREMENTS:
    # SUPPORT: python2.7, python3.3 (or higher)
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*",
    install_requires=[
        "behave>=1.2.6",
        # -- BEHAVE EXAMPLES REQUIRE:
        "PyHamcrest>=1.9",
        "parse>=1.8.2",
        "parse_type>=0.4.2",
        "six>=1.11.0",
        # -- BEHAVE EXAMPLE DOCS REQUIRE:
        # "Sphinx>=1.6,<2.0",
        # "sphinx_bootstrap_theme >= 0.4.12",
        # "sphinxcontrib-ansi",   # >= 0.6",
        # "sphinxcontrib-programoutput >=0.8,<0.10.0",
    ],
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
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
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
