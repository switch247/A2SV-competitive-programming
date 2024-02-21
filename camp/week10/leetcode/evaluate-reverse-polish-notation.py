class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  #stack
        #operations done on the last 2 elements of the stack
        for i in tokens:
            if i == '+' or i== '-' or i== '*' or i== '/':
                t = stack.pop()
                if(i == '+'): stack[-1] += t
                elif(i == '-'): stack[-1] -= t
                elif(i == '*'): stack[-1] *= t
                else: stack[-1] = int((stack[-1])/t)
            else:
                stack.append(int(i))
        return stack[0]