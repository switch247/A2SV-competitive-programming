class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp={}
        for i,j in zip(s,t):
            if i not in mp:
                if j in mp.values():
                    return False
                mp[i]=j
            elif( mp[i]!=j ):
                return False
        return True