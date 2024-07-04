# array v/s list
# array are more faster than list
# so we will use numpy array to implement this

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr)
print(arr[0])
print(arr[1:5])
print(type(arr))
print(arr.dtype)       # checking data types of element s of array

newarr = arr.astype('f')
print(newarr)
print(newarr.dtype)

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

print(arr.shape)        # returns a tuple of (rows, column)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.concatenate((arr1, arr2))
print(arr3)