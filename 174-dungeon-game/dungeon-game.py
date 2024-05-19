class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n,m = len(dungeon), len(dungeon[0])
        def inbound(i,j):return 0<=i<n and 0<=j<m
        cache = {}
        def dp(i,j):
            if not inbound(i,j):
                return float('-inf')
            if (i,j) not in cache:
                if i == n-1 and j == m-1:
                    return dungeon[i][j] if dungeon[i][j] < 0 else 0

                d = min(0, dp(i+1, j ) + dungeon[i][j]   ) 
                r = min(0, dp(i, j+1 ) + dungeon[i][j]   ) 

                cache[(i,j)] = max(d,r) 
            
            return cache[(i,j)]
        
        return abs(dp(0,0)-1)