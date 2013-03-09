# ============================================================================
# PAVER MAKEFILE (pavement.py) -- behave.example
# ============================================================================
# REQUIRES: paver >= 1.2
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
sys.path.insert(0, ".")

# -- PAVER-EXTENSIONS: More tasks and utilities...
# NOT-USED: import paver.doctools
from paver.setuputils import setup, install_distutils_tasks
from paver_ext.python_requirements import read_requirements
from paver_ext.pip_download import download_depends, localpi
from paver_ext.python_checker import pychecker, pylint
from paver_ext import paver_require, paver_patch

paver_require.min_version("1.2")
paver_patch.ensure_path_with_pmethods(path)
paver_patch.ensure_path_with_smethods(path)

# -- REQUIRED-FOR: setup, sdist, ...
# NOTE: Adds a lot more python-project related tasks.
install_distutils_tasks()


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
    develop=Bunch(
        requirements_files=[
            "requirements.txt",
        ],
        # download_dir="downloads",
        download_dir= path("$HOME/.pip/downloads").expandvars(),
    ),
    test=Bunch(
        default_args=[
            "features/",
            "datatype.features/",
            "step_matcher.features/",
        ],
        behave_cmdopts = "--tags=-@xfail",
        behave_formatter = "progress",
    ),
    pychecker = Bunch(default_args=NAME),
    pylint    = Bunch(default_args=NAME),
    sphinx=Bunch(
        # docroot=".",
        sourcedir= "docs",
        destdir  = "../build/docs"
    ),
    minilib=Bunch(
        extra_files=[ 'doctools', 'virtual' ]
    ),
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
            partpath.rmtree_p()
        else:
            partpath.remove_p()

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
    behave_cmdopts = "-f {formatter} {opts}".format(
        formatter=options.test.behave_formatter,
        opts=options.test.behave_cmdopts,
    )

    for arg in args:
        behave(arg, options=behave_cmdopts)


# ----------------------------------------------------------------------------
# TASK: clean
# ----------------------------------------------------------------------------
@task
def clean():
    """Cleanup the project workspace."""

    # -- STEP: Remove build directories.
    path("build").rmtree_s()
    path("dist").rmtree_s()
    path("test_results").rmtree_s()
    path(".tox").rmtree_s()

    # -- STEP: Remove temporary directory subtrees.
    patterns = [
        "*.egg-info",
        ".cache",       #< py.test cache directory.
        "__pycache__",  #< Python compiled objects cache.
    ]
    for pattern in patterns:
        dirs = path(".").walkdirs(pattern, errors="ignore")
        for d in dirs:
            d.rmtree()

    # -- STEP: Remove files.
    path(".coverage").remove_s()
    path("paver-minilib.zip").remove_s()

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
    """Clean everything, like in newly installed state."""
    path("downloads").rmtree_s()

    # -- MORE: Use normal cleanings, too.
    call_task("clean")

# ----------------------------------------------------------------------------
# UTILS:
# ----------------------------------------------------------------------------
HERE   = path(__file__).dirname()
BEHAVE = HERE.joinpath("bin/behave")
if sys.platform == "win32":
    BEHAVE = path(BEHAVE).normpath()

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
    destdir   = options.sphinx.destdir
    command = "sphinx-build {opts} -b {builder} . {destdir}/{builder}" \
            .format(builder=builder, sourcedir=sourcedir, destdir=destdir,
                    opts=cmdopts)
    sh(command, cwd=sourcedir)
