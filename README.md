# 🧴 Perfume Livestream Analytics

This project analyzes order and sales performance data from a perfume livestream store on TikTok. It aims to identify key purchasing patterns, high-impact products, and sales trends to support decision-making around restocking, scheduling, and campaign optimization.

---

## 📦 Data Source

- Raw data: `AllOrder_0701.csv` (TikTok 商家后台导出)
- Rows: 29,917
- Fields include: `SKU ID`, `Order Amount`, `SKU Unit Original Price`, `Quantity`, `Created Time`, `City`, etc.
- Cleaned and saved as:
  - `data/clean_orders.pkl`
  - `data/clean_orders.parquet`

---

## 🔄 Data Pipeline

```text
Raw CSV
   ↓
Column cleanup & amount computation
   ↓
✅ clean_orders.pkl
   ↓
▶ clean_orders.parquet (for dashboard use)
   ↓
📊 Jupyter EDA / 📈 Streamlit dashboardPerfume E-commerce Analytics – WIP
