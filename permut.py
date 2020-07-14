from itertools import permutations
str="ABC"
per=permutations(str)
l=[]
for item in per:
    k=""
    for i in item:
        k+=i
    l.append(k)
l=sorted(l)
print(l)
    
