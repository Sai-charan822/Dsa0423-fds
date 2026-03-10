import numpy as np
import random

# Population dataset
data = [12, 15, 18, 20, 22, 25, 27, 30, 32, 35]

# Mean estimation
mean_value = np.mean(data)
print("Mean:", mean_value)

# Variance estimation
variance_value = np.var(data)
print("Variance:", variance_value)

# Sampling technique (random sampling)
sample = random.sample(data, 5)
print("\nRandom Sample:", sample)

# Sample mean and variance
sample_mean = np.mean(sample)
sample_variance = np.var(sample)

print("Sample Mean:", sample_mean)
print("Sample Variance:", sample_variance)