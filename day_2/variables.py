# Day 2: 30 Days of Python Programming

# ==================================================
# Exercise: Level 1
# ==================================================

# Declare individual variables

"""
first_name = "Gurmad"
last_name = "Abdulle"
full_name = "Gurmad Abdulle"
country = "Somaliland"
city = "Hargeisa"
age = 21
year = 2025
is_married = False
is_true = False
is_light_on = False
"""
import math
from math import remainder

# Declare multiple variables in one line
first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on = "Gurmad", "Abdulle", "Gurmad Abdulle", "Somaliland", "Hargeisa", 21, 2025, False, False, False

# ==================================================
# Exercise: Level 2
# ==================================================

#Check DataTypes
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# Find the length & compare
first_name_length = len(first_name)
last_name_length = len(last_name)

print(first_name_length == last_name_length)  # Are they equal?
print(first_name_length > last_name_length)   # Is first name longer?
print(first_name_length < last_name_length)   # Is last name longer?

# Declare 5 as num_one and 4 as num_two
num_one, num_two = 5,4

# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two

# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two

# Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two

# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one

# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_two ** num_two

# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

# Take radius as user input and calculate the area.
radius = float(input("Enter radius: "))

# Calculate the area
area_of_circle = math.pi * radius ** 2

print("Area of the circle:", area_of_circle)

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))
