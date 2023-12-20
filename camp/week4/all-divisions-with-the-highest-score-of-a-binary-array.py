from collections import defaultdict
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        d = defaultdict( list )
        one = nums.count(1)
        zero = 0
        mx = float('-inf')
        for index in range(len(nums)+1):
            # print(zero, one , index)
            if (one + zero) >= mx:
                mx = (one + zero)
                # mx = max(mx, (one + zero))
                d[ one + zero ].append(index)
            if index < len(nums):
                if nums[index] == 0:
                    zero += 1
                else:
                    one -= 1
            
        return d[mx]
