class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for i in s:
            print(i,end=' ')
            if i == ')':
                poped = stack.pop()
                if poped =='(':
                    # if not stack or stack[-1] =='(':
                    s = 1
                    c = 0
                    while (stack and stack[-1]!='('):
                        print('df')
                        c += stack.pop()
                    stack.append(c+s)
                else:
                    # more
                    stack[-1] = (2 * poped)
                    c = 0
                    b =False
                    while (stack and stack[-1]!='('):
                        b =True
                        print('df')
                        c += stack.pop()
                    if b: stack.append(c)
                    

            else: #(
                stack.append('(')
            print(stack)
        
             
        return stack[-1]
        