class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        win=len(p)
        n = len(s)
        ans = []
        sorted_p =sorted(p)
        if n < win:return ans 
        def is_anagram(s):
            return s ==sorted_p
        for i in range(n-win+1):  
            if is_anagram( sorted(s[i:i+win])  ):
                ans.append(i)

        return ans