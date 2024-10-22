class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        if indexDifference== 0 and valueDifference==0:
            return [0,0]
        maps = defaultdict(list)
        for j in range(len(nums)):
            cur_val = nums[j]
            for old_val in maps:
                if abs(old_val - cur_val) >= valueDifference:
                    for i in maps[old_val]:
                        if abs(i - j) >= indexDifference:
                            return [i,j]
            maps[cur_val].append(j)

        return [-1,-1]