class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                p1=str(nums[i])+str(nums[j])
                p2=str(nums[j])+str(nums[i])
                if p1 < p2:#to find the largest combo and put 9 in 1st position
                    nums[i],nums[j]=nums[j],nums[i]
        result=""
        for i in nums:
            result+=str(i)
        return str(int(result)) # this removes'0' from '00' 
