import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'CustomerID':[1,2,3,4,5,6,7,8,9,10],
    'AmountSpent':[200,500,150,800,1200,300,450,700,1000,650],
    'VisitFrequency':[5,10,3,12,15,6,8,11,14,9]
}

df = pd.DataFrame(data)

# Selecting features
X = df[['AmountSpent','VisitFrequency']]

# K-Means Model
kmeans = KMeans(n_clusters=3)
df['Cluster'] = kmeans.fit_predict(X)

print(df)

# Visualization
plt.scatter(df['AmountSpent'], df['VisitFrequency'], c=df['Cluster'], cmap='rainbow')
plt.xlabel("Amount Spent")
plt.ylabel("Visit Frequency")
plt.title("Customer Segmentation")
plt.show()