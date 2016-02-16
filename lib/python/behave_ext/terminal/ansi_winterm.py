# -*- coding: utf-8 -*-
"""
Use colorama as converter from ASCII escape codes to Windows text attributes.

REQUIRES: colorama >= 0.2.7
"""

from __future__ import absolute_import
from .ansiterm import AnsiTerminalWriter
import sys

# -----------------------------------------------------------------------------
# FUNCTIONS:
# -----------------------------------------------------------------------------
#def colorama_init():
#    import colorama
#    if not colorama_init.done:
#        colorama.init()
#    colorama_init.done = True
#colorama_init.done = False
#
#
#class Ansi2WinTerminalWriter0(AnsiTerminalWriter):
#    """
#    TOO LATE: Need to ensure that coloram.init() is done elsewhere.
#    Ensure that colorama.init() is called.
#    Then use
#    """
#    def __init__(self, stream=None, **kwargs):
#        colorama_init()
#        if not stream:
#            stream = sys.stdout
#        super(Ansi2WinTerminalWriter, self).__init__(stream, **kwargs)
#        self.winterm = winterm.WinTerm()
#
#    def reset_style(self):
#        colorama_reset_all()
#
#    def move_cursor_up(self, rows):
#        self.winterm.cursor_up(rows)
#
#    def close(self):
#        self.reset_style()

# -----------------------------------------------------------------------------
# VARIANT 1: Use colorama ANSI-to-WIN32 bridge
# -----------------------------------------------------------------------------
from colorama.ansitowin32 import AnsiToWin32
from colorama.initialise import \
    wrap_stream as colorama_wrap_stream, reset_all as colorama_reset_all

class Ansi2WinTerminalWriter(AnsiTerminalWriter):
    """
    Use :func:`colorama.initialize.wrap_stream()` to wrap only this stream.
    Hopefully, nobody has called colorama.init() before.
    """

    def __init__(self, stream=None, **kwargs):
        if not stream:
            stream = sys.stdout
        stream2 = self.__wrap_stream_if_needed(stream)
        super(Ansi2WinTerminalWriter, self).__init__(stream2, **kwargs)

    @staticmethod
    def __wrap_stream_if_needed(stream):
        if isinstance(stream, AnsiToWin32):
            return stream
        return colorama_wrap_stream(stream, convert=None, strip=None,
                           autoreset=False, wrap=True)

    def reset_style(self):
        colorama_reset_all()

    def close(self):
        self.reset_style()


# -----------------------------------------------------------------------------
# VARIANT 2: Use colorama.winterm directly w/o ANSI-to-WIN32 bridge
# -----------------------------------------------------------------------------
from .baseterm import BaseTerminalWriter
from .style import default_stylesheet
from colorama import winterm

class WintermStyleWriter(object):
    __slots__ = ("stream", "winterm", "text_attributes")

    def __init__(self, style_description, stream, winterm):
        self.stream = stream
        self.winterm = winterm
        self.text_attributes = self.parse(style_description)

    def write(self, text):
        self.winterm.set_console(self.text_attributes)
        self.stream.write(text)
        self.winterm.reset_all()

    @staticmethod
    def parse(style_description):
        """
        Parse style description and extract windows foreground color.
        """
        color_name = style_description.split(",")[0]
        assert color_name != "bold"
        if color_name == "white":
            color_name = "grey"
        text_attributes  = getattr(winterm.WinColor, color_name.upper())
        if "bold" in style_description and text_attributes < 8:
            # -- BOLD STYLE: Use bright/light color variant.
            text_attributes += winterm.WinStyle.BRIGHT
        return text_attributes

class WintermTerminalWriter(BaseTerminalWriter):
    """
    Provides a terminal writer based on colorama.winterm.
    """
    style_writer_class = WintermStyleWriter
    default_stylesheet = default_stylesheet

    def __init__(self, stream=None, **kwargs):
        kwargs["colored"] = True
        BaseTerminalWriter.__init__(self, stream=stream, **kwargs)
        self._winterm = winterm.WinTerm()

    def add_style(self, name, style_description):
        self.styles[name] = WintermStyleWriter(style_description,
                                               self.stream, self)

    def move_cursor_up(self, rows=1):
        """
        Moves the cursor up for a number of rows (relative positioning).
        """
        self._winterm.cursor_up(rows)

    def reset_style(self):
        """Reset text/coloring attribute to default values."""
        self._winterm.reset_all()
