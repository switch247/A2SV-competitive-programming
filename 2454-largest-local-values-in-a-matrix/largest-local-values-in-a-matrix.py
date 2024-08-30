class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        return list(map(lambda i: list(
    map(lambda j: max(*grid[i - 1][j - 1:j + 2], *grid[i][j - 1:j + 2], *grid[i + 1][j - 1:j + 2]),
        range(1, len(grid) - 1))), range(1, len(grid) - 1)))