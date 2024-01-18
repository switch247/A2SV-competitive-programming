class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #decrease capacity when you pick someone up
        #increase when dropping off
        #if you go over capacity limit False 
        lst = []
        for [n, start, end] in trips:
            lst.append((start, n))
            lst.append((end, -n))
        lst.sort()
        #print(lst)
        pas = 0
        for loc in lst:
            pas += loc[1]
            #print(pas)
            if pas > capacity:
                return False
        return True