@echo off
echo ========================================
echo Smart Onboarding InfoBoard Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python from https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo Python detected successfully!
echo.

echo Installing required packages...
pip install -r requirements.txt

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo To run the InfoBoard:
echo 1. Double-click 'start_infoboard.bat'
echo 2. Or run: python dashboard.py
echo.
echo To auto-start with Windows:
echo 1. Copy 'start_infoboard.bat' to Windows Startup folder
echo 2. Press Win+R, type: shell:startup, press Enter
echo 3. Copy the batch file to that folder
echo.
pause
