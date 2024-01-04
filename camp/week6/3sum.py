class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums[i] + nums[j] + nums[k] == 0
        # nums[i] + nums[k]  == - nums[j]
        nums.sort()
        # print(nums)
        ans = set()
        for i in range(len(nums)):
            j , k = i+1, len(nums)-1
            while j < k :
                if nums[j] + nums[k] ==  -nums[i] : #
                    ans.add( (nums[i], nums[j], nums[k]) )
                    j += 1
                    k -=  1
                elif nums[j] + nums[k] < -nums[i] :
                    j+=1
                else:
                    k-=1
        return ans

# 1 2 3 4 5 6 7 i+j = 8
# -3 -2 -1 0 1 2 3  i+j = 0      
# -5 -4 -3 -2 -1 i+j  = -6