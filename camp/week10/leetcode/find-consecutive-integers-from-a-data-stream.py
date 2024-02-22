class DataStream:

    def __init__(self, value: int, k: int):
        self.val = value
        self.k = k
        self.data=[value]
        self.start = 0

    def consec(self, num: int) -> bool:
        # print('-----')
        # print(self.data, self.start, len(self.data) - self.start)
        if num != self.val:
            self.start = len(self.data) 
        # before updating check if the last k elements are = value
        b =  ( len(self.data) - self.start ) >= self.k
        self.data.append(num)
        # print(self.data, self.start, len(self.data) - self.start)
        # if b: print('valid')
        return b
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)