class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        for num in arr:
            val = 1
            previous_num = num - difference
            if  previous_num in dp:
                val += dp[previous_num]
            dp[num] = val
        
        return max(dp.values())

