class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0 , len(nums)-1
        ans = 50001
        while l<=r:
            mid = (l+r)//2
            if nums[mid] >= nums[r]:
                ans = min(ans, nums[mid])
                l = mid +1
            else:
                ans = min(ans, nums[mid])
                r = mid -1
        # print(l,mid,r , (ans))
        return ans
        # return min(nums)