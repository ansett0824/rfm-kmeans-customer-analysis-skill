# Customer Segment Definitions

## Purpose

This file defines how to interpret customer segments after RFM scoring and K-means clustering.

It is used as a reference for the `customer-segmentation-report` Skill and the direct Python execution workflow. The purpose is to make customer segment labels easier to understand and connect the analysis result with practical management actions.

---

## Important Concept

K-means clustering only produces cluster numbers, such as Cluster 0, Cluster 1, and Cluster 2.

These cluster numbers do not have fixed business meanings.

Therefore, the correct approach is:

1. Calculate the average RFM values of each cluster.
2. Compare the RFM characteristics of each cluster.
3. Assign meaningful customer segment names based on the cluster profile.
4. Provide management recommendations for each customer type.

Do not directly define Cluster 0, Cluster 1, or Cluster 2 as a fixed customer type.

---

## Segment 1: High-value Customers

### Definition

High-value customers are customers who show strong customer value and stable purchasing behavior.

They usually have:

- High Monetary score
- High Frequency score
- High or medium Recency score
- Recent purchase behavior
- Stable or repeated transactions
- Large contribution to total sales

### Typical RFM Pattern

| Indicator | Expected Pattern |
|---|---|
| Recency | Recently purchased |
| Frequency | Purchases frequently |
| Monetary | High total purchase amount |
| RFM Total | High |

### Business Meaning

High-value customers are the most important customer group. Although they may not represent the largest number of customers, they usually contribute a high percentage of sales revenue.

This group should be treated as a priority customer group.

### Recommended Actions

- Maintain close relationship
- Provide priority service
- Track future orders
- Offer customized quotation
- Provide faster response or follow-up
- Observe changes in order frequency
- Avoid losing these customers to competitors

### Suggested Report Label

Recommended label in the Excel report: `高價值客戶`

---

## Segment 2: General Customers

### Definition

General customers are customers with stable but not outstanding purchasing behavior.

They usually have:

- Medium Monetary score
- Medium Frequency score
- Medium Recency score
- Stable but moderate purchase behavior
- Potential to become higher-value customers

### Typical RFM Pattern

| Indicator | Expected Pattern |
|---|---|
| Recency | Medium or acceptable |
| Frequency | Medium |
| Monetary | Medium |
| RFM Total | Medium |

### Business Meaning

General customers are the basic customer group of the company. They may not have the highest contribution, but they can provide stable sales.

This group can be developed through follow-up, product recommendation, or sales promotion.

### Recommended Actions

- Encourage repeat purchases
- Recommend related products
- Observe whether purchase amount increases or decreases
- Track changes in purchasing frequency
- Use them as potential growth customers
- Provide regular but not overly intensive follow-up

### Suggested Report Label

Recommended label in the Excel report: `一般客戶`

---

## Segment 3: At-risk Customers

### Definition

At-risk customers are customers whose purchasing behavior shows signs of decline or inactivity.

They usually have:

- Low Recency score
- Low Frequency score
- Low or declining Monetary score
- Long time since last purchase
- Possible decline in purchase intention
- Possible risk of customer loss

### Typical RFM Pattern

| Indicator | Expected Pattern |
|---|---|
| Recency | Long time since last purchase |
| Frequency | Low |
| Monetary | Low or declining |
| RFM Total | Low |

### Business Meaning

At-risk customers may have stopped purchasing or reduced their purchase frequency.

This group should be reviewed carefully because some customers may still have potential value but require follow-up.

### Recommended Actions

- Check whether the customer has stopped purchasing
- Contact the customer to understand reasons
- Review price, delivery, product, or service issues
- Compare past purchase behavior with recent purchase behavior
- Design reactivation strategy if the customer still has potential
- Avoid spending too many resources on customers with very low potential

### Suggested Report Label

Recommended label in the Excel report: `可能流失客戶`

Alternative label: `需追蹤客戶`

---

## Segment 4: Higher-value Customers

### Definition

If the dataset contains too few customers and K-means only creates two clusters, the highest scoring group can be labeled as higher-value customers instead of high-value customers.

This label is useful when the data size is small and the result should be interpreted more carefully.

### Typical RFM Pattern

| Indicator | Expected Pattern |
|---|---|
| Recency | Better than the other group |
| Frequency | Better than the other group |
| Monetary | Better than the other group |
| RFM Total | Higher than the other group |

### Suggested Report Label

Recommended label in the Excel report: `較高價值客戶`

---

## Segment 5: Follow-up Customers

### Definition

If the dataset contains too few customers and K-means only creates two clusters, the lower scoring group can be labeled as follow-up customers.

This label is safer than directly calling them at-risk customers because the sample size may be too small.

### Typical RFM Pattern

| Indicator | Expected Pattern |
|---|---|
| Recency | Lower than the other group |
| Frequency | Lower than the other group |
| Monetary | Lower than the other group |
| RFM Total | Lower than the other group |

### Suggested Report Label

Recommended label in the Excel report: `需追蹤客戶`

---

## Labeling Logic for Three Clusters

When there are enough customers and the model creates three clusters, the recommended labeling logic is:

1. The cluster with the highest average RFM total is labeled as `高價值客戶`.
2. The cluster with the middle average RFM total is labeled as `一般客戶`.
3. The cluster with the lowest average RFM total is labeled as `可能流失客戶` or `需追蹤客戶`.

| Cluster Ranking by Average RFM Total | Suggested Label |
|---|---|
| Highest | 高價值客戶 |
| Middle | 一般客戶 |
| Lowest | 可能流失客戶 / 需追蹤客戶 |

---

## Labeling Logic for Two Clusters

If the number of customers is too small and only two clusters are created, the recommended labeling logic is:

| Cluster Ranking by Average RFM Total | Suggested Label |
|---|---|
| Highest | 較高價值客戶 |
| Lowest | 需追蹤客戶 |

This avoids over-interpreting the result when the dataset is too small.

---

## Notes for Interpretation

When interpreting the customer segmentation result, do not rely only on the final customer label.

The following indicators should also be reviewed:

- Total purchase amount
- Transaction frequency
- Last purchase date
- RFM total score
- Cluster average values
- Product purchase pattern, if available
- Region or customer location, if available

A customer segment label should be treated as a management reference, not an absolute judgment.

---

## Example Explanation for Report

The customer segmentation result is based on RFM scores and K-means clustering. Since K-means cluster numbers do not have fixed business meanings, each cluster is interpreted according to its average Recency, Frequency, Monetary, and total RFM score.

Customers with higher RFM performance are labeled as high-value customers, customers with medium performance are labeled as general customers, and customers with lower or inactive purchasing behavior are labeled as at-risk or follow-up customers.

---

## Important Rule

K-means cluster numbers are arbitrary.

The correct approach is to compare each cluster's average RFM values, then assign meaningful labels according to the business meaning of each group.
