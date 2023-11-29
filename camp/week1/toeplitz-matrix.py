class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True

        