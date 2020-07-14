#linear search using recursion
#  recurrsive t(n)=t(n-1)+c and t(0)=c
# 
def linearSearch(A,low,high,key):
    if low==high:
        return "NOT FOUND"
    if A[low]==key:
        return low
    return linearSearch(A,low+1,high,key)

print(linearSearch([1,2,3,4,5,6,7],0,7,9))