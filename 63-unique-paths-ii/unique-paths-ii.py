class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0]==1 or obstacleGrid[n-1][m-1]== 1:
            return 0
            
        if n==1 and m==1 : return 1

        def inbound(i,j): return 0<=i<n and 0<=j<m
        mat = [ [0]*m for _ in range(n) ]
        mat[0][0] = 1
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j]==1:
                    mat[i][j] = -1
        


        for i in range(n):
            for j in range(m):
                if mat[i][j] == -1:
                    continue
                if inbound(i-1,j) :
                    if mat[i-1][j]!=-1:
                        mat[i][j]+=mat[i-1][j]
                if inbound(i,j-1) :
                    if mat[i][j-1]!=-1:
                        mat[i][j] += mat[i][j-1]
        print(*mat, sep ='\n')
        # wow bottom up wow
        return mat[n-1][m-1]