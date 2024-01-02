class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if not  (s[left].isalpha() or s[left].isnumeric() ):# alphanumeric
                left+=1
            elif not( s[right].isalpha() or s[right].isnumeric() ) :# alphanumeric
                right-=1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left+=1
                right-=1
        return True
        