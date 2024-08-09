# function
# np.empty(size(the array)), np.searchsorted(), np.arange(range), np.reshape(r,c),
# np.extract(a2>50,a2), np.split(array, indices or sections, axis = 0,1), np.where(condition, valueiftrue, valueiffalse)
# arr.flatten(), np.sort(arr)[::-1] - desc order // arr[::-1].sort(), np.concatenate((arr1, arr2), axis=01, out=none)),
# np.vstack() , np.hstack(tuple, list, or array), np.argmin(arr) returns min ka index, np.argmax(), np.argsort()[::-1]



# 2d array to 1d array
import numpy as np
#
# arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#
# print("a1 : ", arr_2d)
# # print("length:", len(arr_2d))     // this will show only number of colums 3
# print("length of 2d array: ", np.size(arr_2d))        # total elements in array
# arr_1d = np.empty(np.size(arr_2d), dtype=np.int32)
# print("length of 1d array: ", np.size(arr_1d))
#
# i = 0
# for r in arr_2d:
#     for c in r:
#         arr_1d[i]=c
#         i += 1
# print(arr_1d)

import numpy as np
# arr = np.array([3, 1, 2, 4, 5])
# sorted_arr = np.sort(arr)
# print("Sorted array (ascending):", sorted_arr)
# sorted_arr_desc = np.sort(arr)[::-1]
# print("Sorted array (descending):", sorted_arr_desc)

arr = np.array([3, 1, 2, 4, 5])
arr.sort()
# print("Sorted array (ascending):", arr)
arr[::-1].sort()
# print("Sorted array (descending):", arr)
# print(arr)

mtx = np.array([[3, 1, 2],[6, 5, 4]])
sorted_mtx = np.sort(mtx, axis=1)
# print("Sorted matrix (ascending along rows):")
# print(sorted_mtx)


data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
train_data, test_data = np.split(data, [int(0.9 * len(data))])
# print("Training Data:")
# print(train_data)
# print("\nTesting Data:")
# print(test_data)

sales_data = np.array([[101, 500], [102, 750], [103, 350], [104, 900], [105, 600]])
sorted_sales_data = sales_data[sales_data[:, 1].argsort()[::-1]]
print("Top-selling products:")
print(sorted_sales_data)