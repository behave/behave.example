# -*- coding: utf-8 -*-
"""
This module provides functionality to automatically select the best
matching terminal for your platform or operating system.
"""

from __future__ import absolute_import
from . import baseterm, style, win32
from ctypes import byref
import os
import six

__all__ = [ "WindowsStyle", "Terminal" ]

# -----------------------------------------------------------------------------
# TERMINAL: Windows Terminal
# -----------------------------------------------------------------------------
class WindowsTextStyle(object):
    @staticmethod
    def parse(style_description):
        """
        Parse style description and extract windows foreground color.
        """
        color_name = style_description.split(",")[0]   #< Only one color
        assert color_name != "bold"
        # win_color  = getattr(win32.WinColor, color_name, win32.WinColor.black)
        win_color  = getattr(win32.WinColor, color_name)
        if "bold" in style_description and win_color < 8:
            # -- BOLD STYLE: Use bright/light color variant.
            win_color += 8
        return win_color

class WindowsStyleWriter(WindowsTextStyle):
    def __init__(self, style_description, terminal):
        self.terminal = terminal
        self.stream = terminal.stream
        self.color = self.parse(style_description)

    def write(self, text):
        self.terminal.set_color(self.color)
        self.stream.write(text)
        self.terminal.reset_style()

class WindowsTerminalWriter(baseterm.BaseTerminalWriter):
    """
    Provides a terminal class for Windows shell terminals (cmd windows).
    """
    style_writer_class = WindowsStyleWriter
    default_stylesheet = style.default_stylesheet

    def __init__(self, stream=None, **kwargs):
        kwargs["colored"] = True
        super(WindowsTerminalWriter, self).__init__(stream=stream, **kwargs)
        self._stdout_handle = win32.GetStdHandle(win32.STDOUT)
        self._default_attribute = self.__get_text_attribute()

    def add_style(self, name, style_description):
        self.styles[name] = WindowsStyleWriter(style_description, self)

    def move_cursor_up(self, rows):
        """
        Moves the cursor up for a number of rows (relative positioning).
        """
        # pylint: disable=W0201
        #   W0201   position.y definted outside __init__ (cytpes.Structure)
        csbi = self.__get_console_info()
        y = csbi.cursor_position.y - rows
        if y < 0:
            y = 0
        position = win32.COORD(csbi.cursor_position.x, y)
        win32.SetConsoleCursorPosition(self._stdout_handle, position)

    def reset_style(self):
        """Reset text/coloring attribute to default values."""
        self.__set_text_attribute(self._default_attribute)

    def set_color(self, color):
        if isinstance(color, six.string_types):
            color_value = getattr(win32.WinColor, color, None)
            if color_value is None:
                raise AttributeError("unknown color='%s'" % color)
            color = color_value
        self.__set_color(color)

    def __set_color(self, foreground_color=None, background_color=None):
        current = self.__get_text_attribute()
        if foreground_color == None:
            foreground_color = current & 0x000F
        if background_color == None:
            background_color = current & 0x00F0
        else:
            assert 0 <= background_color < 16
            background_color <<= 4
            background_color = background_color & 0x00F0
        self.__set_text_attribute(foreground_color + background_color)

    def __get_console_info(self):
        csbi = win32.CONSOLE_SCREEN_BUFFER_INFO()
        win32.GetConsoleScreenBufferInfo(self._stdout_handle, byref(csbi))
        return csbi

    def __get_text_attribute(self):
        return self.__get_console_info().attributes

    def __set_text_attribute(self, color):
        self.stream.flush()
        win32.SetConsoleTextAttribute(self._stdout_handle, color)

# -----------------------------------------------------------------------------
# FUNCTIONS:
# -----------------------------------------------------------------------------
def get_terminal_size():
    """
    Determines the terminal size of an Windows terminal (platform=win32, ...).
    NOTE: Python 3.3 supports shutil.get_terminal_size() : (columns, lines)
    """
    # pylint: disable=W0703
    #   W0703 Catching too general exception
    try:
        stdout_handle = win32.GetStdHandle(win32.STDOUT)
        csbi = win32.CONSOLE_SCREEN_BUFFER_INFO()
        win32.GetConsoleScreenBufferInfo(stdout_handle, byref(csbi))
        columns = csbi.size.x
        lines = csbi.size.y
        return (columns, lines)
    except Exception:   # pragma: no cover
        # -- Due to test_formatter, normally IOError, ...
        columns = int(os.environ.get("COLUMNS", 80))
        lines = int(os.environ.get("LINES", 24))
        return (columns, lines)

