class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if days == 1:
            return sum(weights)
        l = max(weights)
        r = sum(weights)
        self.ans = r
        def check(n):
            # print(n)
            c = 1
            s = 0
            for w in weights:
                if s+w > n:
                    s = 0
                    c+=1
                s +=w
                if c > days:
                    break
            return c <= days
        
        while l <= r:
            mid = (l+r)//2
            # print(l,mid,r)
            if check(mid):
                r = mid - 1
            else:
                l = mid+1
            
        return l
        