import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Dataset
data = {
    "age": [25, 35, 45, 23, 40],
    "income": [30000, 60000, 80000, 20000, 75000],
    "browsing_duration": [5, 20, 15, 3, 25],
    "device_type": ["mobile", "desktop", "mobile", "tablet", "desktop"],
    "purchase": ["no", "yes", "yes", "no", "yes"]
}

df = pd.DataFrame(data)

# Encode categorical variable
le_device = LabelEncoder()
df["device_type"] = le_device.fit_transform(df["device_type"])

le_purchase = LabelEncoder()
df["purchase"] = le_purchase.fit_transform(df["purchase"])

X = df[["age", "income", "browsing_duration", "device_type"]]
y = df["purchase"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Predict new customer
new_customer = [[30, 50000, 10, le_device.transform(["mobile"])[0]]]
prediction = model.predict(new_customer)

print("Purchase Prediction:", le_purchase.inverse_transform(prediction))