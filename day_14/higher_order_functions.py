# =============================================================
# Day 14: Higher Order Functions
# ==============================================================
import string
from functools import reduce

#-------------------------- Level 1 ------------------------------
countries = ['Estonia', 'Finland', 'Sweden', 'Somaliland', 'Denmark', 'Norway', 'Iceland']
names = ['Gurmad', 'Dirie', 'Muse', 'Farah']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#1. Explain the difference between map, filter, and reduce.
"""
`map` transforms each element, `filter` keeps elements that 
pass a test, and `reduce` combines elements into a single value.
"""

#2. Explain the difference b/w higher order function, closure and decorator
"""
Higher-order functions take / return functions, closures capture and remember 
surrounding vars, & decorators are funcs that wrap others to add / modify behavior.
"""

#3. Define a call function before map, filter or reduce, see examples.
def get_length(item):
    return len(item)

# Map: get length of each country
countries_lengths = map(get_length, countries)
print(list(countries_lengths))

def is_even(num):
    if num % 2 == 0:
        return True
    return False

# Filter: keep only even numbers
even_numbers = filter(is_even, numbers)
print(list(even_numbers))

def add(num1, num2):
    return num1 + num2

# Reduce: sum all numbers
total = reduce(add, numbers)
print(total)

#4. Use for loop to print each country in the countries list.
for country in countries:
    print(country)

#5. Use for to print each name in the names list.
for name in names:
    print(name)

#6. Use for to print each number in the numbers list.
for number in numbers:
    print(number)


# ------------------------------- level 2 ---------------------------------
#1. Use map to create a new list by changing each country to uppercase.
uppercase_countries =map(lambda x: x.upper(), countries)
print(list(uppercase_countries))

#2. Use map to create a new list by changing each number to its square.
squared_numbers = map(lambda x: x ** 2, numbers)
print(list(squared_numbers))

#3. Use map to change each name to uppercase in the names list
uppercase_names = map(lambda x: x.upper(), names)
print(list(uppercase_names))

#4. Use filter to filter out countries containing 'land'.
land_countries = filter(lambda country: 'land' in country, countries)
print(list(land_countries))

#5. Use filter to filter out countries having exactly six characters.
six_character_countries = filter(lambda country: len(country) == 6, countries)
print(list(six_character_countries))

#6. Use filter to filter out countries containing six letters and more.
long_countries = filter(lambda country: len(country) > 5, countries)
print(list(long_countries))

#6. Use filter to filter out countries starting with an 'E'
e_countries = filter(lambda country: country.startswith('E'), countries)
print(list(e_countries))

#7. Chain two or more list iterators
result = reduce(
    lambda a, b: a + b,
    filter(
        lambda x: x % 2 == 0,
        map(lambda x: x ** 2, numbers)
    )
)

print(result)

#8. Returns only string items from a list
def get_string_lists(lst):
    return list(filter(lambda item: isinstance(item, str), lst))

print(get_string_lists(['1', 1, 2, '2', 3, 4, '3']))

#10. Use reduce to sum all the numbers in the numbers list.
sum_nums = reduce(lambda x, y: x + y, numbers)
print(sum_nums)

#11. Concatenate country names into one sentence using reduce
filtered_countries = list(filter(lambda c: c != "Somaliland", countries))

sentence = reduce(
    lambda a, b: a + ", " + b,
    filtered_countries[:-1]
) + ", and " + filtered_countries[-1] + " are north European countries"

print(sentence)

# Correct import
from day_10.data.countries import countries as country_data

# 12. Return lists of countries grouped by common naming patterns
def categorize_countries(countries):
    patterns = ['land', 'ia', 'island', 'stan']
    categorized = {p: [] for p in patterns}

    for country in countries:
        for pattern in patterns:
            if pattern in country.lower():
                categorized[pattern].append(country)

    return categorized


result = categorize_countries(country_data)
print(result)

#13. Count countries by their starting letterdef count_countries_by_letter(countries):
def count_countries_by_letter(countries):
    letters = list(string.ascii_lowercase)
    letter_count = {letter: 0 for letter in letters}

    for country in countries:
        first_letter = country[0].lower()
        if first_letter in letter_count:
            letter_count[first_letter] += 1

    return letter_count

result = count_countries_by_letter(country_data)
print(result)

#14. Return the first ten countries from the list
def get_first_ten_countries(countries):
    return countries[:10]
result = get_first_ten_countries(country_data)
print(result)

#15. Return the last ten countries from the list
def get_last_ten_countries(countries):
    return countries[-10:]

result = get_last_ten_countries(country_data)
print(result)

