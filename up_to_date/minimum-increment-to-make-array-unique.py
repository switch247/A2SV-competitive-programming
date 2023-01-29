class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves=0
        for i in range(1,len(nums)):
            if nums[i] <=nums[i-1]:
                moves+= 1 + nums[i-1] - nums[i]
                nums[i] =  nums[i-1] +1
            #moves = prev -cur +1
            # moves+=1 if cur==prev
            #moves+=2 if cur<prev
            # cur = prev+1
        return moves
