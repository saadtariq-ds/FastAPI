"""
VARIABLES ASSIGNMENT

- You have $50

- You buy an item that is $15, that has a 3% tax

- Using the print()  Print how much money you have left, after purchasing the item.
"""

purse = 50
item = 15
tax_percent = .03
tax = item * tax_percent

purse_left = purse - item - tax
print(purse_left)