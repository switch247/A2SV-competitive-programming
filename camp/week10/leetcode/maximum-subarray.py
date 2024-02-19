class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # running_sum =0
        # max_sum = -float('inf')
        # for i in range( len(nums) ):
        #     running_sum +=nums[i]
        #     if running_sum < nums[i]:
        #         running_sum = nums[i]
        #     if max_sum < running_sum :
        #         max_sum = running_sum
        # return max_sum
        # kadne's algorithm
        

        max_sum = nums[0]
        running_sum = 0
        for num in nums:
            if running_sum < 0:
                running_sum = 0
            running_sum += num

            if running_sum > max_sum:
                max_sum = running_sum
        return max_sum

        