class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m= len(grid[0]) -2
        n = len(grid) -2
        mx = float("-inf")
        for row in range(n):
            for col in range(m):
                n = grid[row][col] + grid[row][col+1] + grid[row][col+2] + grid[row+1][col+1] + grid[row+2][col] + grid[row+2][col+1] + grid[row+2][col+2]
                mx = max(mx,n)
        return mx
        