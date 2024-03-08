class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        seen = set(s)
        ans = []
        for i in range(len(s)):
            if s[i].swapcase() in seen:
                ans.append( s[i])
            else: 
                # print(s[i], 'nocounterpart-> reset')
                left = s[:i]
                right = s[i+1:]
                left_valid = self.longestNiceSubstring(left)
                right_valid = self.longestNiceSubstring(right)
                # print(left_valid,left_valid)
                if len(left_valid) >= len(right_valid):
                     return left_valid
                
                return right_valid
            # print(ans,'..')

        return ''.join(ans)
