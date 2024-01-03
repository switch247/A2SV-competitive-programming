class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1) ,  len(nums2)
        l, r = 0 , 0
        while  l < n and r < m:
            if nums1[l] == nums2[r]:
                return nums1[l] 
            elif nums1[l] < nums2[r]:
                l+=1
            else:
                r+=1
    
        return -1
