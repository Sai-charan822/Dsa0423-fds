import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

data = {
    'Price': [20000, 25000, 30000, 22000, 27000],
    'Mileage': [15, 18, 12, 16, 14],
    'Engine': [1500, 1800, 2000, 1600, 1700],
    'Horsepower': [100, 120, 150, 110, 130]
}

df = pd.DataFrame(data)

plt.scatter(df['Price'], df['Mileage'])
plt.xlabel('Price')
plt.ylabel('Mileage')
plt.title('Multivariate Scatter Plot')
plt.show()

scatter_matrix(df)
plt.show()