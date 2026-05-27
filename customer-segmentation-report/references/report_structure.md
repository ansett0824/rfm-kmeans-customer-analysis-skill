# Customer Segmentation Report Structure

## Purpose

This file defines the recommended Excel report structure for the `customer-segmentation-report` Skill and the direct Python execution workflow.

The report structure is designed to help users understand customer value, customer segmentation results, and follow-up priorities based on RFM analysis and K-means clustering.

---

## Direct Execution Output Structure

When users run `一鍵產生報表.bat`, the Python program generates an Excel report named:

`output/客群分析結果報表.xlsx`

The default output report includes the following worksheets:

1. 報表總覽
2. 客群分析結果
3. 分群摘要
4. 客戶類型摘要
5. 高價值客戶
6. 需追蹤客戶
7. 負值或退貨資料

---

## 1. 報表總覽

### Purpose

Provide a quick summary for managers.

This worksheet helps users understand the overall analysis result without reading all detailed data.

### Suggested Contents

| Field | Description |
|---|---|
| 分析基準日 | The latest transaction date used as the reference date |
| 總客戶數 | Total number of customers included in the analysis |
| 正向銷售總金額 | Total positive sales amount |
| 負值或退貨資料筆數 | Number of negative sales or return records |
| 輸出報表 | Output file location |

### Management Meaning

This worksheet is suitable for quick review by managers. It summarizes the basic scale of the analysis, including customer count, total sales amount, and whether return or negative sales records exist.

---

## 2. 客群分析結果

### Purpose

Show the complete customer-level RFM analysis and customer segmentation result.

This is the main worksheet of the report.

### Suggested Columns

| Column | Description |
|---|---|
| 客戶名稱 | Customer name or customer identifier |
| LastPurchaseDate | Customer's most recent purchase date |
| Frequency | Number of purchases or transaction records |
| Monetary | Total positive sales amount |
| Recency | Days since the customer's most recent purchase |
| R_Score | Recency score |
| F_Score | Frequency score |
| M_Score | Monetary score |
| RFM_Total | Total RFM score |
| Cluster | K-means cluster number |
| 客戶類型 | Final customer segment label |

If customer data is provided, additional customer information may also appear in this worksheet, such as region, address, contact information, or customer type.

### Management Meaning

This worksheet allows users to review each customer's RFM performance and final segment classification.

It can be used to identify:

- High-value customers
- General customers
- Customers that require follow-up
- Customers with declining purchase behavior

---

## 3. 分群摘要

### Purpose

Show the average characteristics of each K-means cluster.

This worksheet is used to explain why each cluster is labeled as a certain customer type.

### Suggested Columns

| Column | Description |
|---|---|
| Cluster | K-means cluster number |
| R_Score | Average Recency score of the cluster |
| F_Score | Average Frequency score of the cluster |
| M_Score | Average Monetary score of the cluster |
| RFM_Total | Average total RFM score |
| Monetary | Average sales amount |
| Frequency | Average purchase frequency |
| Recency | Average recency value |

### Management Meaning

K-means cluster numbers do not have fixed business meanings. Therefore, this worksheet is used to compare the average RFM performance of each cluster and assign meaningful customer labels.

For example:

- The cluster with the highest average RFM total can be labeled as 高價值客戶.
- The cluster with the middle average RFM total can be labeled as 一般客戶.
- The cluster with the lowest average RFM total can be labeled as 可能流失客戶 or 需追蹤客戶.

---

## 4. 客戶類型摘要

### Purpose

Summarize the number of customers and sales contribution of each customer segment.

### Suggested Columns

| Column | Description |
|---|---|
| 客戶類型 | Customer segment label |
| 客戶數 | Number of customers in the segment |
| 銷售金額 | Total sales amount of the segment |
| 平均RFM分數 | Average RFM total score of the segment |
| 銷售占比 | Sales contribution ratio of the segment |

### Management Meaning

This worksheet helps managers understand the structure of customer value.

It can answer questions such as:

- Which customer group contributes the most sales?
- How many customers are classified as high-value customers?
- How many customers require follow-up?
- Is the sales contribution concentrated in a small number of customers?

---

## 5. 高價值客戶

### Purpose

List customers that should be prioritized for relationship management and sales follow-up.

### Suggested Columns

| Column | Description |
|---|---|
| 客戶名稱 | Customer name |
| Monetary | Total sales amount |
| Frequency | Purchase frequency |
| LastPurchaseDate | Most recent purchase date |
| RFM_Total | Total RFM score |
| 客戶類型 | Customer segment label |
| Additional customer fields | Region, address, contact information, or customer type if available |

### Management Meaning

High-value customers are important customers who usually have high purchase amount, high purchase frequency, or recent transaction behavior.

Suggested management actions:

- Maintain close relationship
- Provide priority service
- Track future orders
- Offer customized quotation
- Observe changes in purchase frequency
- Avoid losing these customers to competitors

---

## 6. 需追蹤客戶

### Purpose

List customers that may need follow-up or reactivation.

This worksheet may include customers labeled as `可能流失客戶` or `需追蹤客戶`.

### Suggested Columns

| Column | Description |
|---|---|
| 客戶名稱 | Customer name |
| LastPurchaseDate | Most recent purchase date |
| Recency | Days since last purchase |
| Frequency | Purchase frequency |
| Monetary | Total sales amount |
| RFM_Total | Total RFM score |
| 客戶類型 | Customer segment label |
| Additional customer fields | Region, address, contact information, or customer type if available |

### Management Meaning

These customers may have lower recent activity, lower purchase frequency, or lower total purchase amount.

Suggested management actions:

- Check whether the customer has stopped purchasing
- Contact the customer to understand reasons
- Review price, delivery, product, or service issues
- Compare past purchase behavior with recent purchase behavior
- Design reactivation strategy if the customer still has potential

---

## 7. 負值或退貨資料

### Purpose

Record negative sales, return records, or abnormal transaction values.

This worksheet is generated only when negative or zero sales records exist.

### Suggested Columns

This worksheet should preserve the original columns from the sales data.

### Management Meaning

Negative sales or return records should not be included in positive Monetary scoring because they may distort customer value calculation.

However, these records are still useful for reviewing:

- Return behavior
- Discount or adjustment records
- Abnormal sales data
- Data quality issues
- Customers with frequent return records

---

## Optional Worksheets for Future Improvement

The current direct execution tool generates the basic worksheets listed above.

In future versions, the report can be expanded with the following worksheets.

---

## Optional 1. Regional Sales Analysis

### Purpose

Analyze sales performance by region.

### Suggested Contents

- Sales amount by region
- Number of customers by region
- Customer segment distribution by region
- High-value customers by region
- At-risk customers by region

### Suggested Charts

- Bar chart of sales amount by region
- Pie chart of customer distribution by region
- Stacked bar chart of customer segment by region

---

## Optional 2. Product Sales Analysis

### Purpose

Analyze which products contribute more sales.

### Suggested Contents

- Top products by sales amount
- Top products by quantity
- Product preference by customer segment
- Product purchase frequency
- Product sales contribution ratio

### Suggested Charts

- Top product ranking chart
- Product sales Pareto chart
- Product preference by customer segment

---

## Optional 3. Charts and Dashboard

### Purpose

Place important visualizations in one dashboard sheet.

### Suggested Charts

- Customer segment distribution
- Sales contribution by segment
- Top 10 or Top 20 customers
- Pareto chart of customer contribution
- RFM score distribution
- K-means cluster scatter plot
- Regional sales comparison
- Product sales ranking

### Dashboard Design Notes

Charts should be placed close to their related tables.

The dashboard should be easy for managers to read and should avoid too many complicated statistical details.

---

## Optional 4. Data Quality Notes

### Purpose

Record data problems and assumptions.

### Suggested Contents

- Missing columns
- Missing customer names
- Negative sales records
- Duplicated records
- Date format issues
- Amount format issues
- Fields not available for analysis
- Assumptions used in the analysis

---

## Suggested Report Interpretation Order

When presenting the report, the recommended order is:

1. Start with `報表總覽` to explain the analysis scope.
2. Use `客戶類型摘要` to explain the overall customer structure.
3. Use `分群摘要` to explain why the clusters are labeled as different customer types.
4. Use `客群分析結果` to review detailed customer-level results.
5. Use `高價值客戶` to identify priority customers.
6. Use `需追蹤客戶` to identify customers that may require follow-up.
7. Use `負值或退貨資料` to explain excluded or abnormal records.

---

## Important Notes

- The Excel report structure should match the actual output of the Python program.
- K-means cluster numbers should not be interpreted directly.
- Customer segment labels should be assigned based on average RFM values.
- Negative sales and return records should be separated from positive Monetary scoring.
- If product or region columns are not available, product and regional analysis should be omitted.
- The report should focus on management interpretation, not only statistical calculation.
