class Solution:
    def concact(self, x, n):
        if n==1:
            return x
        return x + self.concact(x, n-1)
    def decodeString(self, s: str) -> str:
        x = self.concact( "x", 3 )
        print( x )
        stack = []
        ans=""
        num = 0
        for ch in s:
            # print(stack,sub,num)
            if ch == '[':
                stack.append( (ans, num) )
                ans, num = '', 0
            elif ch == ']':
                # [a] ==not posible num[x]
                prev_sub, repeat_times = stack.pop()
                # just because i wanted to use recursion some where
                ans = prev_sub + self.concact(ans,repeat_times)
            elif ch.isdigit():
                # 32[a]
                # 3 -> 2 -> [ -> a -> ]
                num = num*10 + int(ch)
            else:
                ans+= ch


                
        return ans


