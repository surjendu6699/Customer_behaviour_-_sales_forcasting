# 🛒 Customer Behavior & Sales Forecasting Dashboard
📌 Project Overview

This project analyzes customer purchasing behavior and sales performance using historical retail data.
It includes data cleaning, feature engineering, clustering, forecasting, and an interactive dashboard built with Streamlit.

The dashboard provides:

Key KPIs (Total Sales, Customers, Avg Order Value)

Sales Trends (monthly performance)

Sales Forecasting (using Prophet / ARIMA)

Customer Segmentation (RFM Clustering)

Customer Behavior Insights (recency, frequency, spending, top customers)

⚙️ Features
🔑 KPIs

💰 Total Sales

👥 Number of Customers

📦 Average Order Value (AOV)

📊 Sales Analysis

Monthly sales trends

Forecasted sales (12 months ahead)

👥 Customer Behavior

RFM segmentation (Recency, Frequency, Monetary)

Distribution of customer clusters

Top 10 customers by spending

Recency vs Frequency scatter (loyalty vs engagement)

Average spending by cluster

🛠️ Tech Stack

Python (Pandas, NumPy, Matplotlib, Seaborn, Plotly)

Machine Learning: ARIMA / SARIMA, Prophet

Streamlit (dashboard & visualization)

Power BI (optional business reporting)

🚀 Getting Started
1️⃣ Clone the repo
git clone https://github.com/surjendu6699/Customer_behaviour_-_sales_forcasting
cd sales-customer-dashboard

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit dashboard
streamlit run app.py

📂 Project Structure
📦 sales-customer-dashboard
 ┣ 📜 cleaned_sales_data.csv      # Cleaned transaction data
 ┣ 📜 forecast_sales.csv          # Forecast results
 ┣ 📜 monthly_sales.csv           # Aggregated monthly sales
 ┣ 📜 rfm_segments.csv            # Customer RFM clusters
 ┣ 📜 app.py                      # Streamlit dashboard
 ┣ 📜 requirements.txt            # Python dependencies
 ┗ 📜 README.md                   # Project documentation

📈 Example Dashboard

🔹 KPIs & Sales Trends

Total Sales, Customers, AOV

Monthly Sales Trend

Forecasted Sales vs Actual

🔹 Customer Behavior

RFM Segments distribution

Top Customers by spending

Engagement analysis (Recency vs Frequency)

📌 Future Enhancements

Add Product Behavior Analysis (top products, product clusters)

Customer Churn Prediction

Recommendation system (cross-selling/upselling)

👨‍💻 Author

Your Name
📧 surjendubanerjee79@gmail.com

 https://github.com/surjendu6699/Customer_behaviour_-_sales_forcasting
