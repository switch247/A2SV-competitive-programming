class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n = min(len(nums1),len(nums2))
        nums11=Counter(nums1)
        nums22=Counter(nums2)
        ans=-1
        if len(nums1)<=len(nums2):
            for i in range(n):
                if nums1[i] in nums22:
                    ans= nums1[i]
                    break
        else:
            for i in range(n):
                if nums2[i] in nums11:
                    ans= nums2[i]
                    break
        return ans
            