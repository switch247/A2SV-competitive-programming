class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        copy = sorted(strs)
        # print(copy)
        first = copy[0]
        last = copy[-1]
        min_len = min( len(first), len(last) ) 
        print(min_len)
        for i in range( min_len ):
            if( first[i]!=last[i] ):
                return ans
            ans+= first[i]
        return ans 
"""
if you see how words are arranged in a word dictionary
1 abc
2 abd
3 abde
4 bcd
the max amount of  prefixes the words can have is as large as how many they have in common
with the word that is farthest away from it
"""

        