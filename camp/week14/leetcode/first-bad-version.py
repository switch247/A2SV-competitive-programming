# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0 ,n
        mid = (l+r)//2
        while (l< r):
            mid = (l+r)//2
            # print(l,mid, r)
            if isBadVersion(mid):
                r = mid 
            else:
                l = mid + 1
        if mid == r:
            return mid 
        return mid +1

        # for i in range(1,n+1):
        #     if isBadVersion(i):
        #         return i

        # 1 2 b | b b b 
        # 1 2 3 b b b b