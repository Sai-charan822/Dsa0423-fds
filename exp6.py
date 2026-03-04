import numpy as np

# Example NumPy arrays
time = np.array([0, 1, 2, 3, 4])          # Time in seconds
position = np.array([0, 5, 15, 20, 18])   # Vertical position in meters

# Calculate average velocity
average_velocity = (position[-1] - position[0]) / (time[-1] - time[0])

print("Time Intervals:", time)
print("Vertical Positions:", position)
print("\nAverage Velocity:", average_velocity, "m/s")