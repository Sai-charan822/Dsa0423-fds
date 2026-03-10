from collections import Counter

# Product sales data
products = [
    "Laptop", "Mobile", "Laptop", "Tablet", "Mobile",
    "Laptop", "Headphones", "Mobile", "Tablet",
    "Laptop", "Mobile", "Mobile"
]

# Calculate frequency distribution
frequency = Counter(products)

print("Product Frequency Distribution:")
for product, count in frequency.items():
    print(product, ":", count)

# Find most popular product
most_popular = max(frequency, key=frequency.get)

print("\nMost Popular Product:", most_popular)
print("Sold", frequency[most_popular], "times")