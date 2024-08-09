# Write a Python program to calculate the sum of the numbers in a given tuple.

# Input: tuples_list = [(1, 2), (3, 4), (5, 6)]

tuples_list = [(1, 2), (3, 4), (5, 6)]
sum = 0
for lists in tuples_list:
    for i in lists:
        sum = sum + i

print(f"Sum: {sum}")