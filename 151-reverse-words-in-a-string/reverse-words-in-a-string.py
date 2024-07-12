class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        z = s.split(' ')
        ans = []
        for i in z:
            if i:
                ans.append(i)
        return ' '.join(ans[::-1])