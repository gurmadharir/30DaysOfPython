# =========================
# Day 4 Python Exercises
# =========================

# --- Section 1: Concatenation ---
challenge = "Thirty" + " Days" + " Of" + " Python"  # Combine words
print(challenge)

code = "Coding " + "For " + "All"  # Combine words
print(code)

# --- Section 2: Variables & Basic Info ---
company = "Coding For All"  # Declare variable
print(company)
print(len(company))          # Length of string

# --- Section 3: String Methods ---
print(company.upper())       # Uppercase
print(company.lower())       # Lowercase
print(company.capitalize())  # Capitalize first letter
print(company.title())       # Title case
print(company.swapcase())    # Swap case

# --- Section 4: Slicing & Indexing ---
print(company[0:6])          # First word
print(company[0])            # First character
print(company[-1])           # Last character
print(company[10])           # Character at index 10

# --- Section 5: Searching & Replacing ---
print(company.find("Coding"))               # Check if word exists
print("Coding" in company)                  # Boolean check
print(company.replace("Coding", "Python"))  # Replace word

# Replace for another example
text = "Python for Everyone"
print(text.replace("Everyone", "All"))

# --- Section 6: Splitting & Joining ---
print(company.split())  # Split by space

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(','))  # Split by comma

py_libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(py_libs))    # Join with hash and space

# --- Section 7: Acronyms ---
print("Python For Everyone"[:1] + "F" + "E")  # Simple PFE
# Better using comprehension
phrase = "Python For Everyone"
acronym = "".join([word[0] for word in phrase.split()])
print(acronym)

phrase2 = "Coding For All"
acronym2 = "".join([word[0] for word in phrase2.split()])
print(acronym2)

# --- Section 8: Indexing & rfind ---
print(company.index("C"))                 # First C
print(company.index("F"))                 # First F
print("Coding For All People".rfind("l")) # Last l

# --- Section 9: Searching 'because' ---
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find("because"))    # First occurrence
print(sentence.rindex("because"))  # Last occurrence
print(sentence[31:54])             # Slice phrase

# --- Section 10: Start/End Checks & Strip ---
print(company.startswith("Coding"))      # Starts with Coding?
print(company.endswith("coding"))        # Ends with coding?
print('   Coding For All      '.strip()) # Remove spaces

# --- Section 11: Valid Identifiers ---
print("30DaysOfPython".isidentifier())        # False
print("thirty_days_of_python".isidentifier()) # True

# --- Section 12: Escape Sequences ---
print("I am enjoying this challenge.\nI just wonder what is next.")  # Newline
print("Name\tAge\tCountry\tCity")                                      # Tab
print("Gurmad\t21\tHargeisa\tSomaliland")                               # Tabbed data

# --- Section 13: String Formatting ---
# Circle area old-style
radius = 10
pi = 3.14
area = pi * radius ** 2
print("The area of circle with radius %d is %.2f" % (radius, area))

# Arithmetic operations with new-style formatting
a, b = 8, 6
print(f"\n{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")
