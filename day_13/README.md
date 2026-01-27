# 💻 Day 13 – List Comprehension and Lambda Exercises (Python)

## 1️⃣ Filter Negative Numbers and Zero

Filter only negative numbers and zero from the list using list comprehension.

```python
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
````

## 2️⃣ Flatten a List of Lists

Flatten the following list of lists of lists to a one-dimensional list.

```python
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

**Output**

```text
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## 3️⃣ List of Tuples Using List Comprehension

Using list comprehension, create the following list of tuples:

```text
[(0, 1, 0, 0, 0, 0, 0),
 (1, 1, 1, 1, 1, 1, 1),
 (2, 1, 2, 4, 8, 16, 32),
 (3, 1, 3, 9, 27, 81, 243),
 (4, 1, 4, 16, 64, 256, 1024),
 (5, 1, 5, 25, 125, 625, 3125),
 (6, 1, 6, 36, 216, 1296, 7776),
 (7, 1, 7, 49, 343, 2401, 16807),
 (8, 1, 8, 64, 512, 4096, 32768),
 (9, 1, 9, 81, 729, 6561, 59049),
 (10, 1, 10, 100, 1000, 10000, 100000)]
```

## 4️⃣ Flatten Country and City Data

Flatten the following list to a new list:

```python
countries = [[('Finland', 'Helsinki')],
             [('Sweden', 'Stockholm')],
             [('Norway', 'Oslo')]]
```

**Output**

```text
[['FINLAND', 'FIN', 'HELSINKI'],
 ['SWEDEN', 'SWE', 'STOCKHOLM'],
 ['NORWAY', 'NOR', 'OSLO']]
```

## 5️⃣ Convert List to a List of Dictionaries

Change the following list to a list of dictionaries:

```python
countries = [[('Finland', 'Helsinki')],
             [('Sweden', 'Stockholm')],
             [('Norway', 'Oslo')]]
```

**Output**

```text
[{'country': 'FINLAND', 'city': 'HELSINKI'},
 {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
 {'country': 'NORWAY', 'city': 'OSLO'}]
```

## 6️⃣ Concatenate Names

Change the following list of lists to a list of concatenated strings:

```python
names = [[('Asabeneh', 'Yetayeh')],
         [('David', 'Smith')],
         [('Donald', 'Trump')],
         [('Bill', 'Gates')]]
```

**Output**

```text
['Asabeneh Yetayeh', 'David Smith', 'Donald Trump', 'Bill Gates']
```

## 7️⃣ Lambda Function

Write a lambda function which can solve a slope or y-intercept of linear functions.

---
**Gurmad Harir**  
January 27, 2026.
