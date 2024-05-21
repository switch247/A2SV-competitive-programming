class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n,m = len(triangle), len(triangle[0])
        # def inbound(i,j): return 0<=i<n and 0<=j<m
        @cache
        def dp (i,j):
            if i==n-1:
                return triangle[i][j]
            # d | dr (l |L)
            return min(dp(i+1,j),  dp(i+1,j+1) ) + triangle[i][j]
        return dp(0,0)