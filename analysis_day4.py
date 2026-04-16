import pandas as pd

df = pd.read_csv("sales_Day4.csv")

print("Original dataset:")
print(df)
print()

print("Missing values in each column:")
print(df.isnull().sum())
print()

print("Rows with missing values:")
print(df[df.isnull().any(axis=1)])
print()

print("Number of duplicate rows:")
print(df.duplicated().sum())
print()

p=df["Price"].isnull().sum()
print("number of missing details of price before cleaning\n",p)
print(df[df.isnull().any(axis=1)][["Product", "Category", "Price"]])
print()
print(df[df.isnull().any(axis=1)].index)
print()

# Fill missing Quantity with 0
df["Quantity"] = df["Quantity"].fillna(0)

# Fill missing Price with column average
df["Price"] = df["Price"].fillna(df["Price"].mean())

# Remove duplicate rows
df = df.drop_duplicates()

print("Cleaned dataset:")
print(df)
print()

print("Missing values after cleaning:")
print(df.isnull().sum())
print()

print("Number of duplicate rows after cleaning:")
print(df.duplicated().sum())
print()

df["TotalSales"] = df["Quantity"] * df["Price"]

print("Dataset with TotalSales after cleaning:")
print(df)
print()