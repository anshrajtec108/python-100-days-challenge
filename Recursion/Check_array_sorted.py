def CheckIfArray_sorted(arr, n):
    if (n==0 or n==1):
        return True
    return arr[n-1]>=arr[n-2] and CheckIfArray_sorted(arr,n-1)
    

arr=[1,2,3,4,5,6]
print(CheckIfArray_sorted(arr,6))