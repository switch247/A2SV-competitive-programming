class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(s):
            new = 0
            for i in str(s):
                new += int(i)**2
            return str(new)

        s = helper(n)
        while len(s) != 1:
            s = helper(s)
        # print(2**31 -1)
        return s in '17'
        


        