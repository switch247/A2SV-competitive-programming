class Solution:
    def interpret(self, command: str) -> str:
        # () = 0
        # command consists of "G", "()", and/or "(al)"
        ans = ''
        stack = []
        temp = ''
        for i in command:
            if  i == 'G':
                ans+=i
            else:
                if i == ')':
                    if temp == '(':
                        ans+='o'
                        temp = ''
                    else:
                        # ans+= 'al'
                        ans+=temp[1:]
                        temp = ''
                else:
                    temp+=i
        return ans

