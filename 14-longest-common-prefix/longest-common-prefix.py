class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        copy = sorted(strs)
        # print(copy)
        first = copy[0]
        last = copy[-1]
        min_len = min( len(first), len(last) ) 
        # print(min_len)
        for i in range( min_len ):
            if( first[i]!=last[i] ):
                return ans
            ans+= first[i]
        return ans 

        