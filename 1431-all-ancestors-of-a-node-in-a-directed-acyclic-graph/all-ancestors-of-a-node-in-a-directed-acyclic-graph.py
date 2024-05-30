class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = [set() for _ in range(n)]
        indeg = [0]*n
        graph =  [set() for _ in range(n)]
        for x,y in edges:
            indeg[y]+=1
            graph[x].add(y)
        
        queue = deque()
        for i in range(n):
            if indeg[i]==0:
                queue.append(i)
        while queue:
            par = queue.popleft()
            for child in graph[par]:
                ancestors[child].add(par)
                # add the ancestors of current parent
                ancestors[child].update(ancestors[par])

                indeg[child]-=1
                if indeg[child]==0:
                    queue.append(child)
        for i in range(n):
            ancestors[i] = sorted(list(ancestors[i] ))

        return ancestors
