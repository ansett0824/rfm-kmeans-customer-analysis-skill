@echo off
setlocal
cd /d "%~dp0"

if not exist input mkdir input
if not exist output mkdir output

echo ==========================================
echo RFM K-means Customer Report Generator
echo ==========================================
echo.
echo Current folder:
echo %cd%
echo.

echo [1/5] Checking input files...
echo Files in input folder:
dir input
echo.

echo Please make sure Excel files are placed in the input folder.
echo Close Excel files before running this tool.
echo.
pause

echo.
echo [2/5] Checking Python...
python --version

if errorlevel 1 (
    echo.
    echo Python was not found.
    echo Please install Python and check Add python.exe to PATH during installation.
    echo.
    pause
    exit /b 1
)

echo.
echo [3/5] Checking required files...

if not exist requirements.txt (
    echo requirements.txt not found.
    pause
    exit /b 1
)

if not exist scripts\rfm_kmeans_report.py (
    echo scripts\rfm_kmeans_report.py not found.
    pause
    exit /b 1
)

echo requirements.txt found.
echo scripts\rfm_kmeans_report.py found.

echo.
echo [4/5] Installing required packages...
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo Package installation failed.
    echo Please check Python, pip, and internet connection.
    echo.
    pause
    exit /b 1
)

echo.
echo [5/5] Generating report...
python scripts\rfm_kmeans_report.py

if errorlevel 1 (
    echo.
    echo Report generation failed.
    echo Please check output\error_log.txt if it exists.
    echo.
    pause
    exit /b 1
)

echo.
echo ==========================================
echo Done.
echo Please check output folder.
echo Output file: customer segmentation report Excel
echo ==========================================
echo.

pause
