a,b,m=map(int,input().split())
for n in range(a,b+1):
    if (n*(2*n-1))==0 and (n*(n+1)/2)==0:
        print(n)