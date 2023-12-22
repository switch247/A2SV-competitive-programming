class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n<3:
            return False

        # d = defaultdict( list )
        # s = set()
        # for num in nums:#O(n *n)
        #     for key in s:
        #         if num > key :
        #             d[key].append(num)
        #     s.add(num)
        
        # for arr in d.values():
        #     for i in arr:
        #         if i in d:
        #             return True
        # return False
        a = float('inf')
        b = float('inf')
        # a < b < c
        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            else:
                return True

        return False

# 12334
# a b num
# - - -
# 1 - 1
# 1 2 2
# 1 2 3 X
