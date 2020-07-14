from itertools import combinations

n=int(input())
boxes=int(input())

binb=list(combinations(n,boxes))
print(binb)