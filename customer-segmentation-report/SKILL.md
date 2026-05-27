---
name: customer-segmentation-report
description: Use this skill when creating customer segmentation reports from sales data and customer data. This skill supports RFM analysis, K-means clustering, Excel report planning, and a direct Python execution workflow.
---

# Customer Segmentation Report Skill

## Purpose

This skill helps transform raw sales data and customer data into a structured customer segmentation report.

It supports two usage modes:

1. AI-guided workflow: guides the assistant through data inspection, RFM scoring, K-means clustering, customer segment labeling, Excel report planning, visualization design, and management recommendations.
2. Direct execution workflow: allows users to download the repository ZIP, place Excel files into the `input` folder, and run `一鍵產生報表.bat` to generate an Excel customer segmentation report.

This skill is suitable for business analysis, customer value classification, customer follow-up planning, and management reporting.

## Repository Execution Files

This repository includes:

- `一鍵產生報表.bat`: one-click execution file for Windows users
- `requirements.txt`: Python package requirements
- `scripts/rfm_kmeans_report.py`: main Python program for RFM and K-means analysis
- `input/`: folder for placing sales data and customer data Excel files
- `output/`: folder for generated customer segmentation report

## Direct Execution Workflow

Use this workflow when the user wants to run the tool directly without asking AI to process the data.

### Step 1: Download the Repository

Download the repository ZIP from GitHub, then unzip the downloaded file.

### Step 2: Place Excel Files

Place sales data and customer data Excel files into the `input` folder.

The file names do not need to be fixed. The program detects files by required columns.

### Step 3: Required Excel Columns

The sales data must include at least:

- `客戶名稱`
- `銷貨日期`
- `銷售金額`

The customer data should include at least:

- `客戶名稱`

Optional columns may include:

- `地址`
- `地區`
- `聯絡電話`
- `產品名稱`
- `品號`
- `數量`
- `單價`

If optional columns exist, the program should preserve or merge them into the output report whenever possible.

### Step 4: Run the Tool

Double-click `一鍵產生報表.bat`.

The batch file should:

1. Check the `input` folder
2. Check whether Python is available
3. Install required packages from `requirements.txt`
4. Run `scripts/rfm_kmeans_report.py`
5. Generate the Excel report

### Step 5: Output Result

The generated report should be saved as:

- `output/客群分析結果報表.xlsx`

## When to Use This Skill

Use this skill when the user asks to:

- Analyze customer sales data
- Create a customer segmentation report
- Calculate RFM scores
- Classify customers into high-value, general, or at-risk groups
- Use K-means clustering for customer analysis
- Create an Excel-based customer analysis report
- Summarize customer contribution and purchasing behavior
- Provide management recommendations based on sales data
- Build a directly executable customer segmentation report generator

## Required Inputs

### Sales Data

Required fields:

- Customer name or customer ID
- Transaction date or month
- Sales amount

Recommended fields:

- Product name or item code
- Quantity
- Unit price
- Region or sales area

### Customer Data

Required field:

- Customer name or customer ID

Recommended fields:

- Region or address
- Contact information
- Customer type
- Responsible salesperson

## Standard Analysis Workflow

### Step 1: Data Inspection

Check whether the dataset includes the required columns:

- Customer identifier
- Sales amount
- Transaction date or month
- Quantity, if available
- Product information, if available

Identify missing columns, abnormal values, duplicated records, negative sales, blank customer names, and inconsistent formats.

If the file contains returns, discounts, or negative amounts, separate them from normal sales before calculating positive customer value.

### Step 2: Data Cleaning

Clean the data using the following principles:

- Standardize customer names
- Remove completely blank rows
- Convert amount fields into numeric format
- Convert date fields into date format
- Exclude negative sales from positive Monetary scoring
- Keep return records in a separate worksheet if needed
- Merge customer information by customer name or customer ID

### Step 3: RFM Calculation

Calculate the following indicators for each customer:

- Recency: how recently the customer purchased
- Frequency: how often the customer purchased
- Monetary: how much the customer purchased

Suggested definitions:

- Recency: number of days or months since the most recent purchase
- Frequency: number of transactions or purchasing months
- Monetary: total positive sales amount

Use `references/rfm_scoring_rules.md` for scoring rules.

### Step 4: RFM Scoring

Convert RFM indicators into scores.

Recommended scoring direction:

- R Score: more recent purchase gets a higher score
- F Score: higher transaction frequency gets a higher score
- M Score: higher purchase amount gets a higher score

The default score range is 1 to 5.

If extreme Monetary values exist, consider percentile scoring, logarithmic transformation, capped values, or separate review for extremely high-value customers.

### Step 5: K-means Clustering

Use RFM scores or standardized RFM indicators as clustering features.

Recommended features:

- R score
- F score
- M score
- Total sales amount
- Transaction frequency
- Product diversity, if available
- Region, if encoded or summarized

Before applying K-means:

- Remove invalid rows
- Standardize numeric variables
- Decide the number of clusters
- Use random_state for reproducibility

Recommended default number of clusters: 3.

Suggested cluster labels:

1. High-value customers
2. General customers
3. At-risk or inactive customers

Use `references/customer_segment_definitions.md` for labeling logic.

### Step 6: Customer Segment Labeling

After clustering, label each group according to its average RFM characteristics.

High-value customers usually have:

- High Monetary
- High Frequency
- Recent purchases
- Large sales contribution

General customers usually have:

- Medium Monetary
- Medium Frequency
- Stable but not outstanding purchase behavior

At-risk customers usually have:

- Low Recency score
- Low Frequency
- Long time since last purchase
- Declining or inactive purchase behavior

Do not label clusters only by cluster number. Always interpret the average RFM profile of each cluster before assigning names.

### Step 7: Report Sheet Planning

The Excel report should include the following worksheets when possible:

1. Report Overview
2. Customer RFM Summary
3. Customer Segmentation Results
4. High-value Customer List
5. At-risk Customer List
6. Regional Sales Analysis
7. Product Sales Analysis
8. Charts and Dashboard
9. Data Quality Notes

Use `references/report_structure.md` for detailed report layout.

### Step 8: Visualization Planning

Recommended charts:

- Customer segment distribution chart
- Sales contribution by customer segment
- Top customers by sales amount
- RFM score distribution
- K-means cluster scatter plot
- Regional sales comparison
- Product sales ranking
- Pareto chart of customer contribution

Charts should be placed close to their related tables in the Excel report.

### Step 9: Management Summary

Generate a concise management summary including:

- Total number of customers
- Total sales amount
- Number and percentage of high-value customers
- Sales contribution of high-value customers
- Number of at-risk customers
- Key customer behavior patterns
- Suggested follow-up actions

The summary should be written in a business reporting tone, not only statistical language.

### Step 10: Recommendations

Provide recommendations based on each customer group.

For high-value customers:

- Maintain relationship
- Provide priority service
- Track repeat purchase patterns
- Offer customized quotation or service

For general customers:

- Encourage repeat purchases
- Recommend related products
- Observe purchasing frequency changes

For at-risk customers:

- Check recent inactivity
- Contact customers with declining purchase frequency
- Review price, delivery, product, or service issues
- Design reactivation strategy

## Output Requirements

When using this skill, the assistant or the executable tool should provide:

1. Data inspection summary
2. RFM calculation result
3. Customer segmentation logic
4. Customer classification result
5. Excel worksheet output
6. Segment summary
7. High-value customer list
8. At-risk or follow-up customer list
9. Management-oriented explanation or recommendations

## Direct Execution Output

When using the executable workflow, the output Excel file should include:

- 報表總覽
- 客群分析結果
- 分群摘要
- 客戶類型摘要
- 高價值客戶
- 需追蹤客戶
- 負值或退貨資料

The output file should be saved as:

- `output/客群分析結果報表.xlsx`

## Writing Style

Use clear and formal business language.

When explaining to users, avoid overly technical explanations unless the user asks for details.

For academic or assignment use, explain the analysis steps clearly and sequentially.

For company reporting use, emphasize practical interpretation and management actions.

## Important Notes

- Do not treat K-means cluster numbers as fixed customer types.
- Always interpret each cluster based on its RFM averages.
- Exclude negative sales from positive customer value calculation unless the user requests otherwise.
- If the dataset does not include dates, Recency cannot be calculated accurately.
- If customer identifiers are inconsistent, customer merging may affect the accuracy of the analysis.
- If product data is unavailable, product diversity and product preference analysis should be omitted.
- For direct execution, users must place Excel files into the `input` folder.
- The Windows batch file requires Python to be installed on the user's computer.
```
