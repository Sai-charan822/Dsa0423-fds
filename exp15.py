import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Sample data (recovery scores)
control_group = np.array([60, 62, 58, 61, 59, 63, 57])
treatment_group = np.array([70, 72, 68, 71, 69, 74, 73])

# Hypothesis testing (t-test)
t_stat, p_value = stats.ttest_ind(treatment_group, control_group)

print("T-statistic:", t_stat)
print("P-value:", p_value)

# Visualization
groups = ['Control', 'Treatment']
means = [np.mean(control_group), np.mean(treatment_group)]

plt.bar(groups, means)
plt.title("Treatment vs Control Effect")
plt.ylabel("Average Recovery Score")
plt.text(0.5, max(means)-1, f"p-value = {p_value:.4f}", ha='center')
plt.show()