# RFM Scoring Rules

## Purpose

This file defines the RFM scoring rules used by the `customer-segmentation-report` Skill and the direct Python execution workflow.

RFM is used to measure customer value based on three indicators:

- R: Recency
- F: Frequency
- M: Monetary

The scoring result is used for customer segmentation and K-means clustering.

---

## Required Sales Data Columns

The sales data must include at least the following columns:

| Column | Description |
|---|---|
| 客戶名稱 | Customer name or customer identifier |
| 銷貨日期 | Sales or transaction date |
| 銷售金額 | Sales amount |

Optional fields may include product name, item code, quantity, unit price, region, or customer information.

---

## RFM Definition

### Recency

Recency measures how recently a customer purchased.

In this project, Recency is calculated as:

Recency = Analysis Date - Customer's Last Purchase Date

The analysis date is the latest transaction date in the sales dataset.

A smaller Recency value means the customer purchased more recently.

Therefore:

- Lower Recency value means better customer activity.
- More recent customers should receive higher R scores.
- Customers who have not purchased for a long time should receive lower R scores.

---

### Frequency

Frequency measures how often a customer purchased.

In this project, Frequency is calculated as the number of positive sales records for each customer.

A higher Frequency value means the customer purchased more often.

Therefore:

- Higher Frequency means stronger purchase activity.
- Customers with more transactions should receive higher F scores.

---

### Monetary

Monetary measures the total positive sales amount of each customer.

In this project, Monetary is calculated as:

Monetary = Sum of positive sales amount for each customer

Only positive sales amounts are included in Monetary scoring.

Negative sales, returns, discounts, or adjustment records should not be included in positive customer value calculation.

---

## RFM Scoring Direction

The default score range is 1 to 5.

| Score | Meaning |
|---|---|
| 5 | Best performance |
| 4 | Good performance |
| 3 | Medium performance |
| 2 | Low performance |
| 1 | Lowest performance |

---

## Recency Scoring Rule

Recency is different from Frequency and Monetary because a smaller value is better.

A customer who purchased more recently should receive a higher R score.

| Recency Condition | R Score |
|---|---:|
| Purchased most recently | 5 |
| Purchased recently | 4 |
| Medium recency | 3 |
| Long time since purchase | 2 |
| No recent purchase or longest inactivity | 1 |

In the Python program, Recency is converted so that customers with smaller Recency values receive higher scores.

---

## Frequency Scoring Rule

Frequency measures how often a customer purchased.

A customer with more transactions should receive a higher F score.

| Frequency Condition | F Score |
|---|---:|
| Very high frequency | 5 |
| High frequency | 4 |
| Medium frequency | 3 |
| Low frequency | 2 |
| Very low frequency | 1 |

---

## Monetary Scoring Rule

Monetary measures total positive sales amount.

A customer with higher total purchase amount should receive a higher M score.

| Monetary Condition | M Score |
|---|---:|
| Very high purchase amount | 5 |
| High purchase amount | 4 |
| Medium purchase amount | 3 |
| Low purchase amount | 2 |
| Very low purchase amount | 1 |

---

## Suggested Scoring Method

The default method is percentile-based scoring.

The data is divided into five groups, and scores are assigned from 1 to 5.

| Percentile Range | Score |
|---|---:|
| Top 20% | 5 |
| 60% to 80% | 4 |
| 40% to 60% | 3 |
| 20% to 40% | 2 |
| Bottom 20% | 1 |

This method is suitable when customer values are not evenly distributed.

---

## Handling Small Datasets or Duplicate Values

In some datasets, the number of customers may be small, or many customers may have the same value.

This may make percentile scoring difficult.

To avoid scoring errors, the Python program uses a safer scoring method:

1. Try percentile-based scoring first.
2. If percentile scoring fails, use rank-based interval scoring.
3. Keep the score range from 1 to 5 whenever possible.

This makes the report more stable when working with small or imperfect Excel datasets.

---

## RFM Total Score

After calculating R, F, and M scores, the total RFM score is calculated as:

RFM_Total = R_Score + F_Score + M_Score

The maximum score is 15, and the minimum score is 3.

| RFM Total | General Meaning |
|---|---|
| High total score | Strong customer value |
| Medium total score | General or stable customer |
| Low total score | Customer may require follow-up |

The RFM total score is used as one of the main references for customer segmentation.

---

## Negative Sales and Returns

Negative sales, returns, discounts, and adjustment records should not be included in positive Monetary scoring.

In the direct execution workflow:

- Records with `銷售金額 > 0` are used for RFM calculation.
- Records with `銷售金額 <= 0` are separated.
- Negative or zero sales records may be stored in the `負值或退貨資料` worksheet.

This prevents return records from distorting customer value calculation.

---

## Extreme Monetary Values

If a few customers have extremely high sales amounts, Monetary scoring may be distorted.

Possible solutions include:

1. Use percentile scoring.
2. Apply logarithmic transformation.
3. Cap values at an upper bound.
4. Separate extremely high-value customers for independent review.
5. Compare Monetary score with Frequency and Recency before making decisions.

For this project, percentile-based scoring is used as the default method because it is simple and suitable for business reporting.

---

## Relationship with K-means Clustering

The RFM scores are used as clustering features for K-means.

The common clustering features are:

- R_Score
- F_Score
- M_Score

K-means then groups customers based on their RFM similarity.

After clustering, the average RFM values of each cluster should be reviewed before assigning business labels.

Do not directly interpret Cluster 0, Cluster 1, or Cluster 2 as fixed customer types.

---

## Suggested Interpretation

A customer with high R, high F, and high M scores is usually a high-value customer.

A customer with medium RFM scores is usually a general customer.

A customer with low R, low F, or low M scores may require follow-up.

However, the final customer type should be interpreted together with:

- Total purchase amount
- Transaction frequency
- Last purchase date
- Cluster average values
- Business context
- Product or regional information, if available

---

## Important Notes

- Recency must be interpreted in the opposite direction from Frequency and Monetary.
- A smaller Recency value means better recent activity.
- Negative sales should be separated from positive Monetary scoring.
- Percentile scoring is suitable for most customer datasets.
- If the dataset is too small, the scoring result should be interpreted carefully.
- RFM scores are management references, not absolute judgments.
