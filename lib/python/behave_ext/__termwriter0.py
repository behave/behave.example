# -*- coding: utf-8 -*-
"""
Terminal writer experiment using :mod:`py.io.terminalwriter`.

REQUIRES: py >= 1.4.17 (actually: py.io.terminalwriter)
"""

from __future__ import absolute_import
from py._io import terminalwriter
import os
import sys

_platform_windows = (sys.platform == "win32")


# -----------------------------------------------------------------------------
# CLASS: TextStyle
# -----------------------------------------------------------------------------
class TextStyle(object):
    """
    Base class (tag) for all text styles.
    """
    # -- STYLE DESCRIPTIONS: For a colored terminal.
    arg_names = set([
        "undefined", "pending", "executing",
        "failed", "passed", "skipped"
    ])
    style_descriptions = {
        "undefined":    "yellow",
        "pending":      "yellow",
        "executing":    "blue", # grey
        "failed":       "red",
        "passed":       "green",
        "skipped":      "cyan",
        "outline":      "cyan",
        "comments":     "grey", # XXX grey
        "tag":          "cyan",  # cyan, purple
        # -- MORE STYLES:
        "feature":      "black,bold",
        "scenario":     "blue,bold",
        "error":        "red",
    }

    @classmethod
    def setup_style_descriptions_from_environment(cls):
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
            cls.style_descriptions.update(dict(descriptions))

    @classmethod
    def setup_style_descriptions(cls):
        cls.setup_style_descriptions_from_environment()

        # -- SETUP ARG-STYLE DESCRIPTIONS:
        for style_name, description in list(cls.style_descriptions.items()):
            if style_name.endswith("_arg"):
                continue
            arg_style_name = "{0}_arg".format(style_name)
            arg_style = cls.style_descriptions.get(arg_style_name, None)
            if not arg_style:
                arg_description = "{0},bold".format(description)
                cls.style_descriptions[arg_style_name] = arg_description

TextStyle.setup_style_descriptions()


class WriterWithStyle(object):
    def __init__(self, writer, style):
        self.writer = writer
        self.style = style

    def write(self, text):
        self.writer.write(text, style=self.style)

class StyledTerminalWriter(object):
    """
    XXX
    """
    DEFAULT_STYLES = TextStyle.style_descriptions
    NO_STYLES = {}
    NULL_STYLE = {}

    def __init__(self, file=None, encoding=None, styled=None, colored=True):
        self._terminal = terminalwriter.TerminalWriter(file, encoding=encoding)
        self.styles = None
        if styled is None:
            styled = self._terminal.hasmarkup
            # and (self.isatty() or _platform_windows))
        if styled and colored:
            self.styles = self._setup_styles()
        # self._styled = styled and bool(self.styles)

    def isatty(self):
        stream = self._terminal._file
        return hasattr(stream, "isatty") and stream.isatty()

    def _setup_styles(self):
        if not _platform_windows:
            grey = self._terminal._esctable.get("grey", None)
            if not grey:
                self._terminal._esctable["grey"] = 90
        styles = {}
        for style_name, description in TextStyle.style_descriptions.items():
            params = {}
            for param_name in description.split(","):
                params[param_name] = True
            styles[style_name] = params
        return styles

    @property
    def encoding(self):
        return self._terminal.encoding

    @property
    def width(self):
        return self._terminal.fullwidth

    @property
    def styled(self):
        return bool(self.styles)


    def write(self, text, style=None):
        if self.styled:
            style_params = self.styles.get(style, self.NULL_STYLE)
            return self._terminal.write(text, **style_params)
        else:
            return self._terminal.write(text)

    def flush(self):
        self._terminal._file.flush()

    def use_style(self, style):
        styled_writer = WriterWithStyle(self, style)
        yield styled_writer

    if _platform_windows:
        def move_cursor_up(self, rows):
            win32_move_cursor_up(rows)
    else:
        # -- ANSI PLATFORM:
        # assert os.name == "posix"
        def move_cursor_up(self, rows):
            # -- ANSI-TERMINAL: Move cursor up by using ANSI escapes.
            cursor_ups = u"\x1b[%dA" % rows
            self._terminal.write(cursor_ups)

# -----------------------------------------------------------------------------
# WINDOWS-SPECIFIC (win32):
# -----------------------------------------------------------------------------
if terminalwriter.win32_and_ctypes:
    from ctypes import windll
    _win32 = terminalwriter
    _win32_SetConsoleCursorPosition = windll.kernel32.SetConsoleCursorPosition

    def win32_move_cursor_up(rows):
        console_handle = _win32.GetStdHandle(_win32.STD_OUTPUT_HANDLE)
        console_info = _win32.GetConsoleInfo(console_handle)
        Y = console_info.dwCursorPosition.Y - rows
        if Y < 0:
            Y = 0
        position = _win32.COORD(console_info.dwCursorPosition.X, Y)
        _win32_SetConsoleCursorPosition(console_handle, position)
