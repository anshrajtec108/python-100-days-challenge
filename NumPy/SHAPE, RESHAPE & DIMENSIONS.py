'''1. SHAPE (Structure of Array)
👉 Shape = rows × columns'''

import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6]
])

print("shape",arr.shape)

'''DIMENSIONS (ndim)
👉 How many axes (levels) your data has'''

print("DIMENSIONS",arr.ndim)


'''3. RESHAPE (VERY IMPORTANT)
👉 Change structure of data without changing values'''

arr1 = np.array([1,2,3,4,5,6])

new_arr = arr1.reshape(2,3)
print(arr1.reshape(6))

print("1D - 2D",new_arr)

arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr2.reshape(2, 3, 2)
print("1D - 3D",newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)
