class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        new = [([0]*n)for i in range(m)]
        for i in range(n):
            for j in range(m):
                # print(matrix[i][j], i,j)
                new[j][i] = matrix[i][j]
        return new