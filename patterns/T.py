for row in range(7):
    for col in range(7):
        if col==3 or (row==0 and col!=3):
            print("*",end="")
        else:
            print(end=" ")
    print()