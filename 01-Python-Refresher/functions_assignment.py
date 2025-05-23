"""
FUNCTION ASSIGNMENT

- Create a function that takes in 3 parameters(firstname, lastname, age) and

returns a dictionary based on those values
"""

def my_dictionary(first_name, last_name, age):
    return {"first_name": first_name, "last_name": last_name, "age": age}

details = my_dictionary(first_name="Saad", last_name="Tariq", age=27)
print(details)
