"""
FUNCTIONS
"""

# Function with No Parameter
def my_function():
    print("Inside my function")

my_function()


# Function with One Parameter
def print_my_name(name):
    print(f"Hello {name}")

print_my_name("Saad")

# Function with Two Parameters
def print_name(first_name, last_name):
    print(f"Hello {first_name} {last_name}")

print_name(first_name="Saad", last_name="Tariq")

# Function with Local Variable
def print_color_red():
    color = "Red"
    print(color)
print_color_red()


# Function with Return
def multiply_numbers(number1, number2):
    return number1 * number2

solution = multiply_numbers(number1=10, number2=6)
print(solution)

# Function with List as Parameter
def print_list(list_of_numbers):
    for number in list_of_numbers:
        print(number)

number_list = [1, 2, 3, 4, 5]
print_list(list_of_numbers=number_list)


# Function calling Function
def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)

def add_tax_to_item(cost_of_item):
    current_tax_rate = .15
    return cost_of_item * current_tax_rate

final_cost = buy_item(cost_of_item=50)
print(final_cost)