import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("shoe_sales.csv")

frequency = df.groupby('shoe_size')['quantity'].sum()

print("Frequency Distribution:")
print(frequency)

plt.bar(frequency.index, frequency.values)
plt.xlabel("Shoe Size")
plt.ylabel("Frequency")
plt.title("Shoe Size Distribution")

plt.show()