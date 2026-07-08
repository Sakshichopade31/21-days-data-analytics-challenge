from pathlib import Path
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use("ggplot")

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "dataset" / "data.csv"

if not DATA_PATH.exists():
    raise FileNotFoundError(f"Dataset not found at: {DATA_PATH}")

# Load dataset
print("Loading dataset...")
df = pd.read_csv(DATA_PATH, encoding="latin1")

# Data overview
print("Shape:", df.shape)
print("Columns:", list(df.columns))
print("Data types:")
print(df.dtypes)
print("\nDataset information:")
df.info()
print("\nFirst 5 rows:")
print(df.head())
print("\nLast 5 rows:")
print(df.tail())
print("\nSummary statistics:")
print(df.describe())
print("\nSummary of categorical columns:")
print(df.describe(include=object))
print("\nUnique values per column:")
print(df.nunique())
print("\nInvoiceDate range:")
print(df["InvoiceDate"].min())
print(df["InvoiceDate"].max())

# Data cleaning
print("\nMissing values:")
print(df.isnull().sum())
print("\nMissing percentage:")
print((df.isnull().sum() / len(df)) * 100)
print("\nDuplicate rows:")
print(df.duplicated())
print("Duplicate count:", df.duplicated().sum())

# Remove duplicates
print("\nRemoving duplicates...")
df.drop_duplicates(inplace=True)
print("Duplicate rows after cleanup:", df.duplicated().sum())
print("Shape after cleanup:", df.shape)

# Check invalid values
print("\nRows with negative quantity:")
print(df[df["Quantity"] < 0])
print("\nRows with zero or negative price:")
print(df[df["UnitPrice"] <= 0])

# Convert InvoiceDate to datetime
print("\nConverting InvoiceDate to datetime...")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
print(df["InvoiceDate"].head())

# Cancelled orders
print("\nCancelled orders:")
print(df[df["InvoiceNo"].astype(str).str.startswith("C")])

# Drop missing CustomerID rows
print("\nDropping rows with missing CustomerID...")
df = df.dropna(subset=["CustomerID"])
print(df.head(30))
print("\nMissing values after cleanup:")
print(df.isnull().sum())
print("\nDuplicate rows after cleanup:", df.duplicated().sum())

# Feature engineering
print("\nCreating new features...")
df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]
df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month
df["MonthName"] = df["InvoiceDate"].dt.month_name()
df["Day"] = df["InvoiceDate"].dt.day
df["Weekday"] = df["InvoiceDate"].dt.day_name()
df["Hour"] = df["InvoiceDate"].dt.hour
df["IsCancelled"] = df["InvoiceNo"].astype(str).str.startswith("C")

# EDA - sales analysis
print("\nTotal revenue:", df["TotalPrice"].sum())
print("Average transaction value:", df["TotalPrice"].mean())
print("Maximum sale:", df["TotalPrice"].max())
print("Minimum sale:", df["TotalPrice"].min())
print("Number of countries:", df["Country"].nunique())
print("Countries present:", df["Country"].unique())
print("\nTop countries by revenue:")
print(df.groupby("Country")["TotalPrice"].sum().sort_values(ascending=False))
print("\nTop countries by orders:")
print(df["Country"].value_counts())

# Product analysis
print("\nBest selling products:")
print(df.groupby("Description")["Quantity"].sum().sort_values(ascending=False))
print("\nHighest revenue products:")
print(df.groupby("Description")["TotalPrice"].sum().sort_values(ascending=False))
print("\nMost expensive products:")
print(df.groupby("Description")["UnitPrice"].max().sort_values(ascending=False))
print("\nMost returned products:")
print(df[df["Quantity"] < 0]["Description"].value_counts())

# Customer analysis
print("\nNumber of customers:", df["CustomerID"].nunique())
print("\nTop customers:")
print(df.groupby("CustomerID")["TotalPrice"].sum().sort_values(ascending=False))
print("\nOrders per customer:")
print(df.groupby("CustomerID")["InvoiceNo"].nunique())
print("\nAverage customer spending:", df.groupby("CustomerID")["TotalPrice"].sum().mean())

# Time analysis
print("\nMonthly revenue:")
print(df.groupby("MonthName")["TotalPrice"].sum())
print("\nDaily revenue:")
print(df.groupby("Day")["TotalPrice"].sum())
print("\nWeekday revenue:")
print(df.groupby("Weekday")["TotalPrice"].sum())
print("\nHourly revenue:")
print(df.groupby("Hour")["TotalPrice"].sum())

# Return analysis
print("\nNumber of returns:", (df["Quantity"] < 0).sum())
print("Return percentage:", ((df["Quantity"] < 0).sum() / len(df)) * 100)
print("Returned products:")
print(df[df["Quantity"] < 0]["Description"].value_counts())

# Visualizations
monthly_revenue = df.groupby("MonthName")["TotalPrice"].sum().reindex([
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
])

plt.figure(figsize=(10, 5))
monthly_revenue.plot(marker="o")
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()

top_country = df.groupby("Country")["TotalPrice"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
top_country.plot(kind="bar")
plt.title("Top 10 Countries by Revenue")
plt.xlabel("Country")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.show()

top_products = df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
top_products.plot(kind="barh", color="green")
plt.title("Top 10 Selling Products")
plt.xlabel("Quantity Sold")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df["TotalPrice"], bins=50, color="red")
plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df["UnitPrice"], bins=50)
plt.title("Unit Price Distribution")
plt.xlabel("Unit Price")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df["Quantity"], bins=50)
plt.title("Quantity Distribution")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(8, 4))
plt.boxplot(df["TotalPrice"])
plt.title("Boxplot of TotalPrice")
plt.show()

plt.figure(figsize=(6, 5))
sns.heatmap(
    df[["Quantity", "UnitPrice", "TotalPrice"]].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.show()

orders_hour = df.groupby("Hour")["InvoiceNo"].count()
plt.figure(figsize=(10, 5))
orders_hour.plot(marker="o")
plt.title("Orders by Hour")
plt.xlabel("Hour")
plt.ylabel("Orders")
plt.show()

weekday_orders = df.groupby("Weekday")["InvoiceNo"].count().reindex([
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
])
plt.figure(figsize=(8, 5))
weekday_orders.plot(kind="bar")
plt.title("Orders by Weekday")
plt.ylabel("Orders")
plt.show()

returns = df[df["Quantity"] < 0]
top_returns = returns["Description"].value_counts().head(10)
plt.figure(figsize=(10, 5))
top_returns.plot(kind="bar")
plt.title("Top Returned Products")
plt.ylabel("Returns")
plt.show()

# Business insights
print("\nBusiness insights:")
print("1. The United Kingdom generated the highest revenue and dominated overall sales.")
print("2. Revenue reached its peak during November, indicating strong seasonal demand before Christmas.")
print("3. A small number of products accounted for a significant portion of total sales.")
print("4. Most customers made only one or two purchases, while a few high-value customers contributed a large share of the revenue.")
print("5. Several products showed a high return rate, suggesting possible issues related to quality, customer expectations, or product descriptions.")
print("6. Sales activity was highest during business hours, indicating that customers preferred shopping during the daytime.")

