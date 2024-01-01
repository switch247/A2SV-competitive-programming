class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans = last = 0
        # last = position of the last 1 of the consecutive 1s on the left
        for i, f in enumerate(flips):
            last = max(last, f)
            if i+1 ==last:
                ans+=1
        return ans
        