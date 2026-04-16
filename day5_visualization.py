import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

df["TotalSales"] = df["Quantity"] * df["Price"]

print("Dataset:")
print(df)
print()

# Product-wise total sales
product_sales = df.groupby("Product")["TotalSales"].sum()

print("Product-wise total sales:")
print(product_sales)
print()

plt.figure(figsize=(10, 5))
plt.bar(product_sales.index, product_sales.values)
plt.title("Product-wise Total Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Category-wise total sales
category_sales = df.groupby("Category")["TotalSales"].sum()

print("Category-wise total sales:")
print(category_sales)
print()

plt.figure(figsize=(8, 5))
plt.bar(category_sales.index, category_sales.values)
plt.title("Category-wise Total Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# Daily total sales
daily_sales = df.groupby("Date")["TotalSales"].sum()

print("Daily total sales:")
print(daily_sales)
print()

plt.figure(figsize=(10, 5))
plt.plot(daily_sales.index, daily_sales.values, marker="o")
plt.title("Daily Total Sales")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()