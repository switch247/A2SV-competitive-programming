class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c=Counter(s1)
        x= len(s1)
        for i in range(len(s2)-x +1):
            if Counter(s2[i:i+x]) ==c:
                return True
        return False