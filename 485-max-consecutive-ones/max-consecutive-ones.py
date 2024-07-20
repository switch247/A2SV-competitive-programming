class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = float('-inf')
        one =  0
        for i in nums:
            if i == 1:
                one+=1
            else:
                ans = max(one, ans)
                one = 0

        return max(one, ans)
            
        