class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        # for a, b in pairwise(sorted(x for x, _ in points)): print(a, b)
        return max((
            b - a
            for a, b in pairwise(sorted(x for x, _ in points))
        ), default=0)




        