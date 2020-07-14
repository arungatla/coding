# n=int(input())
# rows=n
"""
6,28,66,120,190,276..........
28-6=22
66-28=38(22+16)
120-66=54(38+16).......



"""
# def element(n):
#     k=1
#     series=0
#     for i in range(1,n+1):
#         series=(2*k*(4*k-1))
#         k+=1
#     return series





    # first=6
    # second=22
    # next=0
    # if n==1:
    #     return first
    # if n==2:
    #     return first+second
    # second=first+second
    # for i in range(3,n+1):
    #     next=(second*2)-first+16
    #     first=second
    #     second=next
    # return next


    # first=6
    # second=22
    # next=0
    
        
    # for i in range(3,n+1):
    #     next=(second*2)-first+16
    #     first=second
    #     second=next
    # return next





"""
for i in range(1,n+1):
    print(" "*(n-i)*3,end="")
    for j in range(1,i+1):
        if i>3:
            i+=1
            print(format(element(i),'05'),end=" ")
        else:
            print(format(element(i),'05'),end=" ")
            i+=1
"""


"""
6,28,66,120,190,270
6=2x1x(3=(4-1))
28=2x2x(7=(8-1))

kth series 2*k*(4*k-1)


"""





# code

n=int(input())
k=1
for row in range(1,n+1):
    print("   "*(n-row),end="")
    for col in range(1,row+1):
        series=(2*k*(4*k-1))
        print(format(series,'05'),end=" ")
        k+=1
    print()


