# NumPy Array Indexing
# Access Array Elements
# Array indexing is the same as accessing an array element.
# You can access an array element by referring to its index number.
# The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.

import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr[0])  # first element
print(arr[1])  # second element
print(arr[2] + arr[3])  # adding third and furth element


# To access elements from 2-D arrays we can use comma separated integers representing the dimension
# and the index of the element.
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('2nd element on 1st row: ', arr[0, 1])
print('3rd element on 2st row: ', arr[1, 2])


# To access elements from 3-D arrays we can use comma separated integers representing the dimensions
# and the index of the element.
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])  # the third element of the second array of the first array


# Negative Indexing
print(arr[1, -1, -1])  # last element of second arrary of second array
