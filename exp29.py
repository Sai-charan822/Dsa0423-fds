import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv("customer_reviews.csv")

ratings = df['rating']

mean_rating = np.mean(ratings)
std_dev = np.std(ratings, ddof=1)
n = len(ratings)

confidence = 0.95
t_critical = stats.t.ppf((1 + confidence) / 2, df=n-1)

margin_error = t_critical * (std_dev / np.sqrt(n))

lower = mean_rating - margin_error
upper = mean_rating + margin_error

print("Average Rating:", mean_rating)
print("Confidence Interval (95%):", (lower, upper))

if mean_rating >= 4:
    print("Customer Satisfaction: High")
elif mean_rating >= 3:
    print("Customer Satisfaction: Moderate")
else:
    print("Customer Satisfaction: Low")