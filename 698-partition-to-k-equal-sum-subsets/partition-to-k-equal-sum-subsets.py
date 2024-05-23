class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:return False
        targ = total // k
        parts = [0] * k
        nums.sort(reverse = True)
        @cache
        def dp(i, t):
            if i >= len(nums): return True

            for j in range(k):
                # print(parts)
                if parts[j] + nums[i] <= targ:
                    parts[j] += nums[i]
                    if dp(i + 1, tuple(parts)): return True
                    parts[j] -= nums[i]


            return False

        return dp(0, tuple())


