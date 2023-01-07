class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats=0
        # print(people)
        i=0
        j = len(people)-1
        while(i<j):
            if(  (people[i] +  people[j]) > limit ):
                j-=1
                boats+=1
            else:
                i+=1
                j-=1
                boats+=1
        if (i==j):
            return boats+1
        else:
            return boats
