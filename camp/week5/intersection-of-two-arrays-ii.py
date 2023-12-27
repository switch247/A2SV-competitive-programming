class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d= Counter(nums1)
        new =[]
        for num in nums2:
            if num in d and d[num]>0:
                d[num]-=1
                new.append(num)
        return new

        