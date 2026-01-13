# =========================
# Day 8: Sets
# =========================

# Create an empty dictionary dog
dog = dict()

# Add name, color, breed, legs, age
dog['Name'] = 'Buddy'
dog['Color'] = 'Brown'
dog['Breed'] = 'Labrador'
dog['Legs'] = 4
dog['Age'] = 5

print(dog)

""""
Create a student dictionary, add first_name, last_name, gender, age, 
marital status, skills, country, city and address as keys for the dictionary
"""
student = {
    'first Name': 'Gurmad',
    'last Name': 'Abdulle',
    'age': 22,
    'gender': 'Male',
    'is_married': False,
    'skills': ['Python', 'Excel', 'SQL'],
    'country': 'Somaliland',
    'city': 'Hargeisa',
    'address': 'Waaheen'
}

# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type.
print(student.get('skills'))
print(type(student['skills']))

# Modify the skills values by adding one or two skills
student['skills'].append('HTML')
student['skills'].append('PHP')

print(student['skills'])

# Get the dictionary keys as a list
student_keys = student.keys()
print(student_keys)

# Get the dictionary values as a list
student_values = student.values()
print(student_values)

# Change the dictionary to a list of tuples
std_ls = student.items()
print(std_ls)

# Delete one of the items in the dictionary
del student['address']

# Delete one of the dictionaries
del dog