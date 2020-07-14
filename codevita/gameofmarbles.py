from math import gcd
def lcm(nums):
    a=nums[0]
    b=nums[1]
    curr_lcm=(a*b)//(gcd(a,b))
    for num in range(2,len(nums)):
        curr_lcm=(curr_lcm*num)//(gcd(curr_lcm,num))
    return curr_lcm

N=int(input())
N=N//2
point_dict={"Darrell":0,"Sally":0}
try:
    for case in range(N):
        questain_input=input()
        questain_input=questain_input.split()
        questainer=questain_input[0]
        nums_str=questain_input[1]
        nums=list(map(int,nums_str.split(',')))
        
        assert 2<=len(nums)<=7
        for num in nums:
            assert 1<=num<=100
        

        answer_input=input().split()
        answerer=answer_input[1]


        if case==0:
            first=questainer
            second=answerer
        

        correct_answer=lcm(nums)
        print(f"{questainer}'s question is : {nums_str}")
        if answer_input[2]:
            if answer_input[2]!='PASS':
                ans=int(answer_input[2])
                if ans==correct_answer:
                    print("Correct Answer")
                    print(f"{answerer}: 10points")
                    point_dict[answerer]+=10
                else:
                    print("Incorrect Answer")
                    print(f"{answerer}: 0points")
            else:

                print("Question is PASSed")

                print(f"Answer is: {correct_answer}")
                print(f"{answerer}: 0points")
        if case==N-1:
            print("Total Points:")
            print(f'{first}: {point_dict[first]}points')
            print(f"{second}: {point_dict[second]}points")
            if point_dict['Darrell']==point_dict['Sally']:
                print("Game Result: Draw")
            elif point_dict['Darrell']>point_dict['Sally']:
                print("Game Result: Darrell is winner")
            else:
                print("Game Result: Sally is winner")
except:
    print("Invalid Input")







