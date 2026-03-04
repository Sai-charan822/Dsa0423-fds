import matplotlib.pyplot as plt

# Monthly data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

temperature = [22, 24, 28, 32, 35, 36, 34, 33, 31, 29, 25, 23]  # in °C
rainfall = [10, 15, 20, 25, 60, 120, 200, 180, 140, 80, 30, 15]  # in mm

# ---------------- Line Plot (Temperature) ----------------
plt.figure()
plt.plot(months, temperature, marker='o')
plt.title("Monthly Temperature Data")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

# ---------------- Scatter Plot (Rainfall) ----------------
plt.figure()
plt.scatter(months, rainfall)
plt.title("Monthly Rainfall Data")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.show()