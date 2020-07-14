try:
    for _ in range(int(input())):
        N=int(input())
        A=list(map(int,input().strip().split()))
        B=list(map(int,input().strip().split()))
        count=0
        c1=0
        c2=0
        for i in range(N):
            c1+=A[i]
            c2+=B[i]
            if A[i]==B[i] and c1==c2:
                count+=A[i]
        print(count)
except:
    pass