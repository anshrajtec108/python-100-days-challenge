import numpy as np

arr = np.array([10, 20, 30, 40])
print(arr)

print(arr[0])   # first element
print(arr[2])   # third element
print(arr[-1])   # last element

#SLICING (Access Multiple Elements)
print(arr[1:3])
'''👉 Rule:
start = included ✅
end = excluded ❌'''

print(arr[:3])   # from start
print(arr[2:])   # till end

#3. STEP SLICING
print(arr[::2])

#2D ARRAY INDEXING
print("2D ARRAY INDEXING")

arr2 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(arr2[1,1])
#🔹 Access row
print(arr2[0])
#🔹 Access column
print(arr2[:,1])    

#2D SLICING
print("2D SLICING")
print(arr2[0:2, 1:3])