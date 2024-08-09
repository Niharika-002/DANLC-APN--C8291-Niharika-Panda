# Write a Python program to count and display the vowels of a given text

# String="Welcome to python Training"

str = "Welcome to python Training"

count = 0
for vowels in str.lower():
    if vowels in "aeiou":
        count += 1

print(f"Number of vowels in the string: {count}")

