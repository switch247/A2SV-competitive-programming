class Solution: #very slow
    def fib(self, n: int) -> int:
        if n ==0 or n==1:
            return n
        else: return  self.fib(n-1) + self.fib(n-2)

        
 """
 #very fast but takes alot of space
class Solution:
    def __init__(self):
        self.memo = {}
        # memo{qustion:answer}
    
    def fib(self, N):
        return self.helper(N)
    def helper(self,N):
        if N == 0 or N==1: 
            return N
        if N in self.memo:
            return self.memo[N]
        
        self.memo[N] = self.helper(N-1) + self.helper(N-2)
        return self.memo[N]

"""
        
