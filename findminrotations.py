# def minRot(arr):
#     if not arr: return -1
#     n = len(arr[0])
#     cnt = {(arr[0][i:] + arr[0][:i]) : i for i in range(n)}
#     print(cnt)
#     for s in arr[1:]:
#         if len(s) != n: return -1
#         for i in range(n):
#             cur = s[i:] + s[:i]
            
#             if cur not in cnt: return -1
#             cnt[cur] += i
#     return cnt[min(cnt, key = lambda x: cnt[x])]



def minrot(arr):
    if not arr: return -1 
    n = len(arr[0])
    minarr=arr[0]
    arr=arr[1:]
    cnt=0
    for s in arr:
        if len(s) != n: return -1
        if s==minarr:cnt+=0
        else:
            for i in range(1,len(s)+1):
                temp=s[i:]+s[:i]
                if temp==minarr:
                    
                    cnt+=i
                    break
    return cnt


n=int(input())
arr=[]
for i in range(n):
    k=input()
    arr.append(k)
print(minrot(arr))