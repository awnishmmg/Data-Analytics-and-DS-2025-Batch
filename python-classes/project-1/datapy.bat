@echo off 
title Python Data Compiler
goto :main 

:main
set /p  filename="Enter the Filename:"
if exist %filename% (
    echo File exists. Compiling...
    python run.py %filename%
) else (
    echo File does not exist. Please check the filename and try again.
)
pause