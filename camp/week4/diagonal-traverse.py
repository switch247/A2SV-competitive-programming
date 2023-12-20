class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # row,col
        m, n = len(mat[0]), len(mat)
        d = defaultdict(list)
        for row in range(n):
            for col in range(m):
                d[row+col].append( mat[row][col] )
        ans = []
        for key, val in d.items():
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
                




        