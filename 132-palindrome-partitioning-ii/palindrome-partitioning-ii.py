class Solution:
    def minCut(self, s: str) -> int:
        def isPali( i, j ):
            return s[i:j + 1]==s[i:j + 1][::-1]
            # while i <= j:
            #     if s[i] != s[j]:
            #         return False
            #     i += 1
            #     j -= 1
            # return True
        
        cache = {}
        def dfs(i):
            if i >= len(s):
                return 0
            res = []
            if i in cache:
                return cache[i]
            for j in range(i, len(s)):
                if isPali(i, j):
                    res.append( 1 + dfs(j + 1) )

            if res:
                cache[i] = min(res) 
            else:
                cache[i] = 0 

            return  cache[i]

        return dfs(0) -1

       

