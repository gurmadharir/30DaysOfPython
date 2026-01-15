# ====================================================
# Day 11: Functions
# =====================================================
import math
import cmath

from day_10.loops import total


# --------------------- Level 1 -----------------------

#1: Define a function that returns the sum of two numbers.
def add_two_numbers(num_1, num_2):
    return num_1 + num_2

print(add_two_numbers(10,20))

#2: Write a function to calculate the area of a circle.
def calculate_area(r):
    area = math.pi * r ** 2
    return round(area, 2)

print(calculate_area(3))

#3: Sum all numeric arguments and validate types.
def add_all_nums(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add_all_nums(10,20,30,40))

#4: Write a function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

print(celsius_to_fahrenheit(25))

#5: Function that returns the season for a given month.
def check_season(month):
    # Convert month to lowercase for flexibility
    month = month.lower()

    # Define seasons
    if month in ["september", "october", "november"]:
        return "Autumn"
    elif month in ["december", "january", "february"]:
        return "Winter"
    elif month in ["march", "april", "may"]:
        return "Spring"
    elif month in ["june", "july", "august"]:
        return "Summer"
    else:
        return "Invalid month"

print(check_season("August"))

#6: Function to return the slope of a line.
def calculate_slope(x1, y1, x2, y2):
    if x2 == x1:
        raise ValueError("Slope is undefined for vertical lines (x1 = x2).")
    return (y2 - y1) / (x2 - x1)

print(calculate_slope(1, 2, 3, 6))

#7: Function to solve a quadratic equation ax² + bx + c = 0.
def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be 0 for a quadratic equation.")

    # Calculate the discriminant
    discriminant = cmath.sqrt(b ** 2 - 4 * a * c)

    # Calculate the two roots
    root1 = (-b + discriminant) / (2 * a)
    root2 = (-b - discriminant) / (2 * a)

    return root1, root2

print(solve_quadratic(1, -3, 2))

#8: Declare a function that prints each element in a list.
def print_list(lst):
    for item in lst:
        print(item)

fruits = ['Banana', 'Apple', 'Orange', 'Mango', 'Watermelon']
print_list(fruits)

#9: Declare a function, returns the array in reverse order using loops.
def reverse_lst(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

print(reverse_lst([1,2,3,4,5]))

#10: Declare a function, returns a list with all items capitalized.
def capitalize_list_items(lst):
    capitalized = []
    for item in lst:
        if type(item) == str:
            capitalized.append(item.capitalize())
        else:
            capitalized.append(item)
    return capitalized

print(capitalize_list_items(['jama', 'ali']))

#11: Declare func that adds an item to the end of a list and returns it.
def add_item(lst, *item):
    lst.extend(item)
    return lst

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff, 'Meat', 'Fish'))

#12: Declare func, removes an item from a list and returns the updated list.
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

print(remove_item(food_stuff, 'Mango'))

#13: Declare func, returns the sum of all numbers up to a given number.
def sum_of_numbers(rng):
    tot = 0
    for i in range(rng +1):
        tot += i

    return tot

print(sum_of_numbers(5))
print(sum_of_numbers(100))

#14: Declare a func, takes a num parameter & adds all the odd numbers in that range.
def sum_of_odds(rng):
    odd_sums = 0
    for num in range(rng):
        if num % 2 != 0:
            odd_sums += num
    return odd_sums

print(sum_of_odds(100))

#15: Declare a func, takes a num parameter & adds all the even numbers in that range.
def sum_of_evens(rng):
    even_sums = 0
    for num in range(rng):
        if num % 2 == 0:
            even_sums += num
    return even_sums

print(sum_of_evens(100))

# --------------------- Level 2 -----------------------

#1: Count evens and odds in a range number
def evens_and_odds(n):
    evens = 0
    odds = 0
    for i in range(n + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1

    print(f"The number of odds are {odds}.")
    print(f"The number of evens are {evens}.")

evens_and_odds(100)

#2: Function factorial, takes a whole number as a parameter, returns a factorial of the number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(10))

#3: Call your function is_empty, it takes a parameter & it checks if it is empty or not
def is_empty(value):
    return not bool(value)

print(is_empty(""))
print(is_empty([]))
print(is_empty("Hello"))
print(is_empty([1, 2]))

#4: Define a func to compute basic stats on a list (mean, median, mode, variance & std)
def calculate_statistics(numbers):
    from collections import Counter
    import math

    n = len(numbers)
    sorted_numbers = sorted(numbers)

    # Mean
    mean = sum(numbers) / n

    # Median
    mid = n // 2
    if n % 2 == 0:
        median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        median = sorted_numbers[mid]

    # Mode
    count = Counter(numbers)
    max_freq = max(count.values())
    modes = [k for k, v in count.items() if v == max_freq]
    mode = modes if len(modes) != len(count) else "No mode"

    # Range
    range_val = max(numbers) - min(numbers)

    # Variance
    variance = sum((x - mean) ** 2 for x in numbers) / n

    # Standard Deviation
    std_dev = math.sqrt(variance)

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "range": range_val,
        "variance": variance,
        "std_dev": std_dev
    }

# Example usage
data = [1, 2, 2, 3, 4, 5, 5, 5, 6]
stats = calculate_statistics(data)

for key, value in stats.items():
    print(f"{key.capitalize()}: {value}")

#5: Define a function that greets a user, default "Guest"
def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet()) # Default -> Guest
print(greet("Gurmad"))

#6: Define function that prints names and values of any given keyword arguments
def show_args(**kwargs):
    received = "Received: "
    for name, value in kwargs.items():
        received += f"{name}: {value}, "

    # Remove the trailing comma and space
    received = received.rstrip(", ")
    print(received)

# Example usage
show_args(name="Alice", age=30, city="New York")

# --------------------- Level 3 -----------------------

#1: Write a function called is_prime, which checks if a number is prime.

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Example
print(is_prime(2))   # True
print(is_prime(17))  # True
print(is_prime(18))  # False

#2: Write a functions which checks if all items are unique in the list.
def is_unique(lst):
    return len(lst) == len(set(lst))

print(is_unique([1, 2, 3, 4]))      # True
print(is_unique([1, 2, 2, 3, 4]))   # False

#3: Write a func, which checks if all the items of the list are of the same data type.
def same_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    return all(type(item) == first_type for item in lst)

print(same_type([1, 2, 3, 4]))          # True
print(same_type([1, "2", 3, 4]))        # False
print(same_type([]))                     # True
print(same_type(["a", "b", "c"]))       # True

#4: Write a function which check if provided variable is a valid python variable
def is_valid_variable(name):
    return name.isidentifier()

print(is_valid_variable("my_var"))   # True
print(is_valid_variable("2var"))     # False
print(is_valid_variable("var-name")) # False
print(is_valid_variable("_temp"))    # True
