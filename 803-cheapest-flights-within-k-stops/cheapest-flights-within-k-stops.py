class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [float('inf')]*n
        cost[src] = 0
        
        for i in range(k+1):
            any_relaxation = False
            new = cost[:]
            for u, v, w in flights:
                if cost[u] != float('inf'):
                    new[v] =min(new[v], cost[u] + w)
                    # any_relaxation = True
            # print(new)
            cost =new[:]
            # if not any_relaxation:
            #     break
        return cost[dst] if cost[dst] != float('inf') else -1
