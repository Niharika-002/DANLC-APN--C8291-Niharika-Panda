# Write a Python program to reverse words in a string

# String = “Deeptech Python Training”

str = "Deeptech Python Training"
print(str)

words = str.split()

str2 = ""

for k in words:
    str2 += k[::-1] + " "

print(str2)
