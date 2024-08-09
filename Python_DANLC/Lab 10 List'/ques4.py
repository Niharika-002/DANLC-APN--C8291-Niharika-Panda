# Write a Python program to split a given list into two parts where the length
# of the first part of the list is given.
#
# Original list: [1, 1, 2, 3, 4, 4, 5, 1]
#
# Length of the first part of the list: 3
#
# Splitted the said list into two parts: ([1, 1, 2], [3, 4, 4, 5, 1])

def split_list(li, n):
    s1 = li[:n]
    s2 = li[n:]
    print(f"Original list is {li}")
    print(f"First part of the list is {s1}\nSecond part of the list os {s2}")


split_list(li=[1, 1, 2, 3, 4, 4, 5, 1], n=3)
