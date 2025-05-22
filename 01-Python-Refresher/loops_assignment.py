"""
LOOPS ASSIGNMENT

Given: my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

- Create a while loop that prints all elements of the my_list variable 3 times.

- When printing the elements, use a for loop to print the elements

- However, if the element of the for loop is equal to Monday, continue without printing
"""

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

count = 0
while count < 3:
    for item in my_list:
        if item == "Monday":
            continue
        print(item)
    count += 1
    print()
