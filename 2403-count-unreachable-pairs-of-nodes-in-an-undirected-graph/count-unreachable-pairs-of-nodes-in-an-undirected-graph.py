class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node, seen):
            if node in seen:
                return 0
            
            seen.add(node)
            size = 1
            for neighbor in adj[node]:
                size += dfs(neighbor, seen)
                
            return size

        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        seen = set()
        result = 0
        sum_ = dfs(0, seen)
        for node in range(n):
            if node not in seen:
                size = dfs(node, seen)
                result += size * sum_
                sum_ += size

        return result