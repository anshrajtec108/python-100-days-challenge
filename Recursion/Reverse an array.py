def Reverse_an_array(arr,left, right):
    if left>= right:
        return arr
    temp=arr[left]
    arr[left]=arr[right]
    arr[right]=temp
    return Reverse_an_array(arr,left+1,right-1)

arr=[1,2,3]
print(Reverse_an_array(arr,0,(len(arr)-1)))