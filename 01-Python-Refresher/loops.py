"""
LOOPS
"""

# For Loop
my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)

print()

for number in range(3, 6):
    print(number)

print()

sum_of_loop = 0
for item in my_list:
    sum_of_loop += item
print(sum_of_loop)

print()

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in weekdays:
    print(f"Today is {day}")

print()

# While Loop
i = 0
while i < 5:
    i += 1
    print(i)

print()

i = 0
while i < 5:
    i += 1
    print(i)
else:
    print("i is now larger than 5")