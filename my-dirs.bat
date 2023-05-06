@echo off

rem Activate the virtual environment
call .explorer_env\Scripts\activate

rem Run the Python script in the background
start /MIN py main.py

rem Deactivate the virtual environment
call .explorer_env\Scripts\deactivate
