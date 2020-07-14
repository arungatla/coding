# R round tables
# N attendees

# N is a exact multiple of R (N//R)
from itertools import combinations
for _ in range(int(input())):
    R,N=map(int,input().strip().split())
    attendees=[i for i in range(1,N+1)]
    combi1=list(combinations(attendees,N-(N//R)))
    combi2=list(combinations(attendees,(N//R)))
    print(combi1)
    
        
    
