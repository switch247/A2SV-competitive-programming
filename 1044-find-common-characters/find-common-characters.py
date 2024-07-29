class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        temp = [2**31 - 1]*26
        for word in words:
            t = [0]*26
            for char in word:
                t[ord(char) - ord('a')] +=1
            for i in range(26):
                temp[i] = min(temp[i],t[i])
        
        res = list()
        for i in range(26):
            while temp[i]>0:
                res.append(chr(i + ord('a')))
                temp[i] -=1
        return res