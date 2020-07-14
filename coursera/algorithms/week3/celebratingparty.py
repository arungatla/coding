# sorting the children c

children=list(map(float,input().strip().split()))
children.sort()
n=len(children)
R=[]
i=0
count=0

while i<=n:
    l,r=children[i],children[i]+1
    print(l,r)
    R.append([l,r])
    count+=1
    i+=1

    while i<=n and children[i]<=r:
        i+=1
# print(len(R))
print(count)