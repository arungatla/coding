# ===================Quick Sort=======================

def partition(l,h,arr):
    i=(l-1)
    
    pivot=arr[h]
    

    for j in range(l,h):
        
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return (i+1)

def quicksort(low,high,arr):
    if low<high:
        pi=partition(low,high,arr)
        quicksort(low,pi-1,arr)
        quicksort(pi+1,high,arr)


arr=list(map(int,input().strip().split()))
n=len(arr)
quicksort(0,n-1,arr)
print(*arr)

