import numpy as np

# Fuel efficiency of different car models (miles per gallon)
fuel_efficiency = np.array([22, 25, 28, 30, 35])

# Calculate average fuel efficiency
average_efficiency = np.mean(fuel_efficiency)

# Select two models for comparison
model1 = fuel_efficiency[1]   # 25 mpg
model2 = fuel_efficiency[4]   # 35 mpg

# Percentage improvement
percentage_improvement = ((model2 - model1) / model1) * 100

print("Fuel Efficiency Data:", fuel_efficiency)
print("Average Fuel Efficiency:", average_efficiency, "mpg")
print("Percentage Improvement from Model1 to Model2:", percentage_improvement, "%")