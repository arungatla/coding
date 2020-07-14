def fibnum(n):
    f=[0,1]
    for i in range(2,n+1):
        f.append(f[i-1]+f[i-2])
    print(f[n])

n = int(input())

if n<=1:
    print(n)  
    quit()

fibnum(n)