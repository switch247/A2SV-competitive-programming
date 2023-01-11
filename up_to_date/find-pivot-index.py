class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot =sum(nums)
        
        left=0 
        for i in range(len(nums)):
            right= tot-nums[i]-left
            if left==right:
                return i
            left +=nums[i]
        return -1
"""
#very slow
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for a in range( len(nums) ):
            if sum(nums[:a+1]) == sum(nums[a:]):
                return a
        return -1



"""
        
        
