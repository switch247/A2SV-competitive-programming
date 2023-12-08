class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a = set( range( len(nums)+1 ) )
        b = set(nums)
        ans = 0
        for i in (a.symmetric_difference(b)):
          ans = i
        return ans
        