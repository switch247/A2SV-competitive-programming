class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #decrease capacity when you pick someone up
        #increase when dropping off
        #if you go over capacity limit False 
        # 1 <= trips.length <= 1000
        pick_and_drop_time = [0] * 1003
        for n, start, end in trips:
            pick_and_drop_time[start] += n
            pick_and_drop_time[end] -= n
        # print(pick_and_drop_time)
        tot_passengers = 0
        for passenger in pick_and_drop_time:
            tot_passengers += passenger
            if tot_passengers > capacity:
                return False
        return True