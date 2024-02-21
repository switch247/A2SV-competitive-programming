class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={ '}':'{', ')':'(', ']':'[' }
        for i in s:
            if i  in d: #if it is a closser
                if stack and stack[-1]==d[i]:#stack not empty and last ele in stack is =d[i] (then)
                    stack.pop()
                else:
                    return False
            else:#opener
                stack.append(i)
        return True if not stack else False