for _ in range(int(input())):
    n=int(input())
    if n<=1:
        print('You cannot generate christmas tree')
    elif n>20:
        print('Tree is no more')
    else:
        N=n+1
        F=1
        space=0
        def chrismas(F,N):
            global space
            
            for row in range(F,N+1):
                print(" "*(N+1+space-row),end="")
                print("*"*(2*row-1))
            space+=1


        chrismas(F,N)
        # print(F,N)
        F+=1

        N=n
        l=0
        for i in range(2,N):
            
            # print(F,N-l)
            chrismas(F,N-l)
            l+=1

        space+=1
        g=space
        for i in range(g+1):
            print(" ",end="")
        print("*")
        for i in range(g+1):
            print(" ",end="")
        print("*")

