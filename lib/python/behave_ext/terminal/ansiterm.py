# -*- coding: utf-8 -*-
"""
This module provides a terminal with ANSI escape sequence support.
"""

from __future__ import absolute_import
from . import ansi_escapes, baseterm, style
import logging
import os
import sys

__all__ = [
    "AnsiStyle", "AnsiStyleWriter", "AnsiTerminalWriter", "get_terminal_size"
]

# -----------------------------------------------------------------------------
# TERMINAL: AnsiTerminal
# -----------------------------------------------------------------------------
class AnsiStyle(object):
    __slots__ = ("setup_style", "reset_style")

    def __init__(self, style_description):
        self.setup_style = self.parse_style(style_description)
        self.reset_style = ansi_escapes.escapes["reset"]

    def text(self, text):
        if not self.setup_style:
            return text
        return self.setup_style + text + self.reset_style

    @staticmethod
    def parse_style(style_description):
        """
        Build ANSI escape sequence to setup a text style from style description.
        """
        escape_seq = ""
        for color in style_description.split(","):
            color = color.strip()
            if not color:
                continue    # EMPTY-STRING: Use terminal color
            escape_part = ansi_escapes.colors.get(color, None)
            if not escape_part:
                log = logging.getLogger("behave.terminal")
                log.error("Unknown style_part=%s" % color)
                continue
            escape_seq += escape_part
        return escape_seq
        # -- SHORTER ALTERNATIVE:
        # escape_parts = [ ansi_escapes.colors.get(p.strip(), "")
        #                     for p in style_description.split(",") ]
        # return "".join(escape_parts)

    @staticmethod
    def parse_style2(style_description):
        """
        Build ANSI escape sequence to setup a text style from style description.
        Use composite style for CSI_m sequences if possible.
        """
        escape_seq = ""
        color_codes = []
        for color in style_description.split(","):
            color = color.strip()
            if not color:
                continue    # EMPTY-STRING: Use terminal color
            elif color == "bold":
                color_codes.insert(0, ansi_escapes.AnsiStyle.bright)
                continue
            else:
                # -- CHECK: SIMPLE FOREGROUND COLOR
                color_code = getattr(ansi_escapes.AnsiColor, color, None)
                if color_code:
                    color_codes.append(color_code)
                    continue

            escape_part = ansi_escapes.colors.get(color, None)
            if not escape_part:
                log = logging.getLogger("behave.terminal")
                log.error("Unknown style_part=%s" % color)
                continue
            escape_seq += escape_part
        if color_codes:
            escape_seq += ansi_escapes.CSI_m(*color_codes)
        return escape_seq


class AnsiStyleWriter(AnsiStyle):
    """
    Builds an escaped text style writer by using ANSI escape sequences
    for coloring.

    .. code-block:: python

        style1 = AnsiStyleWriter("red", sys.stdout)
        style1.write("RED")

        style2 = AnsiStyleWriter("green,bold")
        style2.write("GREEN_BOLD")
        sys.stdout.write("Text is black again.")
    """
    __slots__ = AnsiStyle.__slots__ + ("file", )

    def __init__(self, style_description, file=None):
        super(AnsiStyleWriter, self).__init__(style_description)
        if file is None:
            file = sys.stdout
        self.file = file

    def write(self, text):
        self.file.write(self.text(text))


class AnsiTerminalWriter(baseterm.BaseTerminalWriter):
    """
    Provides a terminal writer with style support (and coloring).
    Styles are mapped to ANSI escape sequences (coloring, ...).
    The core functionality is provided by the base class.

    This class defines only the text styles that are expected from a
    behave terminal.

    .. code-block:: python

        terminal = AnsiTerminalWriter(sys.stdout)
        terminal.write("Hello world", style="passed")
    """
    style_writer_class = AnsiStyleWriter
    default_stylesheet = style.default_stylesheet

    def __init__(self, stream=None, stylesheet=None, **kwargs):
        kwargs["colored"] = True
        super(AnsiTerminalWriter, self).__init__(stream, stylesheet, **kwargs)

    def move_cursor_up(self, rows=1):
        self.stream.write(ansi_escapes.cursor_up(rows))


# -----------------------------------------------------------------------------
# FUNCTIONS:
# -----------------------------------------------------------------------------
def get_terminal_size():    # pragma: no cover
    """
    Determines the terminal size of an ANSI terminal (platform=UNIX/POSIX).
    NOTE: Python 3.3 supports shutil.get_terminal_size() : (columns, lines)
    """
    # pylint: disable=W0703
    #   W0703 Catching too general exception
    import struct
    try:
        # -- ONLY-FOR: UNIX
        import fcntl
        import termios

        zero_struct = struct.pack('HHHH', 0, 0, 0, 0)
        syscall_result = fcntl.ioctl(1, termios.TIOCGWINSZ, zero_struct)
        height, width = struct.unpack('HHHH', syscall_result)[:2]
        columns = width or int(os.environ.get("COLUMNS", 80))
        lines = height or int(os.environ.get("LINES", 24))
        return (columns, lines)
    except Exception:   # pragma: no cover
        # -- Due to test_formatter, normally IOError, ...
        columns = int(os.environ.get("COLUMNS", 80))
        lines = int(os.environ.get("LINES", 24))
        return (columns, lines)


# -----------------------------------------------------------------------------
# PLATFORM: win32
# -----------------------------------------------------------------------------
if sys.platform.startswith("win"):
    # -- REQUIRES: colorama
    # PATCH: colorama does not handle high color code for grey(90).
    ansi_escapes.colors["grey"] = ansi_escapes.colors["white"]

    _unix_terminal_size = get_terminal_size
    def get_terminal_size():    # pragma: no cover
        """
        Determines the terminal size of an Windows terminal (platform=win32).
        NOTE: Python 3.3 supports shutil.get_terminal_size() : (columns, lines)
        """
        # -- USE: colorama win32 low-level API.
        from colorama import win32
        try:
            console_info = win32.GetConsoleScreenBufferInfo()
            columns, lines = console_info.dwSize.X, console_info.dwSize.Y
            return (columns, lines)
        except IOError:   # pragma: no cover
            # -- CATCH-MOST ...
            columns = int(os.environ.get("COLUMNS", 80))
            lines = int(os.environ.get("LINES", 24))
            return (columns, lines)



