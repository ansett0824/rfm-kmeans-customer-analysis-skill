# Customer Segment Definitions

## Purpose

This file defines how to interpret customer segments after RFM scoring and K-means clustering.

## Segment 1: High-value Customers

High-value customers usually have:

- High Monetary score
- High Frequency score
- High or medium Recency score
- Stable or repeated purchase behavior
- Large contribution to total sales

Recommended actions:

- Maintain close relationship
- Provide priority service
- Track future orders
- Offer customized quotation
- Avoid losing these customers to competitors

## Segment 2: General Customers

General customers usually have:

- Medium Monetary score
- Medium Frequency score
- Medium Recency score
- Stable but not outstanding purchase behavior

Recommended actions:

- Encourage repeat purchase
- Recommend related products
- Observe whether purchase amount increases or decreases
- Use them as potential growth customers

## Segment 3: At-risk Customers

At-risk customers usually have:

- Low Recency score
- Low Frequency score
- Low or declining Monetary score
- Long time since last purchase
- Possible decline in purchase intention

Recommended actions:

- Check whether the customer has stopped purchasing
- Contact the customer to understand reasons
- Review price, delivery, product, or service issues
- Use reactivation strategy if the customer still has potential

## Important Rule

Do not directly define Cluster 0, Cluster 1, or Cluster 2 as a fixed customer type.

K-means cluster numbers are arbitrary. The correct approach is to compare each cluster's average RFM values, then assign meaningful labels.
