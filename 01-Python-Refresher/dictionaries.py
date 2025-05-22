"""
DICTIONARIES
"""

user_dictionary = {
    "username": "learning_fastapi",
    "name": "Saad",
    "age": 27
}

print(user_dictionary)
print()

# Getting Value of Key
print(user_dictionary.get("username"))
print()

# Adding to Dictionary
user_dictionary["is_married"] = False
print(user_dictionary)
print()

# Length of Dictionary
print(len(user_dictionary))
print()

# Loop Through Dictionary
for item in user_dictionary:
    print(item)
print()

for key, value in user_dictionary.items():
    print(key, value)
print()

# Removing Key
user_dictionary.pop("age")
print(user_dictionary)
print()

# Clearing Dictionary
user_dictionary.clear()
print(user_dictionary)
print()

# Deleting Dictionary
del user_dictionary

