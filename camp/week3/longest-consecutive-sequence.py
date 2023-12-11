class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic={}
        n = len(nums)
        if not nums: return 0
        ans=1
        nums.sort()
        for i in range(n):
            prev = nums[i] - 1
            if prev in dic:
                dic[ nums[i] ] = dic[ prev] + 1
                ans = max( ans, dic[nums[i]] )
            else:
                dic[ nums[i] ] = 1
        return ans
        
        """  this one works too """
        # nums.sort()
        # answer = 0
        # n= len(nums)
        # left, right = 0, 1
        # while(right<n):
        #     if (nums[right-1]+1 < nums[right]):
        #         answer=max(answer, right-left)
        #         left = right
        #     right+=1
        # print(nums)
        # answer = max(answer, right-1-left)
        # return answer
        