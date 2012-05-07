# ============================================================================
# PAVER MAKEFILE (pavement.py) -- behave.example
# ============================================================================
# REQUIRES: paver >= 1.0.5
# DESCRIPTION:
#   Provides platform-neutral "Makefile" for simple, project-specific tasks.
#
# USAGE:
#   paver TASK [OPTIONS...]
#   paver help           -- Show all supported commands/tasks.
#   paver clean          -- Cleanup project workspace.
#   paver test           -- Run all tests (unittests, examples).
#
# SEE ALSO:
#  * http://pypi.python.org/pypi/Paver/
#  * http://www.blueskyonmars.com/projects/paver/
# ============================================================================

from paver.easy import *
from paver.setuputils import setup, install_distutils_tasks
# NOT-USED: import paver.doctools
# -- PAVER-EXTENSIONS: More tasks and utilities...
from paver_ext.python_requirements import read_requirements
from paver_ext.pip_download import download_depends, localpi
from paver_ext.python_checker import pychecker, pylint

install_distutils_tasks()


# -- REQUIRED-FOR: setup, sdist, ...
# NOTE: Adds a lot more python-project related tasks.
install_distutils_tasks()
sys.path.insert(0, ".")

# ----------------------------------------------------------------------------
# PROJECT CONFIGURATION (for sdist/setup mostly):
# ----------------------------------------------------------------------------
NAME    = "behave.example"
VERSION = open("VERSION.txt").read().strip()
DESCRIPTION = """\
Some tutorials and examples to explore behave, a cucumber clone for Python.
"""

CLASSIFIERS = """\
Development Status :: 4 - Beta
Environment :: Console
Framework :: behave
Intended Audience :: Developers
License :: OSI Approved :: BSD License
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Topic :: Software Development :: Testing
Topic :: Documentation
Topic :: Education
"""

INSTALL_REQUIRES = read_requirements("requirements.txt")


# ----------------------------------------------------------------------------
# TASK CONFIGURATION:
# ----------------------------------------------------------------------------
options(
    setup= dict(
        name= NAME,
        version= VERSION,
        url="http://pypi.python.org/pypi/%s/" % NAME,
        author="Jens Engel",
        author_email="Jens_Engel@nowhere.net",
        license="BSD",
        description= DESCRIPTION,
        keywords   = "utility",
        platforms  = [ 'any' ],
        classifiers= CLASSIFIERS.splitlines(),
        install_requires= INSTALL_REQUIRES,
        include_package_data= True,
    ),
    sphinx=Bunch(
        docroot="docs",
        sourcedir=".",
        builddir="../build/docs"
    ),
    minilib=Bunch(
        extra_files=[ 'doctools', 'virtual' ]
    ),
    develop=Bunch(
        requirements_files=[
            "requirements.txt",
        ],
        download_dir="downloads",
    ),
    test=Bunch(
        default_args=[ "features/" ]
    ),
    pychecker = Bunch(
        default_args=NAME
    ),
    pylint = Bunch(
        default_args=NAME
    )
)

# ----------------------------------------------------------------------------
# TASKS:
# ----------------------------------------------------------------------------
@task
def init():
    """Initialze workspace."""
    path("build").makedirs()

@task
@consume_args
def docs(args):
    """Generate the documentation: html, pdf, ... (default: html)"""
    builders = args
    if not builders:
        builders = [ "html" ]
    for builder in builders:
        sphinx_build(builder)

@task
def linkcheck():
    """Check hyperlinks in HTML-based documentation."""
    sphinx_build("linkcheck")

@task
@consume_args
def docs_save(args):
    """Update the local documentation under docs.html/"""
    info("STEP: Generate docs in HTML format")
    if args and "html" not in args:
        args.append("html")
    call_task("docs")

    info("STEP: Save docs under docs.html/")
    docs_save = path("docs.html")
    docs_save.rmtree()
    path("build/docs/html").copytree(docs_save)

    # -- POST-PROCESSING: Polish up.
    for part in [ ".buildinfo", ".doctrees" ]:
        partpath = docs_save / part
        if partpath.isdir():
            partpath.rmtree()
        else:
            partpath.remove()

# ----------------------------------------------------------------------------
# TASK: test
# ----------------------------------------------------------------------------
@task
@consume_args
@needs("init")
def test(args):
    """Execute tests with behave"""
    if not args:
        args = options.test.default_args
    for arg in args:
        behave(arg)


# ----------------------------------------------------------------------------
# TASK: clean
# ----------------------------------------------------------------------------
@task
def clean():
    """Cleanup the project workspace."""

    # -- STEP: Remove build directories.
    path("build").rmtree()
    path("dist").rmtree()
    path("test_results").rmtree()
    path(".tox").rmtree()

    # -- STEP: Remove temporary directory subtrees.
    patterns = [
        "*.egg-info",
        "__pycache__",
    ]
    for pattern in patterns:
        dirs = path(".").walkdirs(pattern, errors="ignore")
        for d in dirs:
            d.rmtree()

    # -- STEP: Remove files.
    path(".coverage").remove()
    path("paver-minilib.zip").remove()

    # -- STEP: Remove temporary files.
    patterns = [
        "*.pyc", "*.pyo", "*$py.class",
        "*.bak", "*.log", "*.tmp",
        ".coverage", ".coverage.*",
        "pylint_*.txt", "pychecker_*.txt",
        ".DS_Store", "*.~*~",   #< MACOSX
    ]
    for pattern in patterns:
        files = path(".").walkfiles(pattern)
        for f in files:
            f.remove()

@task
def clean_all():
    """Clean everything.."""
    # -- ORDERING: Is important
    path("downloads").rmtree()

    # -- MORE: Use normal cleanings, too.
    call_task("clean")

# ----------------------------------------------------------------------------
# UTILS:
# ----------------------------------------------------------------------------
BEHAVE = "behave"

def python(cmdline, cwd="."):
    """Execute a python script by using the current python interpreter."""
    return sh("%s %s" % (sys.executable, cmdline), cwd=cwd)

def behave(args, options=""):
    """Run the behave command"""
    return sh("{behave} {options} {args}".format(
                behave=BEHAVE, options=options, args=args))

def sphinx_build(builder="html", cmdopts=None):
    if not cmdopts:
        # -- REQUIRED-FOR: sphinxcontrib-programoutput
        # Invalidate Sphinx cache
        # SEE ALSO: https://bitbucket.org/birkenfeld/sphinx-contrib (issues)
        cmdopts = "-E"
    sourcedir = options.sphinx.sourcedir
    destdir   = options.sphinx.builddir
    cmd = "sphinx-build {opts} -b {builder} {sourcedir} {destdir}/{builder}" \
            .format(builder=builder, sourcedir=sourcedir, destdir=destdir,
                    opts=cmdopts)
    sh(cmd, cwd=options.sphinx.docroot)
