# Given two lists `a = [1, 2, 3]` and `b = [4, 5, 6]`, write code to merge
# them into a single list and then flatten a list of lists `c = [[1, 2], [3, 4], [5, 6]]` into a single list.

import numpy as np

a = [1, 2, 3]
b = [4, 5, 6]

merged_list = a + b
print("Merged List:", merged_list)


c = [[1, 2], [3, 4], [5, 6]]

flattened_list = np.array(c).flatten().tolist()
print("Flattened list : ", flattened_list)