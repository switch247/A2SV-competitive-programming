class Solution:
    def dijkstra(self, graph, start_node, n):
        distances = {node: float("inf") for node in range(1, n+1)}
        distances[start_node] = 0
        processed = set()
        heap = [(0, start_node)]

        while heap:
            cost, curr = heapq.heappop(heap)
            if curr in processed:
                continue
            processed.add(curr)
            distances[curr] = cost

            for weight, neighbor in graph[curr]:
                possible_distance = cost + weight
                if distances[neighbor] > possible_distance:
                    heapq.heappush(heap, (possible_distance, neighbor))
        return distances

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for trio in times:
            graph[trio[0]].append((trio[2], trio[1]))
        
        ans = self.dijkstra(graph, k, n)
        ans = max(ans.values()) if len(ans) > 0 else 0

        return -1 if ans == float("inf") else ans
