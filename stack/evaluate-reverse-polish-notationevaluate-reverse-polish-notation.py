class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        S = []  #stack
        #goal is to have 2 elements in yor stack when you encounter an operation 
        for i in tokens:
            if i == '+' or i== '-' or i== '*' or i== '/':
                t = S.pop()
                if(i == '+'): S[-1] += t
                elif(i == '-'): S[-1] -= t
                elif(i == '*'): S[-1] *= t
                else: S[-1] = int((S[-1])/t) #int(6.6) aprox 6 wrong other wise
            else:
                S.append(int(i))
        return S[0]
    '''
    [2,2,+,4,*,4,/]
    [(2+2),4,,*,4,/]
    [(4*4),4,/]
    [16/4]
    ==[4]
    return stack[0 or -1]
    '''
