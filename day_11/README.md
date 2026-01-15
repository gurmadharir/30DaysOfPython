# 💻 Day 11 – Functions Exercises (Python)

## 📘 Level 1

1. **Declare a function `add_two_numbers`**  
   - It takes two parameters and returns their sum.


2. **Area of a circle**  
   - Formula: `area = π × r × r`  
   - Write a function `area_of_circle` to calculate it.


3. **Add all numbers**  
   - Function `add_all_nums` takes arbitrary number of arguments and sums them.  
   - Check if all arguments are numbers; if not, give feedback.


4. **Convert Celsius to Fahrenheit**  
   - Formula: `°F = (°C × 9/5) + 32`  
   - Function: `convert_celsius_to_fahrenheit`


5. **Check season**  
   - Function `check_season` takes a month and returns the season: Autumn, Winter, Spring, or Summer.


6. **Calculate slope**  
   - Function `calculate_slope` returns the slope of a linear equation.


7. **Solve quadratic equation**  
   - Quadratic formula: `ax² + bx + c = 0`  
   - Function `solve_quadratic_eqn` calculates the solution set.


8. **Print list elements**  
   - Function `print_list` takes a list and prints each element.


9. **Reverse list**  
   - Function `reverse_list` takes a list and returns it reversed using loops.  
   - Example:  
     ```
     print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
     print(reverse_list(["A", "B", "C"]))  # ["C", "B", "A"]
     ```

10. **Capitalize list items**  
    - Function `capitalize_list_items` takes a list and returns a list with all items capitalized.


11. **Add item to list**  
    - Function `add_item(list, item)` returns the list with the item added at the end.  
    - Example:
      ```
      food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
      print(add_item(food_stuff, 'Meat'))  # ['Potato', 'Tomato', 'Mango', 'Milk', 'Meat']
      numbers = [2, 3, 7, 9]
      print(add_item(numbers, 5))  # [2, 3, 7, 9, 5]
      ```

12. **Remove item from list**  
    - Function `remove_item(list, item)` returns the list with the item removed.  
    - Example:
      ```
      food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
      print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk']
      numbers = [2, 3, 7, 9]
      print(remove_item(numbers, 3))  # [2, 7, 9]
      ```

13. **Sum of numbers in a range**  
    - Function `sum_of_numbers(n)` returns the sum of numbers from 1 to `n`.  
    - Example:
      ```
      print(sum_of_numbers(5))   # 15
      print(sum_of_numbers(10))  # 55
      print(sum_of_numbers(100)) # 5050
      ```

14. **Sum of odd numbers**  
    - Function `sum_of_odds(n)` returns the sum of all odd numbers in the range 1 to `n`.


15. **Sum of even numbers**  
    - Function `sum_of_even(n)` returns the sum of all even numbers in the range 1 to `n`.

---

## 📗 Level 2

1. **Count evens and odds**  
   - Function `evens_and_odds(n)` counts the number of even and odd digits in numbers from 1 to `n`.  
   - Example:
     ```
     print(evens_and_odds(100))
     # The number of odds are 50.
     # The number of evens are 51.
     ```

2. **Factorial**  
   - Function `factorial(n)` returns the factorial of a whole number `n`.


3. **Check if empty**  
   - Function `is_empty(value)` checks if the value is empty.


4. **List statistics**  
   - Functions to calculate mean, median, mode, range, variance, and standard deviation of a list.


5. **Greet with default argument**  
   - Function `greet(name="Guest")` prints a greeting.  
   - Example:
     ```
     greet()         # "Hello, Guest!"
     greet("Alice")  # "Hello, Alice!"
     ```

6. **Show named arguments**  
   - Function `show_args(**kwargs)` prints names and values of all provided keyword arguments.  
   - Example:
     ```
     show_args(name="Alice", age=30, city="New York")
     # Received: name: Alice, age: 30, city: New York
     show_args(name="Bob", pet="Fluffy, the bunny")
     # Received: name: Bob, pet: Fluffy, the bunny
     ```

---

## 📕 Level 3

1. **Check prime**  
   - Function `is_prime(num)` checks if a number is prime.


2. **Check uniqueness**  
   - Function checks if all items in a list are unique.


3. **Check same type**  
   - Function checks if all items in a list have the same data type.


4. **Valid Python variable**  
   - Function checks if a string is a valid Python variable name.

---
**Gurmad Harir**  
January 15, 2026.