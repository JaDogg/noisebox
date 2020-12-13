@echo off
del *.spec >nul
pyinstaller noisebox.py --icon wind.ico --onefile