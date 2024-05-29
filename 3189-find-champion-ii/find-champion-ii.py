class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        g = [1]*n

        for i,j in edges:
            g[j] = 0
        x = sum(g)
        print(g)
        return -1 if x!=1 else g.index(1)
        
