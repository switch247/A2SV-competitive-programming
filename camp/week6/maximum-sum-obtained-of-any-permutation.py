class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        nums.sort()
        nums = nums[::-1]
        test = [0] * (1+ n)
        for l, r in requests:
            test[l] +=1
            test[r+1] -=1
        for i in range(1, len(test)):
            test[i] += test[i-1]
        test.sort()
        test = test[::-1]
        # print (test)
        ans = 0
        for i, v in enumerate(nums):
            ans += (v * test[i])

        return ans % mod






        [1,2,1,1, 0, 0]
        [1,2,3,4,5]