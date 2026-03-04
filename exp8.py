import numpy as np

# Example house_data array
# Columns: [Bedrooms, Square Footage, Sale Price]
house_data = np.array([
    [3, 1500, 200000],
    [5, 2500, 350000],
    [4, 1800, 275000],
    [6, 3200, 500000],
    [2, 1200, 150000],
    [5, 2800, 400000]
])

# Step 1: Select houses with more than 4 bedrooms
houses_more_than_4 = house_data[house_data[:, 0] > 4]

# Step 2: Extract sale prices (column index 2)
sale_prices = houses_more_than_4[:, 2]

# Step 3: Compute the average sale price
average_price = np.mean(sale_prices)

print("Average sale price:", average_price)