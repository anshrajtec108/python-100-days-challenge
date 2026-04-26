import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)

for x in arr:
  for y in x:
    for z in y:
      print(z)

'''Iterating Arrays Using nditer()'''
print("Iterating Arrays Using nditer()")
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)