class Itemvalue:
    def __init__(self,weight,value,index):
        self.weight=weight
        self.value=value
        self.index=index
        self.cost=value//weight
    def __lt__(self, other): 
        return self.cost < other.cost
    
class FractionalKnapsack:
    @staticmethod
    def getMaxValue(weight,value,capacity):
        letval=[]
        for i in range(len(weight)):
            letval.append(Itemvalue(weight[i],value[i],i))
        letval.sort(reverse=True)

        


        totalValue=0
        for values in letval:
            currentWeight=values.weight
            currentValue=values.value
            if capacity-currentWeight>=0:
                capacity-=currentWeight
                totalValue+=currentValue
            else:
                fraction=capacity/currentWeight
                totalValue+=currentValue*fraction
                capacity=int(capacity-(currentWeight*fraction))
                break
        return totalValue

if __name__=="__main__":
    weight=[10, 40, 20, 30]
    value=[60, 40, 100, 120]
    capacity=50
    maxValue=FractionalKnapsack.getMaxValue(weight,value,capacity)
    print(maxValue)




