class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i,j = 0,0
        new = []
        while(i< len(nums1) and j < len(nums2) ):
            if nums1[i]==nums2[j]:
                new.append(nums1[i])
                i+=1
                j+=1
            elif( nums1[i]<nums2[j] ):
                i+=1
            else:
                j+=1
        return new
        # What if the given array is already sorted? How would you optimize your algorithm?
        # What if nums1's size is small compared to nums2's size? Which algorithm is better?
        # What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
        