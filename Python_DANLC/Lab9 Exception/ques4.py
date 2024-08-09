# Write a Python program that prompts the user to input two numbers and raises a
# TypeError exception if the inputs are not numerical

class NotaNumberError(Exception):
    def __init__(self):
        super().__init__("Both the number should be numerical\nEnter only numeric values")

try:
    num1 = input("enter 1st number - ")
    num2 = input("enter 2nd number - ")
    if not (num1.isnumeric() and num2.isnumeric()):
        raise NotaNumberError
    print(f"{num1} and {num2} are numerical")

except NotaNumberError as e:
    print(e)





