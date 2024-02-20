class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # without greedy
        # target = len(nums)-1
        # for i in range(len(nums)-1,-1,-1):
        #     if i + nums[i]>= target:
        #         target = i
        # return not target
        step = nums[0]
        for i in range( len(nums) ):
            step = max( step, i+nums[i] )
            if i==step: #0 means you can't move on
                if i == len(nums)-1: # if you have reachched the end
                    return True
                return False
        return True
            
        
                