class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        #sorting it takes most of the time
        ans=[]
        l=0
        r=len(nums)-1
        while(len(ans) != len(nums)):
            ans.append(nums[l])
            l+=1
            if l <= r:
                ans.append(nums[r])
                r-=1
        return ans
    #1st,last......... make sure elements anround another ele are both >/< the ele
    
