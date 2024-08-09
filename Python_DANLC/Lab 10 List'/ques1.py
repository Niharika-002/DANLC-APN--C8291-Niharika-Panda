# Write a Python program to sum all the items in a list.

def sum_elements(li):

    try:
        total = 0
        for i in li:
            total = total + i
        print(f"sum of the given list is {total}")

    except TypeError as ve:
        print("Please enter integer to add")


sum_elements(li=[2, 3, 4, 5, "abv"])
