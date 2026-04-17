def BS(arr, targ, st, end):
    if st > end:
     return "Not Found"
    mid=(st + end)//2
    if arr[mid]==targ:
        return mid
    elif arr[mid]< targ:
        return BS(arr, targ, mid+1, end )
    elif  arr[mid]>targ:
        return BS(arr, targ, st, mid-1)


arr=[1,2,3,4,5,67,8,9]
print(BS(arr,1,0,8))