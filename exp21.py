import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

# Dataset
data = {
    "weight": [150, 170, 140, 130, 160, 120],
    "color": ["red", "orange", "yellow", "yellow", "orange", "red"],
    "texture": ["smooth", "rough", "smooth", "smooth", "rough", "smooth"],
    "type": ["apple", "orange", "banana", "banana", "orange", "apple"]
}

df = pd.DataFrame(data)

# Convert categorical values
le_color = LabelEncoder()
le_texture = LabelEncoder()
le_type = LabelEncoder()

df["color"] = le_color.fit_transform(df["color"])
df["texture"] = le_texture.fit_transform(df["texture"])
df["type"] = le_type.fit_transform(df["type"])

X = df[["weight", "color", "texture"]]
y = df["type"]

# kNN model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Predict new fruit
new_fruit = [[155, le_color.transform(["red"])[0], le_texture.transform(["smooth"])[0]]]
prediction = model.predict(new_fruit)

print("Predicted Fruit:", le_type.inverse_transform(prediction))