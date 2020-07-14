def countDer(n): 
    der = [0 for i in range(n + 1)] 
      
    # Base cases 
    der[0] = 1
    der[1] = 0
    der[2] = 1
      
    # Fill der[0..n] in bottom up manner  
    # using above recursive formula 
    for i in range(3, n + 1): 
        der[i] = (i - 1) * (der[i - 1] + 
                            der[i - 2]) 
          
    # Return result for n 
    return der[n]  
n=int(input())
try:
    
    if n>=1 and n<=1000000:   
        k=countDer(n)%1000000007
        print(k)
    
    
except:
    exit()
    

    





