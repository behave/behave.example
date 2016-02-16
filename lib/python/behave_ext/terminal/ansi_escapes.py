# -*- coding: utf-8 -*-
# BASED-ON: behave.formatter.ansi_escapes, but without unnecessary parts.
# pylint: disable=C0111,R0801
#   C0111   missing docstrings
#   R0801   Similarities: behave.formatter.ansi_escapes
"""
Provides ANSI escape sequences and color map for ANSI terminals.

.. seealso:

    * http://cukes.info/gherkin/api/ruby/latest/Gherkin/Formatter/AnsiEscapes.html
    * http://en.wikipedia.org/wiki/ANSI_escape_code
"""

from __future__ import absolute_import
from six.moves import range
class AnsiColor(object):
    """ANSI foreground color codes."""
    black   = 30
    red     = 31
    green   = 32
    yellow  = 33
    blue    = 34
    magenta = 35
    cyan    = 36
    white   = 37
    default = 39    # Normal foreground color.
    grey    = 90

class AnsiStyle(object):
    """ANSI style codes."""
    reset  = 0
    bright = 1
    # NOT-SUPPORTED: dark   = 2  # DIM

# -- CONTROL SEQUENCE INTRODUCER (CSI):
CSI = u"\x1b["

def CSI_m(*color_codes):
    """
    Build ANSI escape sequence for chain "CSI{x};...;{y}m" operations.
    Daisy-chain multiple colors an style.
    """
    if not color_codes:
        return CSI + "m"    #< SAME AS: CSI 0m (reset)
    return CSI + ";".join([str(c) for c in color_codes]) + "m"

def CSI_color256_m(color_code):
    """
    Builds ANSI escape sequence for terminals with 256 foreground colors::

        0x00-0x07:  standard colors (as in ESC [ 30..37 m)
        0x08-0x0f:  high intensity colors (as in ESC [ 90..97 m)
        0x10-0xe7:  6*6*6=216 colors: 16 + 36*r + 6*g + b (0 <= r,g,b <= 5)
        0xe8-0xff:  grayscale from black to white in 24 steps
    """
    return CSI + ("38;5;%dm" % color_code)


# -- ANSI ESCAPE SEQUENCES:
colors = {
    "black":        CSI_m(AnsiColor.black),
    "red":          CSI_m(AnsiColor.red),
    "green":        CSI_m(AnsiColor.green),
    "yellow":       CSI_m(AnsiColor.yellow),
    "blue":         CSI_m(AnsiColor.blue),
    "magenta":      CSI_m(AnsiColor.magenta),
    "cyan":         CSI_m(AnsiColor.cyan),
    "white":        CSI_m(AnsiColor.white),
    "grey":         CSI_m(AnsiColor.grey),
    "default":      CSI_m(AnsiColor.default),

    # -- MORE FOREGROUND COLORS:
    "lightblack":   CSI_m(AnsiStyle.bright, AnsiColor.black),
    "lightred":     CSI_m(AnsiStyle.bright, AnsiColor.red),
    "lightgreen":   CSI_m(AnsiStyle.bright, AnsiColor.green),
    "lightyellow":  CSI_m(AnsiStyle.bright, AnsiColor.yellow),
    "lightblue":    CSI_m(AnsiStyle.bright, AnsiColor.blue),
    "lightmagenta": CSI_m(AnsiStyle.bright, AnsiColor.magenta),
    "lightcyan":    CSI_m(AnsiStyle.bright, AnsiColor.cyan),
    "lightwhite":   CSI_m(AnsiStyle.bright, AnsiColor.white),
    #"darkblack":    CSI_m(AnsiStyle.dark, AnsiColor.black),
    #"darkred":      CSI_m(AnsiStyle.dark, AnsiColor.red),
    #"darkgreen":    CSI_m(AnsiStyle.dark, AnsiColor.green),
    #"darkyellow":   CSI_m(AnsiStyle.dark, AnsiColor.yellow),
    #"darkblue":     CSI_m(AnsiStyle.dark, AnsiColor.blue),
    #"darkmagenta":  CSI_m(AnsiStyle.dark, AnsiColor.magenta),
    #"darkcyan":     CSI_m(AnsiStyle.dark, AnsiColor.cyan),
    #"darkwhite":    CSI_m(AnsiStyle.dark, AnsiColor.white),

    # -- TEXT STYLING:
    "bold":         CSI_m(AnsiStyle.bright),
}

# -- FOREGROUND COLORS, TEXT STYLES:
#__colors = {
#    "black":        u"\x1b[30m",
#    "red":          u"\x1b[31m",
#    "green":        u"\x1b[32m",
#    "yellow":       u"\x1b[33m",
#    "blue":         u"\x1b[34m",
#    "magenta":      u"\x1b[35m",
#    "cyan":         u"\x1b[36m",
#    "white":        u"\x1b[37m",
#    "grey":         u"\x1b[90m",
#    # -- MORE FOREGROUND COLORS:
#    "lightblack":   u"\x1b[1;30m",
#    "lightred":     u"\x1b[1;31m",
#    "lightgreen":   u"\x1b[1;32m",
#    "lightyellow":  u"\x1b[1;33m",
#    "lightblue":    u"\x1b[1;34m",
#    "lightmagenta": u"\x1b[1;35m",
#    "lightcyan":    u"\x1b[1;36m",
#    "lightwhite":   u"\x1b[1;37m",
#    # -- TEXT STYLING:
#    "bold":         u"\x1b[1m",
#}

escapes = {
    'reset':        u'\x1b[0m',
    'up':           u'\x1b[1A',
}

def cursor_up(n=1):
    """
    Move cursor several rows up (ANSI CUU).
    """
    return u"\x1b[%dA" % n

# -----------------------------------------------------------------------------
# OPTIONAL:
# -----------------------------------------------------------------------------
# import os
import sys

def setup_color256_map():
    for color_number in range(256):
        color_name = "color%d" % color_number
        colors[color_name] = CSI_color256_m(color_number)

# TERM = os.environ.get("TERM", "")
# BEHAVE_TERM_STYLE = os.environ.get("BEHAVE_TERM_STYLE", "")
# if (not sys.platform.startswith("win") and
#     (("256color" in TERM) or BEHAVE_TERM_STYLE.startswith("color256"))):
if not sys.platform.startswith("win"):
    setup_color256_map()


if __name__ == "__main__":
    def print_color_map():
        import sys
        escape_reset = escapes["reset"]
        sys.stdout.write("COLOR-MAP[%d]:\n" % len(colors))
        for color_name in sorted(colors.keys()):
            escape_setup = colors[color_name]
            text = escape_setup + color_name + escape_reset
            sys.stdout.write(text + "\n")

    print_color_map()

