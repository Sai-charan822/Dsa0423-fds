import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample data
data = {
    'CustomerID':[1,2,3,4,5,6,7,8],
    'AmountSpent':[500,700,200,1000,1200,300,450,800],
    'ItemsPurchased':[5,7,2,10,12,3,4,8]
}

df = pd.DataFrame(data)

X = df[['AmountSpent','ItemsPurchased']]

# K-Means clustering
kmeans = KMeans(n_clusters=3)
df['Cluster'] = kmeans.fit_predict(X)

print(df)

# Scatter Plot
plt.scatter(df['AmountSpent'], df['ItemsPurchased'], c=df['Cluster'], cmap='viridis')
plt.xlabel("Amount Spent")
plt.ylabel("Items Purchased")
plt.title("Customer Purchase Segments")
plt.show()