class Solution:#recursive
    def findTheWinner(self, n: int, k: int) -> int:
        result=[i for i in range(1,n+1)]#changes the input into a list
        
        def rec(x: list,start: int):
            if len(x)==1: return x[0]          
            loser = (start+k-1)%len(x)
            start = loser if loser<=len(x) else 0
            
            return rec(x[:loser] +x[loser+1:], start)
        
        return rec(result,0)



"""
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        result=[i for i in range(1,n+1)]#changes the input into a list
        start = 0
        while len(result)>1:#when only 1 remain you found the winner
            loser = (start+k-1)%len(result) 
            del result[loser]
            start = loser if loser<=len(result) else 0
        return result[0]
"""
