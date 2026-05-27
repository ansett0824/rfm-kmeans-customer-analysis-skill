@echo off
chcp 65001 >nul
title RFM 與 K-means 客群分析報表產生工具

cd /d "%~dp0"

if not exist input (
    mkdir input
)

if not exist output (
    mkdir output
)

echo ==========================================
echo RFM 與 K-means 客群分析報表產生工具
echo ==========================================
echo.

echo 目前執行位置：
echo %cd%
echo.

echo [1/5] 檢查 input 資料夾...
echo input 資料夾內的檔案：
dir input
echo.

echo 請確認 Excel 檔案已放入 input 資料夾。
echo 若 Excel 檔案正在開啟，請先關閉 Excel 後再執行。
echo.
pause

echo.
echo [2/5] 檢查 Python 是否可用...
python --version

if errorlevel 1 (
    echo.
    echo 找不到 Python，請先安裝 Python。
    echo 安裝時請勾選 Add python.exe to PATH。
    echo.
    pause
    exit /b 1
)

echo.
echo [3/5] 檢查必要檔案...

if not exist requirements.txt (
    echo 找不到 requirements.txt
    pause
    exit /b 1
)

if not exist scripts\rfm_kmeans_report.py (
    echo 找不到 scripts\rfm_kmeans_report.py
    pause
    exit /b 1
)

echo requirements.txt 存在
echo scripts\rfm_kmeans_report.py 存在

echo.
echo [4/5] 安裝必要套件...
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo 套件安裝失敗。
    echo 請確認 Python、pip 或網路連線是否正常。
    echo.
    pause
    exit /b 1
)

echo.
echo [5/5] 開始產生客群分析報表...
python scripts\rfm_kmeans_report.py

if errorlevel 1 (
    echo.
    echo 報表產生失敗。
    echo 請查看 output 資料夾內是否有 error_log.txt。
    echo.
    pause
    exit /b 1
)

echo.
echo ==========================================
echo 執行完成
echo 報表已產生在 output 資料夾
echo 檔案名稱：客群分析結果報表.xlsx
echo ==========================================
echo.

pause
