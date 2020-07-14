# finding the minimum number of platforms in the railway station.
# time complexity is O(n+nlogn) if it is not in sorted order.

def minPlt(arrival,departure):
    arrival.sort()
    departure.sort()
    print(arrival)
    print(departure)
    maxPltforms=1
    needPltforms=1
    i=1
    j=0
    while i!=len(arrival) and j!=len(departure):
        
        if departure[j]<arrival[i]:
            maxPltforms-=1
            j+=1
        if arrival[i]<departure[j]:
            i+=1
            maxPltforms+=1
        if maxPltforms>needPltforms:
            needPltforms+=1
    print(needPltforms)

minPlt([900,940,950,1100,1500,1800],[910,1200,1120,1130,1900,2000])


