import os
import pandas as pd
import matplotlib.pyplot as plt

# Create output folder if it does not exist
os.makedirs("output", exist_ok=True)

df = pd.read_csv("sales_data.csv")

# Clean missing values
df["Quantity"] = df["Quantity"].fillna(0)
df["Price"] = df["Price"].fillna(df["Price"].mean())

# Remove duplicates
df = df.drop_duplicates()

# Create TotalSales column
df["TotalSales"] = df["Quantity"] * df["Price"]

print("Cleaned Dataset:")
print(df)
print()

# Summary report
total_revenue = df["TotalSales"].sum()
total_quantity = df["Quantity"].sum()
top_product = df.groupby("Product")["TotalSales"].sum().sort_values(ascending=False).head(1)
top_category = df.groupby("Category")["TotalSales"].sum().sort_values(ascending=False).head(1)

print("SALES SUMMARY REPORT")
print("--------------------")
print("Total Revenue:", total_revenue)
print("Total Quantity Sold:", total_quantity)
print()
print("Top Product by Sales:")
print(top_product)
print()
print("Top Category by Sales:")
print(top_category)
print()

# Product-wise sales chart
product_sales = df.groupby("Product")["TotalSales"].sum()

plt.figure(figsize=(10, 5))
plt.bar(product_sales.index, product_sales.values)
plt.title("Product-wise Total Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/product_sales.png")
plt.show()

# Category-wise sales chart
category_sales = df.groupby("Category")["TotalSales"].sum()

plt.figure(figsize=(8, 5))
plt.bar(category_sales.index, category_sales.values)
plt.title("Category-wise Total Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("output/category_sales.png")
plt.show()

# Daily sales chart
daily_sales = df.groupby("Date")["TotalSales"].sum()

plt.figure(figsize=(10, 5))
plt.plot(daily_sales.index, daily_sales.values, marker="o")
plt.title("Daily Total Sales")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/daily_sales.png")
plt.show()


# Product-wise average price chart
product_price_average = df.groupby("Product")["Price"].mean()

plt.figure(figsize=(10, 5))
plt.bar(product_price_average.index, product_price_average.values)
plt.title("Product-wise Average Price")
plt.xlabel("Product")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/product_price_average.png")
plt.show()