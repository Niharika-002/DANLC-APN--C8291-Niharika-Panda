# Write a function `rotate_list(lst, k)` that rotates a list to the right by `k` positions.
# For example, `rotate_list([1, 2, 3, 4, 5], 2)` should return `[4, 5, 1, 2, 3]`.


def rotate_list(lst, k):
    k = k % len(lst) if lst else 0
    return lst[-k:] + lst[:-k]


result = rotate_list([1, 2, 3, 4, 5], 2)
print(result)  # Output: [4, 5, 1, 2, 3]
