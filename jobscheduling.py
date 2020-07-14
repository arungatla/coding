n=int(input())

jobs=[]
for _ in range(n):
    job=list(map(int,input().split()))
    jobs.append(job)
first=0
last=max()
for job in jobs:
    
    first=job[0]
    last=job[1]
    profit=job[2]
    