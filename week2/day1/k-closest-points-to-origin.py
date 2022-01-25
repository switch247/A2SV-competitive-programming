class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        x = sorted(points, key = lambda p: p[0]**2 + p[1]**2)
        return x[0:k]
    # k tells you how many answers you have
