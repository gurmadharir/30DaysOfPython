# =============================================================
# Day 13: List Comprehension
# ==============================================================

#1. Use list comprehension to keep only values ≤ 0 from the list.
numbers = [-4, -3, -2, -1, 1, 2, 3, 4, 5, 6]
result = [_ for _ in numbers if _ >= 0]
print(result)

#2. Flatten a nested list into a single list.
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)

#3. Create a list of tuples using list comprehension.
list_of_tuples = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
for t in list_of_tuples:
    print(t)

#4. Flatten the following list to a new list.
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [
    [country.upper(), country[:3].upper(), capital.upper()]
    for row in countries
    for country, capital in row
]

print(flattened_countries)

#5. Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

countries_dict = []
for row in countries:
    for country, capital in row:
        countries_dict.append([country, capital])

print(countries_dict)

#6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [f"{first_name} {last_name}" for row in names for first_name, last_name in row]
print(concatenated_names)

#7. Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
print(slope(1, 1, 3, 2))
