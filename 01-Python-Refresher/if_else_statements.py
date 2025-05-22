"""
FLOW CONTROL: IF ELSE STATEMENTS
"""


x = 1

if x == 1:
    print("x is 1")

print("Outside of If Statements")

print()

x = 2

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

print("Outside of If Statements")

print()

hour = 13
if hour < 15:
    print("Good Morning")
elif hour < 20:
    print("Good Evening")
else:
    print("Good Night")
