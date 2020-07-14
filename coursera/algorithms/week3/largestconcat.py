from itertools import permutations 
def largest(l): 
    lst = [] 
    for i in permutations(l, len(l)): 
        # provides all permutations of the list values, 
        # store them in list to find max 
        lst.append("".join(map(str,i)))  
    return max(lst) 
  
print(largest([5,52,57,517,532,569,581]))