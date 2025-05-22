"""
CONTINUE AND BREAK STATEMENTS
"""

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in weekdays:
    if day == "Tuesday":
        continue
    print(day)

print()

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
for month in months:
    if month == "October":
        break
    print(month)
