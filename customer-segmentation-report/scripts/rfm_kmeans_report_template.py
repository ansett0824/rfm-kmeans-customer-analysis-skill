import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# ==============================
# RFM 與 K-means 客群分析範例程式
# ==============================

# 1. 讀取資料
sales_file = "sales_data.xlsx"
customer_file = "customer_data.xlsx"

sales_df = pd.read_excel(sales_file)
customer_df = pd.read_excel(customer_file)

# 2. 欄位名稱設定
customer_col = "客戶名稱"
date_col = "銷貨日期"
amount_col = "銷售金額"

# 3. 基本資料清理
sales_df = sales_df.dropna(subset=[customer_col])
sales_df[date_col] = pd.to_datetime(sales_df[date_col], errors="coerce")
sales_df[amount_col] = pd.to_numeric(sales_df[amount_col], errors="coerce")

# 排除負值銷售金額，避免退貨影響正向客戶價值
positive_sales = sales_df[sales_df[amount_col] > 0].copy()

# 4. 設定分析基準日
analysis_date = positive_sales[date_col].max()

# 5. 計算 RFM 指標
rfm = positive_sales.groupby(customer_col).agg(
    LastPurchaseDate=(date_col, "max"),
    Frequency=(date_col, "count"),
    Monetary=(amount_col, "sum")
).reset_index()

rfm["Recency"] = (analysis_date - rfm["LastPurchaseDate"]).dt.days

# 6. RFM 分數計算
# Recency 越小越好，所以使用 ascending=False 讓最近購買者分數較高
rfm["R_Score"] = pd.qcut(
    rfm["Recency"].rank(method="first", ascending=False),
    5,
    labels=[1, 2, 3, 4, 5]
).astype(int)

rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    5,
    labels=[1, 2, 3, 4, 5]
).astype(int)

rfm["M_Score"] = pd.qcut(
    rfm["Monetary"].rank(method="first"),
    5,
    labels=[1, 2, 3, 4, 5]
).astype(int)

rfm["RFM_Total"] = rfm["R_Score"] + rfm["F_Score"] + rfm["M_Score"]

# 7. K-means 分群
features = rfm[["R_Score", "F_Score", "M_Score"]]

scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
rfm["Cluster"] = kmeans.fit_predict(features_scaled)

# 8. 根據各群平均 RFM 表現命名客群
cluster_summary = rfm.groupby("Cluster")[["R_Score", "F_Score", "M_Score", "RFM_Total", "Monetary"]].mean()

# 依照 RFM_Total 平均值排序
cluster_order = cluster_summary["RFM_Total"].sort_values(ascending=False).index.tolist()

segment_map = {
    cluster_order[0]: "高價值客戶",
    cluster_order[1]: "一般客戶",
    cluster_order[2]: "可能流失客戶"
}

rfm["CustomerSegment"] = rfm["Cluster"].map(segment_map)

# 9. 合併客戶資料
result = rfm.merge(customer_df, on=customer_col, how="left")

# 10. 輸出 Excel
output_file = "客群分析結果報表.xlsx"

with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    result.to_excel(writer, sheet_name="客群分析結果", index=False)
    cluster_summary.to_excel(writer, sheet_name="分群摘要")
    
    result[result["CustomerSegment"] == "高價值客戶"].to_excel(
        writer,
        sheet_name="高價值客戶",
        index=False
    )
    
    result[result["CustomerSegment"] == "可能流失客戶"].to_excel(
        writer,
        sheet_name="可能流失客戶",
        index=False
    )

print(f"報表已產生：{output_file}")
