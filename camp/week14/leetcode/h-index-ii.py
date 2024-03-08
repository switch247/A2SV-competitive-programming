class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        def pos(x):
            z = bisect_left(citations,x)
            return len(citations) - z >= x
        l, r = 0 , citations[-1]
        ans = 0
        while l <= r:
            mid = (l+r)//2
            if pos(mid):
                ans = mid
                l = mid +1
            else:
                r = mid -1
        return ans
            