"""
SETS
"""

my_set = {1, 2, 3, 4, 5, 1, 2, 3}
print(my_set)
print(len(my_set))
print()

# Looping through set
for item in my_set:
    print(item)

# Removing Item from Set
my_set.discard(3)
print(my_set)

# Add Item to Set
my_set.add(6)
print(my_set)

# Add More Than 1 Item in Set
my_set.update([7, 8])
print(my_set)

# Clear Set
my_set.clear()
print(my_set)