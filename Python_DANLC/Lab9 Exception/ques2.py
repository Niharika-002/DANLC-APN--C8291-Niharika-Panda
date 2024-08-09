class IntegerNotBetween1to1000(Exception):
    def __init__(self):
        super().__init__("the number you entered is not between 1 to 1000\nPlease enter number between 1 to 1000")


try:
    num = int(input("enter a number : "))
    if not 1 <= num <= 1000:
        raise IntegerNotBetween1to1000()
    print("number is valid integer")

except IntegerNotBetween1to1000 as e:
    print(e)

except ValueError as ve:
    print("Invalid Integer")
