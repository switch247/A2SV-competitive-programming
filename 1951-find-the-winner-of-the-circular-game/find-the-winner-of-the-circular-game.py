class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        result=[i for i in range(1,n+1)]
        
        def rec(x, start):
            if len(x)==1:
                return x[0]          
            loser = (start+k-1)% len(x)
            start = loser if loser <= len(x) else 0
            return rec(x[:loser] +x[loser+1:], start)
        
        return rec(result,0)

        
    