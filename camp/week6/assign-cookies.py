class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ans = 0
        s.sort()
        g.sort()
        z = 0
        for min_size in g:
            while z < len(s):
                if min_size <= s[z]:
                    ans+=1
                    z+=1 
                    break
                else:
                    # if z == len(s): break
                    z+=1 
            
        return ans
