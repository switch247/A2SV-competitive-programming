class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n,m = len(mat), len(mat[0])
        ans=0
        for i in range(n):
            ans+= mat[i][i] + mat[i][m-i-1]
        offset = mat[n//2][m//2]  if n%2 else 0
        return ans - offset