class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==1 or x==0:
            return x
        l, r = 0, x
        ans = x//2
        while l<=r:
            mid = (l+r)//2
            if mid * mid == x:
                return mid
            elif mid*mid < x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans