@echo off
setlocal
cd /d "%~dp0"

echo Building Fadi Calculator 2.1...
py -m PyInstaller --noconfirm --clean --onefile --windowed --name "Fadi Calculator" --icon "fadi_calculator.ico" --add-data "index.html;." calculator.py

if errorlevel 1 (
    echo.
    echo BUILD FAILED. Please review the error messages above.
    pause
    exit /b 1
)

echo.
echo BUILD SUCCESSFUL.
echo Your application is:
echo %CD%\dist\Fadi Calculator.exe
echo.
pause
