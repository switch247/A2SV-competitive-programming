class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] <  nums[i-1]:
                count+= 1
                if count > 1:return False
                if i>=2 and nums[i-2] > nums[i]:
                    nums[i] = nums[i-1]
                    # fix it one time 
        # if the first or  element is the one causing problems it can be fixed
        return True    