# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

num1 = int(input("enter a number : "))
num2 = int(input("enter a number : "))

try:
    print("division -", num1/num2)

except ZeroDivisionError:
    print("Division is undefined")


