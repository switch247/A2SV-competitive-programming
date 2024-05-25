class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans=[]
        n = len(s)
        def dp(i,temp):
            if i >= n:
                ans.append(''.join(temp))
                return 
            if s[i].isalpha():
                # norm
                temp.append(s[i])
                dp(i+1,temp)
                temp.pop()
                #swaped
                temp.append(s[i].swapcase())
                dp(i+1,temp)
                temp.pop()
            else:
                temp.append(s[i])
                dp(i+1,temp)
                temp.pop()

        dp(0,[])
        return ans
        