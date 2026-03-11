import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset (can also read from CSV)
data = {
    "Temperature": [30, 32, 31, 29, 28, 33, 34, 30, 31, 29],
    "Rainfall": [5, 3, 4, 7, 8, 2, 1, 6, 4, 7]
}

df = pd.DataFrame(data)

# Calculate correlation coefficient
correlation = df["Temperature"].corr(df["Rainfall"])
print("Correlation Coefficient:", correlation)

# Scatter Plot
plt.scatter(df["Temperature"], df["Rainfall"])
plt.xlabel("Temperature")
plt.ylabel("Rainfall")
plt.title("Temperature vs Rainfall Scatter Plot")
plt.show()