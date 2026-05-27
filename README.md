# RFM 與 K-means 客群分析報表 Skill

## 專案簡介

本專案是一個代表個人工作流程的 Skill，主要用於協助使用者將企業銷貨資料與客戶資料轉換成可供管理決策使用的「客群分析結果報表」。

此專案同時包含兩個部分：

1. `customer-segmentation-report/`：Skill 文件，說明客群分析的標準流程。
2. `scripts/rfm_kmeans_report.py` 與 `一鍵產生報表.bat`：可直接執行的客群分析報表產生工具。

使用者下載本專案 ZIP 並解壓縮後，只要將 Excel 檔案放入 `input/` 資料夾，再雙擊 `一鍵產生報表.bat`，即可自動執行 RFM 與 K-means 客群分析，並產生 Excel 報表。

---

## 設計動機

在企業資料分析與輔導過程中，常需要將原始銷貨資料整理成主管能理解的分析報表。然而，原始 Excel 資料通常欄位不一致、格式不統一，且缺乏明確的客戶分群與管理建議。

因此，本專案將個人常用的客群分析流程整理成標準化工作流程，並進一步提供可直接執行的 Python 程式，使使用者可以透過簡單操作完成資料清理、RFM 分數計算、K-means 分群、客戶類型判定與 Excel 報表產出。

---

## 主要功能

1. 檢查銷貨資料與客戶資料欄位
2. 整理客戶購買金額、交易頻率與最近交易時間
3. 計算 RFM 指標
4. 進行 K-means 客戶分群
5. 區分高價值客戶、一般客戶與可能流失客戶
6. 產出 Excel 客群分析結果報表
7. 提供主管可讀的分析摘要與客戶分類結果

---

## 適用情境

- 銷售資料分析
- 客戶分群分析
- RFM 分析
- K-means 客戶分群
- 中小企業管理報表
- Excel 自動化報表製作
- 客戶流失風險初步判斷

---

## Repository 結構

```text
rfm-kmeans-customer-analysis-skill/
├── README.md
├── 一鍵產生報表.bat
├── requirements.txt
├── input/
│   └── .gitkeep
├── output/
│   └── .gitkeep
├── scripts/
│   └── rfm_kmeans_report.py
└── customer-segmentation-report/
    ├── SKILL.md
    └── references/
        ├── rfm_scoring_rules.md
        ├── report_structure.md
        └── customer_segment_definitions.md
