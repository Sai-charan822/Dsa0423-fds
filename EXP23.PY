import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Dataset
data = {
    "income": [40000, 80000, 50000, 30000, 90000],
    "credit_score": [600, 750, 650, 550, 800],
    "debt_ratio": [0.4, 0.2, 0.35, 0.5, 0.1],
    "employment_duration": [2, 5, 3, 1, 7],
    "risk": ["high", "low", "high", "high", "low"]
}

df = pd.DataFrame(data)

X = df[["income", "credit_score", "debt_ratio", "employment_duration"]]
y = df["risk"]

# CART model (Decision Tree using Gini index)
model = DecisionTreeClassifier(criterion="gini")
model.fit(X, y)

# Predict new applicant
new_applicant = [[60000, 700, 0.3, 4]]
prediction = model.predict(new_applicant)

print("Predicted Credit Risk:", prediction[0])