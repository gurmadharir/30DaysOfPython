# =========================
# Day 7: Sets
# =========================

# ------- Level 1 ---------

it_companies = {"Apple", "IBM", "Microsoft", "Meta", "Google"}

# find length
print(len(it_companies))

# Add 'Twitter'
it_companies.add("Twitter")

# Add multiple IT companies
more_companies = {'Amazon', 'Oracle', 'Adobe', 'Intel', 'Tesla'}
it_companies.update(more_companies)

print(it_companies)

# Remove a company
it_companies.remove('Adobe')

# remove() errors if missing, discard() doesn't
it_companies.discard('Adobe')

# -------------- Level 2 -----------------
A = {1, 2, 3}
B = {3, 4, 5}

# Join A and B
joined = A.union(B)
print("A union B:", joined)

# Find A intersection B
intersect = A.intersection(B)
print("A intersection B:", intersect)

# Is A subset of B
is_subset = A.issubset(B)
print("Is A subset of B:", is_subset)

# Are A and B disjoint sets
is_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets:", is_disjoint)


# Join A with B
joined_ab = A.union(B)
print("A union B:", joined_ab)

# Join B with A
joined_ba = B.union(A)
print("B union A:", joined_ba)

# find symmetric difference
sym_diff = A.symmetric_difference(B)
print("Symmetric difference of A & B:", sym_diff)

# Delete the sets completely
del A
del B

# ---------------- Level 3 ------------------

# Compare list and set lengths
ages = [22, 25, 22, 30, 25, 40]
ages_set = set(ages) # Removes duplicates

print("Length of list ages:", len(ages))
print("Length of set ages:", len(ages_set))

# Explain the difference between the following data types: string, list, tuple and set.
# Answer: Lists and sets are mutable; strings and tuples are immutable

# How many unique words have been used in the sentence?
sentence = "I am a teacher and I love to inspire and teach people"

# First, split
words = sentence.split(' ')

# Second, change to set
unique_words = set(words)
print("\nNumber of the unique words are:", unique_words)
