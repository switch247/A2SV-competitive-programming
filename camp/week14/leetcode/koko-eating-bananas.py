class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(k):
            hours = 0
            for pile in piles:
                hours += ceil(pile/k)
                if hours> h:
                    break
            return hours<= h

        l = 1
        r =  max(piles)
        
        while l<=r:
            mid = (l+r)//2
            # print(l,mid, r)
            if possible(mid):
                r = mid -1
            else:
                l = mid +1
        return l
