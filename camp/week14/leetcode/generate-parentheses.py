class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def valid(s):
            stack = []
            for i in s:
                if i == ')':
                    if not stack:
                        return False
                    stack.pop()
                else:
                    stack.append(i)
                # print(stack)
            return not len(stack) > 0
        x = '()'
        ans = []
        sub = []
        def backtrack(i):
                 
            if len(sub) ==2*n :
                # print(sub)
                if (sub[0]=='(' and sub[-1]==')') and  valid(sub):
                    ans.append( ''.join(sub) )
                return
            for j in range(i,2*n):
                for ch in x:
                    sub.append(ch)
                    if sub[0]=='(':
                        backtrack(j+1)
                    sub.pop()
        backtrack(0)
        return ans
