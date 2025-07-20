# Create content.txt file
content_txt = """# Smart Onboarding InfoBoard Content File
# Add your welcome messages under [MESSAGES]
# Add QR code links under [QR_LINKS] in format: Title|URL

[MESSAGES]
🎉 Welcome to TechCorp! We're excited to have you join our team!
📚 Don't forget to complete your onboarding checklist
💼 Your manager will reach out to you within 24 hours
🏢 Building tour starts at 10 AM - meet at reception
🍕 Join us for lunch at 12:30 PM in the cafeteria
🎯 Visit our Learning Management System for training modules
📞 IT Helpdesk is available 24/7 for technical support
🌟 Ask questions, explore, and make yourself at home!

[QR_LINKS]
Company LMS|https://www.tcs.com/careers
IT Helpdesk|https://helpdesk.company.com
Employee Portal|https://portal.company.com
"""

with open("content.txt", "w", encoding="utf-8") as f:
    f.write(content_txt)

print("✅ Created content.txt")

# Create requirements.txt file
requirements_txt = """opencv-python==4.8.1.78
qrcode==7.4.2
Pillow==10.0.1
numpy==1.24.3
"""

with open("requirements.txt", "w", encoding="utf-8") as f:
    f.write(requirements_txt)

print("✅ Created requirements.txt")

# Create a batch file for Windows auto-start
batch_file_content = """@echo off
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
"""

with open("start_infoboard.bat", "w", encoding="utf-8") as f:
    f.write(batch_file_content)

print("✅ Created start_infoboard.bat")

# Create install.bat for easy setup
install_batch = """@echo off
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
"""

with open("install.bat", "w", encoding="utf-8") as f:
    f.write(install_batch)

print("✅ Created install.bat")