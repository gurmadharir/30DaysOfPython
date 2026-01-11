# =========================
# Day 6: Tuples
# =========================

# ---------- Level 1 ----------

# Empty tuple
empty_tuple = ()

# Siblings
brothers = ('Kah', 'Kal', 'Kasmal')
sisters = ('Zurare', 'Safi', 'Sirad')

# Combine siblings
siblings = brothers + sisters
print("Number of siblings:", len(siblings))

# Add parents
family_members = ('Harir', 'Habibo') + siblings


# ---------- Level 2 ----------

# Unpack parents and siblings
father, mother, *siblings = family_members
parents = (father, mother)

print("Parents:", parents)
print("Siblings:", siblings)

# Food tuples
fruits = ('Mango', 'Orange', 'Grape', 'Lime')
vegetables = ('Spinach', 'Kale', 'Tomato', 'Potato')
animal_products = ('Cat', 'Dog', 'Goat', 'Sheep', 'Camel')

# Join food tuples
food_stuff_tp = fruits + vegetables + animal_products
print("Food tuple:", food_stuff_tp)

# Convert tuple to list
food_stuff_lt = list(food_stuff_tp)
print("Food list:", food_stuff_lt)

# Middle item(s)
length = len(food_stuff_lt)
mid = length // 2
middle_items = food_stuff_lt[mid-1:mid+1] if length % 2 == 0 else food_stuff_lt[mid:mid+1]
print("Middle item(s):", middle_items)

# First and last three items
print("First three:", food_stuff_lt[:3])
print("Last three:", food_stuff_lt[-3:])

# Delete tuple
del food_stuff_tp

# Nordic countries check
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print("Estonia is Nordic:", 'Estonia' in nordic_countries)
print("Iceland is Nordic:", 'Iceland' in nordic_countries)
