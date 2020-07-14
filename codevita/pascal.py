from itertools import permutations
def pascal(l):
  k=5
  for x in range(0,4):
    for y in range(k):
      l[y]=l[y]+l[y+1]
    del l[k]
    k=k-1
    
  return(l[1]*l[0])

n=int(input())
a=list(map(int,input().strip().split()))
a.sort(reverse=True)
a=a[:6]
max1,value=0,0
for i in permutations(a,6):
  value=pascal(list(i))
  if value>max1:
    max1=value
print(max1)
