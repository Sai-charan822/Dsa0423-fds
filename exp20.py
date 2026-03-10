import pandas as pd
import matplotlib.pyplot as plt

# Create dataset
data = {
    "Name": ["Messi", "Ronaldo", "Mbappe", "Haaland", "Neymar", "Salah", "Kane", "Lewandowski"],
    "Age": [36, 38, 25, 23, 31, 31, 30, 35],
    "Position": ["Forward", "Forward", "Forward", "Forward", "Forward", "Forward", "Forward", "Forward"],
    "Goals": [30, 28, 35, 40, 20, 25, 27, 29],
    "Salary": [900000, 850000, 700000, 650000, 750000, 500000, 480000, 520000]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save dataset to CSV
df.to_csv("players.csv", index=False)

# Read CSV file
df = pd.read_csv("players.csv")

# Top 5 players with highest goals
top_goals = df.nlargest(5, "Goals")
print("Top 5 Players with Highest Goals:")
print(top_goals[["Name", "Goals"]])

# Top 5 players with highest salaries
top_salary = df.nlargest(5, "Salary")
print("\nTop 5 Players with Highest Salaries:")
print(top_salary[["Name", "Salary"]])

# Calculate average age
avg_age = df["Age"].mean()
print("\nAverage Age of Players:", avg_age)

# Players above average age
print("\nPlayers above Average Age:")
print(df[df["Age"] > avg_age]["Name"])

# Bar chart for position distribution
df["Position"].value_counts().plot(kind="bar")
plt.title("Distribution of Players by Position")
plt.xlabel("Position")
plt.ylabel("Number of Players")
plt.show()