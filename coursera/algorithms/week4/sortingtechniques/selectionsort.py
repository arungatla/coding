#==========================Selection Sort=====================================
# the time complexity of the selection sort id O(n^2)

#Arithmetic series 1+2+3.....=n(n+1)/2
#     1,2,3,4..........n
#     n,n-1,n-1........1
#     n+1,n+1,.........n+1=n(n+1)


A=list(map(int,input().strip().split()))


for i in range(len(A)):
    min_idx=i
    for j in range(i+1,len(A)):
        if A[min_idx]>A[j]:
            min_idx=j

    A[i],A[min_idx]=A[min_idx],A[i]

print(*A)


