import numpy as np

# Create a 4x4 NumPy array (Rows = Students, Columns = Subjects)
# Order of subjects: Math, Science, English, History
student_scores = np.array([
    [85, 78, 92, 88],
    [76, 85, 89, 90],
    [90, 88, 84, 86],
    [88, 79, 91, 87]
])

print("Student Scores:\n", student_scores)

# 1️⃣ Calculate average score for each subject (column-wise mean)
subject_averages = np.mean(student_scores, axis=0)

print("\nAverage Score for Each Subject:")
subjects = ["Math", "Science", "English", "History"]

for i in range(len(subjects)):
    print(subjects[i], ":", subject_averages[i])

# 2️⃣ Identify the subject with the highest average score
highest_avg_index = np.argmax(subject_averages)
highest_avg_subject = subjects[highest_avg_index]

print("\nSubject with Highest Average Score:", highest_avg_subject)