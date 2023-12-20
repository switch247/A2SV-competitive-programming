class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        def issorted (s):
            prev = ord( s[0])
            for i in range(1, len(s)):
                if  ord(s[i]) < prev :
                    # print(s)
                    return False
                prev = ord(s[i])
            return True

        n, m  = len(strs), len( strs[0] )
        cols = zip(*strs)
        count = 0
        for col in cols:
            # print(col)
            if not issorted(col):
                count+=1
        return count
# abcd efgh ijk lmno pqrst uvw xyz
        