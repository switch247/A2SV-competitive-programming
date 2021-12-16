"""not very effiecient"""
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        
        nums.sort()
        x = len(nums)


        if x >= 3:
            nums=int(nums[-3])
        else:
            nums= int(nums[-1])
        return nums
   
