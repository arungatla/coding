from itertools import permutations
a,b=map(int,input().strip().split())

if 1<=a<=10000000 and 1<=b<=10000000:

    a=list(str(a))
    strb=list(str(b))
    blen=len(strb)
    a=list(map(int,a))
    combi1=list(permutations(a,blen))
    combi2=[]
    ind=0
    for num in combi1:
        num=list(map(str,num))
        num="".join(num)
        num=int(num)
        combi2.append(num)
    combi2.sort()
    for num in combi2:
        if num>b:

            print(num)
            break
    else:
        print(-1)
else:
    print(-1)
    
       