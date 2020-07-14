def solve(B,N,Z):
    Z=sorted(Z,reverse=True)
    for zombie in Z:
        if B<zombie:
            print("NO")
            return False
        B=B-((zombie//2)+(zombie%2))
    print("YES")
    return True

try:
    B,N=input().split()
    B,N=int(B),int(N)
    assert 1<=B<=1000000000
    assert 1<=N<=10000
    Z=input().strip().split()
    print(Z)
    assert len(Z)==N
    for zi in Z:
        assert zi.isdigit()
        
        assert 1<=int(zi)<=100000
    Z=[int(zi) for zi in Z]
    
except:
    print("Invalid Input")
    exit(0)

solve(B,N,Z)




