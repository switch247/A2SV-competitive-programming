class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        sub=""
        num = 0
        for i in s:
            if i == '[':
                # save current substring and current number into stack 
                #current number is how many times the next substring will be repeated
                stack.append( (sub, num) )
                sub = ""
                num = 0                
            elif i == ']':
                prev_sub, repeat_times = stack.pop()
                # update substring with specified repeat times
                sub = prev_sub + sub * repeat_times
                
            elif i.isdigit():
                # update current number
                num = num*10 + int(i) #num=12
            
            else:    
                # update substring
                sub += i
        return sub
