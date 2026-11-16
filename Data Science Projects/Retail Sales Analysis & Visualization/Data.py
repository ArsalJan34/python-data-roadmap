# ============================================================
# FILE 1: generate_data.py
# Purpose: Create sales_data.csv
# ============================================================

# ============================================================
# CELL 1: Import Libraries
# ============================================================
import numpy as np
import pandas as pd

np.random.seed(42)  # reproducible results


# ============================================================
# CELL 2: Generate the Dataset
# ============================================================
n = 2000  # number of transactions

dates = pd.date_range("2024-01-01", "2024-12-31", periods=n)
categories = ["Electronics", "Clothing", "Groceries", "Furniture", "Sports"]
regions = ["North", "South", "East", "West"]

df = pd.DataFrame({
    "Order_ID": np.arange(1001, 1001 + n),
    "Date": np.random.choice(dates, n),
    "Category": np.random.choice(categories, n, p=[0.25, 0.25, 0.25, 0.10, 0.15]),
    "Region": np.random.choice(regions, n),
    "Quantity": np.random.randint(1, 10, n),
    "Unit_Price": np.round(np.random.uniform(5, 500, n), 2),
    "Customer_Age": np.random.randint(18, 70, n),
})

# Add missing values + duplicates (for data cleaning practice)
df.loc[np.random.choice(df.index, 50, replace=False), "Customer_Age"] = np.nan
df = pd.concat([df, df.sample(10, random_state=1)], ignore_index=True)


# ============================================================
# CELL 3: Save to CSV
# ============================================================
df.to_csv("sales_data.csv", index=False)

print("Saved sales_data.csv")
print("Shape:", df.shape)
df.head()
