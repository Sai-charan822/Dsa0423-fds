import pandas as pd

# ---------------------------------------------------
# Step 1: Create Sample Dataset
# ---------------------------------------------------

data = {
    'customer_id': [101, 102, 101, 103, 102, 101, 104, 103],
    'order_date': [
        '2024-01-01', '2024-01-02', '2024-01-05',
        '2024-02-10', '2024-02-12', '2024-03-01',
        '2024-03-05', '2024-03-10'
    ],
    'product_name': [
        'Laptop', 'Mobile', 'Tablet',
        'Laptop', 'Mobile', 'Mobile',
        'Tablet', 'Laptop'
    ],
    'order_quantity': [1, 2, 1, 3, 1, 2, 2, 1]
}

order_data = pd.DataFrame(data)

# Convert order_date to datetime
order_data['order_date'] = pd.to_datetime(order_data['order_date'])

print("Original DataFrame:\n")
print(order_data)

# ---------------------------------------------------
# 1. Total quantity ordered for each product
# ---------------------------------------------------
total_quantity_per_product = order_data.groupby('product_name')['order_quantity'].sum()
print("\nTotal Quantity per Product:")
print(total_quantity_per_product)

# ---------------------------------------------------
# 2. Total quantity ordered by each customer
# ---------------------------------------------------
total_quantity_per_customer = order_data.groupby('customer_id')['order_quantity'].sum()
print("\nTotal Quantity per Customer:")
print(total_quantity_per_customer)

# ---------------------------------------------------
# 3. Number of orders placed by each customer
# ---------------------------------------------------
orders_per_customer = order_data.groupby('customer_id').size()
print("\nNumber of Orders per Customer:")
print(orders_per_customer)

# ---------------------------------------------------
# 4. Most ordered product
# ---------------------------------------------------
most_ordered_product = total_quantity_per_product.idxmax()
print("\nMost Ordered Product:")
print(most_ordered_product)

# ---------------------------------------------------
# 5. Total orders per month
# ---------------------------------------------------
orders_per_month = order_data.groupby(order_data['order_date'].dt.to_period('M')).size()
print("\nOrders per Month:")
print(orders_per_month)