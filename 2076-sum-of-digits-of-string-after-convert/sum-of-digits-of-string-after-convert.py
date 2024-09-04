class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def transform(s):
            ans = 0
            for c in s:
                ans+=int(c)
            return ans
        
        ans = ""
        for c in s:
            ans+=str(ord(c)-96)
        
        
        for i in range(k):
            ans = transform(str(ans))
        return int(ans)
        