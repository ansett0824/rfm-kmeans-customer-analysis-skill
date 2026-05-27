---
name: customer-segmentation-report
description: Use this skill when the user needs to create a customer segmentation report from sales data and customer data. This skill guides the assistant through data inspection, RFM scoring, K-means clustering, customer segment labeling, Excel report planning, visualization design, and management recommendations.
---

# Customer Segmentation Report Skill

## Purpose

This skill helps transform raw sales data and customer data into a structured customer segmentation report. It is designed for business analysis, customer value classification, and management reporting.

The skill focuses on RFM analysis, K-means clustering, Excel report structure, chart planning, and business recommendations.

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

## Required Inputs

Ask the user to provide or confirm the following data when available:

1. Sales data
   - Customer name or customer ID
   - Transaction date or month
   - Sales amount
   - Product name or item code
   - Quantity
   - Unit price, if available

2. Customer data
   - Customer name or customer ID
   - Region or address
   - Contact information, if available
   - Customer type, if available

3. Analysis settings
   - Analysis period
   - Whether returns or negative sales should be excluded
   - Desired number of clusters for K-means
   - Report output format

If some fields are missing, continue with the available data and clearly explain the limitation.

## Standard Workflow

Follow this workflow whenever possible.

### Step 1: Data Inspection

Check whether the dataset includes the required columns:

- Customer identifier
- Sales amount
- Transaction date or month
- Quantity
- Product information

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

If extreme Monetary values exist, consider using percentile scoring, logarithmic transformation, or capped values to reduce the influence of outliers.

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

Recommended default number of clusters: 3

Suggested cluster labels:

1. High-value customers
2. General customers
3. At-risk or inactive customers

Use `references/customer_segment_definitions.md` for labeling logic.

### Step 6: Customer Segment Labeling

After clustering, label each group according to its average RFM characteristics.

Example logic:

- High-value customers:
  - High Monetary
  - High Frequency
  - Recent purchases

- General customers:
  - Medium Monetary
  - Medium Frequency
  - Stable but not outstanding purchases

- At-risk customers:
  - Low Recency score
  - Low Frequency
  - Long time since last purchase

Do not label clusters only by cluster number. Always interpret the average RFM profile of each cluster before assigning names.

### Step 7: Report Sheet Planning

The Excel report should include the following worksheets:

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
- Top 10 or Top 20 customers by sales amount
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
- Review price, delivery, or service issues
- Design reactivation strategy

## Output Requirements

When using this skill, the assistant should provide:

1. Data inspection summary
2. RFM calculation explanation
3. Customer segmentation logic
4. Suggested Excel worksheet structure
5. Suggested charts
6. Customer classification rules
7. Management summary
8. Actionable recommendations
9. Python implementation guidance, if requested

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
