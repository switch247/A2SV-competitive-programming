class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)<=4:
            return 0
        # we can turn 3 of the large once to the same number
        l,r = 0 , len(nums)-4
        ans = nums[r] - nums[l]
        while r < len(nums):
            ans  = min(ans, nums[r] - nums[l])
            r+=1
            l+=1

        return ans
