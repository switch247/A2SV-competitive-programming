class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #decrease capacity when you pick someone up
        #increase when dropping off
        #if you go over capacity limit False 
        lst = []
        for n, start, end in trips:
            lst.append((start, n))
            lst.append((end, -n))
        lst.sort()
        # print(lst)
        tot_passengers = 0
        for loc in lst:
            tot_passengers += loc[1]
            #print(pas)
            if tot_passengers > capacity:
                return False
        return True
