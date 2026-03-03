# Item prices and quantities
prices = [10.50, 5.25, 3.75]   # example prices
quantities = [2, 4, 3]         # example quantities

# Discount and tax rates (percentages)
discount_rate = 10   # 10% discount
tax_rate = 8         # 8% tax

# Step 1: Calculate subtotal
subtotal = 0
for i in range(len(prices)):
    subtotal += prices[i] * quantities[i]

# Step 2: Apply discount
discount_amount = subtotal * (discount_rate / 100)
after_discount = subtotal - discount_amount

# Step 3: Apply tax
tax_amount = after_discount * (tax_rate / 100)
total_cost = after_discount + tax_amount

# Output results
print("Subtotal:", subtotal)
print("Discount Amount:", discount_amount)
print("Tax Amount:", tax_amount)
print("Total Cost:", total_cost)
