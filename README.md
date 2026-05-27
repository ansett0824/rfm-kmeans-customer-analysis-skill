# RFM 與 K-means 客群分析報表 Skill

## 專案簡介

本專案是一個代表個人工作流程的 Skill，主要用於協助使用者將企業銷貨資料與客戶資料轉換成可供管理決策使用的「客群分析結果報表」。

此 Skill 會引導 AI 依序完成資料檢查、RFM 指標計算、K-means 客戶分群、客戶類型判定、Excel 報表規劃、圖表設計與管理建議產出。適合應用於中小企業銷售資料分析、客戶價值分層、客戶流失風險初步判斷與管理報表自動化。

## 設計動機

在企業資料分析與輔導過程中，常需要將原始銷貨資料整理成主管能理解的分析報表。然而，原始 Excel 資料通常欄位不一致、格式不統一，且缺乏明確的客戶分群與管理建議。

因此，本 Skill 將個人常用的客群分析流程整理成標準化工作流程，使 AI 可以依照固定步驟協助完成資料清理、RFM 分數計算、K-means 分群、圖表規劃與報表摘要撰寫。

## 主要功能

1. 檢查銷貨資料與客戶資料欄位
2. 整理客戶年度購買金額、交易頻率與最近交易時間
3. 計算 RFM 指標
4. 進行 K-means 客戶分群
5. 區分高價值客戶、一般客戶與可能流失客戶
6. 規劃 Excel 報表工作表與圖表
7. 產出主管可讀的分析摘要與管理建議

## 適用情境

- 銷售資料分析
- 客戶分群分析
- RFM 分析
- 中小企業管理報表
- Excel 自動化報表製作
- 客戶流失風險初步判斷

## 直接執行方式

本專案除了提供 Skill 文件外，也包含一份 Python 範例程式，可直接執行 RFM 與 K-means 客群分析。

### 1. 下載專案

可從 GitHub 點選：

Code → Download ZIP

下載後解壓縮。

### 2. 準備 Excel 檔案

請將銷貨資料與客戶資料放在專案最外層，並命名為：

```text
sales_data.xlsx
customer_data.xlsx


## Repository 結構

```text
rfm-kmeans-customer-analysis-skill/
├── README.md
├── requirements.txt
├── customer-segmentation-report/
│   ├── SKILL.md
│   └── references/
│       ├── rfm_scoring_rules.md
│       ├── report_structure.md
│       └── customer_segment_definitions.md
└── scripts/
    └── rfm_kmeans_report.py
