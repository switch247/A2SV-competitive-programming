class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s = set()
        left = 0
        ans = 0
        for right in range( len(nums) ):
            while nums[right] in s:
                s.discard(nums[left])
                left+=1
            s.add(nums[right])
            # print(s,sum(s))
            ans = max(ans, sum(s) )
        return ans