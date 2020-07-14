for _ in range(int(input())):
    n = int(input())
    a = list(input())
    b = list(input())
    ase = set(a)
    bse = set(b)
    if a==b:
        print(0)
    
    elif bse.issubset(ase):
        d={}
        wr = {}
        f=0
        for i in range(n):
            if a[i]!=b[i]:
                if b[i] in d:
                    d[b[i]].append(i)
                    wr[b[i]].append(a[i])
                else:
                    d[b[i]]=[]
                    wr[b[i]]=[]
                    d[b[i]].append(i)
                    wr[b[i]].append(a[i])

        print(wr,d)
        for k,v in sorted(wr.items(),reverse=True):
            print(k,v)
            for i in v:
                print(k,i)
                if ord(k)>ord(i):
                    f=1
                    break
            if f==1:
                break
        print(f)
        if f==1:
            print(-1)
        else:
            print(len(d))
            for k,v in sorted(d.items(),reverse=True):
                print(len(d[k])+1,end=" ")
                print(*d[k],a.index(k))
        
        
    else:
        print(-1)