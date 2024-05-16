class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = Counter(nums)
        ans = []
        for c in x:
            if x[c]==1:
                ans.append(c)
        return ans
