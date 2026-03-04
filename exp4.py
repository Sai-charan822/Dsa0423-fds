import pandas as pd

# Create sample dataset
data = {
    'Property_ID': [101, 102, 103, 104, 105, 106],
    'Location': ['Chennai', 'Mumbai', 'Chennai', 'Delhi', 'Mumbai', 'Delhi'],
    'Bedrooms': [3, 5, 4, 6, 2, 5],
    'Area_sqft': [1500, 2500, 1800, 3200, 1200, 2800],
    'Listing_Price': [7500000, 15000000, 9000000, 20000000, 6000000, 17500000]
}

property_data = pd.DataFrame(data)

print("Property Data:\n")
print(property_data)

# 1. Average listing price in each location
avg_price = property_data.groupby('Location')['Listing_Price'].mean()

print("\n1. Average Listing Price by Location:\n")
print(avg_price)

# 2. Number of properties with more than 4 bedrooms
more_than_4_bedrooms = property_data[property_data['Bedrooms'] > 4].shape[0]

print("\n2. Number of Properties with more than 4 Bedrooms:")
print(more_than_4_bedrooms)

# 3. Property with the largest area
largest_area_property = property_data.loc[property_data['Area_sqft'].idxmax()]

print("\n3. Property with the Largest Area:\n")
print(largest_area_property)