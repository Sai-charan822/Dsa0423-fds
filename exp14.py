import pandas as pd
import string
from collections import Counter
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("data.csv")

# Stop words list
stop_words = ['the','and','is','in','to','of','for','on','with','a','an']

# Preprocess text
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return words

all_words = []

for feedback in data['feedback']:
    all_words.extend(preprocess(str(feedback)))

# Frequency distribution
word_freq = Counter(all_words)

# User input for top N words
N = int(input("Enter number of top words to display: "))

top_words = word_freq.most_common(N)

# Display results
print("\nTop", N, "Words:")
for word, freq in top_words:
    print(word, ":", freq)

# Plot bar graph
words = [item[0] for item in top_words]
freqs = [item[1] for item in top_words]

plt.bar(words, freqs)
plt.title("Top Frequent Words in Customer Feedback")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.show()