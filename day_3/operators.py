# ===========================================
# DAY 3 EXERCISES - PYTHON
# ===========================================


# -------------------------------------------
# VARIABLES
# -------------------------------------------
# Declare your age as integer
age = 21

# Declare your height as float
height = 1.75

# Declare a complex number
complex_number = 3 + 4j


# -------------------------------------------
# TRIANGLE CALCULATIONS
# -------------------------------------------
# Area of a triangle
base = float(input("Enter base of the triangle: "))
triangle_height = float(input("Enter height of the triangle: "))
triangle_area = 0.5 * base * triangle_height
print("The area of the triangle is:", triangle_area)

# Perimeter of a triangle
a = float(input("\nEnter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
triangle_perimeter = a + b + c
print("The perimeter of the triangle is:", triangle_perimeter)


# -------------------------------------------
# RECTANGLE CALCULATIONS
# -------------------------------------------
length = float(input("\nEnter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)
print("Area of the rectangle is:", rectangle_area)
print("Perimeter of the rectangle is:", rectangle_perimeter)


# -------------------------------------------
# CIRCLE CALCULATIONS
# -------------------------------------------
pi = 3.14
radius = float(input("\nEnter radius of the circle: "))
circle_area = pi * radius ** 2
circumference = 2 * pi * radius
print("Area of the circle is:", circle_area)
print("Circumference of the circle is:", circumference)


# -------------------------------------------
# LINE AND SLOPE
# -------------------------------------------
# Line: y = 2x - 2
slope_line = 2
y_intercept = -2
x_intercept = 1  # when y = 0

print("\nFor the line y = 2x - 2:")
print(f"Slope: {slope_line}")
print(f"x-intercept: {x_intercept}")
print(f"y-intercept: {y_intercept}")

# Slope and distance between two points
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_points = (y2 - y1) / (x2 - x1)
distance_points = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("\nBetween points (2,2) and (6,10):")
print(f"Slope: {slope_points}")
print(f"Euclidean distance: {distance_points:.2f}")

# Compare slopes
print("\nComparing slopes:")
print(f"Slope of line y=2x-2: {slope_line}")
print(f"Slope between points: {slope_points}")
if slope_line == slope_points:
    print("The slopes are equal.")
else:
    print("The slopes are not equal.")


# -------------------------------------------
# QUADRATIC EQUATION
# -------------------------------------------
# y = x^2 + 6x + 9
print("\nCalculating y = x^2 + 6x + 9 for x in range -6 to 0:")
for x in range(-6, 1):
    y = x ** 2 + 6 * x + 9
    print(f"x = {x:2}, y = {y}")


# -------------------------------------------
# STRING OPERATIONS
# -------------------------------------------
word1, word2 = "Python", "Dragon"
print(f"\nLength comparison (Python != Dragon): {len(word1) != len(word2)}")

# Check if 'on' is in both 'Python' and 'Dragon'
contains_on = ('on' in word1.lower()) and ('on' in word2.lower())
print(f"Is 'on' in both words?: {contains_on}")

# Check if 'jargon' is in the sentence
sentence = "I hope this course is not full of jargon"
contains_jargon = "jargon" in sentence
print(f"Does the sentence contain 'jargon'?: {contains_jargon}")

# Length of 'Python' converted to float and string
length_float = float(len(word1))
length_str = str(length_float)
print(f"Length of 'Python' as float: {length_float}")
print(f"Length of 'Python' as string: '{length_str}'")


# -------------------------------------------
# NUMBER CHECKS
# -------------------------------------------
num = 9
is_even = num % 2 == 0
print(f"\nIs {num} even?: {is_even}")

floor_div_check = (7 // 3) == int(2.7)
print(f"Does 7 // 3 equal int(2.7)?: {floor_div_check}")

print(f"Is type of '10' equal to type of 10?: {type('10') == type(10)}")

int_check = int(float('9.8')) == 10
print(f"Is int('9.8') equal to 10?: {int_check}")


# -------------------------------------------
# CALCULATE PAY
# -------------------------------------------
hours = float(input("\nEnter hours worked: "))
rate_per_hour = float(input("Enter rate per hour: "))
weekly_pay = hours * rate_per_hour
print(f"Your weekly earning is: {weekly_pay}")


# -------------------------------------------
# CALCULATE SECONDS LIVED
# -------------------------------------------
years_lived = int(input("\nEnter number of years you have lived: "))
seconds_in_a_year = 365 * 24 * 60 * 60
total_seconds = years_lived * seconds_in_a_year
print(f"You have lived for {total_seconds} seconds.")


# -------------------------------------------
# DISPLAY TABLE OF NUMBERS
# -------------------------------------------
print("\nTable of numbers, squares, and cubes:")
for i in range(1, 6):
    print(i, 1, i, i ** 2, i ** 3)
