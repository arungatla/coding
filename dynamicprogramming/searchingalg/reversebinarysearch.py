def binarySearch(arr,key):
    low=0
    size=len(arr)
    high=size-1
    while low<=high:
        mid=low+(high-low)//2
        if arr[mid]==key:
            return mid
        elif key<arr[mid]:
            low=mid+1
            
        else:
            high=mid-1
            
    return -1

arr=list(map(int,input().strip().split()))
key=int(input())
arr.sort(reverse=True)
print(arr)

k=binarySearch(arr,key)
if k>-1:
    print(k)
else:
    print("No key in the array")
        
