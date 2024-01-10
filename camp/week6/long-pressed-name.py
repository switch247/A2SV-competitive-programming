class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n, t = len(name), len(typed)
        if n > t: return False
        if name == typed: return True
        l, r = 0 , 0
        while r < t and l < n:
            if typed[r] == name[l]:
                r+=1
                l+=1
            elif r > 0 and typed[r] == typed[r-1]:
                r+=1
            else: #typed[r] !== typed[r-1] or r<=0 
                return False
        # print(l, n, "typed", r, t)
        while r < t and typed[r] == typed[r - 1]:
            r += 1
        if  l == n and r==t:
            return True
        
            
