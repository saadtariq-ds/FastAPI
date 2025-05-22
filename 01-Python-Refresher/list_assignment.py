"""
LIST ASSIGNMENT

- Create a list of 5 animals called zoo

- Delete the animal at the 3rd index.

- Append a new animal at the end of the list

- Delete the animal at the beginning of the list.

- Print all the animals

- Print only the first 3 animals
"""

zoo = ["Lion", "Tiger", "Elephant", "Crocodile", "Monkey"]
print(zoo)

# Removing Animal from 3rd Index
zoo.pop(3)
print(zoo)

# Appending a new Animal
zoo.append("Rhino")
print(zoo)

# Deleting an Animal at the Beginning of the List
zoo.pop(0)
print(zoo)

# Printing all Animals
for animal in zoo:
    print(animal)

# Printing First 3 Animals
print(zoo[0:3])