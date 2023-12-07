class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        # water at position -1 before the array not at the end
        cap = capacity
        answer = 0
        n = len(plants)
        for index, value in enumerate(plants):
            if cap  >= value:
                answer+=1
                cap -= value
            else:
                answer +=  1 + index + (index)
                cap = capacity - value 
            
            # print( "to water = ",( 1+ index ) ,"to refill = ",  index)
        return answer


        