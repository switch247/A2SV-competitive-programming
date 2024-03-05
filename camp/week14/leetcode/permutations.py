class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        def backtracking(subset,nums):
            if len(subset) == len(nums):
                res.append(subset)
            for i in range(len(nums)):
                # print(visited, subset)
                if i not in visited:
                    visited.add(i)
                    new = subset[:]
                    new.append(nums[i])
                    
                    backtracking( new , nums)
                    visited.remove(i)

                
        backtracking( [] , nums )
        return res
        