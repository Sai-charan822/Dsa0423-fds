from collections import Counter

# Sample reviews dataset
reviews = [
    "This product is amazing",
    "Amazing quality and amazing performance",
    "Good product and good value",
    "Quality is very good"
]

# Combine all reviews
text = " ".join(reviews)

# Convert to lowercase and split words
words = text.lower().split()

# Count frequency
word_freq = Counter(words)

print("Word Frequency Distribution:")
for word, freq in word_freq.items():
    print(word, ":", freq)