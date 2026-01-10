# =========================
# Day 5 Python Exercises
# =========================

# ---------- Level 1 ----------

# Declare an empty list
empty_list = []

# Declare a list with more than 5 items
lst = ["Gurmad", "Abdulle", 21, False, True, {"country": "Somaliland", "Capital": "Hargeisa"}]

# Find the length of the list
lst_len = len(lst)

# Get first, middle, and last item
print("First item:", lst[0])
print("Middle item:", lst[(lst_len-1)//2])
print("Last item:", lst[-1])

# Declare a mixed data types list
mixed_data_types = ['Gurmad', 21, 1.78, 'Single', 'Mogadishu']

# Declare IT companies list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print("IT Companies:", it_companies)
print("Number of companies:", len(it_companies))

# Access first, middle, and last company
md = (len(it_companies)-1)//2
print("First:", it_companies[0], "Middle:", it_companies[md], "Last:", it_companies[-1])

# Modify one company
it_companies[0] = 'YouTube'
print("After modification:", it_companies)

# Add an IT company
it_companies.append('Tiktok')
print("After adding:", it_companies)

# Insert a company in the middle
it_companies.insert(md, 'Instagram')
print("After inserting in middle:", it_companies)

# Change a company to uppercase (IBM excluded)
it_companies[1] = it_companies[1].upper()
print("After uppercase:", it_companies)

# Join IT companies with '#;  '
joined_companies = '#; '.join(it_companies)
print("Joined companies:", joined_companies)

# Check if a company exists
print("Is Coursera in the list?", 'Coursera' in it_companies)

# Sort the list
it_companies.sort()
print("Sorted:", it_companies)

# Reverse the list
it_companies.sort(reverse=True)
print("Reversed:", it_companies)

# Slice first 3 companies
print("First 3:", it_companies[:3])

# Slice last 3 companies
print("Last 3:", it_companies[-3:])

# Slice middle company
print("Middle company:", it_companies[md])

# Remove first, middle, last companies
it_companies.pop(0)    # first
it_companies.pop(md)   # middle
it_companies.pop()     # last
print("After removing first, middle, last:", it_companies)

# Remove all companies
it_companies.clear()
print("After clearing all:", it_companies)

# Destroy the list (optional)
# del it_companies

# Join front-end and back-end lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print("Joined front-end & back-end:", front_end)

# Copy joined list and add Python & SQL
full_stack = front_end.copy()
full_stack.insert(full_stack.index('Redux')+1, 'Python')
full_stack.insert(full_stack.index('Python')+1, 'SQL')
print("Full Stack:", full_stack)


# ---------- Level 2 ----------

# Ages list
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort and find min/max
ages.sort()
print("Sorted ages:", ages)
print("Min age:", min(ages))
print("Max age:", max(ages))

# Add min and max again
ages += [min(ages), max(ages)]
print("After adding min and max again:", ages)

# Find median
n = len(ages)
median = (ages[n//2] + ages[(n-1)//2]) / 2
print("Median age:", median)

# Find average
avg = sum(ages)/n
print("Average age:", avg)

# Find range
age_range = max(ages) - min(ages)
print("Age range:", age_range)

# Compare min-average and max-average using abs()
print("abs(min-avg):", abs(min(ages)-avg))
print("abs(max-avg):", abs(max(ages)-avg))

# Countries list
countries = ["USA", "Nepal", "UAE", "Somaliland", "Malaysia", "South Sudan", "Bangladesh"]

# Find middle country
mid = len(countries)//2
print("Middle country:", countries[mid])

# Divide into two halves (first half extra if odd)
mid_split = (len(countries)+1)//2
first_half = countries[:mid_split]
second_half = countries[mid_split:]
print("First half:", first_half)
print("Second half:", second_half)
