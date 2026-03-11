import numpy as np
import scipy.stats as stats

# Sample revenue data (100 customers)
revenue = np.random.normal(200, 50, 100)   # mean=200, std=50

mean = np.mean(revenue)
std_error = stats.sem(revenue)

confidence = 0.95
interval = stats.t.interval(confidence, len(revenue)-1, loc=mean, scale=std_error)

print("Sample Mean Revenue:", mean)
print("95% Confidence Interval:", interval)