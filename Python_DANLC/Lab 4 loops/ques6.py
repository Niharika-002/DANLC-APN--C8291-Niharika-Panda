 # Wap to find the binary number of the given integer.

# 1.      Input a number

# 2.      Find the modulus of this number by 2 and save it into a array

# 3.      After the loop is finished, print the array in reverse.

num = int(input("Enter the number for conversion : "))
result = []

while num > 0:
    result.append(num % 2)    # it stores the remainder
    num //= 2                 # it stores the quotient

print(result)

print("Binary representation is :", end=" ")
for digit in reversed(result):
    print(digit, end="")
print()
