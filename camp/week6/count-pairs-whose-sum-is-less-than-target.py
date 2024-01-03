class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        res = 0
        nums.sort()
        l = 0
        r = len(nums) - 1
        while l < r:
            # minimum sum every time b/c of 
            if nums[l] + nums[r] < target:
                # 1 1 2 3   ( l = 0 r = 3) ( r-l = 3 )
                # if 1 3 then 1 2 and 11
                # r - l == count of numbers between l and r
                res += r - l
                
                l += 1
            else:
                # sum >= target so decrease sum
                r -= 1
        return res

        

