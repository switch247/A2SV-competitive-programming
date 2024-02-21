class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        c = 1
        right = 0
        patch = 0
        while c <= n:
            if right < len(nums) and c >= nums[right]:
                c += nums[right]
                right+=1
            else:
                c *= 2
                patch += 1
                
        return patch

            
    # 1 5 8
    # c 1 r1 
    # 2 5 ?
    # 4 5 ?
    # 8 5
    # 13 8
    # 21