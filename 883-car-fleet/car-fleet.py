class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #time ==(target-position)/speed
        #put each car into a stalk sort by position the rest are limited by the speed of the final car
        #if the cars time is => time for the last merge the two cars
        # if a car arives at time less than the top cars speed add 1 more fleet
        cars=[]
        for i in range(len(position)):
            cars.append((position[i],speed[i]))
        cars.sort(reverse= True)
        
        #time= ((target-cars[0][0])/cars[0][-1])
        cartime=[]
        for i in range(len(cars)):
            cartime.append(((target-cars[i][0])/cars[i][-1]))
                
        stalk=[]
        for i in cartime:
            if not stalk:
                stalk.append(i)
            elif i > stalk[-1]:
                stalk.append(i)
        return len(stalk)
                