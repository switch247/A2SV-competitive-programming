from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums = [str(i) for i in nums]
        
        # bubble
        # for i in range( len(nums) ):
        #     for j in range( len(nums) - 1 -i ):
        #         if nums[j] + nums[j+1] < nums[j+1] + nums[j]:
        #             nums[j] , nums[j+1] = nums[j+1], nums[j]

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            elif n1 < n2:
                return 1
            else:
                return 0
        nums = sorted(nums, key=cmp_to_key(compare))

        return str(int(''.join(nums)))
        