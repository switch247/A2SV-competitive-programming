class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        one = 0
        ans = 0
        for num in s:
            if num == '1':
                one +=1
            else:
                ans += one
        return ans

       
            

        