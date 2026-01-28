# ============================================================================
# Day 18: Regular Expressions
# ============================================================================
import re
from collections import Counter

# ------------------------------- Level 1 ------------------------------------
#1️⃣:  What is the most frequent word in the following paragraph?
paragraph = (
    'I love teaching. If you do not love teaching what else can you love. '
    'I love Python if you do not love something which can give you all the '
    'capabilities to develop an application what else can you love.'
)

# Step 1. Extract words (ignore punctuation)
words = re.findall(r'\b\w+\b', paragraph)

#Step 2. Count Frequency
counter = Counter(words)

# 3. Sort by frequency (descending)
frequent_words = sorted(
    [(count, word) for word, count in counter.items()],
    reverse=True
)

print(frequent_words)

# 2️⃣ Find particle positions and their maximum distance.
text = """The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles."""
regex_pattern = r'-?\d+'

string_numbers = re.findall(regex_pattern, text)

# Convert extracted strings to integers
points = list(map(int, string_numbers))

distance = max(points) - min(points)
print(distance)

# ------------------------------------ Level 2 -----------------------------------
# 1️⃣ Write a pattern which identifies if a string is a valid python variable
pattern = r'^[_a-zA-Z][a-zA-Z0-9_]*$'
def is_valid_variable(var_name):
    return bool(re.match(pattern, var_name))

print(is_valid_variable('first_name'))   # True
print(is_valid_variable('first-name'))   # False
print(is_valid_variable('1first_name'))  # False
print(is_valid_variable('firstname'))    # True

# ------------------------------------- Level 3 ------------------------------------
# 1️⃣ Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# Step 1: Clean
cleaned_sentence = re.sub(r'[^a-zA-Z\s]', '', sentence)

# Step 2: Split into words
s_words = cleaned_sentence.split()

# Step 3: Count frequencies
word_counts = Counter(s_words)
print(counter)

# Step 4: Get 3 most common words
top_three = word_counts.most_common(3)
print(top_three)
