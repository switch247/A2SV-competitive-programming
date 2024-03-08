class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # 0 # 0
        # 1 # 0 | 1 
        # 2 # 01 |10
        # 3 # 01 10 |10 01
        if n == 1:
            return 0
        length = 2 ** (n - 2)
        if k <= length:
            return self.kthGrammar(n - 1, k)
        else:
            return 1 - self.kthGrammar(n - 1, k - length)


        