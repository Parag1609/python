from collections import Counter

# Count characters in a string
c = Counter("hello world")
print(c)  # Output: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# Count words in a list
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
wc = Counter(words)
print(wc)  # Output: Counter({'apple': 3, 'banana': 2, 'orange': 1})

# Most common elements
print(wc.most_common(2))  # Output: [('apple', 3), ('banana', 2)]

# Update the counter
wc.update(['apple', 'grape'])
print(wc)  # Output: Counter({'apple': 4, 'banana': 2, 'orange': 1, 'grape': 1})
