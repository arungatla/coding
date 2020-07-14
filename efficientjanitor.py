def effjan(arr):
    arr.sort()
    left=0
    trips=0
    for i in range(len(arr)-1,-1,-1):
        if arr[i]>1.99:
            trips+=1
        elif arr[i]<=1.99:
            if arr[i]+arr[left]<=3.0:
                left+=1
            trips+=1
        if left>=i:
            break
    return trips

n=int(input())


a=list(map(float,input().split()))

print(effjan(a))

