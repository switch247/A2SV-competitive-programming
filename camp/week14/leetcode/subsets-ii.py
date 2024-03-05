class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        found = set()
        sub = []
        def backtrack(i):
            if i == len(nums):
                s = ''.join( list(map(str, sorted(sub))))
                if s not in found :
                    ans.append(sub[:])
                    found.add( s )
            
            if i < len(nums):
                sub.append(nums[i])
                backtrack( i + 1 )

                sub.pop()
                backtrack( i + 1 )
            
        backtrack(0)
        # print(found)
        return ans


# [[4,4,4,1,4],[4,4,4,1],[4,4,4,4],
# [4,4,4],[4,4,1,4],[4,4,1],[4,4],
# [4,1,4],[4,1],[4],[1,4],[1],[]]