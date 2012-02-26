@echo off
REM ==========================================================================
REM PAVER COMMAND (for local installation)
REM ==========================================================================
REM set PYTHONPATH=%HERE%paver-minilib.zip;%PYTHONPATH%

setlocal
set HERE=%~dp0
if not defined PYTHON   set PYTHON=python

%PYTHON% %HERE%pavercmd.py %*
