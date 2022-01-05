class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #quick sort makes it so much slower dont use '.sort' next time     
        nums1.extend(nums2)
        nums1.sort()
        #print(nums1)
        for i in range(n):
            nums1.remove(0)
