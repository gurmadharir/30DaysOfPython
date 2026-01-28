# 💻 Day 18 – Regular Expressions (Python) AKA Regx

## 📘 Level 1

### 1. Find the most frequent word in the following paragraph:

```python
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
````

Expected output format (example):

```
[
    (6, 'love'),
    (5, 'you'),
    (3, 'can'),
    (2, 'what'),
    (2, 'teaching'),
    (2, 'not'),
    (2, 'else'),
    (2, 'do'),
    (2, 'I'),
    (1, 'which'),
    (1, 'to'),
    (1, 'the'),
    (1, 'something'),
    (1, 'if'),
    (1, 'give'),
    (1, 'develop'),
    (1, 'capabilities'),
    (1, 'application'),
    (1, 'an'),
    (1, 'all'),
    (1, 'Python'),
    (1, 'If')
]
```

---

### 2. Distance Between Furthest Particles

The position of some particles on the horizontal x-axis are:
`-12, -4, -3, -1` in the negative direction, `0` at origin, `4, 8` in the positive direction.

**Task:**

* Extract these numbers from the text
* Find the distance between the two furthest particles

Example:

```
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
```



## 📗 Level 2

### 1. Write a pattern which identifies if a string is a **valid Python variable name**:

```
is_valid_variable('first_name')   # True
is_valid_variable('first-name')   # False
is_valid_variable('1first_name')  # False
is_valid_variable('firstname')    # True
```

## 📕 Level 3

### 1. Clean the following text and then count the **three most frequent words**:

```
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
```

Example of cleaned text output:

```
I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
```

Example of most frequent words:

```
[(3, 'I'), (2, 'teaching'), (2, 'teacher')]
```

---
**Gurmad Harir**  
January 28, 2026.
