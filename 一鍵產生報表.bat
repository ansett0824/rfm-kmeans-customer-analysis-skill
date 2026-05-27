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

echo ========================================== > output\run_log.txt
echo RFM 與 K-means 客群分析報表產生工具 >> output\run_log.txt
echo 執行位置：%cd% >> output\run_log.txt
echo ========================================== >> output\run_log.txt
echo. >> output\run_log.txt

echo ==========================================
echo RFM 與 K-means 客群分析報表產生工具
echo ==========================================
echo.
echo 目前執行位置：
echo %cd%
echo.

echo [1/5] 檢查資料夾與檔案...
echo [1/5] 檢查資料夾與檔案... >> output\run_log.txt

echo.
echo input 資料夾內的檔案：
dir input
echo. >> output\run_log.txt
echo input 資料夾內的檔案： >> output\run_log.txt
dir input >> output\run_log.txt

echo.
echo 請確認 Excel 檔案已放入 input 資料夾。
echo 若 Excel 檔案正在開啟，請先關閉 Excel 後再執行。
echo.
pause

echo.
echo [2/5] 檢查 Python 是否可用...
echo [2/5] 檢查 Python 是否可用... >> output\run_log.txt

python --version >> output\run_log.txt 2>&1
if errorlevel 1 (
    echo python 指令不可用，嘗試使用 py 指令...
    echo python 指令不可用，嘗試使用 py 指令... >> output\run_log.txt

    py --version >> output\run_log.txt 2>&1
    if errorlevel 1 (
        echo.
        echo 找不到 Python。
        echo 請先安裝 Python，並在安裝時勾選 Add python.exe to PATH。
        echo.
        echo 找不到 Python。 >> output\run_log.txt
        pause
        exit /b 1
    )

    set PYTHON_CMD=py
) else (
    set PYTHON_CMD=python
)

echo.
echo 使用 Python 指令：%PYTHON_CMD%
echo 使用 Python 指令：%PYTHON_CMD% >> output\run_log.txt

echo.
echo [3/5] 檢查必要檔案...
echo [3/5] 檢查必要檔案... >> output\run_log.txt

if not exist requirements.txt (
    echo 找不到 requirements.txt
    echo 找不到 requirements.txt >> output\run_log.txt
    pause
    exit /b 1
)

if not exist scripts\rfm_kmeans_report.py (
    echo 找不到 scripts\rfm_kmeans_report.py
    echo 找不到 scripts\rfm_kmeans_report.py >> output\run_log.txt
    pause
    exit /b 1
)

echo requirements.txt 存在
echo scripts\rfm_kmeans_report.py 存在
echo requirements.txt 存在 >> output\run_log.txt
echo scripts\rfm_kmeans_report.py 存在 >> output\run_log.txt

echo.
echo [4/5] 安裝必要套件...
echo [4/5] 安裝必要套件... >> output\run_log.txt

%PYTHON_CMD% -m pip install -r requirements.txt >> output\run_log.txt 2>&1

if errorlevel 1 (
    echo.
    echo 套件安裝失敗。
    echo 請查看 output\run_log.txt。
    echo.
    echo 套件安裝失敗。 >> output\run_log.txt
    pause
    exit /b 1
)

echo.
echo [5/5] 開始產生客群分析報表...
echo [5/5] 開始產生客群分析報表... >> output\run_log.txt

%PYTHON_CMD% scripts\rfm_kmeans_report.py >> output\run_log.txt 2>&1

if errorlevel 1 (
    echo.
    echo 報表產生失敗。
    echo 請查看：
    echo output\run_log.txt
    echo output\error_log.txt
    echo.
    echo 報表產生失敗。 >> output\run_log.txt
    pause
    exit /b 1
)

echo.
echo ==========================================
echo 執行完成
echo 報表應已產生在 output 資料夾
echo 檔案名稱：客群分析結果報表.xlsx
echo ==========================================
echo.

echo 執行完成 >> output\run_log.txt
echo 報表應已產生在 output 資料夾 >> output\run_log.txt

pause
