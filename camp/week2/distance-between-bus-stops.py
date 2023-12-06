class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        a = min(start, destination)
        b = max(start, destination)
        forwards = sum(distance[a:b])
        backwards = sum(distance) - forwards
        return min(forwards, backwards)

