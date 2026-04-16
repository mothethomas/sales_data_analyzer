import pandas as pd

df = pd.read_csv(r"C:\Users\mothe\Machine Learning and Artificial Intelligence\Python_projects\sales_data_analyzer\sales_data.csv")

print("First 5 rows:")
print(df.head())
print()

print("Shape of dataset:")
print(df.shape)
print()

print("Column names:")
print(df.columns)
print()

print("Dataset info:")
print(df.info())
print()

print("Summary statistics:")
print(df.describe())
print("Full dataset:")
print(df)
print()

print("Product column:")
print(df["Product"])
print()

print("Product and Price columns:")
print(df[["Product", "Price"]])
print()

print("Items with price greater than 100:")
print(df[df["Price"] > 100])
print()

print("Items in Electronics category:")
print(df[df["Category"] == "Electronics"])
print()

print("Items with quantity greater than 3:")
print(df[df["Quantity"] > 3])
print()

df["TotalSales"] = df["Quantity"] * df["Price"]

print("Dataset with TotalSales column:")
print(df)
print()

print("Sorted by Price (highest first):")
print(df.sort_values("Price", ascending=False))
print()

print("Sorted by TotalSales (highest first):")
print(df.sort_values("TotalSales", ascending=False))
print()

##Question:Which product has the highest price? 
print("product with highest price\n",df.loc[df["Price"].idxmax(), ["Product", "Price"]])
print()

# 2.	Which product has the highest total sales?
top_product = df.loc[df["TotalSales"].idxmax()]

print("product with the highest total sales\n",top_product)
print()

##3.	How many items are in Electronics?
electronics = df[df["Category"] == "Electronics"]
print("Count of electronics items",len(electronics))
print()

##4.	Which items have quantity greater than 3?
print("items with more than 3\n", df[df["Quantity"] > 3])
print()


##What is the TotalSales for Notebook?
print("totalsales for Notebook\n",df[df["Product"] == "Notebook"]["TotalSales"])
print()

##group by category


print("Dataset with TotalSales:")
print(df)
print()

print("Category-wise total sales:")
category_sales = df.groupby("Category")["TotalSales"].sum()
print(category_sales)
print()

print("Category-wise average price:")
category_avg_price = df.groupby("Category")["Price"].mean()
print(category_avg_price)
print()

print("Category-wise total quantity sold:")
category_quantity = df.groupby("Category")["Quantity"].sum()
print(category_quantity)
print()

print("Category-wise sales sorted highest first:")
print(category_sales.sort_values(ascending=False))
print()

print("Top category by total sales:")
print(category_sales.sort_values(ascending=False).head(1))
print()

## How much total sales came from Electronics
electronics_sales = df[df["Category"] == "Electronics"]["TotalSales"].sum()
print("Total sales from Electronics:", electronics_sales)

##Which category sold the most? 
category_sales = df.groupby("Category")["TotalSales"].sum()

top_category = category_sales.idxmax()

print("Category that sold the most:", top_category)

# Which category has higher average price?
category_avg_price = df.groupby("Category")["Price"].mean()

top_category = category_avg_price.idxmax()

print("Category with highest average price:", top_category)

##Which category has the most quantity sold?
category_quantity = df.groupby("Category")["Quantity"].sum()

top_category = category_quantity.idxmax()

print("Category with most quantity sold:", top_category)

"""
1.	What is total sales for Electronics?
	2.	What is total sales for Stationery?
	3.	Which category has the highest total sales?
	4.	Which category has the highest average price?
	5.	Which category has the highest total quantity?

    """
#group  by using product

print("Product-wise total sales:")
product_sales = df.groupby("Product")["TotalSales"].sum()
print(product_sales.sort_values(ascending=False))
print()

print("Top product by total sales:")
product_wise_sales = df.groupby("Product")["TotalSales"].sum()
print(product_wise_sales.sort_values(ascending=False).head(1))
print()


