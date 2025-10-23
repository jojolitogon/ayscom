import pandas as pd

# Read CSV
df = pd.read_csv("files/sales.csv")

# Preview data
print(df.head())

# Clean and transform
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
df["Product"] = df["Product"].str.strip().str.lower()

# Filter rows
df = df[df["Price"] > 0]

# Add new column
df["Total"] = df["Price"] * df["Quantity"]

print(df.head())

# Write CSV
df.to_csv("files/clean_data.csv", index=False)