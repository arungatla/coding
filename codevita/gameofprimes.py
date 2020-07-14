def ishappy(num):
    summ=0
    while num>0:
        summ+=(num%10)*(num%10)
        num//=10
    if summ==1:
        return True
    if summ==4:
        return False
    
    return ishappy(summ)

def isprime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    else:
        return True
    
    
count=0
try:
    start=int(input())
    assert start>0
    end=int(input())
    assert start<=end
    N=int(input())
    assert N>0
    
    
    
except:
    print("Invalid Input")
    exit(0)

for i in range(start+1,end):
    
    
    if isprime(i) and ishappy(i):
        
        count+=1
    if count==N:
        print(i)
        break
    
else:
    print("No number is present at this index")
    
    





