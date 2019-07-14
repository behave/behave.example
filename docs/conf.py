# -*- coding: UTF-8 -*-
# =============================================================================
# SPHINX CONFIGURATION FOR: behave.example docs
# =============================================================================
# SPHINX EXTENSIONS:
#  * https://github.com/sphinx-contrib
#    (former: https://bitbucket.org/birkenfeld/sphinx-contrib )
#  * http://packages.python.org/sphinxcontrib-programoutput/  (OLD)
#  * https://github.com/NextThought/sphinxcontrib-programoutput (NEW)
#
#  * https://github.com/sphinx-contrib/ansi
#  * https://github.com/jenisys/sphinxcontrib-ansi (v0.6.1: Fix setup.py README)
#
# .. program-output:: command
#   :ellipsis: 2,-2
#   :ellipsis: 2
#   :returncode: 1
#   :shell:
#
# .. command-output:: command-with-prompt
#
# programoutput_prompt_template = "$ {command}\n{output}"
# programoutput_use_ansi = False
# =============================================================================
# RELATED:
#   ansi
#   autorun
## -------------------------------
# https://pypi.org/project/sphinxjp.themes.dotted/0.1.1
# https://github.com/shkumagai/sphinxjp.themes.dotted
# =============================================================================

from __future__ import print_function
import os.path
import sys


# -----------------------------------------------------------------------------
# SETUP PATH: Needed for sphinxcontrib-programoutput
# -----------------------------------------------------------------------------
# -- SETUP PATH: Needed by sphinxcontrib-programoutput (commands)
HERE  = os.path.dirname(__file__)
TOPDIR = os.path.normpath(os.path.join(HERE, ".."))
TOP_BINDIR = os.path.join(TOPDIR, "bin")
os.environ["PATH"] = os.pathsep.join([
    os.path.abspath(TOP_BINDIR), os.environ.get("PATH", "")
])

PY_PATH = [
    ".",
    os.path.abspath(TOPDIR),
    os.path.abspath(os.path.join(TOPDIR, "lib/python"))
]
os.environ["PYTHONPATH"] = os.pathsep.join(PY_PATH)
# -- USE LOCAL PACKAGES:
use_local_packages = not (os.environ.get("TOXRUN", "no") == "yes")
if use_local_packages:
    sys.path.insert(0, TOP_BINDIR)
    import project_sitecustomize
    del sys.path[0]

# -- PATCH FOR: sphinxcontrib-ansi (with behave ANSI color grey=90)
os.environ["GHERKIN_COLORS"] = \
    "executing={color}:comments={color}".format(color="white")

# -- SANITY-CHECK: Everything ok?
import behave
print("BEHAVE.version:  %s" % behave.__version__)
print("BEHAVE.location: %s" % \
      os.path.relpath(os.path.dirname(behave.__file__), HERE))

# -----------------------------------------------------------------------------
# DISCOVER OPTIONAL EXTENSIONS:
# -----------------------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

HAVE_RST2PDF = True
try:
    import rst2pdf
except ImportError:
    HAVE_RST2PDF = False

# -----------------------------------------------------------------------------
# EXTENSIONS CONFIGURATION
# -----------------------------------------------------------------------------
# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.todo",
    "sphinx.ext.ifconfig",
    "sphinx.ext.extlinks",
    "sphinxcontrib.programoutput",
    # 'sphinx.ext.autodoc',
    # 'sphinx.ext.doctest',
    # 'sphinx.ext.coverage',
    # 'sphinx.ext.intersphinx',
    # 'sphinx.ext.viewcode',
    # 'sphinxjp.themecore',
]

if HAVE_RST2PDF:
    extensions.append("rst2pdf.pdfbuilder")

ansiterm_supported = True
if ansiterm_supported:
    # -- CONFIGURE EXTENSIONS:
    #   sphinxcontrib-programoutput.programoutput_use_ansi
    #   sphinxcontrib-ansi.html_ansi_stylesheet
    #   html_ansi_stylesheet = "black-on-white.css"
    extensions.append("sphinxcontrib.ansi")
    programoutput_use_ansi = True
    html_ansi_stylesheet = os.path.join(HERE, "_static/ansi_gherkin.css")

extlinks = {
    "pypi": ("https://pypi.org/project/%s", ""),
    "github": ("https://github.com/%s", "github:/"),
    "issue":
        ("https://github.com/behave/behave.example/issue/%s", "issue #"),
    "behave.issue":
        ("https://github.com/behave/behave/issue/%s", "behave issue #"),
}


def setup(app):
    """Add own ifconfig configuration parameters to sphinx."""
    rebuild = True
    app.add_config_value("ansiterm_supported", True, rebuild)


# -----------------------------------------------------------------------------
# GENERAL CONFIGURATION
# -----------------------------------------------------------------------------
# General information about the project.
project = u"behave.example"
author  = u"Jens Engel"
copyright = u'2012-2019 by %s' % author

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.2'
# The full version, including alpha/beta/rc tags.
release = open(os.path.join(HERE, "../VERSION.txt")).read().strip()
release = '1.2.6'


# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.2'

# Add any paths that contain templates here, relative to this directory.
templates_path = [ '_templates' ]

# The suffix of source filenames.
source_suffix = '.rst'
# source_suffix = '.txt'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = "en_US"

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = "%Y-%m-%d"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"
pygments_style = "friendly"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# -----------------------------------------------------------------------------
# HTML OUTPUT CONFIGURATION
# -----------------------------------------------------------------------------
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# THEMES: default, sphinxdoc, scrolls, agogo, traditional, nature, haiku
# html_theme = "agogo"
html_theme = "sphinxdoc"
html_theme = "haiku"
html_theme = "default"
html_theme = "bootstrap"

if html_theme == "bootstrap":
    # See sphinx-bootstrap-theme for documentation of these options
    # https://github.com/ryan-roemer/sphinx-bootstrap-theme
    import sphinx_bootstrap_theme
    html_theme_options = {
        'navbar_site_name': 'Document',
        'navbar_pagenav': True
    }

    # Add any paths that contain custom themes here, relative to this directory.
    html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "behave %s: Examples and Tutorials" % release

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None
# html_logo = "_static/Leaf32.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = "%Y-%m-%d"

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
html_file_suffix = ".html"

# Output file base name for HTML help builder.
htmlhelp_basename = '%s_doc' % project

# -----------------------------------------------------------------------------
# LATEX OUTPUT CONFIGURATION
# -----------------------------------------------------------------------------
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    "papersize": "a4paper",

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '11pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', '%s.tex' % project, u'%s Documentation' % project, author, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

# -----------------------------------------------------------------------------
# MAN PAGE OUTPUT CONFIGURATION
# -----------------------------------------------------------------------------
# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'behave_example', u'%s Documentation' % project, [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False

# -----------------------------------------------------------------------------
# TEXINFO OUTPUT CONFIGURATION
# -----------------------------------------------------------------------------
# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'behave_example', u'%s Documentation' % project,
   author, 'behave_example', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# -----------------------------------------------------------------------------
# EPUB OUTPUT CONFIGURATION
# -----------------------------------------------------------------------------
# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The language of the text. It defaults to the language option
# or en if the language is not set.
epub_language = 'en'

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
#epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'http://docs.python.org/': None
}


# -----------------------------------------------------------------------------
# RST2PDF OUTPUT CONFIGURATION: builder=pdf
# -----------------------------------------------------------------------------
# Grouping the document tree into PDF files. List of tuples
# (source start file, target name, title, author, options).
#
# If there is more than one author, separate them with \\.
# For example: r'Guido van Rossum\\Fred L. Drake, Jr., editor'
#
# The options element is a dictionary that lets you override
# this config per-document.
# For example,
# ('index', u'MyProject', u'My Project', u'Author Name',
#  dict(pdf_compressed = True))
# would mean that specific document would be compressed
# regardless of the global pdf_compressed setting.
pdf_documents = [
    ('index', project, project, author),
]
# A comma-separated list of custom stylesheets. Example:
pdf_stylesheets = ['sphinx','kerning','a4']
# Create a compressed PDF
# Use True/False or 1/0
# Example: compressed=True
pdf_compressed = True
# A colon-separated list of folders to search for fonts. Example:
# pdf_font_path = ['/usr/share/fonts', '/usr/share/texmf-dist/fonts/']
# Language to be used for hyphenation support
pdf_language = "en_US"
# Mode for literal blocks wider than the frame. Can be overflow, shrink or truncate
pdf_fit_mode = "shrink"
# Section level that forces a break page.
# For example: 1 means top-level sections start in a new page
# 0 means disabled
# pdf_break_level = 0 XXX
pdf_break_level = 1

# When a section starts in a new page, force it to be 'even', 'odd',
# or just use 'any'
#pdf_breakside = 'any'

# Insert footnotes where they are defined instead of
# at the end.
#pdf_inline_footnotes = True
# verbosity level. 0 1 or 2
#pdf_verbosity = 0
# If false, no index is generated.
#pdf_use_index = True
# If false, no modindex is generated.
#pdf_use_modindex = True
pdf_use_modindex = False

# If false, no coverpage is generated.
#pdf_use_coverpage = True
# Name of the cover page template to use
#pdf_cover_template = 'sphinxcover.tmpl'
# Documents to append as an appendix to all manuals.
#pdf_appendices = []
# Enable experimental feature to split table cells. Use it
# if you get "DelayedTable too big" errors
# pdf_splittables = True XXX
pdf_splittables = False

# Set the default DPI for images
#pdf_default_dpi = 72
# Enable rst2pdf extension modules (default is empty list)
# you need vectorpdf for better sphinx's graphviz support
#pdf_extensions = ['vectorpdf']

# Page template name for "regular" pages
pdf_page_template = 'cutePage'
