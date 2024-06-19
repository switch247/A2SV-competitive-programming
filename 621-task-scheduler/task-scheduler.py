class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count= Counter(tasks)
        maxheap = [-c for c in count.values()]
        heapify(maxheap)
        time=0
        q = deque() #[-c,idletime]
        while maxheap or q: #while these are not empty there are tasks left to do
            time+=1
            if maxheap:
                c = 1 + heapq.heappop(maxheap)
                if c: #if c isnt zero
                    q.append([c,time+ n])
            if q and (q[0][1]) == time:#current time equal to[c,t(time it willbe available to add it)]
                # q.popleft()[0] add count to max heap
                heapq.heappush(maxheap , q.popleft()[0])
        return time
        
            