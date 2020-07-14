for _ in range(int(input())):
    n,alp=input().split()
    n=int(n)
    p=alp
    for i in range(1,n+1):
        
            
        for j in range(n):
            if p=='W':
                print(p,end="")
                p='B'
            else:
                print(p,end="")
                p='W'
        if n%2==0 :
            if(p=='W'):
                p='B'
            else:
                p='W'

        print()