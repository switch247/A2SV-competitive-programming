class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        l = r = 0
        ans = 0
        while l < len(g) and r < len(s):
            if g[l]<=s[r]:
                l+=1
                r+=1
                ans+=1
            else:
                r+=1
        return  ans 
