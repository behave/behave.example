# -*- coding: utf-8 -*-
"""
This module describes terminal/text styles in a platform independent way.
"""

from __future__ import absolute_import
import os
import sys

# -----------------------------------------------------------------------------
# CLASS: Stylesheet
# -----------------------------------------------------------------------------
class Stylesheet(dict):
    """
    Helper class to provide style descriptions and style defaults.
    """
    colors = set(["black", "blue", "green", "cyan", "red",
                  "magenta", "yellow", "white", "grey" ])
    styles_with_arg = set([
        "undefined", "pending", "executing", "failed", "passed", "skipped"])

    # -- DEFAULT STYLES (descriptions): For a colored terminal.
    default_styles = {
        # -- STATUS-BASED:
        "undefined":    "yellow",
        "pending":      "yellow",
        "executing":    "grey",     # OR: blue
        "failed":       "red",
        "passed":       "green",
        "skipped":      "cyan",
        # -- CONTENT-BASED:
        "outline":      "cyan",
        "comments":     "grey",     # XXX grey
        "tag":          "cyan",     # cyan, purple
        # -- MORE CONTENT-BASED:
        "feature":      "black",    # XXX "black,bold",
        "scenario":     "black",    # XXX "blue,bold",
        "error":        "red",
        "description":  "black",
        "docstring":    "black",
        "table":        "black",
    }

    @classmethod
    def make(cls, init_styles=None, use_defaults=True, use_environment=True):
        if use_defaults:
            stylesheet = Stylesheet(cls.default_styles)
        else:
            stylesheet = Stylesheet()
        if init_styles:
            stylesheet.update(init_styles)
        if use_environment:
            stylesheet.update_from_environment()
        stylesheet.update_arg_styles(stylesheet, override=False)
        return stylesheet

    def update(self, data=None, **kwargs):
        super(Stylesheet, self).update(data, **kwargs)
        return self

    def update_from_environment(self):
        """
        ENVIRONMENT:
            GHERKIN_COLORS="skipped=blue:failed=red"
            GHERKIN_COLORS="passed=white"
            GHERKIN_COLORS="passed=white,bold:passed_arg=white,bold,underline"
        """
        # pylint: disable=C0103
        GHERKIN_COLORS = os.environ.get("GHERKIN_COLORS", None)
        if GHERKIN_COLORS:
            descriptions = [p.split("=") for p in GHERKIN_COLORS.split(":")]
            self.update(dict(descriptions))
        return self

    def update_arg_styles(self, stylesheet, override=True):
        # -- SETUP ARG-STYLE DESCRIPTIONS:
        for style_name, style_description in list(stylesheet.items()):
            if ( style_name.endswith("_arg") or
                (style_name not in self.styles_with_arg)):
                continue
            arg_style_name = "%s_arg" % style_name
            arg_style = stylesheet.get(arg_style_name, None)
            if not arg_style or override:
                arg_style_description = "%s,bold" % style_description
                stylesheet[arg_style_name] = arg_style_description
        return self


# -----------------------------------------------------------------------------
# STYLESHEETS:
# -----------------------------------------------------------------------------
default_stylesheet = None
stylesheets = {}
stylesheets["std"]  = Stylesheet.make()
stylesheets["std2"] = Stylesheet(stylesheets["std"]).update({
    "description":  "grey"
})

stylesheets["two"] = Stylesheet(stylesheets["std"]).update({
    "tag":          "blue",
    "feature":      "black,bold",
    "scenario":     "black,bold",
    "description":  "grey",
})

stylesheets["blue"] = Stylesheet(stylesheets["two"]).update({
    "tag":          "blue,bold",
    "docstring":    "blue",
    "table":        "blue",
})

stylesheets["dark"] = Stylesheet.make({
    # -- STATUS-BASED:
    "undefined":    "black,bold",
    "executing":    "grey",     # OR: blue
    "failed":       "black,bold",
    "passed":       "black",
    "skipped":      "black",
    # -- CONTENT-BASED:
    "tag":          "black",
    "feature":      "black,bold",
    "scenario":     "black,bold",
    "description":  "grey",
    "outline":      "black",
    "comments":     "grey",     # XXX grey
    "docstring":    "black",
    "table":        "black",
}, use_environment=False)

# -- STYLESHEETS: For terminals that support 256 colors.
if not sys.platform.startswith("win"):
    stylesheets["color256"] = Stylesheet.make({
        # -- STATUS-BASED:
        "undefined":    "lightmagenta",
        "pending":      "lightmagenta",
        "executing":    "color238",    # gray
        "failed":       "lightred",
        "passed":       "green",         # DarkGreen, color22
        "skipped":      "color94",
        # -- CONTENT-BASED:
        "outline":      "cyan",
        "comments":     "grey",   # grey
        "tag":          "color197",     # DarkViolet (purple, magenta).
        # -- MORE CONTENT-BASED:
        "feature":      "color17,bold", # color16 darkgray
        "scenario":     "color17,bold", # color17 blue
        "error":        "lightred",
        "description":  "color238", # DarkGray
        "docstring":    "color60",  # DarkRed, color88
        "table":        "color234",  # DarkBlue, color18
    }, use_environment=False)


# -----------------------------------------------------------------------------
# MODULE-INIT
# -----------------------------------------------------------------------------
def _module_init():
    global default_stylesheet
    name = os.environ.get("BEHAVE_TERM_STYLE", "std")
    primary_stylesheet = stylesheets["std"]
    default_stylesheet = stylesheets.get(name, primary_stylesheet)
    # print("Using style: %s" % name)

_module_init()
