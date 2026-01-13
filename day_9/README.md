
# 💻 Day 9 – Conditionals Exercises (Python)


## 📘 Level 1

1. **Driving Eligibility**

   Get user input using `input("Enter your age: ")`.  
   - If the user is 18 or older, print: `You are old enough to drive.`  
   - If below 18, print how many years are left: `You need X more years to learn to drive.`  

    ```
    Enter your age: 30
    You are old enough to learn to drive.
    
    Enter your age: 15
    You need 3 more years to learn to drive.
    ```

2. **Age Comparison**  
Compare `my_age` and `your_age` using `if ... else`.  
   - Print who is older.  
   - Use a nested condition to print `'year'` for 1 year difference, `'years'` for more, and a custom message if ages are equal.  

    ```
    Enter your age: 30
    You are 5 years older than me.
    ```

3. **Compare Two Numbers**  
Get two numbers from the user.  
   - If `a > b`, print `a is greater than b`.  
   - If `a < b`, print `a is smaller than b`.  
   - Otherwise, print `a is equal to b`.  

    ```
    Enter number one: 4
    Enter number two: 3
    4 is greater than 3
    ```

---

## 📗 Level 2

1. **Grade Students**  
Write code to give grades based on score:  
    ```
    90-100: A
    80-89: B
    70-79: C
    60-69: D
    0-59: F
    ````

2. **Season from Month**  

   Get the month from user input and print the season:  
   - September, October, November → Autumn  
   - December, January, February → Winter  
   - March, April, May → Spring  
   - June, July, August → Summer  


3. **Fruit List**  
    ```
    fruits = ['banana', 'orange', 'mango', 'lemon']
    ````

   * If a fruit doesn’t exist in the list, add it and print the modified list.
   * If it exists, print: `That fruit already exists in the list`.

---

## 📕 Level 3

```python
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
```

1. **Middle Skill**

   * Check if the dictionary has a `skills` key.
   * If so, print the middle skill from the list.


2. **Check for Python Skill**

   * Check if `skills` exists and contains `'Python'`.
   * Print the result.


3. **Developer Type**

   * If `skills` has only `JavaScript` and `React`, print: `He is a front end developer`.
   * If `skills` has `Node`, `Python`, and `MongoDB`, print: `He is a backend developer`.
   * If `skills` has `React`, `Node`, and `MongoDB`, print: `He is a fullstack developer`.
   * Otherwise, print: `unknown title`.

---
**Gurmad Harir**  
January 13, 2026
