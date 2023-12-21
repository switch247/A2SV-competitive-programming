class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check row
        for row in board:
            s = set()
            for n in row:
                if  n!='.':
                    if n in s :
                        return False
                s.add(n)
        # check col
        for col in zip(*board):
            s = set()
            for i in col:
                if  (i!='.'):
                    if i in s :
                        return False
                s.add(i)
        
        new = [[] for i in range(9)]
        c = 0
        # check 3X3
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                new[c] = [board[i][j], board[i][j+1], board[i][j+2], board[i+1][j], board[i+1][j+1],board[i+1][j+2],board[i+2][j], board[i+2][j+1], board[i+2][j+2]]
                c+=1

        # for i in new:
        #     print(i )
        for i in new:
            s = set()
            for ch in i:
                if  ch != '.':
                    if ch in s :
                        return False
                s.add(ch)
        
        return True


        


                    

        