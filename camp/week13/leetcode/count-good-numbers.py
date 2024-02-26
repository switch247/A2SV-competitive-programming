
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        a = pow(5, ( (n + 1) // 2 ), mod)
        b = pow(4, n // 2, mod)
        return (a * b) % mod

        
    