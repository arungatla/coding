import sys 
from collections import Counter 
def factorial( n) : 
    res = [None]*500
    res[0] = 1
    res_size = 1
    x = 2
    while x <= n : 
        res_size = multiply(x, res, res_size) 
        x = x + 1
    i = res_size-1
    k=""
    while i >= 0 : 
        k+=(str(res[i])) 
        sys.stdout.flush() 
        i = i - 1
    return k
          
def multiply(x, res,res_size) : 
      
    carry = 0 
    i = 0
    while i < res_size : 
        prod = res[i] *x + carry 
        res[i] = prod % 10;  
        carry = prod//10; 
        i = i + 1
    while (carry) : 
        res[res_size] = carry % 10
        carry = carry // 10
        res_size = res_size + 1
          
    return res_size 

import math 
  

def primeFactors(n): 
    k=[]
    while n % 2 == 0: 
        k.append(2) 
        n = n // 2
    for i in range(3,int(math.sqrt(n))+1,2):  
        while n % i== 0: 
            k.append(i)
            n = n // i  
    if n > 2: 
        k.append(n)
    return k  
  
try:
    n=int(input())
    if n>1:
        factors=factorial(n)
        factors=int(factors)
        prmefacts=primeFactors(factors)
        d=Counter(prmefacts)
        let=list(set(prmefacts))
        let.sort()
        count=[]
        for facts in let:
            count.append(d[facts])
        print(*count)
            
    else:
        print("Invalid Input")
except:
    print("Invalid Input")



    
    
