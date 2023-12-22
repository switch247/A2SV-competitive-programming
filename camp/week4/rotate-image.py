class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose-> reverse each row
        matrix[:] = [x[::-1] for x in list(zip(*matrix))]

