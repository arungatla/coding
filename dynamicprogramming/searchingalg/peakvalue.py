def peakvalue(arr):
    low=0
    size=len(arr)
    high=len(arr)-1
    while low<=high:
        mid=(low+(high-low)//2) #integer overflow
        if mid>0 and mid<size-1:
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid]<arr[mid-1]:
                high=mid-1
            else:
                low=mid+1
        elif mid==0:
            if arr[0]>arr[1]:
                return 0
            else:
                return 1
        elif mid==size-1:
            if arr[size-1]>arr[size-2]:
                return size-1
            else:
                return size-2
A=list(map(int,input().strip().split()))
print(A[peakvalue(A)])

