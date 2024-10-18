class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = 0
        for i in range(32,-1,-1):
            mask = 1 << i 
            a = (start & mask) >> i
            b = (goal & mask) >> i
            # a, b = value of the ith bit 0|1
            if (a != b):
                ans+=1

        return ans