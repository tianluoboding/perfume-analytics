# utils/plot.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# 📈 Daily GMV 折线图
def plot_daily_gmv(df: pd.DataFrame):
    daily_gmv = df.groupby(df["Created Time"].dt.date)["Order Amount"].sum().reset_index()
    st.line_chart(daily_gmv.rename(columns={"Created Time": "index"}).set_index("index"))

# 🏷️ 品牌 GMV 柱状图
def plot_brand_bar(df: pd.DataFrame, top_k=20):
    top_brands = (
        df.groupby("Product Name")["Order Amount"]
        .sum()
        .sort_values(ascending=False)
        .head(top_k)
    )
    st.bar_chart(top_brands)

# 🔥 Weekday × Hour 热力图
def plot_heatmap(df: pd.DataFrame):
    pivot = (
        df.groupby(["weekday", "hour"])["Order Amount"]
        .sum()
        .unstack()
        .fillna(0)
    )
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(pivot, cmap="YlGnBu", annot=False, fmt=".0f", ax=ax)
    st.pyplot(fig)
