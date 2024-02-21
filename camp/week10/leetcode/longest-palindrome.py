class Solution:
    def longestPalindrome(self, s: str) -> int:
        d =  Counter(s)
        # print(d, *d.values())
        ans = 0
        a =0 
        for val in d.values():
            if val%2 ==0:
                ans+=val
            else:
                a =1
                ans+= (val -1)
               
        return ans + a