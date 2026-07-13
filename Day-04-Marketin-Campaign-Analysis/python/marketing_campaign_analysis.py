import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Load dataset from the parent folder relative to this script.
root_dir = Path(__file__).resolve().parents[1]
file_path = root_dir / "dataset" / "marketing_campaign.csv"

df = pd.read_csv(file_path, sep="\t")

# Data cleaning and feature engineering
if "Dt_Customer" in df.columns:
    df["Dt_Customer"] = pd.to_datetime(df["Dt_Customer"], dayfirst=True, errors="coerce")

current_year = pd.Timestamp.today().year
if "Age" not in df.columns:
    df["Age"] = current_year - df["Year_Birth"]

if "Total_Children" not in df.columns:
    df["Total_Children"] = df["Kidhome"] + df["Teenhome"]

if "Total_Spending" not in df.columns:
    df["Total_Spending"] = (
        df["MntWines"]
        + df["MntFruits"]
        + df["MntMeatProducts"]
        + df["MntFishProducts"]
        + df["MntSweetProducts"]
        + df["MntGoldProds"]
    )

if "Income_Category" not in df.columns:
    df["Income_Category"] = pd.cut(
        df["Income"],
        bins=[df["Income"].min() - 1, 30000, 70000, df["Income"].max()],
        labels=["Low Income", "Medium Income", "High Income"]
    )

if "Age_Group" not in df.columns:
    df["Age_Group"] = pd.cut(
        df["Age"],
        bins=[0, 30, 50, 100],
        labels=["Young", "Adult", "Senior"]
    )

if "Is_Parent" not in df.columns:
    df["Is_Parent"] = (df["Kidhome"] + df["Teenhome"]) > 0

# Prepare summary series for plots
average_spending = df[
    [
        "MntWines",
        "MntFruits",
        "MntMeatProducts",
        "MntFishProducts",
        "MntSweetProducts",
        "MntGoldProds",
    ]
].mean()

education_spending = df.groupby("Education")["Total_Spending"].mean().sort_values(ascending=False)
marital_spending = df.groupby("Marital_Status")["Total_Spending"].mean().sort_values(ascending=False)
income_group_spending = df.groupby("Income_Category")["Total_Spending"].mean()
children_spending = df.groupby("Total_Children")["Total_Spending"].mean()
web_purchase = df.groupby("Income_Category")["NumWebPurchases"].mean()
store_purchase = df.groupby("Income_Category")["NumStorePurchases"].mean()
catalog_purchase = df.groupby("Income_Category")["NumCatalogPurchases"].mean()
product_sales = df[
    [
        "MntWines",
        "MntFruits",
        "MntMeatProducts",
        "MntFishProducts",
        "MntSweetProducts",
        "MntGoldProds",
    ]
].sum()

campaign_acceptance = df[["AcceptedCmp1", "AcceptedCmp2", "AcceptedCmp3", "AcceptedCmp4", "AcceptedCmp5"]].sum()
campaign_response = df.groupby("Response")["Total_Spending"].mean()
complaint = df.groupby("Complain")["Total_Spending"].mean()

correlation_matrix = df.select_dtypes(include="number").corr()

# Plot everything on a single figure with many subplots
sns.set_style("whitegrid")
fig, axes = plt.subplots(nrows=8, ncols=4, figsize=(30, 50))
axes = axes.flatten()

plot_index = 0

sns.histplot(df["Age"], bins=20, kde=True, ax=axes[plot_index])
axes[plot_index].set_title("Distribution of Customer Age")
plot_index += 1

sns.histplot(df["Income"], bins=30, kde=True, ax=axes[plot_index])
axes[plot_index].set_title("Distribution of Annual Income")
plot_index += 1

sns.histplot(df["Total_Spending"], bins=30, kde=True, ax=axes[plot_index])
axes[plot_index].set_title("Distribution of Total Spending")
plot_index += 1

sns.histplot(df["Recency"], bins=20, ax=axes[plot_index])
axes[plot_index].set_title("Distribution of Customer Recency")
plot_index += 1

sns.countplot(data=df, x="Education", order=df["Education"].value_counts().index, ax=axes[plot_index])
axes[plot_index].set_title("Education Level Distribution")
axes[plot_index].tick_params(axis="x", rotation=45)
plot_index += 1

sns.countplot(data=df, x="Marital_Status", order=df["Marital_Status"].value_counts().index, ax=axes[plot_index])
axes[plot_index].set_title("Marital Status Distribution")
axes[plot_index].tick_params(axis="x", rotation=45)
plot_index += 1

sns.countplot(data=df, x="Income_Category", order=["Low Income", "Medium Income", "High Income"], ax=axes[plot_index])
axes[plot_index].set_title("Income Category Distribution")
plot_index += 1

sns.countplot(data=df, x="Age_Group", order=["Young", "Adult", "Senior"], ax=axes[plot_index])
axes[plot_index].set_title("Age Group Distribution")
plot_index += 1

sns.countplot(data=df, x="Is_Parent", ax=axes[plot_index])
axes[plot_index].set_title("Parent vs Non-Parent Customers")
plot_index += 1

average_spending.plot(kind="bar", ax=axes[plot_index])
axes[plot_index].set_title("Average Spending on Products")
axes[plot_index].tick_params(axis="x", rotation=45)
plot_index += 1

sns.histplot(df["NumWebVisitsMonth"], bins=15, ax=axes[plot_index])
axes[plot_index].set_title("Monthly Website Visits")
plot_index += 1

sns.histplot(df["NumStorePurchases"], bins=15, ax=axes[plot_index])
axes[plot_index].set_title("Store Purchases Distribution")
plot_index += 1

sns.histplot(df["NumWebPurchases"], bins=15, ax=axes[plot_index])
axes[plot_index].set_title("Website Purchases Distribution")
plot_index += 1

sns.histplot(df["NumDealsPurchases"], bins=10, ax=axes[plot_index])
axes[plot_index].set_title("Deals Purchase Distribution")
plot_index += 1

sns.countplot(data=df, x="Response", ax=axes[plot_index])
axes[plot_index].set_title("Final Campaign Response")
plot_index += 1

sns.countplot(data=df, x="Complain", ax=axes[plot_index])
axes[plot_index].set_title("Customer Complaints")
plot_index += 1

sns.boxplot(x=df["Total_Spending"], ax=axes[plot_index])
axes[plot_index].set_title("Boxplot of Total Spending")
plot_index += 1

sns.boxplot(x=df["Income"], ax=axes[plot_index])
axes[plot_index].set_title("Boxplot of Income")
plot_index += 1

sns.scatterplot(data=df, x="Income", y="Total_Spending", ax=axes[plot_index])
axes[plot_index].set_title("Income vs Total Spending")
plot_index += 1

sns.scatterplot(data=df, x="Age", y="Total_Spending", ax=axes[plot_index])
axes[plot_index].set_title("Age vs Total Spending")
plot_index += 1

education_spending.plot(kind="bar", ax=axes[plot_index])
axes[plot_index].set_title("Average Spending by Education")
axes[plot_index].tick_params(axis="x", rotation=45)
plot_index += 1

marital_spending.plot(kind="bar", ax=axes[plot_index])
axes[plot_index].set_title("Average Spending by Marital Status")
axes[plot_index].tick_params(axis="x", rotation=45)
plot_index += 1

income_group_spending.plot(kind="bar", ax=axes[plot_index])
axes[plot_index].set_title("Average Spending by Income Category")
plot_index += 1

children_spending.plot(kind="bar", ax=axes[plot_index])
axes[plot_index].set_title("Average Spending by Number of Children")
plot_index += 1

web_purchase.plot(kind="bar", ax=axes[plot_index])
axes[plot_index].set_title("Avg Web Purchases by Income Category")
plot_index += 1

store_purchase.plot(kind="bar", ax=axes[plot_index])
axes[plot_index].set_title("Avg Store Purchases by Income Category")
plot_index += 1

catalog_purchase.plot(kind="bar", ax=axes[plot_index])
axes[plot_index].set_title("Avg Catalog Purchases by Income Category")
plot_index += 1

product_sales.plot(kind="bar", ax=axes[plot_index])
axes[plot_index].set_title("Total Sales by Product")
axes[plot_index].tick_params(axis="x", rotation=45)
plot_index += 1

campaign_acceptance.plot(kind="bar", ax=axes[plot_index])
axes[plot_index].set_title("Marketing Campaign Acceptance")
plot_index += 1

campaign_response.plot(kind="bar", ax=axes[plot_index])
axes[plot_index].set_title("Avg Spending by Campaign Response")
plot_index += 1

complaint.plot(kind="bar", ax=axes[plot_index])
axes[plot_index].set_title("Complaint vs Avg Spending")
plot_index += 1

sns.heatmap(correlation_matrix, cmap="coolwarm", ax=axes[plot_index], cbar=False)
axes[plot_index].set_title("Correlation Heatmap")
plot_index += 1

# Remove unused axes if any remain
for unused_ax in axes[plot_index:]:
    unused_ax.axis("off")

plt.tight_layout()
plt.show()
