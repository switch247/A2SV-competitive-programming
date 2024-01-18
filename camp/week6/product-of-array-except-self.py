class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zeros, product_without_zero, all_prod = 0, 1, 1
        for num in nums:
            all_prod *= num
            if num == 0:
                zeros+=1
            else:
                product_without_zero *= num
        ans = [0]* n
        if zeros > 1: return ans
        print(zeros, product_without_zero, all_prod)
        for i in range(len(nums)):
            if nums[i] == 0:
                ans[i] = product_without_zero 
            else:
                ans[i] = all_prod // nums[i]
        return ans
