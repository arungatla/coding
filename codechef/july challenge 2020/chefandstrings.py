try:
    for _ in range(int(input())):
        timespluck=int(input())
        plucks=list(map(int,input().strip().split()))
        diff=[]
        for i in range(1,timespluck):
            diff.append(abs(plucks[i]-plucks[i-1])-1)
        print(sum(diff))
except:
    pass
