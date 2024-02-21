class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rowmax = [0]*n
        colmax = [0]*n
        for i in range(n):
            for j in range(n):
                c = grid[i][j]
                rowmax[i] = max(rowmax[i],c)
                colmax[j] = max(colmax[j],c)
        tot = 0
        for i in range(n):
            for j in range(n):
                c = grid[i][j]
                z = min(rowmax[i] ,colmax[j])
                tot+= (z -c)
        # print(rowmax,colmax)
        return tot

        