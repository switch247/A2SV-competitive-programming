class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count =left = atmost_k = 0
        for right in range(len(nums)):
            if nums[right]%2:count += 1
            while count > k:
                if nums[left]%2: count -= 1
                left += 1
            atmost_k += right-left+1

        count =  left = atmost_k1 = 0
        for right in range(len(nums)):
            if nums[right]%2:count += 1
            while count > k-1:
                if nums[left]%2: count -= 1
                left += 1
            atmost_k1 += right-left+1
        
        return atmost_k - atmost_k1