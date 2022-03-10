# Iterating means going through elements one by one.

import numpy as np

# Iterating 1-D Arrays
arr = np.array([1, 2, 3])
for x in arr:
    print(x)

# Iterating 2-D Arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    for y in x:
        print(y)

# Iterating 3-D Arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)


# Iterating Arrays Using nditer()
# The function nditer() is a helping function that can be used from very basic to very advanced iterations.
# In basic for loops, iterating through each scalar of an array we need to use n for loops which
# can be difficult to write for arrays with very high dimensionality.
for x in np.nditer(arr):
    print(x)

# Iterating Array With Different Data Types
# We can use op_dtypes argument and pass it the expected datatype to change the datatype of elements while iterating.
# NumPy does not change the data type of the element in-place (where the element is in array)
# so it needs some other space to perform this action, that extra space is called buffer,
# and in order to enable it in nditer() we pass flags=['buffered'].


arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)


# terating With Different Step Size

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
    print(x)


# Enumerated Iteration Using ndenumerate()
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
    print(idx, x)
