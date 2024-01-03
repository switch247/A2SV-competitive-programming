class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = 1
        if len(nums)==1: return ans

        seeker = 1
        for left in range(len(nums)-1):
            # print(nums)
            flag = False
            while(seeker < len(nums) and nums[left]==nums[seeker]):
                # seeeker overlap as a duplicate so it updates itself
                # 1 2 3 => left, seeker = 0, 1 -> 
                #  1 1 ! => 1 2
                seeker+=1
                flag = True
            # print(left, seeker)
            if seeker==len(nums): return ans
            if flag: nums[left+1] = nums[seeker]
            ans +=1
        # print(ans)
        return ans
       
    