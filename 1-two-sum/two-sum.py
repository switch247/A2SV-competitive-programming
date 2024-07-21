class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        #d=val:index
        #diff=0
        for i,v in enumerate(nums):
            #dif=target-v
            if target- v in d:
                return [d[target-v],i]
            else:
                d[v]=i
        