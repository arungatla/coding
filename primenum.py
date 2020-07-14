def print_factors(x):
    l=[]
   for i in range(1, x + 1):
       if x % i == 0 and i*i != x:
           l.append(i)

           
           