class Solution:
    def concact(self, x, n):
        if n==1:
            return x
        return x + self.concact(x, n-1)
    def decodeString(self, s: str) -> str:
        stack = []
        def recurser(idx, sub, num=0):
            # print('called')
            if idx >= len(s):
                return sub
            ch = s[idx]
            if ch == '[':
                stack.append( (sub, num) )
                sub, num = '', 0
            elif ch == ']':
                # [a] ==not posible num[x]
                prev_sub, repeat_times = stack.pop()
                # just because i wanted to use recursion some where else
                sub = prev_sub + self.concact(sub, repeat_times)
            elif ch.isdigit():
                # 32[a]
                # 3 -> 2 -> [ -> a -> ]
                num = num*10 + int(ch)
            else:
                sub+= ch
            
            return recurser(idx+1, sub, num)
        
        return recurser(0,'',0)

        # return ans
# s[i]
# 