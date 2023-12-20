class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in zip(*strs):
            if list(i) != sorted(i):
                count += 1
        return count
# abcd efgh ijk lmno pqrst uvw xyz
        