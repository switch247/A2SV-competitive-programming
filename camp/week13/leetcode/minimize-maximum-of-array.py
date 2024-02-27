class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        s = 0
        ans = 0
        for i in range(len(nums)):
            s = s+nums[i]
            avgsum = s/(i+1)
            # print(avgsum)
            if avgsum > ans:
                ans = avgsum
        return ceil(ans)