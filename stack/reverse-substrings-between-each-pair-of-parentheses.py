class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        # every time you find a '(' ->ss=''  and then add to ss untit u get ) 
        # every time you get ) reverse the string, -> and add it to last ele in stalk, then pop the stalk
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
