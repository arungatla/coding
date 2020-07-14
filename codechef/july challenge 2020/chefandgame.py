try:
    for _ in range(int(input())):
        numofrounds=int(input())
        rounds=[0,0]
        summ1=0
        summ2=0
        for round in range(numofrounds):
            k=list(map(int,input().strip().split()))
            a=k[0]
            b=k[1]
            if a>9:
                while a!=0:
                    summ1=summ1+(a%10)
                    a=a//10
            else:
                summ1=a
            if b>9:
                while b!=0:
                    summ2=summ2+(b%10)
                    b=b//10
            else:
                summ2=b
            if summ1>summ2:
                rounds[0]+=1
            elif summ2>summ1:
                rounds[1]+=1
            elif summ1==summ2:
                rounds[0]+=1
                rounds[1]+=1
            summ1=summ2=0
        if rounds[0]>rounds[1]:
            print(0,rounds[0])
        elif rounds[1]>rounds[0]:
            print(1,rounds[1])
        elif rounds[0]==rounds[1]:
            print(2,rounds[0])
        
            

            
except:
    pass


        

