# Write a Python program to Count all letters, digits, and special symbols from the given string

# Input = “P@#yn26at^&i5ve”

letter = 0
digits = 0
symbols = 0

a = "P@#yn26at^&i5ve"

for char in a:
    if char.isalpha():
        letter += 1
    elif char.isnumeric():
        digits += 1
    else:
        symbols += 1

print("Letters : ", letter)
print("Digits : ", digits)
print("Symbols : ", symbols)
