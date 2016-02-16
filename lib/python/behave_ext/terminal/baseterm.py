# -*- coding: utf-8 -*-
"""
This module provides functionality to automatically select the best
matching terminal for your platform or operating system.
"""

from __future__ import absolute_import
import sys


# -----------------------------------------------------------------------------
# EXCEPTIONS:
# -----------------------------------------------------------------------------
class UnknownStyleError(KeyError):
    """
    Raised when a name text style is unknown/not found.
    """


# -----------------------------------------------------------------------------
# FUNCTIONS:
# -----------------------------------------------------------------------------
def isatty(stream):
    return hasattr(stream, "isatty") and stream.isatty()


# -----------------------------------------------------------------------------
# CLASS: BaseTerminalWriter
# -----------------------------------------------------------------------------
class UnstyledWriter(object):
    def __init__(self, _, file=None):
        if file is None:
            file = sys.stdout
        self.file = file

    def write(self, text):
        self.file.write(text)

class BaseTerminalWriter(object):
    """
    Provides the core functionality for a terminal writer that
    supports text styles in a coloring/non-coloring terminal.
    for behave that supports text output with text styles and style attributes.

    .. code-block:: python

        terminal = MyTerminalWriter(sys.stdout)
        terminal.write("Normal Text without styling")
        terminal.write("STYLED_TEXT", style="passed")
    """
    style_writer_class = UnstyledWriter
    default_stylesheet = None

    def __init__(self, stream=None, stylesheet=None, **kwargs):
        if stream is None:
            stream = sys.stdout
        self.stream  = stream
        self.colored = kwargs.get("colored", False)
        self.styles = {}
        stylesheet = stylesheet or self.default_stylesheet
        if stylesheet:
            self.setup_styles(stylesheet)

    @property
    def styled(self):
        return bool(self.styles)

    def add_style(self, name, style_description):
        style_writer_class = self.style_writer_class
        self.styles[name] = style_writer_class(style_description, self.stream)

    def setup_styles(self, stylesheet):
        for name, style_description in stylesheet.items():
            self.add_style(name, style_description)

    def has_feature(self, feature):
        # -- FEATURES: cursor_up, colored
        if feature == "cursor_up":
            return hasattr(self, "move_cursor_up")
        return bool(getattr(self, feature, False))

    # -- STREAM-LIKE API:
    def write(self, text, style=None):
        if not text:
            return
        elif not style:
            # -- CASE: Write text w/o styling attributes (normal style).
           return self.stream.write(text)
        # -- CASE: Write text w/ style attributes.
        style_writer = self.styles.get(style, None)
        if not style_writer:
            raise UnknownStyleError(style)
        style_writer.write(text)

    def flush(self):
        self.stream.flush()

    #def close(self):
    #    self.flush()
    #    self.stream.close()
    #
    def isatty(self):
        """Indicates if this terminal (stream) is a TTY."""
        return isatty(self.stream)

    def __getattr__(self, name):
        """
        Transparent stream-proxy functionality.
        Provides direct access to stream attributes and methods, like:
          * stream.closed
          * stream.encoding
          * ...
        """
        # -- TRANSPARENT-PROXY: To stream
        attrib_func = getattr(self.stream, name, None)
        if attrib_func:
            return attrib_func
        raise AttributeError(name)


# -----------------------------------------------------------------------------
# CLASS: PlainTerminal
# -----------------------------------------------------------------------------
class PlainTerminalWriter(BaseTerminalWriter):
    """
    Provides a basic terminal without coloring and style support.
    Therefore, all styled text writes are just passed through without styling.
    """

    def __init__(self, file=None, **kwargs):
        assert not kwargs.get("colored", None)
        super(PlainTerminalWriter, self).__init__(file, **kwargs)
        assert not self.colored

    def write(self, text, style=None):
        """
        Overwrite base class implementation to ignore all style settings.
        Writes only the text.
        """
        self.stream.write(text)
