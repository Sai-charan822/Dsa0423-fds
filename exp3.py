import pandas as pd

# Create sample sales_data DataFrame
sales_data = pd.DataFrame({
    'Product': ['Laptop', 'Mobile', 'Tablet', 'Headphones'],
    'Price': [50000, 20000, 15000, 2000],
    'Quantity': [5, 10, 7, 20]
})

# Calculate Total Sales
sales_data['Total Sales'] = sales_data['Price'] * sales_data['Quantity']

# Display the updated DataFrame
print(sales_data)