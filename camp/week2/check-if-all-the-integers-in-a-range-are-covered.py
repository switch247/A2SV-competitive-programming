class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        mn = float('inf')
        mx = float('-inf')
        target = set (range(left,right+1))
        big_set= set()
        for a,b in ranges:
          small_set  =  range(a,b+1) 
          big_set.update( small_set )
        # print(target, big_set)
        # [left, right] is covered by at least one interval in ranges
        # check if target is a subset of the larger set
        return target <= big_set
        