"""
STRING FORMATTING
"""

first_name = "Saad"
print(f"Hi {first_name}")


sentence = "Hi {}"
print(sentence.format(first_name))


sentence = "Hi {} {}"
last_name = "Tariq"
print(sentence.format(first_name, last_name))