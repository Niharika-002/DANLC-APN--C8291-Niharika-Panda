# Multiple Exception Types in User Input

# Write a function `get_valid_date` that prompts the user to enter a date
# in the format `YYYY-MM-DD`. Use exception handling to manage:

# Invalid format (e.g., not enough parts, non-numeric parts).
# Invalid date values (e.g., month not in 1-12, day not valid for the given month).
# Ensure the function keeps asking for input until a valid date is entered and returns a `datetime.date` object.

from datetime import datetime


class InvalidFormatError(Exception):
    def __init__(self):
        super().__init__("Invalid Format")


class InvalidDateValueError(Exception):
    def __init__(self):
        super().__init__("Invalid Date")


def get_valid_date():
    while True:
        try:
            date = input("enter a date : ")
            mm = int(date[5:7])
            dd = int(date[8:])
            if not (1 <= mm <= 12 and 1 <= dd <= 31):
                raise InvalidDateValueError
            if len(date) != 10 and date[4] != '-' and date[7] != '-':
                raise InvalidFormatError

            print("valid date : ", date)

        except InvalidFormatError as fe:
            print(fe)
        except InvalidDateValueError as ve:
            print(ve)


get_valid_date()
