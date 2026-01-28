# ============================================================================
# Day 17: Exception Handling
# ============================================================================
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

# Unpacking the first five countries
nordic_countries = names[:5]
print(nordic_countries)

# store Estonia and Russia in es and ru respectively
*_, es, ru = names
print(es, ru)