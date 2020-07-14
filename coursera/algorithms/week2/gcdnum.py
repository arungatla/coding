#one type
def euclid_gcd(a,b):
    if b==0:
        return a
    return euclid_gcd(b,a%b)
#another type 
def gcdnum1(a,b):
    if a==0:
        return b
    return gcdnum1(b%a,a)
a, b = [int(i) for i in input().split()]

if a>b:
    print(euclid_gcd(a, b))
else:
    print(euclid_gcd(b, a))