# -*- coding: utf-8 -*-
# pylint: disable=C0103
#   C103    Invalid name (COORD, SMALL_RECT, ...)
"""
Provides low-level Win32 API for Windows terminal output.
"""

from __future__ import absolute_import
from ctypes import Structure, c_short as short, c_ushort as ushort
import sys

# -----------------------------------------------------------------------------
# WIN32 API TYPES, Enumerations, Constants
# -----------------------------------------------------------------------------
# -- FROM: winbase.h
STDOUT = -11
STDERR = -12

# -- FROM: wincon.h
class WinColor(object):
    black       =  0
    blue        =  1
    green       =  2
    cyan        =  3
    red         =  4
    magenta     =  5
    yellow      =  6    # BROWN
    grey        =  7
    darkgrey    =  8
    lightblue   =  9
    lightrgreen = 10
    lightcyan   = 11
    lightred    = 12
    lightpurple = 13
    lightyellow = 14    # YELLOW
    white       = 15

class COORD(Structure):
    """XY coordinate structure from "wincon.h" """
    _fields_ = [
        ("x", short),
        ("y", short)
    ]

class SMALL_RECT(Structure):
    """Rectangle structure from "wincon.h" """
    _fields_ = [
        ("left",    short),
        ("top",     short),
        ("right",   short),
        ("bottom",  short)
    ]

class CONSOLE_SCREEN_BUFFER_INFO(Structure):
    """Structure from "wincon.h" """
    _fields_ = [
        ("size",            COORD),
        ("cursor_position", COORD),
        ("attributes",      ushort),
        ("window",          SMALL_RECT),
        ("maximum_window_size", COORD)
    ]

# -----------------------------------------------------------------------------
# WIN32 API FUNCTIONS
# -----------------------------------------------------------------------------
simulated = True
try:
    from ctypes import windll
    simulated = False

    # -- REAL API:
    assert not simulated
    GetStdHandle                = windll.kernel32.GetStdHandle
    SetConsoleTextAttribute     = windll.kernel32.SetConsoleTextAttribute
    GetConsoleScreenBufferInfo  = windll.kernel32.GetConsoleScreenBufferInfo
    SetConsoleCursorPosition    = windll.kernel32.SetConsoleCursorPosition

except ImportError:
    if sys.platform == "win32":
        raise   #< OOPS, something is weird here.

    # -- SIMULATED: Win32 API (on non-Windows platforms)
    assert simulated
    GetStdHandle                = lambda stream_id: -stream_id
    SetConsoleTextAttribute     = lambda *args: None
    GetConsoleScreenBufferInfo  = lambda *args: None
    SetConsoleCursorPosition    = lambda handle, position: None

