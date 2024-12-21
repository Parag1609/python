import re
from collections import defaultdict

WORD_RE = re.compile(r'\w+')  # Matches sequences of word characters
index = defaultdict(list)  # Initializes a defaultdict with lists as default values

paragraph = """
Python is powerful. Python is easy to learn. Programming in Python is fun!
"""

for line_no, line in enumerate(paragraph.splitlines(), 1):
    for match in WORD_RE.finditer(line):
        word = match.group()
        column_no = match.start() + 1
        location = (line_no, column_no)
        index[word].append(location)  # Appends location directly without checking if key exists

# Print the index in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])
