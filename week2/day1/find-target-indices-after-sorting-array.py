class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        new=sorted(nums)
        for i in range(len(new)):
            if target == new[i]:
                ans.append(i)
        return ans
            
