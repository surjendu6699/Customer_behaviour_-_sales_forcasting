import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import plotly.express as px

# ==============================
# Load your data
# ==============================
cleaned_sales_data = pd.read_csv(r"C:\Users\surje\cleaned_sales_data.csv")
forecast_sales = pd.read_csv(r"C:\Users\surje\forecast_sales.csv")
monthly_sales = pd.read_csv(r"C:\Users\surje\monthly_sales.csv")
rfm_segments = pd.read_csv(r"C:\Users\surje\rfm_segments.csv")

# ==============================
# Dashboard Title
# ==============================
st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("📊 Sales & Customer Dashboard")

# ==============================
# KPI CARDS
# ==============================
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)

with col1:
    total_sales = cleaned_sales_data["TotalSales"].sum()
    st.metric("💰 Total Sales", f"${total_sales:,.0f}")

with col2:
    num_customers = cleaned_sales_data["Customer ID"].nunique()
    st.metric("👥 Number of Customers", f"{num_customers:,}")

with col3:
    avg_order_value = total_sales / cleaned_sales_data["Invoice"].nunique()
    st.metric("📦 Avg Order Value", f"${avg_order_value:,.2f}")

# ==============================
# SALES TREND
# ==============================
st.subheader("📈 Monthly Sales Trend")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(monthly_sales["InvoiceDate"], monthly_sales["TotalSales"], marker="o", color="royalblue")
ax.set_xlabel("Date")
ax.set_ylabel("Sales")
ax.set_title("Monthly Sales")
ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
plt.xticks(rotation=45)
st.pyplot(fig)

# ==============================
# FORECAST
# ==============================
st.subheader("🔮 Forecasted Sales")
fig2 = px.line(forecast_sales, x="Date", y="Forecast", title="Sales Forecast", labels={"Forecast": "Predicted Sales"})
fig2.add_scatter(x=monthly_sales["InvoiceDate"], y=monthly_sales["TotalSales"], mode="lines+markers", name="Actual Sales")
st.plotly_chart(fig2, use_container_width=True)

# ==============================
# CUSTOMER SEGMENTS (RFM)
# ==============================
st.subheader("👥 Customer Segments (RFM Clusters)")
cluster_counts = rfm_segments["Cluster"].value_counts().reset_index()
cluster_counts.columns = ["Cluster", "Number of Customers"]

fig3 = px.bar(cluster_counts, x="Cluster", y="Number of Customers",
              title="Customer Distribution by Segment", text_auto=True,
              color="Cluster")
st.plotly_chart(fig3, use_container_width=True)

st.write("📌 Sample of RFM Segments Data")
st.dataframe(rfm_segments.head())

# ==============================
# CUSTOMER BEHAVIOR INSIGHTS
# ==============================
st.subheader("🧑‍🤝‍🧑 Customer Behavior Insights")

# Top 10 customers by Monetary
st.write("### 💎 Top 10 Customers by Spending")
top_customers = rfm_segments.nlargest(10, "Monetary")[["Customer ID", "Monetary"]]
st.table(top_customers)

# Recency vs Frequency Scatter
st.write("### ⏳ Recency vs Frequency")
fig4, ax4 = plt.subplots(figsize=(8, 5))
ax4.scatter(rfm_segments["Recency"], rfm_segments["Frequency"], alpha=0.6, color="teal")
ax4.set_xlabel("Recency (days)")
ax4.set_ylabel("Frequency (orders)")
ax4.set_title("Customer Engagement (Recency vs Frequency)")
st.pyplot(fig4)

# Average Monetary by Cluster
st.write("### 💰 Average Monetary Value per Cluster")
avg_monetary = rfm_segments.groupby("Cluster")["Monetary"].mean().reset_index()
fig5 = px.bar(avg_monetary, x="Cluster", y="Monetary",
              title="Avg Monetary Value by Cluster", text_auto=True, color="Cluster")
st.plotly_chart(fig5, use_container_width=True)
