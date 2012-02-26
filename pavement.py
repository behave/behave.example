# ============================================================================
# PAVER MAKEFILE (pavement.py)
# ============================================================================
# REQUIRES: paver >= 1.0.3
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
        # XXX long_description = ""
        keywords   = "utility",
        platforms  = [ 'any' ],
        classifiers= CLASSIFIERS.splitlines(),
        install_requires= INSTALL_REQUIRES,
        # extra_requires= read_requirements("requirements-develop.txt"),
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
    test=Bunch(
        default_args=[ "features/" ]
    ),
    pychecker = Bunch(
        default_dirs=[ "features/" ]
    ),
    pylint = Bunch(
        default_dirs=[ "features/" ]
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
def docs_html():
    """Generate the HTML-based documentation."""
    # XXX call_task("prepare_docs")
    sphinx_build("html")

@task
def docs_pdf():
    """Generate the PDF-based documentation."""
    sphinx_build("pdf")
    # sh("make -C docs pdf")

@task
def docs():
    """Generate the documentation."""
    call_task("docs_html")

@task
@needs("docs_html")
def docs_save():
    """Update the local documentation under docs.html/"""
    # info("STEP: Generate docs in HTML format")
    # call_task("docs_html")

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
def test(args):
    """Execute tests with behave"""
    if not args:
        args = options.test.default_args
    for arg in args:
        behave(arg)

# ----------------------------------------------------------------------------
# TASK: test coverage
# ----------------------------------------------------------------------------
#@task
#def coverage_report():
#    """Generate coverage report from collected coverage data."""
#    sh("coverage combine")
#    sh("coverage report")
#    sh("coverage html")
#    # -- DISABLED: sh("coverage xml")
#
#@task
#@consume_args
#def coverage(args):
#    """Execute all tests to collect code-coverage data, generate report."""
#    tests = " ".join(args)
#    sh("coverage run bin/pytest.py --cov=%s %s" % (NAME, tests),
#       ignore_error=True)   #< Show coverage-report even if tests fail.
#    call_task("coverage_report")
#

# ----------------------------------------------------------------------------
# TASK: pychecker, pylint
# ----------------------------------------------------------------------------
@task
@consume_args
def pylint(args):
    """Run pylint on sources."""
    if not args:
        args = []
        for dir_ in options.pylint.default_dirs:
            args.extend(path(dir_).walkfiles("*.py"))
    cmdline = " ".join(args)
    sh("pylint --rcfile=.pylintrc %s" % cmdline, ignore_error=True)

@task
@consume_args
def pychecker(args):
    """Run pychecker on sources."""
    if not args:
        args = []
        for dir_ in options.pylint.default_dirs:
            args.extend(path(dir_).walkfiles("*.py"))
    for file_ in args:
        cmdline = file_
        sh("pychecker --config=.pycheckrc %s" % cmdline, ignore_error=True)

# ----------------------------------------------------------------------------
# TASK: bump_version
# ----------------------------------------------------------------------------
#@task
#def bump_version(info, error):
#    """Update VERSION.txt"""
#    try:
#        from xxx.version import VERSION
#        info("VERSION: %s" % VERSION)
#        file_ = open("VERSION.txt", "w+")
#        file_.write("%s\n" % VERSION)
#        file_.close()
#    except StandardError, e:
#        error("Update VERSION.txt FAILED: %s" % e)

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
        "*.pyc", "*.pyo", "*.bak", "*.log", "*.tmp",
        ".coverage", ".coverage.*",
        ".DS_Store", "*.~*~",   #< MACOSX
    ]
    for pattern in patterns:
        files = path(".").walkfiles(pattern)
        for f in files:
            f.remove()


# ----------------------------------------------------------------------------
# PLATFORM-SPECIFIC TASKS: win32
# ----------------------------------------------------------------------------
#if sys.platform == "win32":
#    @task
#    @consume_args
#    def py2exe(args):
#        """Run py2exe to build a win32 executable."""
#        cmdline = " ".join(args)
#        python("setup_py2exe.py py2exe %s" % cmdline)
#
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
