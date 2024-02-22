class RecentCounter:

    def __init__(self):
        self.queue = deque()
        
    def ping(self, t: int) -> int:
        self.queue.appendleft(t)
        # print(self.queue, t, t-3000)
        while self.queue[-1] < t-3000:
            # remove the non overlaping  request times, the ones we incountered first
            self.queue.pop()
        
        return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)