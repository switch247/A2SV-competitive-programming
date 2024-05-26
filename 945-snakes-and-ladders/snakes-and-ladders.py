class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        q= deque([(1,0)])
        visited =set()
        board.reverse()

        while q:
            pos,move = q.popleft()
            for x in range(1,7):
                # min(curr..+ 6)
                nxt = pos + x
                i = (nxt-1)//len(board)
                j = (nxt-1) % len(board) if i%2 != 1 else len(board)-((nxt-1) % len(board)) -1
            

                if board[i][j] != -1:
                    nxt = board[i][j]
                if nxt == len(board)*len(board):
                    return move+1

                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt,move+1))
            

        return -1