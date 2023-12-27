class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0]*3
        # only 3 colors 0 1 2 
        for i in nums: bucket[i]+=1
        left = 0
        for color in range(3):
            while bucket[color] > 0:
                nums[left] = color
                bucket[color]-= 1
                left+=1
        