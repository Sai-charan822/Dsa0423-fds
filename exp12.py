import pandas as pd

# Create sample sales data
data = {
    'Product': ['Laptop','Phone','Tablet','Laptop','Phone','Laptop','Tablet','Watch','Phone','Laptop'],
    'Quantity': [3,5,2,4,6,2,1,3,4,5]
}

sales_df = pd.DataFrame(data)

# Group by product and sum quantities
top_products = sales_df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(5)

print("Top 5 Most Sold Products:")
print(top_products)