class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n,m = len(matrix), len(matrix[0])
        def inbound(i,j): return 0 <= i < n and 0 <= j < m
        ans = 0
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                bot = diag = right = 0
                matrix[i][j]  = int( matrix[i][j] )
                if inbound(i+1,j):
                    # bot
                    bot = int(matrix[i+1][j])
                    
                if inbound(i,j+1):
                    # right                    
                    right = int(matrix[i][j+1])
                    
                if inbound(i+1,j+1):
                    # diag
                    diag = int(matrix[i+1][j+1])
                
                x  = min([bot,diag,right])
                if  matrix[i][j] :
                    matrix[i][j]  = int( matrix[i][j] ) + int(x)
                    
                ans = max(ans, matrix[i][j] )

        return ans**2




