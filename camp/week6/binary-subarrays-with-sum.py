class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = {0: 1}
        ans = 0
        zero = s = 0
        for num in nums:
            s += num
            if (s - goal) in d:
                ans += d[s - goal] 
            # if num==0: zero +=1
            d[s ] = d.get(s, 0) + 1 
        return ans