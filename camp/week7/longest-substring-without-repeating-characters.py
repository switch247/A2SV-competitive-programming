class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        count = []
        pos = -1
        if len(s)==0: return 0
        elif len(s)==1: return 1
        
        
        for i in range( len(s)):
            while( s[i] in count):
                count.pop(0)
        
            count.append(s[i])
            
            output = max(output, len(count))
        
        
        return output
