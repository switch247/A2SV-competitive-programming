class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        arr = list(map(str,s))

        seen = set(s)
        ans = ""
        for i in range(len(s)):
            if s[i].swapcase() in seen:
                ans += s[i]
            else: 
                # print(s[i], 'nocounterpart-> reset')
                left = "".join(arr[:i])
                right = "".join(arr[i+1:])
                left_valid = self.longestNiceSubstring(left)
                right_valid = self.longestNiceSubstring(right)
                # print(left_valid,left_valid)
                if len(left_valid) >= len(right_valid):
                     return left_valid
                
                return right_valid
            # print(ans,'..')

        return ans
