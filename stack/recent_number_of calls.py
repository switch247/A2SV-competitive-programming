class RecentCounter:
     def __init__(self):
        self.requests = deque()
 
    def ping(self, t: int) -> int:
        self.requests.append(t)
        #count = 0
        while self.requests[0] < t - 3000:
            self.requests.popleft()
        return len(self.requests)
    
    '''def __init__(self):
        self.recentRequests=[]

    def ping(self, t: int) -> int:
        self.recentRequests.append(t)
        self.recentRequests.reverse()
        while self.recentRequests[-1]<t-3000:
            self.recentRequests.pop()
        self.recentRequests.reverse() #why
        return len(self.recentRequests)'''
