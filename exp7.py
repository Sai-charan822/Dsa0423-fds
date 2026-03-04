import numpy as np

# Sample house_data array
# Columns: [Bedrooms, Square Footage, Sale Price]
house_data = np.array([
    [3, 1500, 200000],
    [5, 2500, 350000],
    [4, 1800, 275000],
    [6, 3200, 500000],
    [2, 1200, 150000],
    [5, 2800, 400000]
])

# Step 1: Filter houses with more than 4 bedrooms
filtered_houses = house_data[house_data[:, 0] > 4]

# Step 2: Extract sale prices (column index 2)
sale_prices = filtered_houses[:, 2]

# Step 3: Calculate average sale price
average_price = np.mean(sale_prices)

print("Average sale price of houses with more than 4 bedrooms:", average_price)