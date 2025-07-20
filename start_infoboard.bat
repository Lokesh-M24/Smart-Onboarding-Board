@echo off
REM Smart Onboarding InfoBoard Auto-Start Script
REM This batch file automatically runs the InfoBoard application

echo Starting Smart Onboarding InfoBoard...
echo.

REM Change to the directory where this batch file is located
cd /d "%~dp0"

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    echo.
    pause
    exit /b 1
)

REM Install required packages if needed
echo Installing/checking required packages...
pip install -r requirements.txt --quiet

REM Run the InfoBoard application
echo.
echo Running InfoBoard...
python dashboard.py

REM Pause to see any error messages
if errorlevel 1 (
    echo.
    echo Application ended with an error.
    pause
)
