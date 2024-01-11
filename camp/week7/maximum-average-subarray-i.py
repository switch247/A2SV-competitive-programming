class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # @cache
        ans = float("-inf")
        n = len(nums)
        s = 0 
        left,right=0,0
        while (right < n):
            if k> (right-left+1):
                s+= nums[right]
            if k ==(right-left+1):
                #right window size
                s+= nums[right]
                ans = max(s, ans)
                s -= nums[left]
                left+=1
            right+=1
        return ans/k