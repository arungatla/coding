#finding the way that it is possible ti reach all of the gas stations.
# time and space complexity is O(n) and O(1)
def getTour(petrol,distance,n):
    sum=0
    start=0
    diff=0
    for i in range(n):
        sum+=petrol[i]-distance[i]
        if sum<0:
            start=i+1
            diff+=sum
            sum=0
    if sum+diff>0:
        return start
    else:
        return -1

if __name__ == "__main__":
    petrol=[4,6,7,4]
    distance=[6,5,3,5]
    value=getTour(petrol,distance,len(petrol))
    print(value)    