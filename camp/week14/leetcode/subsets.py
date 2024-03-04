class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sub = []
        def backtrack(i):
            if i>=len(nums):
                ans.append(sub[:])
                return
            
            # choose
            sub.append(nums[i])
            backtrack(i+1)
            # don't choose
            sub.pop()
            backtrack(i+1)
            return 
        backtrack(0)
        return ans