class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def inbound(i,j): return 0<=i<n and 0<=j<m
        cache = {}
        def dp(i,j):
            if not inbound(i,j):
                return 0

            if i == n-1 and j == m-1:
                return 1
            if (i,j) not in cache:
                # down | right
                cache[(i,j )] = dp(i+1,j) + dp(i,j+1)
            
            return  cache[(i,j)] 

        return dp(0,0)