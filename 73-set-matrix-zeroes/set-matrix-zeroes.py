class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = set(),set()
        n,m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)
        for i in range(n):
            for j in range(m):
                if j in col:
                    matrix[i][j] = 0
                if i in row:
                    matrix[i][j] = 0
                


         