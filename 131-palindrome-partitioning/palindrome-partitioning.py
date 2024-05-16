class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        temp = []
        def dfs(i):
            if i >= len(s):
                res.append(temp[:])
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    temp.append(s[i:j + 1])
                    dfs(j + 1)
                    temp.pop()
        dfs(0)
        return res
    
    def isPali(self, x, i, j):
        while i<=j:
            if x[i] != x[j]:
                return False
            i += 1
            j -=1
        return True

