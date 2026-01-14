# ====================================================
# Day 10: Loops
# =====================================================
from collections import Counter

from day_10.data.countries import countries
from day_10.data.countries_data import countries_data


# -------------------- Level 1 ------------------------

#1: Iterate from 0 to 10 using both for and while loops.
count = 0
while count <= 10:
    print(count)
    count +=1

for i in range(11):
    print(i)


#2: Iterate from 10 to 0 using both for and while loops.
count = 10
while count >= 0:
    print(count)
    count -= 1

for i in range(10, -1, -1):
    print(i)

#3: Write a loop that prints a triangle using seven `print()` calls.
for i in range(1,8):
    print("#" * i)


#4: Use nested loops to create 8×8 grid (or square) of # characters.
for row in range(8):
    for col in range(8):
        print("#", end=" ")
    print()

#5: Print square number pattern (or squares table).
for n in range(0, 11):
    print(f"{n} x {n} = {n * n}")

#6: Iterate through the list, using a for loop and print out the items.
skills = ['Python', 'Numpy','Pandas','Django', 'Flask']

for skill in skills:
    print(skill)

#7: Use for loop to iterate from 0 to 100 and print only even numbers
for num in range(0, 101, 2):
        print(num)

#8: Use for loop to iterate from 0 to 100 and print only odd numbers
for num in range(0, 101):
    if num % 2 != 0:
        print(num)

# -------------------- Level 2 ------------------------

#1: Use for loop to iterate from 0 to 100 and print the sum.
total = 0
for num in range(101):
    total += num
print(f"The sum of all numbers is {total}")

#2: Print the sum of all even and odd numbers from 0 to 100.
even_sum = 0
odd_sum = 0

for num in range(101):
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print(f"The sum of all evens is {even_sum} and the sum of all odds is {odd_sum}")

# -------------------- Level 2 ------------------------

#1: Extract countries containing "land" from `countries.py`.
for country in countries:
    if "land" in country:
        print(country)

# 2: Reverse the fruit list using a loop.
fruits = ['banana', 'orange', 'mango', 'lemon']

for fruit in reversed(fruits):
    print(fruit)

#3: Go to the data folder and use the countries_data.py file

#I: The total number of languages in the data
unique_languages = set()

for country in countries_data:
    for lang in country.get('languages', []):
        unique_languages.add(lang)

# Print the total number of unique languages
print("Total number of unique languages:", len(unique_languages))

#II: Find the ten most spoken languages from the data
all_languages = []

for country in countries_data:
    all_languages.extend(country.get("languages", []))  # add all languages in this country

# Count occurrences of each language
language_counts = Counter(all_languages)

# Get the 10 most common languages
top_10 = language_counts.most_common(10)

print("Top 10 most spoken languages:")
for lang, count in top_10:
    print(f"{lang}: spoken in {count} countries")

#III: Find the 10 most populated countries in the world
ls_countries = list()

# Step 1: Collect countries and their populations
for country in countries_data:
    ls_countries.append((country["name"],country["population"]))

# Step 2: Sort the list by population in descending order
ls_countries_sorted = sorted(ls_countries, key=lambda x: x[1], reverse=True)

# Step 3: Get the top 10
top_10_countries = ls_countries_sorted[:10]

# Step 4: Print results
for country, population in top_10_countries:
    print(f"{country}: {population}")
