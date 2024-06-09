class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        last = nums[-1]
        ans= 0
        for i in range(len(nums)-1,-1,-1):
            s = nums[i] // last
            # print(nums[i], last, s)
            if nums[i]% last!=0:
                s+=1
                # print(s, '.')
                last = nums[i]//s
            ans+= (s-1)
            # print(ans,';;')
        return ans