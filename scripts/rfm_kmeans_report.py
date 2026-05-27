import os
import sys
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter


# ==============================
# RFM 與 K-means 客群分析報表產生工具
# ==============================

INPUT_DIR = "input"
OUTPUT_DIR = "output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "客群分析結果報表.xlsx")

SALES_REQUIRED_COLUMNS = ["客戶名稱", "銷貨日期", "銷售金額"]
CUSTOMER_REQUIRED_COLUMNS = ["客戶名稱"]


def print_title():
    print("=" * 60)
    print("RFM 與 K-means 客群分析報表產生工具")
    print("=" * 60)


def ensure_folders():
    if not os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR)

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)


def find_excel_files(input_dir):
    files = []

    for file in os.listdir(input_dir):
        if file.endswith(".xlsx") and not file.startswith("~$"):
            files.append(os.path.join(input_dir, file))

    return files


def read_excel_first_sheet(file_path):
    try:
        return pd.read_excel(file_path)
    except Exception as e:
        print(f"讀取 Excel 失敗：{file_path}")
        print(f"錯誤訊息：{e}")
        return None


def detect_sales_and_customer_files(excel_files):
    sales_file = None
    customer_file = None

    for file in excel_files:
        df = read_excel_first_sheet(file)

        if df is None:
            continue

        columns = list(df.columns)

        if all(col in columns for col in SALES_REQUIRED_COLUMNS):
            sales_file = file

        elif all(col in columns for col in CUSTOMER_REQUIRED_COLUMNS):
            customer_file = file

    return sales_file, customer_file


def safe_qcut(series, q=5):
    """
    安全版 qcut：
    避免資料筆數太少或重複值太多導致 qcut 錯誤。
    """
    try:
        return pd.qcut(
            series.rank(method="first"),
            q,
            labels=list(range(1, q + 1))
        ).astype(int)

    except Exception:
        try:
            return pd.cut(
                series.rank(method="first"),
                bins=q,
                labels=list(range(1, q + 1)),
                include_lowest=True
            ).astype(int)

        except Exception:
            return pd.Series([3] * len(series), index=series.index)


def create_segment_summary(result_df, customer_col):
    total_sales = result_df["Monetary"].sum()

    segment_summary = result_df.groupby("客戶類型").agg(
        客戶數=(customer_col, "count"),
        銷售金額=("Monetary", "sum"),
        平均RFM分數=("RFM_Total", "mean")
    ).reset_index()

    if total_sales > 0:
        segment_summary["銷售占比"] = segment_summary["銷售金額"] / total_sales
    else:
        segment_summary["銷售占比"] = 0

    return segment_summary


def format_excel(file_path):
    """
    簡單美化 Excel：
    - 標題列加粗
    - 凍結窗格
    - 自動欄寬
    - 數字格式
    """
    wb = load_workbook(file_path)

    header_fill = PatternFill("solid", fgColor="D9EAF7")
    header_font = Font(bold=True)
    center_alignment = Alignment(horizontal="center", vertical="center")

    for ws in wb.worksheets:
        ws.freeze_panes = "A2"

        for cell in ws[1]:
            cell.fill = header_fill
            cell.font = header_font
            cell.alignment = center_alignment

        for col in ws.columns:
            max_length = 0
            col_letter = get_column_letter(col[0].column)

            for cell in col:
                try:
                    value = str(cell.value) if cell.value is not None else ""
                    if len(value) > max_length:
                        max_length = len(value)
                except Exception:
                    pass

            adjusted_width = min(max_length + 4, 35)
            ws.column_dimensions[col_letter].width = adjusted_width

        for row in ws.iter_rows():
            for cell in row:
                if isinstance(cell.value, (int, float)):
                    if "金額" in str(ws.cell(row=1, column=cell.column).value) or \
                       "Monetary" in str(ws.cell(row=1, column=cell.column).value):
                        cell.number_format = '#,##0'
                    elif "占比" in str(ws.cell(row=1, column=cell.column).value):
                        cell.number_format = '0.00%'
                    else:
                        cell.number_format = '0.00'

    wb.save(file_path)


def main():
    print_title()
    ensure_folders()

    excel_files = find_excel_files(INPUT_DIR)

    if len(excel_files) == 0:
        print("找不到 Excel 檔案。")
        print("請將銷貨資料與客戶資料放入 input 資料夾後，再重新執行。")
        input("按 Enter 結束...")
        sys.exit(1)

    print("已找到以下 Excel 檔案：")
    for file in excel_files:
        print(f"- {file}")

    sales_file, customer_file = detect_sales_and_customer_files(excel_files)

    if sales_file is None:
        print("\n找不到銷貨資料檔案。")
        print("銷貨資料至少需要包含以下欄位：")
        print("、".join(SALES_REQUIRED_COLUMNS))
        input("按 Enter 結束...")
        sys.exit(1)

    if customer_file is None:
        print("\n找不到客戶資料檔案，將只使用銷貨資料進行分析。")
    else:
        print(f"\n偵測到客戶資料：{customer_file}")

    print(f"偵測到銷貨資料：{sales_file}")

    customer_col = "客戶名稱"
    date_col = "銷貨日期"
    amount_col = "銷售金額"

    sales_df = pd.read_excel(sales_file)

    if customer_file:
        customer_df = pd.read_excel(customer_file)
    else:
        customer_df = pd.DataFrame(columns=[customer_col])

    # ==============================
    # 1. 基本資料清理
    # ==============================
    sales_df = sales_df.dropna(subset=[customer_col])
    sales_df[date_col] = pd.to_datetime(sales_df[date_col], errors="coerce")
    sales_df[amount_col] = pd.to_numeric(sales_df[amount_col], errors="coerce")

    sales_df = sales_df.dropna(subset=[date_col, amount_col])

    positive_sales = sales_df[sales_df[amount_col] > 0].copy()
    negative_sales = sales_df[sales_df[amount_col] <= 0].copy()

    if positive_sales.empty:
        print("銷貨資料中沒有正向銷售金額，無法計算 RFM。")
        input("按 Enter 結束...")
        sys.exit(1)

    analysis_date = positive_sales[date_col].max()

    # ==============================
    # 2. RFM 計算
    # ==============================
    rfm = positive_sales.groupby(customer_col).agg(
        LastPurchaseDate=(date_col, "max"),
        Frequency=(date_col, "count"),
        Monetary=(amount_col, "sum")
    ).reset_index()

    rfm["Recency"] = (analysis_date - rfm["LastPurchaseDate"]).dt.days

    # ==============================
    # 3. RFM 分數
    # ==============================
    # Recency 越小越好，因此使用負值讓最近購買者分數較高。
    rfm["R_Score"] = safe_qcut(-rfm["Recency"], 5)
    rfm["F_Score"] = safe_qcut(rfm["Frequency"], 5)
    rfm["M_Score"] = safe_qcut(rfm["Monetary"], 5)

    rfm["RFM_Total"] = rfm["R_Score"] + rfm["F_Score"] + rfm["M_Score"]

    # ==============================
    # 4. K-means 分群
    # ==============================
    customer_count = len(rfm)
    cluster_count = 3 if customer_count >= 3 else customer_count

    if cluster_count >= 2:
        features = rfm[["R_Score", "F_Score", "M_Score"]]

        scaler = StandardScaler()
        features_scaled = scaler.fit_transform(features)

        kmeans = KMeans(n_clusters=cluster_count, random_state=42, n_init=10)
        rfm["Cluster"] = kmeans.fit_predict(features_scaled)

        cluster_summary = rfm.groupby("Cluster")[[
            "R_Score",
            "F_Score",
            "M_Score",
            "RFM_Total",
            "Monetary",
            "Frequency",
            "Recency"
        ]].mean().reset_index()

        cluster_order = cluster_summary.sort_values(
            by="RFM_Total",
            ascending=False
        )["Cluster"].tolist()

        if cluster_count == 3:
            segment_map = {
                cluster_order[0]: "高價值客戶",
                cluster_order[1]: "一般客戶",
                cluster_order[2]: "可能流失客戶"
            }
        else:
            segment_map = {
                cluster_order[0]: "較高價值客戶",
                cluster_order[1]: "需追蹤客戶"
            }

        rfm["客戶類型"] = rfm["Cluster"].map(segment_map)

    else:
        rfm["Cluster"] = 0
        rfm["客戶類型"] = "單一客戶"

        cluster_summary = rfm.groupby("Cluster")[[
            "R_Score",
            "F_Score",
            "M_Score",
            "RFM_Total",
            "Monetary",
            "Frequency",
            "Recency"
        ]].mean().reset_index()

    # ==============================
    # 5. 合併客戶資料
    # ==============================
    if not customer_df.empty and customer_col in customer_df.columns:
        result = rfm.merge(customer_df, on=customer_col, how="left")
    else:
        result = rfm.copy()

    result = result.sort_values(by="RFM_Total", ascending=False)

    # ==============================
    # 6. 摘要資料
    # ==============================
    total_customers = len(result)
    total_sales = result["Monetary"].sum()

    overview = pd.DataFrame({
        "項目": [
            "分析基準日",
            "總客戶數",
            "正向銷售總金額",
            "負值或退貨資料筆數",
            "銷貨資料檔案",
            "客戶資料檔案",
            "輸出報表"
        ],
        "內容": [
            str(analysis_date.date()),
            total_customers,
            total_sales,
            len(negative_sales),
            os.path.basename(sales_file),
            os.path.basename(customer_file) if customer_file else "未提供",
            OUTPUT_FILE
        ]
    })

    segment_summary = create_segment_summary(result, customer_col)

    # ==============================
    # 7. 輸出 Excel
    # ==============================
    with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
        overview.to_excel(writer, sheet_name="報表總覽", index=False)
        result.to_excel(writer, sheet_name="客群分析結果", index=False)
        cluster_summary.to_excel(writer, sheet_name="分群摘要", index=False)
        segment_summary.to_excel(writer, sheet_name="客戶類型摘要", index=False)

        high_value_df = result[result["客戶類型"].str.contains("高價值", na=False)]
        follow_up_df = result[result["客戶類型"].str.contains("流失|追蹤", na=False)]

        high_value_df.to_excel(writer, sheet_name="高價值客戶", index=False)
        follow_up_df.to_excel(writer, sheet_name="需追蹤客戶", index=False)

        if not negative_sales.empty:
            negative_sales.to_excel(writer, sheet_name="負值或退貨資料", index=False)

    format_excel(OUTPUT_FILE)

    print("\n報表產生完成！")
    print(f"輸出位置：{OUTPUT_FILE}")
    print("\n請至 output 資料夾查看 Excel 報表。")
    input("\n按 Enter 結束...")


if __name__ == "__main__":
    main()
