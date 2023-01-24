class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        nums.insert(0,0)
        print(nums)
        for i in range(1,len(nums)):
            if nums[i] == nums[len(nums)-1 ] - nums[i-1]:
                return i-1
        return -1
      
      
 """
 ##faster
 class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot =sum(nums)
        
        left=0 
        for i in range(len(nums)):
            righ= tot-nums[i]-left
            if left==righ:
                return i
            left +=nums[i]
        return -1
 """
