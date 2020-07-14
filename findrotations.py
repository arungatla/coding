def findrotations(str):
    tmp="CDAAB"
    print(tmp)
    n=len(str)
    print(n)
    for i in range(1,n+1):
        substring=tmp[i:i+n]
        print(substring)

        if(str == substring):
            
            return i
    return n


str="AABCD"
print(findrotations(str))
