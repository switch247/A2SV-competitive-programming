class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # row,col
        if not mat or not mat[0]:
            return []
        n, m = len(mat), len(mat[0])

        d = [[] for _ in range(n + m - 1)]
        # switched to list because it is faster to reference list if we have the index
        for row in range(n):
            for col in range(m):
                d[row+col].append( mat[row][col] )
        ans = []
        for key, val in enumerate(d):
            if key%2:
                # norm
                ans.extend ( val )
            else:
                # rev
                ans.extend( val[::-1] )
        return ans

    
        
# row1+col1 == row2+col2 same diagonal
# (00) (10 01) (20 11 02) (21 12)  (22)
# () are al in the same diagonal
                




        