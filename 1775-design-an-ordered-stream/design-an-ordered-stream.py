class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 0
        self.start = 0
        self.tot = n
        self.answer = [None for i in range(n)]
       
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.answer[idKey-1] = value
        # self.answer[self.ptr - 1]
        while(self.ptr < self.tot and self.answer[self.ptr]   ):
            self.ptr+=1
        
        self.start
        x =  self.answer[self.start:self.ptr]
        # print(self.ptr)
        # print(self.answer)
        # print(x)
        self.start = self.ptr
        return x


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)