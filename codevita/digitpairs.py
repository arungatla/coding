def largest(num):
    num=str(num)
    n=9
    while n>=0:
        for i in num:
            if n==int(i):
                return int(i)
        n-=1
def smallest(num):
    num=str(num)
    n=0
    while n<=9:
        for i in num:
            if n==int(i):
                return int(i)
        n+=1

def pair_from(num):
    if num>2:
        return 2
    if num==2:
        return 1
    return 0
# def significant(num):


for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().strip().split()))
    assert(len(a)==n)
    bits=[""]*n
    for i in range(len(bits)):
        
        bit=str((largest(a[i])*11)+(smallest(a[i])*7))
        if len(bit)>2:
            
            bit=bit[-2:]
            
        bits[i]=bit
    even=[0]*10
    odd=[0]*10
    for i in range(len(bits)):
        index=int(str(bits[i])[0])
        if (i+1)%2==0:
            even[index]+=1
        else:
            odd[index]+=1
    count=[0]*10
    for i in range(10):
        if even[i]<=1 and odd[i]<=1:
            continue
        count[i]+=pair_from(even[i])+pair_from(odd[i])
        count[i]=min(2,count[i])

    print(sum(count))
        
        
        
        

        