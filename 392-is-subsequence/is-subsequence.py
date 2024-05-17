class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        @cache
        def dp(i,j):
            if i==n or j==m:
                return 0
            if s[i] == t[j]:
                return 1+ dp(i+1,j+1)
            else:
                return dp(i,j+1)

        ans = dp(0,0)
        return ans ==len(s)