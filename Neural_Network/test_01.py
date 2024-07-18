#import libraries
import matplotlib .pyplot as plt
import numpy as np
from collections import Counter

data_w = [
    "tôi rất thích kem",
    "không ai thích tôi cả",
    "rất muốn kem"
]
words = [word for sentences in data_w for word in sentences.split()]


word_freq = Counter(words)
print(word_freq)
x = list(word_freq.keys())
frequency = list(word_freq.values())
plt.figure(figsize=(12,4))
plt.bar(x, frequency)
plt.xlabel("category")
plt.ylabel("word_freq")
plt.title("Test bar")
plt.show()