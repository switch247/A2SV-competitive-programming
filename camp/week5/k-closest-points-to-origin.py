class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # sort based on distance from origin, return the first k elements
        return sorted(points, key = lambda x: x[0]**2 + x[1]**2 )[:k]
        