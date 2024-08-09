# Write a Python Count vowels in a string
# Input= “Welcome to Python Assignment”
# Output: Total vowels are:8

string = "Welcome to Python Assignment"
string2 = string.lower()
count = 0

for vowels in string2:
    if vowels in "aeiou":
        count += 1

print(f"Total vowels are : {count}")

