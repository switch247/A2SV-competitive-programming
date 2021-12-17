class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
# the index of an element after it is sorted = how many numbers are smaller than it
        a=[];
        new = sorted(nums) #this makeks it faster
        for i in nums:
            a.append(new.index(i))
        return a;
