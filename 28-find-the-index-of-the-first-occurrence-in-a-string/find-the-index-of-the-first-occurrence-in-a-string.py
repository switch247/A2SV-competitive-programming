class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        print(len(haystack) - len(needle))
        for i in range(0,(len(haystack) - len(needle) ) +1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        return -1

