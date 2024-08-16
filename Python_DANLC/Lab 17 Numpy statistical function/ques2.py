# How to find the mean of every NumPy array in the given list?

import numpy as np

lst= [
np.array([3, 2, 8, 9]),
np.array([4, 12, 34, 25, 78]),
np.array([23, 12, 67])]

mean_arr = [i.mean() for i in lst]
print("Mean of each array :",mean_arr)
