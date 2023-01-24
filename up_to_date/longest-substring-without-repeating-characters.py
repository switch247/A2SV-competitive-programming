class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
        ans=1
        left=0
        if len(s) ==0: return 0
        if len(s) ==1: return 1
        seen =[]
        for right in range(len(s)):
            while s[right] in seen:
                seen.pop(0) 
                left+=1

            seen .append( s[right] )
            ans = max(ans, right- left+1)
        return ans
