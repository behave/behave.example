# -*- coding: utf-8 -*-
"""
This module provides functionality to automatically select the best
matching terminal for your platform or operating system.
"""

from __future__ import absolute_import
from .baseterm import PlainTerminalWriter
import os
import sys

__all__ = [
    "get_terminal_size", "select_terminal_class",
    "ColoredTerminalWriter", "PlainTerminalWriter",
]

_python_version = sys.version_info[:2]
if _python_version >= (3, 3):
    # -- SINCE Python 3.3: shutil.get_terminal_size() : (columns, lines)
    from shutil import get_terminal_size
#elif sys.platform.startswith("win"):
#    from .winterm import get_terminal_size
else:
    from .ansiterm import get_terminal_size


def select_terminal_class(colored=True):
    """
    Selects the terminal class which is the best suited one
    for this platform and coloring mode.
    """
    # MAYBE: BEHAVE_TERM
    # TERM = os.environ.get("TERM", None)
    if colored:
        if sys.platform.startswith("win"):     # pragma: no cover
            from behave_ext.terminal import winterm
            return winterm.Terminal
        elif os.name == "posix":        # pragma: no cover
            # -- PLATFORM-GROUP: POSIX/UNIX SYSTEMS
            from behave_ext.terminal import ansiterm
            return ansiterm.AnsiTerminalWriter
    # -- OTHERWISE: Monochrome or unknown platform in colored mode.
    return PlainTerminalWriter

ColoredTerminalWriter = select_terminal_class(colored=True)
