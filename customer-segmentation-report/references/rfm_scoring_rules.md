# RFM Scoring Rules

## RFM Definition

RFM is used to measure customer value based on three indicators:

- R: Recency
- F: Frequency
- M: Monetary

## Recency

Recency measures how recently a customer purchased.

A customer who purchased more recently should receive a higher score.

Example scoring:

| Recency condition | R score |
|---|---:|
| Purchased most recently | 5 |
| Purchased recently | 4 |
| Medium recency | 3 |
| Long time since purchase | 2 |
| No recent purchase | 1 |

If monthly data is used, the latest month in the dataset can be used as the reference month.

## Frequency

Frequency measures how often a customer purchased.

A customer with more transactions or more purchasing months should receive a higher score.

Example scoring:

| Frequency condition | F score |
|---|---:|
| Very high frequency | 5 |
| High frequency | 4 |
| Medium frequency | 3 |
| Low frequency | 2 |
| Very low frequency | 1 |

## Monetary

Monetary measures the customer's total positive sales amount.

A customer with higher total purchase amount should receive a higher score.

Example scoring:

| Monetary condition | M score |
|---|---:|
| Very high purchase amount | 5 |
| High purchase amount | 4 |
| Medium purchase amount | 3 |
| Low purchase amount | 2 |
| Very low purchase amount | 1 |

## Suggested Scoring Method

The default method is percentile scoring.

For example:

| Percentile range | Score |
|---|---:|
| Top 20% | 5 |
| 60% to 80% | 4 |
| 40% to 60% | 3 |
| 20% to 40% | 2 |
| Bottom 20% | 1 |

## Handling Extreme Values

If a few customers have extremely high sales amounts, Monetary scoring may be distorted.

Possible solutions:

1. Use percentile scoring
2. Apply logarithmic transformation
3. Cap values at an upper bound
4. Separate extreme high-value customers for independent review

## Negative Sales and Returns

Negative sales, returns, or discounts should not be included in positive Monetary scoring.

They can be stored in a separate return analysis worksheet.
