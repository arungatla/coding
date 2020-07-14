# =====================Merge Sort=======================

def MergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2

        l=arr[:mid]
        r=arr[mid:]


        MergeSort(l)
        MergeSort(r)

        i=j=k=0


        #copy the data to temp arrays l[] and r[]
        while i<len(l) and j<len(r):
            if l[i]<r[j]:
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1
        #checking if any element was left
        while i<len(l):
            arr[k]=l[i]
            i+=1
            k+=1
        while j<len(r):
            arr[k]=r[j]
            j+=1
            k+=1
        
arr=list(map(int,input().strip().split()))

MergeSort(arr)

print(*arr)




