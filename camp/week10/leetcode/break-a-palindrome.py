class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # asume a = 0  b = 1
        # 00123 < 01023 < 00123
        # goal is to place zero(smallest) closest to the start
        # without making it a palindrome
        # if changing to zero doesnt work change to 2 2
        
        chars=list(map(str,palindrome))
        if len(palindrome)==1:
            return ''
        a = palindrome.count('a')
        for i in range( len(chars) ):
            if chars[i] !='a':
                if a != len(palindrome)-1: # aaabaaa => aaabaab
                    chars[i]='a'
                    break
        else:
            chars[-1] ='b'
        return ''.join(chars)


        