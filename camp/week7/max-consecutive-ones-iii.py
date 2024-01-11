class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n =len(nums)
        left = 0
        for right in range(n):
            if nums[right] == 0:
                k-=1
            #k -= (1 - nums[right]) #if its one do nothing else -1
            if k < 0:
                if nums[left] == 0:
                    k+=1
                #k += (1 - nums[left] ) #if left==0 k+=1                 
                left += 1

        return right - left + 1
            



            