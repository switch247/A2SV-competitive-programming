class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left =0
        presum=0
        flag = False
        ans = len(nums)
        for right in range(len(nums)):
            presum += nums[right]
            while presum>=target:
                flag = True
                presum -= nums[left]
                ans=min(ans,right-left +1)
                left+=1        
        return ans if flag else 0 
