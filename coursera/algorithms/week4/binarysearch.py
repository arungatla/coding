# t(n)=t(n/2)+c and base case= t(0)=c
# log base 2 (n+1) time complexity is log2(n+1)+c

# def binarySearch(A,low,high,key):
#     if high<low:
#         return low-1
#     mid=(low+((high-low)//2))
#     if A[mid]==key:
#         return mid+1
#     elif A[mid]>key:
#         return binarySearch(A,low,mid-1,key)
#     else:
#         return binarySearch(A,mid+1,high,key)
#     return "IMPOSSIBLE"

    
    
    

A=[1,2,3,4,5,6,7]
low=0
high=6
key=70
# print(binarySearch(A,low,high,key))
# iterative version

while low<=high:
    mid=(low+((high-low)//2))
    if A[mid]==key:
        print(mid+1)
        break
    elif A[mid]>key:
        high=mid-1
    elif A[mid]<key:
        low=mid+1
    
