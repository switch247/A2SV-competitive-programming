class Solution:
    def numberOfWays(self, s: str) -> int:
        # 1 0 1 or 0 1 0
        n = len(s)
        right_zero = s.count('0')
        right_one  = n - right_zero
        zero = one = 0
        ans = 0
        for i in range(n):
            if s[i]=='1':
                # Counting the sequences of "010"
                # zeros on the right * zeros on the left
                ans += (zero * right_zero)
                right_one -=1
                one +=1
            else:                       
                # Counting the sequences of "101"
                # ones on the right * ones on the left

                ans+=( right_one * one )
                right_zero -= 1
                zero +=1
            
          
        return ans
 
# 0 0 1 
# 1 0 0 
#  0 1 