class Solution:
    def reverseParentheses(self, s: str) -> str:
        st=''
        stalk = []
        for i in s:
            if i =='(':
                stalk.append(st)
                st=''
            elif i==')':
                #reverse the string(st)
                #and stack+st
                st = (st)[::-1]
                st = stalk.pop()+st
               
            else:
                st+=i
        return st
