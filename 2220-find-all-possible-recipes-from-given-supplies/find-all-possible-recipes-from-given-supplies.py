class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indeg = defaultdict(lambda:0)
        graph=defaultdict(list)

        for i in range(len(recipes)):
            for pre in ingredients[i]:
                graph[pre].append(recipes[i])
                indeg[recipes[i]]+=1
        
        queue = deque(supplies)

        dic=defaultdict(lambda:False)
        while queue:
            node = queue.popleft()
            for neg in graph[node]:
                indeg[neg]-=1
                if indeg[neg]==0:
                    dic[neg]=True
                    queue.append(neg)
        
        ans=[]
        for q in recipes:
            if dic[q]:
                ans.append(q)
            
        return ans