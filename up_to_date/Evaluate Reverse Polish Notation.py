class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        S = []  #stack
        #operation performed on the last two elements on the stalk 
        for i in tokens:
            
            if i == '+' or i== '-' or i== '*' or i== '/':
                t = S[-1]            
                if(i == '+'): 
                    S.pop()
                    S[-1] += t
                elif(i == '-'):
                    S.pop() 
                    S[-1] -= t
                elif(i == '*'): 
                    S.pop()
                    S[-1] *= t
                else: 
                    S.pop()
                    S[-1] = int(S[-1]/  t ) 
                    #negative rounded down gives wrong number
            else:
                S.append( int(i) )
        #print (int(6/-132) )
        return S[-1]
