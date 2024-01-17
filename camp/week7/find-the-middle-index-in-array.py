class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftSum = totalSum = 0
        totalSum= sum(nums)
        for i in range (len(nums)):
            leftSum += nums[i]
            if ( leftSum-nums[i] == totalSum - leftSum): return i
        return -1  

       
        
        