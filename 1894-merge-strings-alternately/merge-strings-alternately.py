class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        a,b=len(word1),len(word2)
        n = a if a < b else b
        for a,b in zip(word1,word2):
            ans+=a+b
        ans+= word1[n:] + word2[n:]
        return ans