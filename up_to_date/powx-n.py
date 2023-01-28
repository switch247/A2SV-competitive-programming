class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n ==0: return 1 
        if n>0: return x*pow(x,n-1)
        else: return 1/ x * pow(x,n+1)
    
