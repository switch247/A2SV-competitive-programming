class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        ans = [-1] * n
        red = defaultdict(set)
        blue = defaultdict(set)
        for i, v in redEdges: red[i].add(v)
        for a, b in blueEdges: blue[a].add(b)
        cols = [blue, red]

        vis = set()
        q = deque()
        q.append([0,0,None]) # node,len,col
       
        vis.add((0,None))

        while q:
            node , length , color = q.popleft()

            if ans[node]== -1:
                ans[node] = length
            
            if color != "r":
                for neighbour in red[node]:
                    if (neighbour,"r") not in vis:
                        q.append([neighbour,length+1,"r"])
                        vis.add((neighbour,"r"))

            if color != "b":
                for neighbour in blue[node]:
                    if (neighbour,"b") not in vis:
                        q.append([neighbour,length+1,"b"])
                        vis.add((neighbour,"b"))
        return ans
