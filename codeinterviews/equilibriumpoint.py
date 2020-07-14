# the element in right and left side of an array so that they are equal
# 
# time complexity is O(n)+O(n)=O(2n)==O(n) and space complexity is O(n), 

def equiLib(elements):
    if len(elements)==1:
        return 1
    elif len(elements)==2 or len(elements)==0:
        return -1
    else:
        lsa=[]
        summ=0
        for i in range(len(elements)):
            summ+=elements[i]
            lsa.append(summ)
        for i in range(1,len(elements)-1):
            if lsa[i]-elements[i] == sum(elements)-lsa[i]:
                print(i)
            


equiLib([1,2,6,4,0,-1])
