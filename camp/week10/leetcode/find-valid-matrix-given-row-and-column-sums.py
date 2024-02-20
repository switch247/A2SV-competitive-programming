class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # 0 0 0
        # 0 0 0
        # 0 0 0
        # Find the smallest rowSum or colSum, and let it be x. 
        # Place that number in the grid, and subtract x from rowSum and colSum. (at point of intesection)
        # Continue until all the sums are satisfied.
        n, m = len(rowSum), len(colSum)
        grid = [[0]*m for _ in range(n)]
        
        # print(grid)
        
        for i in range(n):
            for j in range(m):
                x =  min(rowSum[i], colSum[j])
                if rowSum[i] < colSum[j]:
                    grid[i][j] = rowSum[i] 
                    colSum[j] -=  x
                    rowSum[i] -= x
                else:
                    grid[i][j] = colSum[j] 
                    rowSum[i] -=  x
                    colSum[j] -= x
                
        return grid

                

        
        