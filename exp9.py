import matplotlib.pyplot as plt

# Monthly sales data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [15000, 18000, 17000, 20000, 22000, 21000]

# ---------------- Line Plot ----------------
plt.figure()
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Data - Line Plot")
plt.xlabel("Month")
plt.ylabel("Sales (in Rs)")
plt.grid(True)
plt.show()

# ---------------- Bar Plot ----------------
plt.figure()
plt.bar(months, sales)
plt.title("Monthly Sales Data - Bar Plot")
plt.xlabel("Month")
plt.ylabel("Sales (in Rs)")
plt.show()