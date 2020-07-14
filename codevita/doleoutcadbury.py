def noofsquares(row,col):
    count=0
    total=row*col
    while(row and col):
        count+=1
        if row>col:
            row-=col
        else:
            col-=row
    return count

for _ in range(int(input())):
    p,q,r,s=map(int,input().strip().split())
    out=0
    if(0<p<1501 and 0<q<1501 and 0<r<1501 and 0<s<1501):
        for i in range(p,q+1):
            for j in range(r,s+1):
                out+=noofsquares(i,j)
    print(out)
