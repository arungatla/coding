def SieveOfEratosthenes(n):  
    a=[]
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True):
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    for p in range(2, n+1): 
        if prime[p]: 
            a.append(p)
    return a
            
for _ in range(int(input())):
    n=int(input())
    if n==0 or n<=1:
        print("0")
    else:
        a=SieveOfEratosthenes(n)
        k=-1
        summ=0
        for num in a:
            summ+=num
            if summ in a:
                k+=1
        print(k)



        

    



    