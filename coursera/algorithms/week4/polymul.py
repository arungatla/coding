# polynomials multiplication 
# time complexity is O(n2)
n=2
A=[3,2]
B=[4,5]

product=[0]*(2n-1)

for i in range(n-1):
    for j in range(n-1):
        product[i+j]+=A[i]*B[j]
print(product)


#for time complexity less using divide and conqurer


def mulpoly(A,B,n,a1,b1):
    R=[0]*(2*n-1)
    if n==1:
        R[0]=A[a1]*B[b1]
        return R
    R[-2]=mulpoly(A,B,n//2,a1,b1)


