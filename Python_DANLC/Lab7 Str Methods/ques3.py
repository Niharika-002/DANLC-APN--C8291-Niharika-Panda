# Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string

# Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”

# Output: UpperCase : 5 LowerCase : 18 NumberCase : 5 SpecialCase : 11

Input = "Hell0 W0rld ! 123 * # welcome to pYtHoN"

# result = Input.split()

uppercase = 0
lowercase = 0
special_char = 0
num = 0

for count in Input:
    if count.islower():
        lowercase += 1
    elif count.isupper():
        uppercase += 1
    elif count.isnumeric():
        num += 1
    else:
        special_char += 1


print("Uppercase : ", uppercase)
print("Lowercase : ", lowercase)
print("Special_char : ", special_char)
print("Numeric : ", num)

