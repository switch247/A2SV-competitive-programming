class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # -2,1,2,-2,1,2
        # -2 2 1   

        n =  len(nums)
        stack = []
        # strictly increasing monotonic stack
        # i < j < k and nums[i] < nums[k] < nums[j].
        # 1 3 2
        k = float('-inf')
        for i in range(n-1,-1,-1):
            if nums[i] < k:
                return True
            while stack and stack[-1] < nums[i]:
                k = stack.pop()
            stack.append( nums[i] )
        return False
