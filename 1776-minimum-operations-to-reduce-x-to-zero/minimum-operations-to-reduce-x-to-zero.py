class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target <0:
            return -1
        if target == 0:
            return len(nums)

        l, r = 0, 0
        curr_sum = 0

        operations = float('inf')

        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target and l < len(nums):
                if curr_sum == target:
                    operations = min(operations, len(nums) - (r - l + 1))
                curr_sum -= nums[l]
                l += 1

        return operations if operations != float('inf') else -1
            