try:
    print("hello")
    for _ in range(int(input())):
        print("entered")
        A=list(map(int,input().strip().split()))
        P=A[-1]
        A=A[:-1]
        A=A*P
        tothrweek=24*5
        if sum(A)>tothrweek:
            print("Yes")
        else:
            print("No")
except:
    pass