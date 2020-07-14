
# time complexity is O(n) for while loop
def minrefills(x,n,l):
    numofrefills=0
    currentrefill=0
    while currentrefill<=n:
        lastrefill=currentrefill
        while currentrefill<=n and x[currentrefill+1]-x[lastrefill]<=l:
            currentrefill=currentrefill+1

        if currentrefill==lastrefill:
            return -1
        if currentrefill<=n:
            numofrefills+=1
    return numofrefills




