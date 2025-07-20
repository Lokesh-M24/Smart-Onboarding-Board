# Smart Onboarding InfoBoard – Interactive Welcome Display for New Joiners

Welcome to the **Smart Onboarding InfoBoard** project!

This document contains all setup instructions, usage guides, and troubleshooting tips. If you prefer a printable version, open this file in any Markdown viewer (e.g., VS Code or GitHub) and choose **Print → Save as PDF**.

---

## 1  Overview
The InfoBoard is a Python application that rotates welcome messages and displays QR codes on a TV or monitor. It is designed for passive, full-screen display in office lobbies or training rooms.

Key features:
1. Rotating slides every few seconds (default 5 s)
2. Messages and QR links loaded from **content.txt**
3. Automatic QR-code generation (saved as **lms_qr.png**)
4. Keyboard shortcuts for manual control (`n`, `p`, `r`, `q`)
5. One-click Windows auto-start via **start_infoboard.bat**

---

## 2  Project Structure
```
Smart-Onboarding-InfoBoard/
├─ dashboard.py            ← main application script
├─ content.txt             ← editable messages + links
├─ lms_qr.png              ← QR code image (auto-generated)
├─ requirements.txt        ← Python dependencies
├─ start_infoboard.bat     ← run + auto-start script (copy to Startup)
├─ install.bat             ← one-time setup helper
└─ README.md               ← this file (export to PDF if needed)
```

---

## 3  Prerequisites
1. Windows 10/11 PC with Python 3.8 – 3.12
2. HDMI cable from PC to TV/monitor
3. Internet access for initial `pip install`

> Tip  If Python is missing, download the latest installer from https://python.org and **check “Add Python to PATH”**.

---

## 4  One-Time Installation
1. Open **PowerShell** or **Command Prompt** in the project folder.
2. Run:
   ```bat
   install.bat
   ```
   • Installs required packages (`opencv-python`, `qrcode`, `Pillow`, `numpy`)
   • Creates default *content.txt* (if missing)

3. Verify that **lms_qr.png** appears (auto-generated).

---

## 5 Running the InfoBoard
### 5.1 Quick Start (foreground)
```bat
python dashboard.py
```
Keyboard controls:
* `n` – next slide
* `p` – previous slide
* `r` – reload content.txt on-the-fly
* `q` / `Esc` – quit

### 5.2 Auto-Start With Windows
1. Press **Win + R**, type `shell:startup`, press **Enter**.
2. Copy **start_infoboard.bat** into the Startup folder.
3. Reboot → InfoBoard launches automatically.

To remove auto-start, delete the batch file from Startup.

---

## 6 Customising Slides
### 6.1 Editing Messages
Open **content.txt** and update the `[MESSAGES]` section. Each non-empty line becomes a separate slide.
```
[MESSAGES]
Welcome to ACME Corp!
Please complete your safety training today.
```

### 6.2 Adding / Changing QR Links
Under `[QR_LINKS]`, use `Title|URL` format—first link becomes the on-screen QR code.
```
[QR_LINKS]
HR Portal|https://hr.acme.com
Support Desk|https://support.acme.com
```
On next launch (or press `r`), **lms_qr.png** is regenerated automatically.

---

## 7 Adjusting Timings & Colours
Edit the constants near the top of *dashboard.py*:
```python
self.slide_duration = 5       # seconds per slide
self.bg_color = (240,248,255) # background BGR
self.text_color = (47,79,79)
```
RGB→BGR converter: (R,G,B) → (B,G,R)

---

## 8 Troubleshooting
| Issue | Solution |
|-------|----------|
| `ImportError: cv2` | Run `pip install -r requirements.txt` |
| Black window only | Check that messages exist in *content.txt* |
| QR code not visible | Ensure first link in `[QR_LINKS]` section has a valid URL |
| Script closes instantly | Run from Command Prompt to view traceback |

---

## 9 Uninstallation
1. Delete the project folder.
2. Remove **start_infoboard.bat** from Windows Startup (if copied).
3. Optionally remove Python packages:
   ```bat
   pip uninstall opencv-python qrcode Pillow numpy
   ```

---

© 2025 Smart Onboarding InfoBoard – MIT License
