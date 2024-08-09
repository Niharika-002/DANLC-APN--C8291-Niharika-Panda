# Convert the below list into a numpy array then display the array then
# display the first and last index and then multiply each element by 2 and
# display the result.
# Input: my_list = [1, 2, 3, 4, 5]

import numpy as np

my_list = [1, 2, 3, 4, 5]

my_array = np.array([my_list])

first_element = my_array[0][0]
second_ele = my_array[0][-1]
print("First element : ", first_element)
print("second element : ", second_ele)


def multiply_arr():
    modified_arr = my_array * 2
    print(modified_arr)

multiply_arr()