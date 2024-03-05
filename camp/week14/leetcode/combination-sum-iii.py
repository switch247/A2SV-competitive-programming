class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def backtrack (i, path, ss):
            # print(path)
            if ss == n and len(path)==k:
                if path not in ans:
                    ans.append(path[:])
                return 
            if len(path) >= k or ss > n:
                return
            for j in range(i, 10 ):
                path.append( j )
                sum = ss+ j
                backtrack(j+1, path, sum )
                path.pop()
        backtrack (1, [], 0)
        return ans
 