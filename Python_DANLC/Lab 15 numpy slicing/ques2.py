# Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

import numpy as np

my_arr = np.arange(2, 11)
r = my_arr.reshape(3,3)

print(r)