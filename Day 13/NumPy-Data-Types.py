# Data Types in NumPy
# NumPy has some extra data types, and refer to data types with one character, like i for integers,
# u for unsigned integers etc.
# i - integer, b - boolean, u - unsigned integer, f - float, c - complex float, m - timedelta, M - datetime
# O - object, S - string, U - unicode string, V - fixed chunk of memory for other type ( void )


# Checking the Data Type of an Array
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr.dtype)

# Creating Arrays With a Defined Data Type
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)


# Create an array with data type 4 bytes integer:
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)


# Converting Data Type on Existing Arrays
# The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.
# The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)
