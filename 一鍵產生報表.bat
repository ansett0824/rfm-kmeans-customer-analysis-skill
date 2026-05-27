@echo off
chcp 65001 >nul
title RFM 與 K-means 客群分析報表產生工具

echo ==========================================
echo RFM 與 K-means 客群分析報表產生工具
echo ==========================================
echo.

echo [1/4] 檢查 input 與 output 資料夾...
if not exist input (
    mkdir input
)

if not exist output (
    mkdir output
)

echo.
echo 請確認您的 Excel 檔案已放入 input 資料夾。
echo.
echo Excel 檔案需求：
echo - 銷貨資料需包含：客戶名稱、銷貨日期、銷售金額
echo - 客戶資料建議包含：客戶名稱
echo.
pause

echo.
echo [2/4] 檢查 Python 是否可用...
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo 找不到 Python，請先安裝 Python。
    echo 下載網址：https://www.python.org/downloads/
    echo 安裝時請勾選 Add python.exe to PATH。
    echo.
    pause
    exit /b
)

echo.
echo [3/4] 安裝必要套件...
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo 套件安裝失敗，請確認網路連線或 Python/pip 是否正常。
    echo.
    pause
    exit /b
)

echo.
echo [4/4] 開始產生客群分析報表...
python scripts/rfm_kmeans_report.py

if errorlevel 1 (
    echo.
    echo 報表產生失敗，請檢查 input 資料夾中的 Excel 欄位名稱是否正確。
    echo.
    echo 銷貨資料至少需要包含：
    echo 客戶名稱、銷貨日期、銷售金額
    echo.
    pause
    exit /b
)

echo.
echo ==========================================
echo 執行完成
echo 報表已產生在 output 資料夾
echo 檔案名稱：客群分析結果報表.xlsx
echo ==========================================
echo.
pause
