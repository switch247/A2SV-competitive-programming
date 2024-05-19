class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n,m = len(dungeon), len(dungeon[0])
        # bottom up
        dp = [[0] * m for _ in range(n)]
        dp[n-1][m-1] = max(1, 1-dungeon[n-1][m-1])

        for i in range(n-2, -1, -1):
            # last col prev- cur
            dp[i][m-1] = max(1, dp[i+1][m-1]-dungeon[i][m-1])
        # print(*dp,sep='\n')
        
        for j in range(m-2, -1, -1):
            # last row prev- cur
            dp[n-1][j] = max(1, dp[n-1][j+1]-dungeon[n-1][j])
        # print(*dp,sep='\n')
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                # min prev - cur
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1])-dungeon[i][j], 1)

        # print(*dp,sep='\n')
        return dp[0][0]

        # topdown
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