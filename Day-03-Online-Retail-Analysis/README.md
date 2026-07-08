# 🛒 Day 03 – Online Retail Sales Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge)

---

# 📌 Project Overview

This project is part of my **21 Days Data Analytics Challenge**.

The objective of this project is to perform an end-to-end **Exploratory Data Analysis (EDA)** on an Online Retail dataset and extract meaningful business insights related to customers, products, sales trends, returns, and revenue.

The dataset contains transactional records of a UK-based online retail store, making it an excellent real-world dataset for practicing data cleaning, feature engineering, business analysis, and visualization.

---

# 🎯 Objectives

- Understand the dataset structure
- Perform data cleaning
- Handle missing and duplicate values
- Detect cancelled orders and returned products
- Create business-related features
- Perform Exploratory Data Analysis (EDA)
- Generate business insights
- Visualize important sales trends

---

# 📂 Dataset Information

| Feature | Description |
|----------|-------------|
| InvoiceNo | Invoice Number |
| StockCode | Product Code |
| Description | Product Description |
| Quantity | Quantity Purchased |
| InvoiceDate | Date & Time of Purchase |
| UnitPrice | Price per Product |
| CustomerID | Customer Identifier |
| Country | Customer Country |

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- VS Code
- Git & GitHub

---

# 📋 Project Workflow

## 1️⃣ Data Overview

- Dataset Shape
- Column Names
- Data Types
- Dataset Information
- First & Last Records
- Summary Statistics
- Unique Values
- Time Period Covered

---

## 2️⃣ Data Cleaning

Performed the following preprocessing steps:

- Checked missing values
- Calculated missing value percentage
- Checked duplicate records
- Removed duplicate rows
- Converted `InvoiceDate` to DateTime format
- Identified cancelled orders
- Checked negative quantities
- Checked invalid prices
- Cleaned Customer IDs

---

## 3️⃣ Feature Engineering

Created new features including:

- TotalPrice
- Year
- Month
- Month Name
- Day
- Weekday
- Hour
- Cancelled Order Flag

---

## 4️⃣ Exploratory Data Analysis (EDA)

### 💰 Sales Analysis

- Total Revenue
- Average Transaction Value
- Maximum Sale
- Minimum Sale

### 🌍 Country Analysis

- Number of Countries
- Countries Present
- Top Countries by Revenue
- Top Countries by Orders

### 📦 Product Analysis

- Best Selling Products
- Highest Revenue Products
- Most Expensive Products
- Most Returned Products

### 👤 Customer Analysis

- Number of Customers
- Top Customers
- Orders per Customer
- Average Customer Spending

### 📅 Time Analysis

- Monthly Revenue
- Daily Revenue
- Weekday Revenue
- Hourly Revenue

### ❌ Return Analysis

- Number of Returns
- Return Percentage
- Returned Products

---

# 📊 Visualizations

This project includes the following charts:

- Monthly Revenue Trend
- Top 10 Countries by Revenue
- Top Selling Products
- Revenue Distribution
- Unit Price Distribution
- Quantity Distribution
- TotalPrice Boxplot
- Correlation Heatmap
- Orders by Hour
- Orders by Weekday
- Most Returned Products

---

# 💡 Key Business Insights

- United Kingdom generated the highest overall revenue.
- Revenue peaked during the holiday shopping season.
- A small number of products contributed to a large percentage of sales.
- High-value customers generated a significant portion of total revenue.
- Certain products had frequent returns and require investigation.
- Customer purchasing activity was highest during business hours.

---

# 📈 Business Recommendations

- Focus marketing campaigns on top-performing countries.
- Increase inventory before peak sales months.
- Improve quality control for products with high return rates.
- Launch loyalty programs for high-value customers.
- Optimize staffing based on hourly order trends.

---

# 📁 Project Structure

```text
Day-03-Online-Retail-Analysis
│
├── dataset
│   └── data.csv
│
├── notebook
│   └── Online_Retail_Analysis.ipynb
│
├── python
│   └── online_retail_analysis.py
│
├── screenshots
│
└── README.md
```

---

# 🚀 Skills Demonstrated

- Data Cleaning
- Data Wrangling
- Exploratory Data Analysis
- Feature Engineering
- Data Visualization
- Business Analytics
- Statistical Analysis
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

# 📸 Project Screenshots

Project screenshots are available inside the **screenshots** folder.

They include:

- Monthly Revenue Trend
- Country-wise Revenue
- Product Analysis
- Correlation Heatmap
- Revenue Distribution
- Orders by Hour
- Orders by Weekday
- Return Analysis

---

# 🔮 Future Improvements

- RFM Customer Segmentation
- Customer Clustering using K-Means
- Sales Forecasting
- Market Basket Analysis
- Interactive Power BI Dashboard

---

# ⭐ Conclusion

This project demonstrates a complete data analytics workflow—from data cleaning and feature engineering to visualization and business insight generation.

It showcases practical skills required for real-world retail analytics and serves as one of the projects in my **21 Days Data Analytics Challenge**.

---

## 👩‍💻 Author

**Sakshi Chopade**

Electrical Engineering (AI & Applications) Student  
Aspiring Data Analyst

📌 GitHub: https://github.com/Sakshichopade31

---

⭐ If you found this project useful, consider giving the repository a star.