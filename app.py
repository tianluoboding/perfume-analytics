# app.py
from utils.plot import plot_daily_gmv, plot_brand_bar, plot_heatmap

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Perfume Dashboard", layout="wide")
st.title("📊 Perfume Livestream Dashboard")

# ————————————————————————————————————————
# 📦 加载数据（加缓存避免重复读）
@st.cache_data
def load_data():
    df = pd.read_parquet("data/clean_orders.parquet")
    df["Created Time"] = pd.to_datetime(df["Created Time"])
    df["hour"] = df["Created Time"].dt.hour
    df["weekday"] = df["Created Time"].dt.day_name()
    return df

df = load_data()

# ————————————————————————————————————————
# 🎛️ Sidebar 筛选器（精简）
st.sidebar.header("🧊 Filters")

min_date = df["Created Time"].min()
max_date = df["Created Time"].max()

date_range = st.sidebar.date_input("Date Range", [min_date, max_date])
gmv_min = float(df["Order Amount"].min())
gmv_max = float(df["Order Amount"].max())
gmv_range = st.sidebar.slider("Order Amount Range", min_value=gmv_min, max_value=gmv_max, value=(gmv_min, gmv_max))

filtered_df = df[
    (df["Created Time"] >= pd.to_datetime(date_range[0])) &
    (df["Created Time"] <= pd.to_datetime(date_range[1])) &
    (df["Order Amount"] >= gmv_range[0]) &
    (df["Order Amount"] <= gmv_range[1])
]

# ————————————————————————————————————————
# 🗂️ 页面结构：Tabs
tab1, tab2, tab3 = st.tabs(["📈 GMV Overview", "🏷️ Brand Analysis", "🔥 Heatmap"])

# ——— Tab 1: GMV 时间趋势 ———
with tab1:
    st.subheader("📈 Daily GMV")
    plot_daily_gmv(filtered_df)


with tab2:
    st.subheader("🏷️ GMV by Product Name")
    plot_brand_bar(filtered_df)

with tab3:
    st.subheader("🔥 GMV Heatmap (Weekday x Hour)")
    plot_heatmap(filtered_df)
