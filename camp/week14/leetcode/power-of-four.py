class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==4 or n==1: return True
        elif n<4: return False
        else: return self.isPowerOfFour(n/4)
        