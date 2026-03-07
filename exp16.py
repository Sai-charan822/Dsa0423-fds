import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Sample dataset
data = {
    'Age':[25,45,30,50,23,40,35,60],
    'BloodPressure':[120,140,130,150,115,135,128,160],
    'Cholesterol':[200,240,210,260,190,230,220,270],
    'Outcome':['Good','Bad','Good','Bad','Good','Bad','Good','Bad']
}

df = pd.DataFrame(data)

# Convert label to numeric
df['Outcome'] = df['Outcome'].map({'Good':1,'Bad':0})

X = df[['Age','BloodPressure','Cholesterol']]
y = df['Outcome']

# Split data
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=42)

# KNN model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:",accuracy_score(y_test,y_pred))
print("Precision:",precision_score(y_test,y_pred))
print("Recall:",recall_score(y_test,y_pred))
print("F1 Score:",f1_score(y_test,y_pred))

print("Predictions:",y_pred)