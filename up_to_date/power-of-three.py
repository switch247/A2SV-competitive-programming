class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==3 or n ==1: return True # you could just use n==1 bur use both for speed
        elif n<3: return False
        return self.isPowerOfThree(n/3)
        
    #negative numbers cant be power of three for this question
