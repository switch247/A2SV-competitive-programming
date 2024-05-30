class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n, m = len(board), len(board[0])
        def inbound(i,j):return 0<=i<n and 0<=j<m
        drxn = [(1,0),(0,1),(-1,0),(0,-1), (1,1),(-1,1), (1,-1),(-1,-1) ]
        print(*board,sep='\n')
        vis = set()
        def dfs(i,j):
            if board[i][j] =='M':
                board[i][j] ='X'
                return 
            if (i,j) in vis:
                return 
            vis.add((i,j) )
            board[i][j] = 0
            flag = False
            for dx,dy in drxn:
                x,y  = i+dx, dy+j
                if inbound(x,y) and  board[x][y]== 'M':
                    board[i][j] +=1 
          
            if board[i][j] == 0:
                board[i][j] = 'B'
                for dx,dy in drxn:
                    x,y  = i+dx, dy+j
                    if inbound(x,y)  and  (x,y) not in vis:
                        dfs(x,y)
            else:
                board[i][j] = str(board[i][j])

                

        dfs(*click)
        # print('===========')
        # print(*board,sep='\n')
        return board