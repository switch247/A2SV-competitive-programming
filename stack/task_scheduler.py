class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count= Counter(tasks)
        maxheap = [-c for c in count.values()] # heap of frequency
        heapq.heapify(maxheap)
        time=0
        q = deque() #[-c,idletime]
        while maxheap or q: #while these are not empty there are tasks left to do
            time+=1
            #move the task back and forth between maxheap and q until freq of the task= 0
            if maxheap:
                c = 1 + heapq.heappop(maxheap)  #popleft basicaly /heappop/
                if c: #if c isnt zero
                    q.append([c,time+ n])
            if q and (q[0][1]) == time: # when current_time equal to[c,t(time it willbe available to add it)]
                # q.popleft()[0] add task back to maxheap  at 1st position/heappush/
                heapq.heappush(maxheap , q.popleft()[0])
        return time
        
            
