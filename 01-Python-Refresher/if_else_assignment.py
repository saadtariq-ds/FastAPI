"""
IF ELSE ASSIGNMENT

- Create a variable grade holding an integer between 0 - 100

- Code if, elif, else statements to print the letter grade of the number grade variable

Grades:

A = 90 - 100

B = 80 - 89

C = 70-79

D = 60 - 69

F = 0 - 59

Example:

if grade = 87 then print('B')
"""

grade = 98

if (grade >= 90) and (grade <= 100):
    print("A Grade")
elif (grade >= 80) and (grade <= 89):
    print("B Grade")
elif grade >= 70 and (grade <= 79):
    print("C Grade")
elif grade >= 60 and (grade <= 69):
    print("D Grade")
elif grade > 100:
    print("Incorrect Grade")
else:
    print("F Grade")
