# Write a Python program to get the largest and smallest number from a list without builtin functions.

def lar_and_small(li):
    largest = li[0]
    smallest = li[0]
    try:
        for number in li:
            if number > largest:
                largest = number
            if number < smallest:
                smallest = number
        print(f"Largest number in the list - {largest}\nSmallest number in the list - {smallest}")

    except TypeError as te:
        print("Please enter all integer elements in list")


lar_and_small(li=[1, 2, 3, 4, 5, "abc"])

