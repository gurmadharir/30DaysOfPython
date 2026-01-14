# =========================
# Day 9: Conditionals
# =========================

# --------------- Level 1 -----------------

# 1: Age check for driving eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
elif age < 0 :
    print("Please enter a valid age")
else:
    left_age = 18 - age
    print(f"You need {left_age} more years to learn to drive.")


# 2: Compare two ages to find who is older
my_age = 22
your_age = int(input("Enter your age: "))

if my_age > your_age:
    age_diff = my_age - your_age
    print(f"I am {age_diff} years older than you")
elif my_age < your_age:
    age_diff = your_age - my_age
    print(f"You're {age_diff} years older than me")
else:
    print("We're the same age")


# 3: Compare two numbers and show result
num_1 = float(input("Enter number 1: "))
num_2 = float(input("Enter number 2: "))

if num_1 > num_2:
    print(f"{num_1} is greater than {num_2}")
elif num_2 > num_1:
    print(f"{num_2} is greater than {num_1}")
else:
    print(f"{num_1} and {num_2} are same")

# ---------------- Level 2 -------------------
# 1: Assign grades based on student scores
score = int(input("Enter your score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# 2: Determine season based on month
month = input("Enter a month: ").capitalize()

if month in ["September", "October", "November"]:
    print("Autumn")
elif month in ["December", "January", "February"]:
    print("Winter")
elif month in ["March", "April", "May"]:
    print("Spring")
elif month in ["June", "July", "August"]:
    print("Summer")
else:
    print("Invalid month")

# 3: Add fruit if not in list
fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input("Enter a fruit: ").lower()
if fruit in fruits:
    print("That fruit already exists in the list")
else:
    fruits.append(fruit)
    print(fruits)

# ------------------- Level 3 ----------------------

# Here we have a person dictionary. Feel free to modify it!
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

# Print middle skill if exists
if 'skills' in person and person['skills']:
    md_skill = len(person['skills']) // 2
    print(person['skills'][md_skill])

# Check for Python skill if exists
if 'skills' in person and person['skills']:
    if 'Python' in person['skills']:
        print("Person has Python skills")
    else:
        print("Person does not have Python skills")

# Identify developer type from skills
if 'skills' in person and person['skills']:
    skills = person['skills']
    if set(skills) == {"JavaScript", "React"}:
        print('He is a front end developer')
    elif set(["Node","Python","MongoDB"]).issubset(skills):
        print('He is a backend developer')
    elif set(["React","Node","MongoDB"]).issubset(skills):
        print('He is a fullstack developer')
    else:
        print('unknown title')
