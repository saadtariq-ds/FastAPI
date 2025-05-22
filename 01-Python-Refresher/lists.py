"""
LISTS
"""

my_list = [80, 96, 72, 100, 8]
print(my_list)

people_list = ["Roger", "Clarke", "Luke"]
print(people_list)


# Indexing List
print(people_list[0])
print(my_list[-1])

# Changing List
people_list[0] = "Michael"
print(people_list)

# Length of List
print(len(people_list))

# List Slicing
print(my_list[0:3])
print(my_list[:3])
print(my_list[2:])
print(my_list[2:4])

# Append to List
print(my_list)
my_list.append(150)
print(my_list)

# Insert to List
my_list.insert(3, 111)
print(my_list)

# Removing from List (Item)
my_list.remove(111)
print(my_list)

# Removing from List (Index)
my_list.pop(1)
print(my_list)

# Sorting List
my_list.sort()
print(my_list)
