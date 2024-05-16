class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n==1 and m==1:
            return 1
        def inbound(i,j): return 0<=i<n and 0<=j<m
        mat = [ [0]*m for _ in range(n) ]
        if 1<m:
            mat[0][1] = 1
        if 1<n:
            mat[1][0] = 1
        for i in range(n):
            for j in range(m):
                if inbound(i-1,j) :
                    mat[i][j]+=mat[i-1][j]
                if inbound(i,j-1) :
                    mat[i][j]+= mat[i][j-1]
        print(*mat, sep ='\n')
        return mat[n-1][m-1]